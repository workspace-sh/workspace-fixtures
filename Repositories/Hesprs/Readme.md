# Hesprs

hesprs/json-canvas-viewer — standalone web viewer for the JSON Canvas format with an Obsidian-like UI. The demo canvas exercises every node type and edge style in the spec.

**Source:** https://github.com/hesprs/json-canvas-viewer

## Canvases

- `demo.canvas` — *original path: `packages/shared/demo.canvas`*

## Layout

- `*.canvas` — canvas files at the top level, original filenames preserved (collisions disambiguated with parent-folder prefixes).
- `Assets/` — every non-canvas file referenced by the canvases, flat. Original filenames preserved (collisions disambiguated with `-1`, `-2`, …).

## What was rewritten

Inside each canvas:
- File-type node `file` paths → `Assets/<basename>` (or sibling `<canvas>.canvas` for inter-canvas references)
- Inline `![[embeds]]`, `[[wikilinks]]`, and `[text](url)` markdown links → same rewrite
- External URLs (`http://`, `https://`) are untouched

Total path rewrites in this group: **0**.
All references resolved successfully.

