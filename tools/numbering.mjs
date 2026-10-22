// MyST plugin: numbers theorem-like blocks and labeled equations from each
// page's position in the myst.yml TOC, so pages can be moved around freely.
//
// The first TOC entry is the home page (unnumbered). Every other top-level
// entry is a chapter page numbered 1, 2, ...; its children are 1.1, 1.2, ...
// (MyST numbers the page titles and headings itself: numbering.title and
// numbering.headings.) On page 1.2, theorems, lemmas, definitions, etc. share
// one counter (Theorem 1.2.1, Lemma 1.2.2, ...) and labeled equations get
// (1.2.1), (1.2.2), ... A page whose frontmatter sets
// `numbering: {title: {enumerator: A}}` is numbered A instead (appendices);
// one that sets `numbering: {title: false}` is skipped (front matter).
//
// It also fills in two things MyST cannot:
//   [%s](#page-label)        -> that page's number ("Section [%s](#x)" -> "Section 1.2")
//   \ref{label} inside math  -> the number of that theorem, equation, or page (no link)
import fs from 'node:fs';
import path from 'node:path';
import katex from 'katex';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const CONFIG = path.join(ROOT, 'myst.yml');

// TOC entries as {file, depth}, in order. myst.yml is read with regexes (no
// YAML parser is available to plugins), so keep the toc as `- file:` entries.
function tocEntries(config) {
  const lines = config.split('\n');
  const start = lines.findIndex((l) => /^\s+toc:\s*$/.test(l));
  if (start < 0) return [];
  const tocIndent = lines[start].search(/\S/);
  const entries = [];
  for (const line of lines.slice(start + 1)) {
    if (line.trim() && line.search(/\S/) <= tocIndent) break;
    const m = line.match(/^(\s*)- file:\s*(.+?)\s*$/);
    if (m) entries.push({ file: path.resolve(ROOT, m[2]), indent: m[1].length });
  }
  const indents = [...new Set(entries.map((e) => e.indent))].sort((a, b) => a - b);
  return entries.map((e) => ({ file: e.file, depth: indents.indexOf(e.indent) }));
}

// KaTeX macros from project.math, for re-rendering math that held \ref.
function mathMacros(config) {
  const macros = { '\\mbox': '\\text{#1}' }; // MyST's built-in macro
  const lines = config.split('\n');
  const start = lines.findIndex((l) => /^\s+math:\s*$/.test(l));
  if (start < 0) return macros;
  const mathIndent = lines[start].search(/\S/);
  for (const line of lines.slice(start + 1)) {
    if (line.trim() && !line.trim().startsWith('#') && line.search(/\S/) <= mathIndent) break;
    const m = line.match(/^\s+'(\\[^']+)':\s*'((?:[^']|'')*)'/);
    if (m) macros[m[1]] = m[2].replace(/''/g, "'");
  }
  return macros;
}

// Number every page, theorem-like block, and labeled equation by scanning the
// Markdown source. The transform below numbers the parsed page the same way and
// warns if the two ever disagree.
function scanBook() {
  const config = fs.readFileSync(CONFIG, 'utf8');
  const pages = {}; // absolute path -> page number
  const labels = {}; // label -> number
  const counts = [];
  tocEntries(config).forEach(({ file, depth }, i) => {
    if (i === 0 || !fs.existsSync(file)) return;
    const src = fs.readFileSync(file, 'utf8');
    const front = src.match(/^---\n([\s\S]*?)\n---/)?.[1] ?? '';
    if (/^\s+title:\s*false/m.test(front)) return;
    counts.length = depth + 1;
    counts[depth] = (counts[depth] ?? 0) + 1;
    const template = front.match(/title:\s*\n\s+enumerator:\s*['"]?([^'"\s]+)/)?.[1];
    const num = template ? template.replace(/%s/g, counts.join('.')) : counts.join('.');
    pages[file] = num;
    const pageLabel = front.match(/^label:\s*(\S+)/m)?.[1];
    if (pageLabel) labels[pageLabel] = num;
    let thm = 0;
    let eq = 0;
    const lines = src.slice(front ? front.length + 8 : 0).split('\n');
    lines.forEach((line, j) => {
      const m = line.match(/^(?::{3,}|`{3,})\{(prf:\w+|math)\}/);
      if (!m) return;
      const opts = [];
      for (let k = j + 1; k < lines.length && lines[k].startsWith(':'); k++) opts.push(lines[k]);
      const label = opts.map((o) => o.match(/^:label:\s*(\S+)/)?.[1]).find(Boolean);
      if (m[1] === 'math') {
        if (label) labels[label] = `${num}.${++eq}`;
      } else if (m[1] !== 'prf:proof' && !opts.some((o) => o.startsWith(':nonumber:'))) {
        const n = `${num}.${++thm}`;
        if (label) labels[label] = n;
      }
    });
  });
  return { config, pages, labels };
}

function walk(node, fn) {
  fn(node);
  (node.children ?? []).forEach((child) => walk(child, fn));
}

const numberingTransform = {
  name: 'toc-numbering',
  stage: 'document',
  plugin: () => (tree, vfile) => {
    const { config, pages, labels } = scanBook();
    const num = pages[path.resolve(vfile.path)];
    let macros;
    let thm = 0;
    let eq = 0;
    walk(tree, (node) => {
      if (num && node.type === 'proof' && node.kind !== 'proof' && node.enumerated !== false) {
        node.enumerator = `${num}.${++thm}`;
      } else if (num && node.type === 'math' && node.label) {
        node.enumerator = `${num}.${++eq}`;
        node.enumerated = true;
      }
      if (node.enumerator && node.label && labels[node.label] !== node.enumerator) {
        vfile.message(`numbering: "${node.label}" is ${node.enumerator} here but ${labels[node.label]} in the source scan`);
      }
      if (node.type === 'link' && node.url?.startsWith('#') && node.url.slice(1) in labels) {
        const target = labels[node.url.slice(1)];
        (node.children ?? []).forEach((c) => {
          if (c.type === 'text') c.value = c.value.replace(/%s/g, target);
        });
      }
      if ((node.type === 'math' || node.type === 'inlineMath') && node.value?.includes('\\ref{')) {
        const original = node.value;
        node.value = node.value.replace(/\\ref\{([^}]+)\}/g, (_, label) => {
          if (label in labels) return labels[label];
          vfile.message(`numbering: no target for \\ref{${label}}`);
          return '??';
        });
        macros ??= mathMacros(config);
        try {
          node.html = katex.renderToString(node.value, {
            displayMode: node.type === 'math',
            macros: { ...macros },
            strict: (code) => (code === 'newLineInDisplayMode' ? 'ignore' : 'warn'),
          });
          delete node.error;
          delete node.message;
          // MyST's own render already failed on the \ref (KaTeX rejects
          // underscores in \text{...}); drop that now-stale error.
          vfile.messages = vfile.messages.filter((m) => m.note !== original);
        } catch (err) {
          vfile.message(`numbering: KaTeX could not render math after \\ref: ${err.message}`);
        }
      }
    });
  },
};

export default { name: 'TOC numbering', transforms: [numberingTransform] };
