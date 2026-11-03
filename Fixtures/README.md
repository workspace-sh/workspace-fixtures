# Fixtures

Test fixtures for the Workspace apps and the libraries they use, one folder
per kind of file Workspace opens. A fixture is here because it exercises a
supported file type or a workspace, not because one repository happens to
test with it.

| Folder | File type | What's in it |
|---|---|---|
| [`markdown/`](markdown/) | Markdown (`.md`) | `Every Element.md` with its `pics/`, a long document (`large.md`), a short one (`welcome.md`), and `Table Embeds.md` and `Large Table Embeds.md`, which embed the tables in `table/`, each with its cases (`*.cases.json`) |
| [`canvas/`](canvas/) | JSON Canvas (`.canvas`) | the spec's every-node-type file, a sample, `org-chart.canvas`, an org chart whose portraits are in `portraits/`, and large canvases of 500, 2,000, 5,000 and 10,000 nodes (`big-*.canvas`) |
| [`table/`](table/) | `.table` | the example bundles, each as a folder and as a single file, large tables of 10,000, 50,000 and 1,000,000 rows as single files, and in `broken/` a file named `.table` that isn't one |
| [`textbundle/`](textbundle/) | TextBundle (`.textbundle`) and TextPack (`.textpack`) | a journal with images in four formats, as a folder, a standard pack and a flat pack; a web clip with its `sourceURL`; plain text; and packs that are damaged, unsafe or large |

Plain text (`.txt`) and workspaces (folders, and `.workspace` peer-to-peer
workspaces) get a folder here when they have a fixture. The folders at the top
of this repository (`Markdown/`, `Plaintext/`, `Images/`) are for trying by
hand; these are the files tests are written against.

## Where each one comes from

Most of these are still also kept in the repository whose tests read them.
Until those tests read this repository instead, **when an original changes,
update the copy here too.**

| Fixture | Original |
|---|---|
| `markdown/Every Element.md`, `markdown/pics/` | the workspace monorepo's `Fixtures/`; written by the markdown repository's element sweep (`scripts/callout-check/run.sh --emit-fixture <path>`) |
| `markdown/large.md` | markdown: `src/crates/core/tests/fixtures/large.md` |
| `markdown/welcome.md` | workspace: `apps/linux/tests/fixtures/welcome.md` |
| `markdown/Table Embeds.md`, `markdown/Large Table Embeds.md`, `table/broken/` | written here, for this repository; they have no original elsewhere |
| `markdown/*.cases.json` | written by table-file-format's `npm run fixtures:embed-cases -- <document>` from the document beside each, then read against the document's words; see Cases, below |
| `canvas/sample.canvas` | react-native-jsoncanvas: `src/core/__tests__/fixtures/sample.canvas` |
| `canvas/all-node-types.canvas` | react-native-jsoncanvas: `src/core/__tests__/spec-fixtures/all-node-types.canvas` |
| `canvas/org-chart.canvas`, `canvas/portraits/` | written here, inspired by the organisational chart in [Canvas Candy](https://github.com/TfTHacker/obsidian-canvas-candy) (MIT): its layout and roles, with plain text and file nodes in place of Candy's styling, and new names. The portraits are resized copies of [`Images/Portraits/`](../Images/Portraits/) (CC0; credits in [`Images/README.md`](../Images/README.md)) |
| `canvas/big-*.canvas`, `canvas/drawings/shapes.svg` | made by react-native-jsoncanvas's `npm run fixtures:canvas -- <this folder>` (`scripts/big-canvas.mts`): the canvases its renderer benchmark measures (`example/shared/generateCanvas.ts`, seeded, so the same on every run), with images from `portraits/` and `drawings/`. `shapes.svg` was drawn for this repository |
| `table/*.table` | table-file-format: `fixtures/` |
| `table/large/` | made by table-file-format's `scripts/big-table.mts`; see [`table/README.md`](table/README.md) |
| `textbundle/` | made by this repository's [`scripts/make-textbundles.py`](../scripts/make-textbundles.py) from [`Images/Field Notes/`](../Images/Field%20Notes/) and [`Images/Coast/`](../Images/Coast/); see [`textbundle/README.md`](textbundle/README.md) |

## Notes

- `markdown/Table Embeds.md` and `markdown/Large Table Embeds.md` embed
  views of the tables in `table/` by relative path (`../table/…`), so they
  need `table/` beside `markdown/`, and an app has to open `Fixtures/` (or a
  folder above it) for those paths to stay inside what was opened. Between
  them they hold links that must stay links, embeds that say how much to show
  (`rows=`, `cards=`, `rest=more`), a single file, a large table read through
  its index, and embeds that can't be drawn (a missing file, table and view,
  a file of two tables with no `table=`, a file that isn't a `.table`, and a
  path outside the folder).

- `markdown/Every Element.md` points at `pics/sample.png` beside it, and
  deliberately at a `../outside.png` that doesn't exist. Keep `pics/` next to
  it. It grows with the markdown repository's element sweep: it covers HTML
  `<img>`, `<p align>` and `<div align>` as well (workspace-sh/markdown#345).
- `table/large/` holds single-file `.table`s only; unzip one to get its
  folder.
- `canvas/big-*.canvas` are for camera speed (pinch, pan, zoom) and opening
  time with many nodes: groups of 5×5 cards, text cards with Markdown, link
  cards, an image every 97 nodes (the portraits and `drawings/shapes.svg`, by
  paths relative to the canvas) and edges between neighbours, some labelled.
  Keep `portraits/` and `drawings/` beside them. To change them, change the
  generator in react-native-jsoncanvas and write them again, so they stay the
  canvases the benchmark measures.

## Cases

Beside a document of embeds, `<name>.cases.json` lists each link in it to a
`.table`, in order, and what it should give, so every platform's tests check
the same cases:

```json
{ "line": "[Top tasks](../table/projects.table#table=tasks&view=All%20tasks%20by%20priority&rows=3&rest=more&embed=1 \"The three most urgent\")",
  "address": "../table/projects.table#table=tasks&view=All%20tasks%20by%20priority&rows=3&rest=more&embed=1",
  "expect": { "table": "tasks", "view": "All tasks by priority", "layout": "table", "rows": 8,
              "first": ["Land .table extension", "Markdown editor polish", "Wire RSD + StyleX"],
              "more": "Show 5 more rows" } }
```

`expect` is one of three things:

- **A view drawn:** its table, view and layout; how many rows the view holds;
  `first`, the first rows or cards drawn by their first field (up to five, or
  all the count shows when `rest=more` cuts the view; a board, each column's
  first card, or as many as it's cut to); `groups`, a grouped table's groups
  drawn or a board's columns, each with its count; and `more`, the line
  beneath a cut view, when it leaves anything out.
- **`problem`:** the words drawn in the embed's place, exactly.
- **`link: true`:** the link isn't an embed (it's in a sentence, a list or a
  quote, or says `embed=0`, or has no `embed`), and stays a link.

A platform's test opens `Fixtures/`, draws each case from `markdown/`, and
compares what it shows with `expect`. The `.table` library checks every case
in `packages/app/src/embedCases.test.ts`, on Linux in
`apps/linux/tests/embed-cases.test.tsx`, and on the web on its `#embed-test`
page. To add a case, add its link to a document, write the cases file again
with `npm run fixtures:embed-cases -- <document>` in a table-file-format
checkout, and read what it wrote against what the document says the case
should show.
