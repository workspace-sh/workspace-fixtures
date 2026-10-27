# JSONCanvas

obsidianmd/jsoncanvas — the official JSON Canvas spec repo. `sample.canvas` is the canonical reference example from the spec documentation.

**Source:** https://github.com/obsidianmd/jsoncanvas

## Canvases

- `sample.canvas` — *original path: `sample.canvas`*

## Layout

- `*.canvas` — canvas files at the top level, original filenames preserved (collisions disambiguated with parent-folder prefixes).
- `Assets/` — every non-canvas file referenced by the canvases, flat. Original filenames preserved (collisions disambiguated with `-1`, `-2`, …).

## What was rewritten

Inside each canvas:
- File-type node `file` paths → `Assets/<basename>` (or sibling `<canvas>.canvas` for inter-canvas references)
- Inline `![[embeds]]`, `[[wikilinks]]`, and `[text](url)` markdown links → same rewrite
- External URLs (`http://`, `https://`) are untouched

Total path rewrites in this group: **5**.
All references resolved successfully.

