# Fixtures

Test fixtures for the Workspace apps and the libraries they use, one folder
per kind of file Workspace opens. A fixture is here because it exercises a
supported file type or a workspace, not because one repository happens to
test with it.

| Folder | File type | What's in it |
|---|---|---|
| [`markdown/`](markdown/) | Markdown (`.md`) | `Every Element.md` with its `pics/`, a long document (`large.md`), a short one (`welcome.md`), and `Table Embeds.md`, which embeds the tables in `table/` |
| [`canvas/`](canvas/) | JSON Canvas (`.canvas`) | the spec's every-node-type file, a sample, and `org-chart.canvas`, an org chart whose portraits are in `portraits/` |
| [`table/`](table/) | `.table` | the five example bundles, each as a folder and as a single file, and large tables of 10,000, 50,000 and 1,000,000 rows as single files |

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
| `markdown/Table Embeds.md` | written here, for this repository; it has no original elsewhere |
| `canvas/sample.canvas` | react-native-jsoncanvas: `src/core/__tests__/fixtures/sample.canvas` |
| `canvas/all-node-types.canvas` | react-native-jsoncanvas: `src/core/__tests__/spec-fixtures/all-node-types.canvas` |
| `canvas/org-chart.canvas`, `canvas/portraits/` | written here, inspired by the organisational chart in [Canvas Candy](https://github.com/TfTHacker/obsidian-canvas-candy) (MIT): its layout and roles, with plain text and file nodes in place of Candy's styling, and new names. The portraits are resized copies of [`Images/Portraits/`](../Images/Portraits/) (CC0; credits in [`Images/README.md`](../Images/README.md)) |
| `table/*.table` | table-file-format: `fixtures/` |
| `table/large/` | made by table-file-format's `scripts/big-table.mts`; see [`table/README.md`](table/README.md) |

## Notes

- `markdown/Table Embeds.md` embeds views of `table/projects.table` and
  `table/crm.table` by relative path (`../table/…`), so it needs `table/`
  beside `markdown/`, and an app has to open `Fixtures/` (or a folder above
  it) for those paths to stay inside what was opened. It also holds links
  that must stay links, embeds that say how much to show (`rows=`,
  `cards=`, `rest=more`), and embeds that can't be drawn (a missing file, table and
  view, and a path outside the folder).

- `markdown/Every Element.md` points at `pics/sample.png` beside it, and
  deliberately at a `../outside.png` that doesn't exist. Keep `pics/` next to
  it. It grows with the markdown repository's element sweep: it covers HTML
  `<img>`, `<p align>` and `<div align>` as well (workspace-sh/markdown#345).
- `table/large/` holds single-file `.table`s only; unzip one to get its
  folder.
