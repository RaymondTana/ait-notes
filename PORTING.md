# How the dissertation was ported

Source: `tex/` in this repo (Chapters 1–2 are ported, plus six background
statements from Chapters 4–5; Chapters 3–6 are also kept because numbering is
computed over the whole thesis). Converter: `tools/tex2myst.py`. Re-run with
`npm run convert`; its full report is written to `tools/last_report.txt`.

No words were changed. Everything below is a change of *markup* only.

## Numbering

Every section, theorem-like environment, and equation number is computed from
the full thesis source (all six chapters) and written into the page explicitly
(`:enumerator:`). The converter checks its numbers against the named
destinations in the compiled PDF: **294 of 294 match, 0 missing**.

The PDF's scheme, reproduced here: theorems, lemmas, definitions, etc. share one
counter that resets each section (Lemma 1.5.7); equations use a counter that
resets each *chapter* but prints with the section prefix (1.8.5).

## `\ref`, `\eqref`, `\cite`

| LaTeX | Web |
|---|---|
| `Theorem~\ref{theorem:kraft_inequality}` | `Theorem [1.6.4](#theorem:kraft_inequality)`, which shows as "Theorem 1.6.4" with only the number as the link, and works across pages |
| `\eqref{label}` | `([1.6.4](#label))` |
| `\ref` to Chapters 3–6 (25 refs) | Number links to that spot in the dissertation PDF (`…pdf#nameddest=theorem.4.6.3`) |
| `\ref` to Chapter 1 or 2 itself | Links to that chapter's first section page (chapters are sidebar groups, not pages) |
| `\ref` *inside math*, e.g. `[\text{Lemma~\ref{x}}]` (41) | Plain number, no link (the math renderer can't hold links) |
| `\cite{A, B}` | `{cite:t}` (narrative: "Li & Vitányi (2008)") after *of, in, by, from, see*; otherwise `{cite:p}` (parenthetical). Hover shows the full reference, and a reference list is added to each page. Author–year style replaces `[LV08]` labels |

Labels keep their exact thesis names (`theorem:kraft_inequality`), so the URL of
any result is `…/page#<label>`.

## Macro changes (`myst.yml` → `project.math`)

KaTeX (MyST's math renderer) has no optional arguments, so each optional-argument
macro has a twin taking the subscript as a normal argument:

- `\Kc[r]{x}{y}` → `\KcAt{r}{x}{y}` (16 calls); `\Kcalt[r,s]{x}{y}` →
  `\KcaltAt{r,s}{x}{y}` (25); `\norm[*]{x}` → `\normAt{*}{x}` (2). The same
  twins exist for `\K`, `\I`, `\Ic`, `\Icalt`, `\J`, `\Jc`, `\Jcalt`, `\m`.
  Calls without the optional argument (`\Kc{x}{y}`) are unchanged.
- `\bbrk` is built as `\left[\!\left[ … \right]\!\right]`: KaTeX has no
  `\left\llbracket`, and two `\left[` brackets pulled together still resize.
- `\ensuremath` dropped from definitions (not needed in math mode).
- Not carried over (unused, or text-mode only): `\acro`, `\uv`, `\^`, `\d`,
  `\restr`, `\sump`, bra-ket macros, and the algebra operators like `\Gal`.

## Structure changes

- `%` comments removed (including commented-out epigraphs and drafts).
- Each `\section` is one page; `\subsection` → `##` heading. Numbers are in the
  titles (e.g. "1.6 Prefix Complexity").
- `align`/`align*` → `aligned` inside a display. Where the PDF numbers a single
  row of a multi-row `align`, the number sits beside the whole block instead of
  that row: (1.6.2), (1.6.3), (2.1.2), (2.1.3).
- `enumerate[label=(\roman*)]` → ordered list styled "(i), (ii), …" via
  `assets/custom.css`.
- `\textit`/`\emph` → `*…*`, `\textbf` → `**…**`, ``` ``…'' ``` → “…”, `~` →
  non-breaking space, `--` → –, accents → Unicode.
- One text-mode `\small` (a PDF line-fitting tweak in Theorem 1.10.2) was dropped.
- `\chapter` titles are used as sidebar group names.

## Content worth reviewing

- **§1.1 Introduction** outlines the dissertation's own results and refers to
  Chapters 3–6 (those references link into the PDF). You may want to rewrite it
  as an introduction to the notes.
- **Appendix** quotes six statements cited in Chapters 4–5 (Marstrand–Mattila,
  Orponen Thm 1.3 and Lemma 2.3, Stull, Altaf–Bushling–Wilson, Kechris 7.9),
  statements only (no proofs). The Rogers/Larman net
  theorems were left out because they depend on Chapter 4's definitions. The
  one-sentence intro on that page and on `index.md` is new text.
