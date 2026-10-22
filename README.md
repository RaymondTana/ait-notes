# Algorithmic Information Theory Notes

Much of the content of these notes is based on my [doctoral dissertation](https://raymondtana.github.io/my_assets/documents/Raymond%20Tana%20PhD%20Dissertation.pdf).

## Developer notes

### Preview the book

From the repository root:

```bash
npm start  ## preview on localhost, port ~3000
```

### Edit the book

Modify, add, or delete Markdown content in `notes/`.

Fix the order of pages in `myst.yml`'s table of contents section `toc`.

Refer to a theorem, equation, or page by label: `Lemma [%s](#lemma:foo)` renders "Lemma x.y.z", `([%s](#equation:bar))` renders "(x.y.z)". Or, in math mode, use `\ref{label}`.

Defined terms have a short entry in the glossary (`notes/glossary.md`) linking to their full definition. Link a term to its entry with `` {term}`Name` `` or `` {term}`written form <Name>` `` (keep math out of the link text), typically at its first use on a page.

A page with `numbering: {title: false}` in its frontmatter is unnumbered; while `numbering: {title: {enumerator: A}}` numbers it "A".

### Update the book

From the repository root:

```bash
git add -A && git commit -m "..." && git push
```

### Convert the dissertation source to Markdown

Write every chapter of `legacy_tex/` to `converted_md/` as pages in the same style as `notes/`.

```bash
npm run convert  ## legacy_tex/ -> converted_md/
```
