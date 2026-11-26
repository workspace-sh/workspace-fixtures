# TextBundle and TextPack

[TextBundles](https://textbundle.org/spec/) (`.textbundle`, a folder) and TextPacks (`.textpack`, a zip of one): a Markdown or plain-text document with its images. Each fixture here tests something a reader has to get right.

All of them are made by [`scripts/make-textbundles.py`](../../scripts/make-textbundles.py) from the images in [`Images/Field Notes/`](../../Images/Field%20Notes/), [`Images/Coast/`](../../Images/Coast/) and [`Images/Portraits/`](../../Images/Portraits/). Change the script and run it again rather than editing a fixture by hand. It writes the same bytes on every run.

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
| `JPEG XL.textpack` | JPEG XL images (`.jxl`): a JPEG repacked losslessly (about 15% smaller, the identical JPEG recoverable), a lossy encode, a lossless encode of a PNG, the repacked one again by an HTML `<img>`, one cut short (Apple's decoder shows it full size, blank where data is missing), and a text file named `.jxl`, which shows its alt text. Made with libjxl's `cjxl`. |
| `Travel Journal.textpack` | Large: a week's journal with twelve photos enlarged to 3,072 px on the long side (17 MB), for timing opening and unzipping. |
| `Animated SVG.textbundle` | Animated SVG as a README shows it, in HTML `<img>` tags: twelve weather icons, twelve spinners and twelve loaders that all animate, and nineteen feature tests (CSS keyframes, steps, cubic-bezier, reduced motion; SMIL animate, set, animateTransform, animateMotion on a path, keySplines, discrete, accumulate, begin and freeze, a path morph), each labelled with what should move. Three test what must not happen: a tap starting an animation, `:hover`, and `<script>`. Made by [`scripts/make-animated-svg.py`](../../scripts/make-animated-svg.py) from [`Images/Animated SVG/`](../../Images/Animated%20SVG/), which says where each file came from and under what licence; each bundle carries those licences in `assets/licences/`. |
| `Animated SVG Spinners.textbundle` | Every spinner (46 with SMIL, the same 46 with CSS) and loader (12): 104 moving images. 23 of the SMIL spinners chain one animation off another, which a renderer may not support yet. |
| `Animated SVG Weather Fill.textbundle`, `… Line`, `… Flat`, `… Monochrome` | All 475 Meteocons weather icons in one style each: a stress test of hundreds of animated images in one document, of which only those on screen should draw. |
| `Animated SVG W3C Tests.textbundle` | The 74 W3C SVG 1.1 animation tests that use no script, one per section: a coverage reference, not a pass list. |

Images in a pack are stored, not compressed again, as most apps write them. The rest are deflated.
