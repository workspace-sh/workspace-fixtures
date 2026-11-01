# TextBundle and TextPack

[TextBundles](https://textbundle.org/spec/) (`.textbundle`, a folder) and TextPacks (`.textpack`, a zip of one): a Markdown or plain-text document with its images. Each fixture here tests something a reader has to get right.

All of them are made by [`scripts/make-textbundles.py`](../../scripts/make-textbundles.py) from the images in [`Images/Field Notes/`](../../Images/Field%20Notes/) and [`Images/Coast/`](../../Images/Coast/). Change the script and run it again rather than editing a fixture by hand. It writes the same bytes on every run.

| Fixture | What it tests |
|---|---|
| `Field Notes.textbundle` | A Markdown journal saved by another app, with that app's own keys in `info.json`: a save must keep them. Its images are WebP, HEIC, JPEG and PNG, and include: one with a space and an accent in its name (`assets/Café wall.jpg`, linked as `<…>`); one in a subfolder, shown by an HTML `<img>`; one shown twice; one in `assets/` that the text never uses; and one the text links to that isn't there (`assets/kingfisher.jpg`). It also has a table, a task list and a quote. |
| `Field Notes.textpack` | The same bundle zipped as the spec says, with the `Field Notes.textbundle/` folder inside the zip. |
| `Flat.textpack` | The same bundle zipped without the folder (`info.json`, `text.md` and `assets/` at the top of the zip), as some apps write them. |
| `Finder.textpack` | The same bundle as the Finder's Compress zips it: the folder, plus a `__MACOSX/` folder of AppleDouble files beside it, which a reader passes over. |
| `Clipped Article.textbundle` | A web clip: its `info.json` has a `sourceURL` (`https://example.com/…`), so a reader can say where the text came from. One wide image at the top. |
| `Plain Notes.textbundle` | Plain text: `text.txt`, with `type` `public.plain-text`, and no `assets/`. |
| `No Info.textbundle` | No `info.json` at all, which the spec asks for: still opens, as Markdown. |
| `Broken.textpack` | Not a zip, whatever its name says: unreadable, not missing. |
| `Unsafe.textpack` | A valid pack, plus entries named `../escape.png` and `/abs.png`. A reader must never write them outside the folder it unpacks into. |
| `Travel Journal.textpack` | Large: a week's journal with twelve photos enlarged to 3,072 px on the long side (17 MB), for timing opening and unzipping. |

Images in a pack are stored, not compressed again, as most apps write them. The rest are deflated.
