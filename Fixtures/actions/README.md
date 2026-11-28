# Actions

Workspace actions in every format that holds one: small functions a document carries, which keep a value in it or show one live. They're specified in workspace-protocol's `docs/actions/` (`reference.md` names every trigger, request and result; `in-files.md` says where each format keeps them).

Every value says when it last ran, so whether its action ran can be seen at a glance. An action that's stopped leaves its last value in the file, because a kept value is part of the document.

All of these but this README are made by [`scripts/make-actions.py`](../../scripts/make-actions.py). Change the script and run it again rather than editing a fixture by hand.

| Fixture | What it has |
|---|---|
| `Every Action.md` | One section for each kind: on opening; `:fresh` (kept for a while); fetching from the web, one action in three places with their own inputs; on a tap; on a clock (a cron string, a cron map with a zone, and one moment); on a change to another file, reading text, a `.table` and a canvas; `{:show …}` (live, never saved) and keep and show together; and every way a run fails: an expired certificate (`error`), a host it didn't declare (`refused`), a misspelt function (`failed`), too much work (`timeout`), and `env/locate` and `env/ask`, which apps don't answer yet (`denied`). It ends with a marker and an action in code, which never run. |
| `Every Action.textbundle`, `Every Action.textpack` | The same document as a TextBundle and a TextPack, without the section that reads files beside it. |
| `Every Action.canvas` | Text nodes kept by actions: on opening, from the web, every minute, and on a change to `Packing.txt`. |
| `Every Action.table` | Places whose `coords` are looked up when their `city` is edited (`[:edit "city"]`, kept 30 days), and an `opened` time kept as the table opens. |
| `Packing.txt`, `Budget.table` | What the document and the canvas read. Edit them to make the actions that watch them run again. |

Run through the engine on 28 Nov 2026 with every action allowed: each ran, waited or failed as its section says.
