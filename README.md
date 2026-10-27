# workspace-fixtures

Test material for the Workspace client apps (macOS, iOS, Android, Linux) and
for the agents that build them: documents to open, render, edit and sync,
instead of each checkout inventing its own.

**What may be here:** only files this project made, for testing: generated
(the `.table` examples, the element sweep's Markdown, the portraits) or written
for a test. Each is ours to offer, and the folder's README says how it was made.

Nothing else belongs here: no third-party files, even under an open licence,
and nothing private. A file whose source and licence can't be confirmed is
removed. Because of that rule, any of it can be bundled into an app build or a
test. Useful material elsewhere is linked below instead.

## Layout

| Folder | What's in it |
|---|---|
| [`Markdown/`](Markdown/) | GFM and edge-case test files |
| [`Plaintext/`](Plaintext/) | plain `.txt` test files |
| [`Images/`](Images/) | images made for this repository, kept unedited for reuse (portraits of fictional people) |
| [`Fixtures/`](Fixtures/) | test fixtures, one folder per file type Workspace opens (`markdown/`, `canvas/`, `table/`) |

Each folder has a README saying what it holds and where it came from.

A test device seeded from an older copy may hold files that are no longer
here.

Sample **workspaces** will get their own top-level folder once there are some.

## Elsewhere

Open material worth testing against, kept in its own repositories:

- [JSON Canvas](https://github.com/obsidianmd/jsoncanvas): the spec and its
  sample canvas (MIT).
- [Canvas Candy](https://github.com/TfTHacker/obsidian-canvas-candy): styled
  example canvases for Obsidian (MIT; some images in it are under other terms).
  `Fixtures/canvas/org-chart.canvas` is modelled on its organisational chart.
- [JSON Canvas Viewer](https://github.com/Hesprs/JSON-Canvas-Viewer): a demo
  canvas with every node type and edge style (MIT).

## Using it

Clone it beside the other repositories:

```sh
git clone git@github.com:workspace-sh/workspace-fixtures.git
```

```
Projects/workspace/
  workspace/            the app monorepo
  Research/markdown/
  Research/react-native-jsoncanvas/
  workspace-fixtures/   this repository
```

`.gitattributes` turns off line-ending conversion for every file, so what you
check out is exactly what was committed. Don't reformat or "fix" a fixture: the
odd ones are odd on purpose.

## Adding material

Add files to the matching folder, keep names as they are on the devices, and
say in the folder's README and the commit how the material was made. Third-party
material is linked from **Elsewhere**, not copied in. A new kind of material gets a
new top-level folder with its own README.
