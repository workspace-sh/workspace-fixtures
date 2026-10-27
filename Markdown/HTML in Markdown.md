<p align="center">
  <img src="https://octodex.github.com/images/yaktocat.png" width="160" alt="Yaktocat">
  <br>
  <b>HTML in Markdown</b> — what a README does to a renderer
</p>

# HTML in Markdown

The HTML a README actually uses: a centred banner, badges, a floated logo, a
heading in a `<div>`. Every case below renders on GitHub, so what the app draws
can be compared against the same file there (workspace-sh/markdown#345).

Nothing here runs: `<script>`, `<iframe>` and event attributes are shown as
source, never executed. Remote images are subject to whatever the app's
remote-image policy says.

## A floated logo, with text beside it

<img align="right" src="https://octodex.github.com/images/yaktocat.png" height="140px" alt="Yaktocat">

Text after a right-floated image wraps beside it and returns to the full column
once it has passed the bottom of the image, the way a browser floats
`<img align="right">`. This paragraph is deliberately long enough to do both, so
the wrap and the return are visible without resizing the window. A second
sentence keeps it going past a small image on a wide screen.

<img align="left" src="https://octodex.github.com/images/yaktocat.png" height="140px" alt="Yaktocat">

The same on the left. A code block clears a float rather than squeezing beside
it, so the block below should start under the image, not next to it.

```sh
npm install
```

## Sizes

`width` and `height` are honoured in pixels and as a percentage of the column,
and nothing draws wider than the column.

<img src="https://octodex.github.com/images/yaktocat.png" width="80" alt="80 wide">
<img src="https://octodex.github.com/images/yaktocat.png" width="25%" alt="a quarter of the column">
<img src="https://octodex.github.com/images/yaktocat.png" height="60px" alt="60 tall">
<img src="https://octodex.github.com/images/yaktocat.png" width="4000" alt="wider than any column">

## An image in running text

Built with <img src="https://github.githubassets.com/images/icons/emoji/octocat.png" height="16" alt="Octocat"> and care — an
`<img>` written inline sits in the line like any other image.

## A centred block of markdown

<div align="center">

### Centred heading

Markdown between `<div align="center">` and `</div>` is aligned too, and stays
ordinary, *editable* markdown — this paragraph included.

</div>

## Right-aligned

<div align="right">

Aligned to the trailing edge.

</div>

## What keeps its own edge

<div align="center">

A list inside a centred div keeps its edge, because its markers are laid out
from the leading edge:

- first
- second

And so do code blocks:

```js
const x = 1;
```

</div>

## SVG badges

Badges are SVG, and usually wrapped in a link. The link around them is not
rendered yet (workspace-sh/markdown#345), so a badge row shows as source; the
bare `<img>` forms below it do render.

<a href="https://github.com/workspace-sh/workspace/actions"><img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="build"></a>

<img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="licence">

<img src="https://img.shields.io/badge/platform-macOS%20%7C%20iOS%20%7C%20Android%20%7C%20Linux-lightgrey.svg" alt="platforms">

## Inline tags inside an aligned block

<p align="center">
  <b>bold</b>, <i>italic</i>, <code>code</code>, <kbd>⌘S</kbd>, <mark>marked</mark>,
  H<sub>2</sub>O, x<sup>2</sup>
  <br>
  a second line after a break
</p>

## What must never render

Shown as source, exactly as written, and never run:

<script>alert('nope')</script>

<iframe src="https://example.com"></iframe>

<img src="https://octodex.github.com/images/yaktocat.png" onclick="alert('nope')" alt="an event attribute is ignored, the image still draws">

<div class="not-a-tag-we-honour" style="color: red">

A `class` or `style` is ignored rather than honoured, and kept in the file.

</div>

<!-- A comment stays source; it is not drawn as prose. -->

## Unbalanced and nested

<div align="center">

An opening tag with no closing tag: everything after it should stay ordinary
markdown, and the marker itself shows as source.

<div align="center"><div align="right">nested</div></div>

## After

A final paragraph, so the end of the document is not the end of a container.
