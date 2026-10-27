# A Document for Integration Testing

This fixture is intentionally large enough (≈10 KB) to exercise the
incremental parsing path across multiple block boundaries, fenced code
blocks, lists with nested children, links, blockquotes, and a small table.

## Headings of Various Depths

### Third level

#### Fourth level

##### Fifth level

###### Sixth level

Plain paragraphs separate the headings to avoid the parser collapsing them.

A paragraph with **bold**, *italic*, ***both***, `inline code`, and a
[link to nowhere](https://example.invalid/).

## Lists

### Unordered list with nesting

- Item one
- Item two
  - Nested two-A
  - Nested two-B
    - Triple-nested
- Item three with `code` and a [link](https://example.invalid/)

### Ordered list

1. First step
2. Second step
3. Third step

## Fenced Code Blocks

A small Rust block:

```rust
fn fibonacci(n: u32) -> u64 {
    let mut a: u64 = 0;
    let mut b: u64 = 1;
    for _ in 0..n {
        let next = a + b;
        a = b;
        b = next;
    }
    a
}
```

Some shell:

```bash
#!/usr/bin/env bash
set -euo pipefail

for f in *.md; do
    wc -l "$f"
done
```

A JSON example:

```json
{
    "name": "rsdmd-core",
    "version": "0.1.0",
    "depends_on": ["ropey", "tree-sitter", "tree-sitter-md"]
}
```

## Blockquotes

> A short quoted paragraph that spans
> two visual lines but is one logical
> block.
>
> A second quoted paragraph inside the
> same blockquote.

> ## A heading inside a blockquote
>
> With body text following.

## A Small Table

| Crate            | Role        | Stage       |
| ---------------- | ----------- | ----------- |
| `rsdmd-core`     | Buffer      | Implemented |
| `rsdmd-jsi`      | Bridge      | Stub        |
| `rsdmd-wasm`     | Bridge      | Stub        |

## A Long Paragraph

The portable core is designed so the same parsing and editing primitives can
be exposed to React Native (via JSI) and to the web (via WASM) without
rewriting the underlying logic. This means every public type must be
synchronous, must avoid borrowed return values, and must use byte offsets
rather than character or line/column coordinates so the binding crates can
forward arguments without translation. The text buffer is a rope so that
in-place edits stay cheap even on large documents; the parser is
tree-sitter, configured with the canonical `tree-sitter-md` grammar, fed
directly from the rope's chunk iterator so that no edit ever materialises
the full document as a `String`.

## Mixed Content Section

Paragraph with [a link][ref-link] using a reference, and then another
[inline link](https://example.invalid/another).

[ref-link]: https://example.invalid/ref

> A blockquote that contains a list:
>
> - Quoted item one
> - Quoted item two
>
> And a code span: `let x = 42;`

## End

The fixture ends with a single trailing newline — POSIX correct.
