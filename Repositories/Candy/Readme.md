# Candy

Canvas Candy — TfTHacker's collection of decorated card styles, stencil libraries, and sample diagrams demonstrating cssclasses-driven rendering inside Obsidian's canvas. Heavy use of frontmatter cssclasses (`cc-*` rules), shape variants, and embedded stencil SVGs.

**Source:** https://github.com/TfTHacker/obsidian-canvas-candy

**Left out:** the stock photos (Unsplash and Pexels, which aren't under Candy's MIT licence) and the brand logos (Facebook, Instagram, Twitter, YouTube). `Organizational Chart.canvas`, `Apollo Missions Timeline.canvas` and `Stencils - Stickers.canvas` point at some of them, so those image nodes are missing files: a case an app should draw sensibly too.

## Canvases

- `00 START HERE.canvas` — *original path: `00 START HERE.canvas`*
- `05 Video Tutorials.canvas` — *original path: `05 Video Tutorials.canvas`*
- `Accounts Receivable Flowchart.canvas` — *original path: `Samples/Accounts Receivable Flowchart.canvas`*
- `Annotating Markdown Files.canvas` — *original path: `Samples/Annotating Markdown Files.canvas`*
- `Apollo Missions Timeline.canvas` — *original path: `Samples/Apollo Missions Timeline.canvas`*
- `BPMN Travel Agency.canvas` — *original path: `Samples/BPMN Travel Agency.canvas`*
- `Borders Stencil.canvas` — *original path: `Stencils/Borders Stencil.canvas`*
- `Borders.canvas` — *original path: `Features/Borders.canvas`*
- `Cards.canvas` — *original path: `Features/Cards.canvas`*
- `Database Structure Diagram.canvas` — *original path: `Samples/Database Structure Diagram.canvas`*
- `Diabetes Research.canvas` — *original path: `Samples/Diabetes Research.canvas`*
- `Flowcharts - Circles.canvas` — *original path: `Stencils/Flowcharts - Circles.canvas`*
- `Flowcharts - Diamonds.canvas` — *original path: `Stencils/Flowcharts - Diamonds.canvas`*
- `Flowcharts - Ovals.canvas` — *original path: `Stencils/Flowcharts - Ovals.canvas`*
- `Flowcharts - Parallelogram.canvas` — *original path: `Stencils/Flowcharts - Parallelogram.canvas`*
- `Flowcharts - Squares.canvas` — *original path: `Stencils/Flowcharts - Squares.canvas`*
- `Footers.canvas` — *original path: `Stencils/Footers.canvas`*
- `Gradients.canvas` — *original path: `Stencils/Gradients.canvas`*
- `Headers Footers Combined.canvas` — *original path: `Stencils/Headers Footers Combined.canvas`*
- `Headers and Labels.canvas` — *original path: `Features/Headers and Labels.canvas`*
- `Headers.canvas` — *original path: `Stencils/Headers.canvas`*
- `Home Network.canvas` — *original path: `Samples/Home Network.canvas`*
- `Labels.canvas` — *original path: `Stencils/Labels.canvas`*
- `Lesson 01 - Getting Started.canvas` — *original path: `Tutorial/Lesson 01 - Getting Started.canvas`*
- `Lesson 02 - Decorating a card.canvas` — *original path: `Tutorial/Lesson 02 - Decorating a card.canvas`*
- `Lesson 03 - Try decorating a card for yourself.canvas` — *original path: `Tutorial/Lesson 03 - Try decorating a card for yourself.canvas`*
- `Lesson 04 - Using multiple decorations in a card.canvas` — *original path: `Tutorial/Lesson 04 - Using multiple decorations in a card.canvas`*
- `Lesson 05 - Using Callout decorations.canvas` — *original path: `Tutorial/Lesson 05 - Using Callout decorations.canvas`*
- `Next Steps - Learn about the different decorations.canvas` — *original path: `Tutorial/Next Steps - Learn about the different decorations.canvas`*
- `Organizational Chart.canvas` — *original path: `Samples/Organizational Chart.canvas`*
- `Product Development Flowchart.canvas` — *original path: `Samples/Product Development Flowchart.canvas`*
- `SETUP YOUR VAULT.canvas` — *original path: `SETUP YOUR VAULT.canvas`*
- `Stakeholder Map.canvas` — *original path: `Samples/Stakeholder Map.canvas`*
- `Stencils - Stickers.canvas` — *original path: `Stencils/Stickers.canvas`*
- `Stickers.canvas` — *original path: `Features/Stickers.canvas`*
- `Storyboard - Getting Start with CNLV.canvas` — *original path: `Samples/Storyboard - Getting Start with CNLV.canvas`*
- `UML Class Diagram for a Banking System.canvas` — *original path: `Samples/UML Class Diagram for a Banking System.canvas`*
- `Venn Diagram.canvas` — *original path: `Samples/Venn Diagram.canvas`*
- `Wardley map.canvas` — *original path: `Samples/Wardley map.canvas`*
- `Writing Process Mind Map.canvas` — *original path: `Samples/Writing Process Mind Map.canvas`*

## Layout

- `*.canvas` — canvas files at the top level, original filenames preserved (collisions disambiguated with parent-folder prefixes).
- `Assets/` — every non-canvas file referenced by the canvases, flat. Original filenames preserved (collisions disambiguated with `-1`, `-2`, …).

## What was rewritten

Inside each canvas:
- File-type node `file` paths → `Assets/<basename>` (or sibling `<canvas>.canvas` for inter-canvas references)
- Inline `![[embeds]]`, `[[wikilinks]]`, and `[text](url)` markdown links → same rewrite
- External URLs (`http://`, `https://`) are untouched

Total path rewrites in this group: **127**.
See "Unresolved references" below for paths that could not be located.

## Unresolved references

These references couldn't be located in the source repo. They've been left as-is — likely the source repo doesn't include the asset, the canvas was authored against a personal vault, or the path is intentionally external.

### `Borders Stencil.canvas`
- `02 Stencil Index`
### `Flowcharts - Circles.canvas`
- `02 Stencil Index`
### `Flowcharts - Diamonds.canvas`
- `02 Stencil Index`
### `Flowcharts - Ovals.canvas`
- `02 Stencil Index`
### `Flowcharts - Parallelogram.canvas`
- `02 Stencil Index`
### `Flowcharts - Squares.canvas`
- `02 Stencil Index`
### `Footers.canvas`
- `02 Stencil Index`
### `Gradients.canvas`
- `02 Stencil Index`
### `Headers Footers Combined.canvas`
- `02 Stencil Index`
### `Headers.canvas`
- `02 Stencil Index`
### `Labels.canvas`
- `02 Stencil Index`
### `Stencils - Stickers.canvas`
- `02 Stencil Index`
### `Next Steps - Learn about the different decorations.canvas`
- `02 Stencil Index`
