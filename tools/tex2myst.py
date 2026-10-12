#!/usr/bin/env python3
"""Port dissertation LaTeX (Chapters 1-2, plus selected background results)
into MyST Markdown pages.

Design goals:
  * Words and math are carried over verbatim. Only *structure* is rewritten:
    environments -> MyST directives, \\ref -> hyperlinks, \\cite -> {cite:p},
    \\textit -> *...*, etc.
  * Every theorem/equation/section number is computed from the full thesis
    source (all chapters) so the web numbering matches the PDF exactly. The
    computed numbers are verified against the named destinations in the PDF.
  * Anything the converter does not understand is reported, never dropped.

Usage:  python3 tools/tex2myst.py            (reads tex/, writes notes/)
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

PDF_URL = ("https://raymondtana.github.io/my_assets/documents/"
           "Raymond%20Tana%20PhD%20Dissertation.pdf")

THEOREM_ENVS = {"theorem", "lemma", "proposition", "corollary", "remark",
                "definition", "example", "fact", "claim", "observation"}
MATH_ENVS = {"align", "align*", "equation", "equation*", "gather", "gather*",
             "multline", "multline*"}
LIST_ENVS = {"itemize", "enumerate"}
# Macros from UserDefinedCommands.tex whose first argument is optional.
# KaTeX cannot express optional arguments, so `\Kc[r]{x}{y}` is rewritten to
# `\KcAt{r}{x}{y}` (same rendering; see myst.yml for the definitions).
OPTIONAL_ARG_MACROS = ["Kcalt", "Kc", "K", "Icalt", "Ic", "I", "Jcalt", "Jc",
                       "J", "mc", "m", "norm"]

# Chapters/pages that are ported. Everything else is "out of scope": refs into
# it link to the named destination in the PDF instead.
PORTED_CHAPTERS = {1, 2}
APPENDIX_LABELS = [
    "theorem:marstrand_projection_original",
    "theorem:Orponen_weak_Marstrand",
    "lemma:Lemma_2.3_of_Orponen",
    "theorem:Stull_pinned_distance_theorem",
    "theorem:Bushling_pinned_distance_theorem",
    "theorem:Polish_space_as_continuous_image_of_Baire",
]

REPORT = defaultdict(Counter)   # category -> Counter(detail)


def note(cat, detail):
    REPORT[cat][detail] += 1


# --------------------------------------------------------------------------
# Lexing helpers
# --------------------------------------------------------------------------

def strip_comments(src):
    """Remove % comments. Whole-line comments are removed entirely (LaTeX
    treats them as nothing, *not* as a blank line)."""
    out = []
    for line in src.split("\n"):
        m = re.search(r"(?<!\\)%", line)
        if m:
            kept = line[:m.start()]
            if kept.strip() == "":
                continue
            line = kept
        out.append(line)
    return "\n".join(out)


def read_group(s, i, open_="{", close="}"):
    """s[i] == open_. Return (content, index after closing)."""
    assert s[i] == open_, (s[i:i + 40])
    brace, j = 0, i + 1
    if open_ == "{":
        brace = 1
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            brace += 1
        elif c == "}":
            brace -= 1
            if open_ == "{" and brace == 0:
                return s[i + 1:j], j + 1
        elif c == "]" and open_ == "[" and brace == 0:
            return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced group at %r" % s[i:i + 60])


def skip_ws(s, i):
    while i < len(s) and s[i] in " \t\n":
        i += 1
    return i


def skip_inline_math(s, i):
    """s[i] == '$'. Return index after the closing '$'."""
    j = i + 1
    while j < len(s):
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == "$":
            return j + 1
        j += 1
    raise ValueError("unclosed $ at %r" % s[i:i + 60])


# --------------------------------------------------------------------------
# Parsing into a small tree
# --------------------------------------------------------------------------

def parse(s, i=0, stop_env=None):
    """Return (nodes, i). Node kinds:
       ('text', str) ('heading', cmd, star, title, label)
       ('env', name, opt, children) ('math', name, raw) ('item', opt)
       ('label', name)
    """
    nodes, buf = [], []

    def flush():
        if buf:
            nodes.append(["text", "".join(buf)])
            buf.clear()

    while i < len(s):
        c = s[i]
        if c == "$":
            j = skip_inline_math(s, i)
            buf.append(s[i:j])
            i = j
            continue
        if c != "\\":
            buf.append(c)
            i += 1
            continue
        m = re.compile(r"\\([A-Za-z]+\*?|.)").match(s, i)
        cmd = m.group(1)
        if cmd == "begin":
            name, j = read_group(s, m.end())
            if name in MATH_ENVS:
                end = "\\end{%s}" % name
                k = s.index(end, j)
                flush()
                nodes.append(["math", name, s[j:k]])
                i = k + len(end)
                continue
            opt = None
            k = skip_ws(s, j)
            if k < len(s) and s[k] == "[":
                opt, j = read_group(s, k, "[", "]")
            flush()
            children, i = parse(s, j, name)
            nodes.append(["env", name, opt, children])
            continue
        if cmd == "end":
            name, j = read_group(s, m.end())
            if name != stop_env:
                raise ValueError("\\end{%s} while in %s" % (name, stop_env))
            flush()
            return nodes, j
        if cmd == "[":
            k = s.index("\\]", m.end())
            flush()
            nodes.append(["math", "equation*", s[m.end():k]])
            i = k + 2
            continue
        if cmd.rstrip("*") in ("chapter", "section", "subsection",
                               "subsubsection"):
            k = skip_ws(s, m.end())
            if s[k] == "[":           # \section[short]{long}: keep long
                _, k = read_group(s, k, "[", "]")
                k = skip_ws(s, k)
            title, j = read_group(s, k)
            label = None
            k = skip_ws(s, j)
            if s.startswith("\\label{", k):
                label, j = read_group(s, k + 6)
            flush()
            nodes.append(["heading", cmd.rstrip("*"), cmd.endswith("*"),
                          title, label])
            i = j
            continue
        if cmd == "item":
            opt, j = None, m.end()
            k = skip_ws(s, j)
            if k < len(s) and s[k] == "[":
                opt, j = read_group(s, k, "[", "]")
            flush()
            nodes.append(["item", opt])
            i = j
            continue
        if cmd == "label":
            name, j = read_group(s, m.end())
            flush()
            nodes.append(["label", name])
            i = j
            continue
        buf.append(m.group(0))
        i = m.end()
    if stop_env:
        raise ValueError("missing \\end{%s}" % stop_env)
    flush()
    return nodes, i


def env_label(env):
    """Pop the first direct \\label child of an environment."""
    for k, ch in enumerate(env[3]):
        if ch[0] == "label":
            del env[3][k]
            return ch[1]
    return None


# --------------------------------------------------------------------------
# Numbering (mirrors the PDF: theorem counter reset per section; equation
# counter reset per chapter but printed as section.n, e.g. (1.8.5))
# --------------------------------------------------------------------------

def split_rows(raw):
    """Split math content at top-level \\\\ (ignoring nested environments)."""
    rows, depth, start, i = [], 0, 0, 0
    while i < len(raw):
        if raw.startswith("\\begin{", i):
            depth += 1
        elif raw.startswith("\\end{", i):
            depth -= 1
        elif raw.startswith("\\\\", i) and depth == 0:
            rows.append(raw[start:i])
            i += 2
            start = i
            continue
        if raw[i] == "\\":
            i += 2
            continue
        i += 1
    rows.append(raw[start:])
    return rows


class Numberer:
    def __init__(self):
        self.ch = self.sec = self.sub = self.thm = self.eq = 0
        self.labels = {}      # label -> dict(number, dest, chapter, kind)
        self.dests = []

    def add_label(self, label, number, dest, kind):
        if label in self.labels:
            note("duplicate label", label)
        self.labels[label] = dict(number=number, dest=dest, chapter=self.ch,
                                  kind=kind, page=getattr(self, "page", None))
        self.dests.append(dest)

    def walk(self, nodes):
        for n in nodes:
            kind = n[0]
            if kind == "heading" and not n[2]:
                cmd, label = n[1], n[4]
                if cmd == "chapter":
                    self.ch += 1
                    self.sec = self.eq = 0
                    num, dest = str(self.ch), "chapter.%d" % self.ch
                elif cmd == "section":
                    self.sec += 1
                    self.sub = self.thm = 0   # equation counter is per chapter
                    num = "%d.%d" % (self.ch, self.sec)
                    dest = "section." + num
                    self.page = num
                elif cmd == "subsection":
                    self.sub += 1
                    num = "%d.%d.%d" % (self.ch, self.sec, self.sub)
                    dest = "subsection." + num
                else:
                    num = dest = None
                n.append(num)
                if label:
                    self.add_label(label, num, dest, cmd)
                else:
                    self.dests.append(dest)
            elif kind == "env":
                if n[1] in THEOREM_ENVS:
                    self.thm += 1
                    num = "%d.%d.%d" % (self.ch, self.sec, self.thm)
                    label = env_label(n)
                    n.append(dict(number=num, label=label))
                    if label:
                        self.add_label(label, num, n[1] + "." + num, n[1])
                    else:
                        self.dests.append(n[1] + "." + num)
                self.walk(n[3])
            elif kind == "math":
                rows = []
                numbered_env = not n[1].endswith("*")
                parts = split_rows(n[2]) if n[1] != "equation" else [n[2]]
                for row in parts:
                    labels = re.findall(r"\\label\{([^}]*)\}", row)
                    if re.search(r"\\(nonumber|notag)\b", row):
                        has_num = False
                    else:
                        has_num = numbered_env
                    num = None
                    if has_num:
                        self.eq += 1
                        num = "%d.%d.%d" % (self.ch, self.sec, self.eq)
                        for lab in labels:
                            self.add_label(lab, num, "equation." + num,
                                           "equation")
                        if not labels:
                            self.dests.append("equation." + num)
                    elif labels:
                        note("label on unnumbered math row", labels[0])
                    rows.append(dict(src=row, number=num, labels=labels))
                n.append(rows)


# --------------------------------------------------------------------------
# Inline conversion
# --------------------------------------------------------------------------

class Converter:
    def __init__(self, labels):
        self.labels = labels

    # ---- references -----------------------------------------------------
    def ref_target(self, label):
        info = self.labels.get(label)
        if info is None:
            note("unresolved \\ref", label)
            return "??", None
        if info["chapter"] in PORTED_CHAPTERS or label in APPENDIX_LABELS:
            if info["kind"] == "chapter":
                # Chapters are sidebar groups, not pages: link to x.1.
                first = next(l for l, v in self.labels.items()
                             if v["kind"] == "section"
                             and v["number"] == info["number"] + ".1")
                return info["number"], "#" + first
            return info["number"], "#" + label
        note("ref outside ported chapters -> PDF link", label)
        return info["number"], PDF_URL + "#nameddest=" + info["dest"]

    def ref_md(self, label, paren=False):
        num, url = self.ref_target(label)
        text = "(%s)" % num if paren else num
        if url is None:
            return text
        if paren:
            return "([%s](%s))" % (num, url)
        return "[%s](%s)" % (text, url)

    # ---- math -----------------------------------------------------------
    def math(self, m):
        for name in OPTIONAL_ARG_MACROS:
            pat = re.compile(r"\\%s(?![A-Za-z])\s*\[" % name)
            while True:
                mm = pat.search(m)
                if not mm:
                    break
                opt, j = read_group(m, mm.end() - 1, "[", "]")
                m = m[:mm.start()] + "\\%sAt{%s}" % (name, opt) + m[j:]
                note("macro call rewritten (optional arg)",
                     "\\%s[...] -> \\%sAt{...}" % (name, name))

        def ref(mm):
            num, _ = self.ref_target(mm.group(2))
            note("\\ref inside math (plain number, no link)", mm.group(2))
            return "(%s)" % num if mm.group(1) == "eqref" else num
        m = re.sub(r"\\(ref|eqref)\{([^}]*)\}", ref, m)
        m = re.sub(r"\\label\{[^}]*\}", "", m)
        m = re.sub(r"\\(nonumber|notag)\b", "", m)
        return m

    # ---- text -----------------------------------------------------------
    ACCENTS = {"'": "\u0301", '"': "\u0308", "`": "\u0300", "^": "\u0302",
               "~": "\u0303", "c": "\u0327", "v": "\u030c", "H": "\u030b"}

    def inline(self, s):
        """Convert a run of LaTeX paragraph text (with $math$) to MyST."""
        out, i = [], 0
        while i < len(s):
            c = s[i]
            if c == "$":
                j = skip_inline_math(s, i)
                out.append("$" + self.math(s[i + 1:j - 1]).strip() + "$")
                i = j
                continue
            if c == "\\":
                piece, i = self.command(s, i)
                out.append(piece)
                continue
            if c == "{":
                inner, i = read_group(s, i)
                out.append(self.inline(inner))
                continue
            if c == "}":
                note("stray }", s[max(0, i - 30):i + 1])
                i += 1
                continue
            if s.startswith("``", i):
                out.append("\u201c"); i += 2; continue
            if s.startswith("''", i):
                out.append("\u201d"); i += 2; continue
            if c == "`":
                out.append("\u2018"); i += 1; continue
            if s.startswith("---", i):
                out.append("\u2014"); i += 3; continue
            if s.startswith("--", i):
                out.append("\u2013"); i += 2; continue
            if c == "~":
                out.append("\u00a0"); i += 1; continue
            if c in "*_<":
                out.append("\\" + c); i += 1; continue
            out.append(c)
            i += 1
        return "".join(out)

    def arg(self, s, i):
        i = skip_ws(s, i)
        return read_group(s, i)

    def command(self, s, i):
        m = re.compile(r"\\([A-Za-z]+|.)").match(s, i)
        cmd, j = m.group(1), m.end()
        if cmd in ("textit", "emph", "textsl"):
            a, j = self.arg(s, j)
            inner = self.inline(a)
            lead = inner[:len(inner) - len(inner.lstrip())]
            trail = inner[len(inner.rstrip()):]
            return lead + "*" + inner.strip() + "*" + trail, j
        if cmd == "textbf":
            a, j = self.arg(s, j)
            return "**" + self.inline(a).strip() + "**", j
        if cmd in ("text", "mbox", "textrm", "textnormal"):
            a, j = self.arg(s, j)
            return self.inline(a), j
        if cmd == "cite":
            k = skip_ws(s, j)
            pre = None
            if s[k] == "[":
                pre, k = read_group(s, k, "[", "]")
                note("\\cite with optional note", pre)
            keys, j = read_group(s, k)
            keys = "; ".join(x.strip() for x in keys.split(","))
            # "Section 4.5 of \cite{LV08}" reads best as a narrative citation,
            # "Li & Vitanyi (2008)"; elsewhere use parenthetical "(Li ..., 2008)".
            before = s[max(0, i - 12):i].replace("~", " ").split()
            narrative = before and before[-1].lower() in (
                "of", "in", "by", "from", "see")
            role = "cite:t" if narrative else "cite:p"
            note("citation style", role)
            return "{%s}`%s`" % (role, keys), j
        if cmd in ("ref", "cref", "Cref", "autoref"):
            a, j = self.arg(s, j)
            if cmd != "ref":
                note("\\%s treated as \\ref" % cmd, a)
            return self.ref_md(a), j
        if cmd == "eqref":
            a, j = self.arg(s, j)
            return self.ref_md(a, paren=True), j
        if cmd in self.ACCENTS:
            k = j
            if k < len(s) and s[k] == "{":
                a, k = read_group(s, k)
            else:
                a, k = s[k], k + 1
            a = a.replace("\\i", "i")
            return a + self.ACCENTS[cmd], k
        if cmd in ("ldots", "dots"):
            return "\u2026", j
        if cmd == "@":
            return "", j
        if cmd in (" ", ","):
            return " ", j
        if cmd in ("%", "&", "#", "$", "{", "}"):
            return ("\\" if cmd in "#$" else "") + cmd, j
        if cmd == "_":
            return "\\_", j
        if cmd in ("noindent", "medskip", "smallskip", "bigskip", "par",
                   "small", "footnotesize"):
            note("layout command dropped", "\\" + cmd)
            return "", j
        note("unknown text command kept verbatim", "\\" + cmd)
        return m.group(0), j


# --------------------------------------------------------------------------
# Block rendering
# --------------------------------------------------------------------------

def indent(text, n):
    pad = " " * n
    return "\n".join(pad + ln if ln.strip() else "" for ln in text.split("\n"))


def fence_depth(md):
    """Longest colon fence used inside md."""
    runs = re.findall(r"^\s*(:{3,})", md, re.M)
    return max((len(r) for r in runs), default=0)


class Renderer:
    def __init__(self, conv):
        self.conv = conv

    def blocks(self, nodes):
        """Render a node list into Markdown blocks (list of strings)."""
        out, para = [], []

        def flush_para():
            text = "".join(para)
            para.clear()
            for chunk in re.split(r"\n\s*\n", text):
                chunk = " ".join(chunk.split())
                if chunk:
                    md = self.conv.inline(chunk).strip()
                    if md:
                        out.append(md)

        for n in nodes:
            k = n[0]
            if k == "text":
                para.append(n[1])
                continue
            flush_para()
            if k == "math":
                out.extend(self.math_block(n))
            elif k == "env":
                out.append(self.env(n))
            elif k == "heading":
                out.append(self.heading(n))
            elif k == "label":
                note("stray \\label (emitted as target)", n[1])
                out.append("(%s)=" % n[1])
            elif k == "item":
                note("\\item outside list", "")
        flush_para()
        return out

    def heading(self, n):
        cmd, star, title, label, num = n[1], n[2], n[3], n[4], n[5]
        hashes = {"section": "#", "subsection": "##",
                  "subsubsection": "###"}[cmd]
        text = self.conv.inline(title)
        line = "%s %s%s" % (hashes, (num + " ") if num else "", text)
        return ("(%s)=\n" % label if label else "") + line

    # ---- math -----------------------------------------------------------
    def math_block(self, n):
        name, rows = n[1], n[3]
        inner_env = {"align": "aligned", "align*": "aligned",
                     "gather": "gathered", "gather*": "gathered"}.get(name)

        def body(rs):
            src = "\\\\\n".join(self.conv.math(r["src"]).strip("\n")
                                for r in rs)
            src = "\n".join(ln.strip() for ln in src.split("\n")
                            if ln.strip())
            if inner_env:
                return "\\begin{%s}\n%s\n\\end{%s}" % (inner_env, src,
                                                       inner_env)
            return src

        numbered = [r for r in rows if r["number"]]
        if not numbered:
            return ["$$\n%s\n$$" % body(rows)]
        # Group rows so each group holds exactly one numbered row.
        groups, cur = [], []
        for r in rows:
            cur.append(r)
            if r["number"]:
                groups.append(cur)
                cur = []
        if cur:
            groups[-1].extend(cur)
        if len(rows) > 1:
            if len(groups) > 1:
                note("numbered align split into one block per number",
                     ", ".join(g_num(g) for g in groups))
            else:
                note("align row number moved to the block",
                     g_num(groups[0]))
        out = []
        for g in groups:
            r = next(r for r in g if r["number"])
            label = r["labels"][0] if r["labels"] else \
                "equation-" + r["number"].replace(".", "-")
            if len(r["labels"]) > 1:
                note("extra labels on one equation", ", ".join(r["labels"]))
            out.append("```{math}\n:label: %s\n:enumerator: %s\n%s\n```"
                       % (label, r["number"], body(g)))
        return out

    # ---- environments ---------------------------------------------------
    def env(self, n):
        name, opt, children = n[1], n[2], n[3]
        if name in THEOREM_ENVS:
            meta = n[4]
            inner = "\n\n".join(self.blocks(children))
            label = meta["label"] or "theorem-" + meta["number"].replace(
                ".", "-")
            head = "{prf:%s}" % name
            if opt:
                head += " " + " ".join(self.conv.inline(opt).split())
            return self.fence(head, [":label: " + label,
                                     ":enumerator: " + meta["number"]], inner)
        if name == "proof":
            inner = "\n\n".join(self.blocks(children))
            head = "{prf:proof}"
            if opt:
                head += " " + " ".join(self.conv.inline(opt).split())
            return self.fence(head, [":nonumber:"], inner)
        if name in LIST_ENVS:
            return self.list_env(name, opt, children)
        note("unknown environment (rendered as plain div)", name)
        return self.fence("{div}", [], "\n\n".join(self.blocks(children)))

    def fence(self, head, opts, inner):
        colons = ":" * max(3, fence_depth(inner) + 1)
        parts = [colons + head] + opts + [inner, colons]
        return "\n".join(p for p in parts if p != "")

    def list_env(self, name, opt, children):
        items, cur = [], None
        for ch in children:
            if ch[0] == "item":
                if ch[1] is not None:
                    note("\\item[...] custom label", ch[1])
                cur = []
                items.append(cur)
            elif cur is None:
                if ch[0] != "text" or ch[1].strip():
                    note("content before first \\item", str(ch)[:60])
            else:
                cur.append(ch)
        ordered = name == "enumerate"
        marker = "1. " if ordered else "- "
        rendered = []
        for it in items:
            bl = self.blocks(it)
            if not bl:
                rendered.append(marker.rstrip())
                continue
            first = bl[0]
            rest = bl[1:]
            text = marker + indent(first, len(marker)).lstrip(" ")
            for b in rest:
                text += "\n\n" + indent(b, len(marker))
            rendered.append(text)
        md = "\n".join(rendered) if all("\n\n" not in r for r in rendered) \
            else "\n\n".join(rendered)
        cls = None
        if opt:
            if "\\roman*" in opt:
                cls = "roman-list"
            elif "\\alph*" in opt:
                cls = "alpha-list"
            else:
                note("enumerate option not mapped", opt)
        if cls:
            return self.fence("{div}", [":class: " + cls], md)
        return md


def g_num(g):
    return next(r["number"] for r in g if r["number"])


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------

def slugify(title):
    s = re.sub(r"\$[^$]*\$", "", title)
    s = re.sub(r"\\[A-Za-z]+", "", s)
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def main(thesis, outdir):
    thesis, outdir = Path(thesis).expanduser(), Path(outdir)
    trees = []
    for c in range(1, 7):
        src = (thesis / ("Chapter-%d.tex" % c)).read_text()
        nodes, _ = parse(strip_comments(src))
        trees.append(nodes)
    num = Numberer()
    for t in trees:
        num.walk(t)

    # ---- verify numbering against PDF named destinations ---------------
    dest_file = Path(__file__).with_name("pdf_dests.json")
    if dest_file.exists():
        pdf = set(json.loads(dest_file.read_text()))
        ours = set(d for d in num.dests if d)
        kinds = tuple(k + "." for k in THEOREM_ENVS) + (
            "chapter.", "section.", "subsection.", "equation.")
        pdf_k = {d for d in pdf if d.startswith(kinds)}
        print("numbering check: %d of our %d anchors exist in the PDF; "
              "%d PDF anchors of these kinds not produced by us"
              % (len(ours & pdf_k), len(ours), len(pdf_k - ours)))
        for d in sorted(ours - pdf_k)[:20]:
            print("   ours-only:", d)
        for d in sorted(pdf_k - ours)[:20]:
            print("   pdf-only: ", d)

    conv = Converter(num.labels)
    rend = Renderer(conv)
    toc = []
    for c in sorted(PORTED_CHAPTERS):
        tree = trees[c - 1]
        chap = next(n for n in tree if n[0] == "heading" and n[1] == "chapter")
        sections, cur = [], None
        for n in tree:
            if n[0] == "heading" and n[1] == "section":
                cur = [n, []]
                sections.append(cur)
            elif cur is not None:
                cur[1].append(n)
            elif n[0] not in ("heading",) and not (
                    n[0] == "text" and not n[1].strip()):
                note("content before first section (skipped)", str(n)[:60])
        chdir = outdir / ("ch%d" % c)
        chdir.mkdir(parents=True, exist_ok=True)
        files = []
        for k, (h, body) in enumerate(sections, 1):
            title, label, number = h[3], h[4], h[5]
            fname = "%02d-%s.md" % (k, slugify(title))
            fm = ["---", "title: %s" % json.dumps(
                "%s %s" % (number, conv.inline(title)), ensure_ascii=False)]
            if label:
                fm.append("label: %s" % label)
            fm.append("---")
            md = "\n".join(fm) + "\n\n" + "\n\n".join(rend.blocks(body)) + "\n"
            (chdir / fname).write_text(md)
            files.append("ch%d/%s" % (c, fname))
        toc.append(dict(title="Chapter %s: %s" % (chap[5],
                                                  conv.inline(chap[3])),
                        files=files))

    # ---- appendix: selected background results from later chapters -----
    found = {}

    def find(nodes):
        for n in nodes:
            if n[0] == "env":
                if n[1] in THEOREM_ENVS and n[4]["label"] in APPENDIX_LABELS:
                    found[n[4]["label"]] = n
                find(n[3])
    for t in trees:
        find(t)
    blocks = []
    for lab in APPENDIX_LABELS:
        if lab not in found:
            note("appendix label not found", lab)
            continue
        blocks.append(rend.env(found[lab]))
    appdir = outdir / "appendix"
    appdir.mkdir(parents=True, exist_ok=True)
    (appdir / "background.md").write_text(
        "---\ntitle: Background Results\n---\n\n"
        "Statements of results from the literature that are cited in later "
        "chapters of the dissertation, numbered as in the "
        "[dissertation PDF](%s).\n\n" % PDF_URL
        + "\n\n".join(blocks) + "\n")

    (outdir / "toc.json").write_text(json.dumps(toc, indent=2,
                                                ensure_ascii=False))
    print("\n==== conversion report ====")
    for cat, ctr in sorted(REPORT.items()):
        print("\n[%s] (%d)" % (cat, sum(ctr.values())))
        for d, c in ctr.most_common():
            print("   %3d  %s" % (c, d))


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    main(*(sys.argv[1:3] or [root / "tex", root / "notes"]))
