# workspace-fixtures

Test material for the Workspace client apps (macOS, iOS, Android, Linux) and
for the agents that build them: documents to open, render, edit and sync,
instead of each checkout inventing its own.

**What may be here:** nothing private. Only two kinds of file:

- files made by this project for testing: generated (the `.table` examples,
  the element sweep's Markdown) or written for a test;
- third-party material under an open-source licence, kept with that licence.
  The sets are Candy, the JSON Canvas spec's sample and the demo from Hesprs'
  JSON Canvas Viewer, all MIT (see their folders in
  [`Repositories/`](Repositories/)).

Anything else, such as personal notes, stock photos or brand logos, doesn't
belong here. Because of that rule, any of it can be bundled into an app build
or a test.

## Layout

| Folder | What's in it |
|---|---|
| [`Canvas/`](Canvas/) | single JSON Canvas files from the MIT sets in `Repositories/` |
| [`Markdown/`](Markdown/) | GFM and edge-case test files |
| [`Plaintext/`](Plaintext/) | plain `.txt` test files |
| [`Images/`](Images/) | images made for this repository, kept unedited for reuse (portraits of fictional people) |
| [`Repositories/`](Repositories/) | whole example sets whose canvases reference their notes and images (Candy, JSONCanvas, Hesprs), each with its licence |
| [`Fixtures/`](Fixtures/) | test fixtures, one folder per file type Workspace opens (`markdown/`, `canvas/`, `table/`) |

Each folder has a README saying what it holds and where it came from.

A test device seeded from an older copy may hold files that are no longer
here.

Sample **workspaces** will get their own top-level folder once there are some.

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
say in the commit where the material came from. A new kind of material gets a
new top-level folder with its own README.
