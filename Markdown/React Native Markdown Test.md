# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6

Heading 1 (setext)
==================

Heading 2 (setext)
------------------

## Paragraphs + line breaks

A regular paragraph spanning multiple source lines should join into one rendered line on screen. A hard break inside a paragraph (trailing backslash) forces a real newline.\\
Second line of the same paragraph, after the hard break.

## Inline formatting

**Strong text**, *emphasised text*, ~~struck-through text~~, and inline `code()` in a sentence. Combinations: **bold with *italic* inside**, *italic with `code` inside*, ~~struck **bold** struck~~.

Links: [explicit link](https://commonmark.org), bare-URL autolink https://github.com/kivikakk/comrak, and an email autolink test@example.com.

Reference-style links resolve against definitions elsewhere in the document: a [full reference][cmref], a [collapsed reference][], and a [shortcut reference]. The definition lines themselves render nothing.

[cmref]: https://commonmark.org
[collapsed reference]: https://spec.commonmark.org
[shortcut reference]: https://github.github.com/gfm/

## Inline HTML

Raw inline HTML styling tags map onto native text styles: H<sub>2</sub>O and E = mc<sup>2</sup>, press <kbd>Cmd</kbd>+<kbd>S</kbd>, some <mark>highlighted</mark> text, plus <b>bold</b>, <i>italic</i>, <u>underline</u>, <s>struck</s>, and <code>inline code</code>. A forced<br>line break sits mid-sentence. Unknown tags such as <span>this span</span> drop the tag but keep their text.

## Block HTML

Block-level HTML chrome is stripped to its content. The wrapper tags below drop away; the summary label and the body markdown render as normal prose:

<details>
<summary>Click to expand</summary>

Hidden **body** content with a [link](https://commonmark.org).

</details>

<!-- This HTML comment renders nothing at all. -->

## Lists

### Bullet list

- one
- two
- three
  - nested 3.1
  - nested 3.2
    - deeply nested 3.2.1

### Ordered list

1. first
2. second
3. third

### Mixed nesting

1. ordered parent
   - bullet child
   - another bullet child
2. ordered sibling

### Multi-paragraph list item

- First item, paragraph one.

  First item, paragraph two — a blank line between paragraphs but still inside the same list item.

- Second item.

### Task list (GFM)

- [x] done
- [x] also done
- [ ] still pending
- [ ] another todo

## Blockquotes

> A blockquote on a single line.

> A blockquote
> spread across multiple lines
> that wraps as one paragraph.

> Nested:
>
> > one level deeper
> >
> > > two levels deeper

A table nested inside a blockquote flattens to readable prose (per-row, cells separated by a dot, header bold) rather than the per-segment grid used for top-level tables:

> | Col A | Col B |
> |-------|-------|
> | 1     | 2     |
> | 3     | 4     |

## Images

Remote image with `remoteImagePolicy="prompt"` on the view: ![the Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png). The first render shows a tappable chip ("Load <alt>") in place of the image; tapping the chip fires `onImagePrompt` so the host can decide whether to fetch. A broken URL: ![broken](https://example.invalid/missing.png) — once you tap-allow it the chip swaps to a broken-image badge with the alt text.

Inline images sit in a line of text and render at text height — ![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png) — and more than one can share a line: ![Octocat](https://github.githubassets.com/images/icons/emoji/octocat.png) ![Yaktocat](https://octodex.github.com/images/yaktocat.png). A block image on its own line renders at natural size, clamped to the viewport width:

![Yaktocat](https://octodex.github.com/images/yaktocat.png)

An image wrapped in a link stays tappable: [![Yaktocat](https://octodex.github.com/images/yaktocat.png "Octodex")](https://octodex.github.com/).

An HTML `<img>` with explicit dimensions: <img alt="Octocat" src="https://octodex.github.com/images/yaktocat.png" width="120" height="80" />.

A reference-style image resolves against a definition elsewhere in the document: ![Yaktocat][yak].

[yak]: https://octodex.github.com/images/yaktocat.png "Yaktocat"

## Alerts (GitHub-flavoured)

> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.

## Code blocks

Fenced with a language hint:

```rust
fn main() {
    println!("hello, comrak");
}
```

Another language to show per-language highlighting:

```ts
// a typed greeting
const answer: number = 42;
function greet(name: string): string {
  return "hello, " + name;
}
```

Fenced without a language hint:

```
plain fenced block
no syntax shown
```

Indented code block (four-space prefix):

    let x = 42;
    x + 1

## Thematic break

Above the line.

---

Below the line.

## Tables (GFM)

| Feature       | Status   | Notes                        |
|:--------------|:--------:|-----------------------------:|
| Headings      | yes      | h1 – h6, ATX + setext        |
| Inline code   | yes      | `backticked()`               |
| Tables        | yes      | per-cell, alignment-honoured |
| Footnotes     | yes      | comrak resolves refs         |
| Task lists    | yes      | rendered as checkboxes       |

A deliberately wide table to exercise `tableOverflow="scroll"` (set on the
`<Markdown>` view below): columns size to their content and the grid
scrolls sideways rather than cramming every column into the screen width.
Switch the prop to `"wrap"` (the default) to constrain the table to the
viewport and wrap each cell instead.

| ID  | Name              | Department   | Location       | Start date | Status   | Manager         | Email                   |
|-----|-------------------|--------------|----------------|------------|----------|-----------------|-------------------------|
| 001 | Ada Lovelace      | Engineering  | London, UK     | 2021-03-01 | Active   | Charles Babbage | ada@example.com         |
| 002 | Alan Turing       | Research     | Manchester, UK | 2020-06-15 | Active   | Max Newman      | alan@example.com        |
| 003 | Grace Hopper      | Compilers    | Arlington, US  | 2019-01-20 | On leave | Howard Aiken    | grace@example.com       |
| 004 | Katherine Johnson | Aerospace    | Hampton, US    | 2018-11-05 | Active   | Dorothy Vaughan | katherine@example.com   |

## Footnotes

Comrak parses CommonMark[^cm] and the GFM extension set[^gfm] — see the Notes section at the bottom of the document for the resolved definitions.

[^cm]: CommonMark — the strongly specified, highly compatible Markdown spec: https://commonmark.org
[^gfm]: GitHub Flavoured Markdown: tables, strikethrough, task lists, autolinks, footnotes.
