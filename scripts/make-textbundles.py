#!/usr/bin/env python3
"""
Writes Fixtures/textbundle/ from the images in Images/Field Notes/ and
Images/Coast/: TextBundles (folders) and TextPacks (zips) that test what
a reader of them has to get right. See Fixtures/textbundle/README.md.

    python3 scripts/make-textbundles.py

Needs macOS (`sips`, for HEIC) and Pillow (for WebP). The output is the
same on every run: zip entries are sorted and dated 1 Nov 2026.
"""

import io
import json
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
FIELD = ROOT / "Images" / "Field Notes"
COAST = ROOT / "Images" / "Coast"
OUT = ROOT / "Fixtures" / "textbundle"
DATE = (2026, 11, 1, 0, 0, 0)

# ---------- Images ----------


def resized(src: Path, long_side: int) -> Image.Image:
    image = Image.open(src).convert("RGB")
    scale = long_side / max(image.size)
    size = (round(image.width * scale), round(image.height * scale))
    return image.resize(size, Image.LANCZOS)


def save_jpeg(image: Image.Image, dest: Path, quality: int = 88) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    image.save(dest, "JPEG", quality=quality, optimize=True)


def save_webp(image: Image.Image, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    image.save(dest, "WEBP", quality=85, method=6)


def save_heic(src: Path, dest: Path, long_side: int) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["sips", "-s", "format", "heic", "-Z", str(long_side), str(src), "--out", str(dest)],
        check=True, capture_output=True,
    )


def save_png(src: Path, dest: Path, long_side: int) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    resized(src, long_side).save(dest, "PNG", optimize=True)


# ---------- Bundles ----------


def write_info(bundle: Path, info: dict) -> None:
    (bundle / "info.json").write_text(json.dumps(info, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def fresh(bundle: Path) -> Path:
    if bundle.exists():
        shutil.rmtree(bundle)
    bundle.mkdir(parents=True)
    return bundle


def entries_of(folder: Path, prefix: str) -> list[tuple[str, Path | None]]:
    """A folder's files and folders as zip entry names, sorted, folders ending in /."""
    out: list[tuple[str, Path | None]] = []
    if prefix:
        out.append((prefix, None))
    for path in sorted(folder.rglob("*")):
        name = prefix + path.relative_to(folder).as_posix()
        out.append((name + "/", None) if path.is_dir() else (name, path))
    return out


def write_zip(dest: Path, entries: list[tuple[str, Path | bytes | None]]) -> None:
    """Writes entries as given (names kept exactly, `../` and all), dated DATE."""
    if dest.exists():
        dest.unlink()
    with zipfile.ZipFile(dest, "w") as zf:
        for name, source in entries:
            info = zipfile.ZipInfo(name, date_time=DATE)
            info.filename = name  # ZipInfo can tidy a name; these are meant as written
            info.external_attr = (0o40755 << 16) | 0x10 if name.endswith("/") else 0o100644 << 16
            if source is None:
                zf.writestr(info, b"")
                continue
            data = source if isinstance(source, bytes) else source.read_bytes()
            # Images are already compressed: stored, as most apps do.
            info.compress_type = zipfile.ZIP_STORED if name.lower().endswith((".jpg", ".png", ".heic", ".webp")) else zipfile.ZIP_DEFLATED
            zf.writestr(info, data)


def pack(bundle: Path, dest: Path, inside_folder: bool = True) -> None:
    """A TextPack of a bundle: the spec's form has the bundle's folder inside the zip."""
    prefix = bundle.name + "/" if inside_folder else ""
    write_zip(dest, entries_of(bundle, prefix))


# ---------- Texts ----------

FIELD_NOTES = """\
# Field Notes: the river walk

*Saturday, early.* Out of the door before six, with the mist still lying on the water meadows. The path follows the river for the first two miles, then climbs to the wall and the stile.

![A grey heron standing in the shallows at dawn](assets/heron.webp)

The heron was there again, in the same shallows below the weir, as still as a post. It let me get within twenty yards before it lifted off, legs trailing, and settled again further down.

## Along the bank

- Ferns just unfurling under the alders, the fronds still tight as fists.
- Meadowsweet not out yet. Another fortnight, perhaps.
- A kingfisher, a flash of blue, gone before I could look properly.

![An unfurling fern frond](assets/fern.heic)

![A kingfisher on a branch](assets/kingfisher.jpg)

## The wall

The dry-stone wall by the stile is more moss than stone now. Someone has rebuilt the top course since last year: the new stones are paler and have nothing growing on them yet.

![Moss on the wall by the stile](<assets/Café wall.jpg>)

| Mile | Where | Time |
|---:|---|---|
| 0 | Front door | 05:50 |
| 2 | Weir | 06:35 |
| 3 | Stile and wall | 07:05 |
| 5 | Bridge, and home | 08:10 |

## The route

I drew the route when I got back, so I can find the far bridge again.

<img src="assets/sketches/walk-map.png" alt="A pencil map of the walk: the river, the bridge and the hill" width="480">

- [x] Weir
- [x] Stile
- [ ] The far bridge (next time)

> Notes to self: start earlier, bring the long lens, and look for the kingfisher below the bridge, not above it.

The heron again, on the way home, as if it hadn't moved all morning:

![The heron again](assets/heron.webp)
"""

CLIPPED_ARTICLE = """\
# The Last Keepers

![A white lighthouse on a rocky headland at dusk](assets/lighthouse-dusk.jpg)

For more than a century, the light on the headland was kept by hand. Three keepers lived in the cottages below it, taking the night in watches: trimming the wick, winding the clockwork that turned the lens, and writing up the log at the end of each watch.

The last of them left in the spring of the year the light was automated. The lens still turns, but nobody climbs the hundred and twelve steps at dusk any more.

## A night's watch

The first watch began at sunset. The keeper lit the lamp, started the clockwork, and checked the light from the gallery before settling in the watch room with the log. Every two hours the weights had to be wound back up, and every hour the weather was written down: the wind, the sea, and how far the light could be seen.

## What is left

The cottages are holiday lets now. The log books went to the county archive, where anyone can read them: page after page of wind directions, the odd ship's name, and once, in pencil in the margin, *saw the whales again tonight*.
"""

PLAIN_NOTES = """\
Things to take on the coast walk

- waterproof
- flask
- the map (the folded one, not the book)
- binoculars
- something for the rock pools: a net, a bucket

Tide times for Saturday: low at 11:40, high at 17:55.
Bus back from the harbour at 18:20, the last one.
"""

NO_INFO = """\
# No info.json

This bundle has its text and nothing else: no `info.json`, which the spec asks for. A reader should still open it, as Markdown.
"""

UNSAFE = """\
# A pack with unsafe names

Besides this text, the pack holds entries named `../escape.png` and `/abs.png`. A reader must never write them outside the folder it unpacks into.
"""

TRAVEL = [
    ("Monday", "harbour", "We arrived on the evening train and walked straight down to the harbour. High tide, every boat afloat, and the light on the end of the pier just coming on."),
    ("Tuesday", "cliffs", "The coast path west, along the top of the cliffs. Hard going in places, and a long way down."),
    ("Tuesday", "beach-huts", "Down to the cove for lunch, past the beach huts. Somebody has painted theirs a different colour every year we've been."),
    ("Wednesday", "fishing-boats", "The boats were pulled up on the shingle this morning, nets drying, too rough to go out."),
    ("Wednesday", "market-stall", "Market day. Mackerel, crab and the first strawberries."),
    ("Thursday", "cafe-table", "Rain. The café on the corner, the window seat, and the best pastry in the town."),
    ("Thursday", "train-window", "The little branch line along the coast and back, for the view."),
    ("Friday", "rock-pools", "Low tide just before noon. Anemones, a shore crab the size of a saucer, and periwinkles everywhere."),
    ("Friday", "cottage-lane", "Back up through the town by the steep lane. Every cottage has a different door."),
    ("Friday", "sunset", "Sunset from the harbour wall, chips on our knees."),
    ("Saturday", "bookshop", "The bookshop by the steps: an hour in there and a bag of second-hand paperbacks."),
    ("Saturday", "lighthouse-night", "Last night. The lighthouse beam going round over the water as we walked back."),
]


def travel_text() -> str:
    lines = ["# Travel Journal: a week on the coast", ""]
    day = None
    for when, image, words in TRAVEL:
        if when != day:
            lines += [f"## {when}", ""]
            day = when
        alt = image.replace("-", " ")
        lines += [words, "", f"![{alt}](assets/{image}.jpg)", ""]
    lines += ["We'll be back next year. Same cottage, same week."]
    return "\n".join(lines) + "\n"


# ---------- The fixtures ----------


def field_notes(bundle: Path) -> None:
    fresh(bundle)
    (bundle / "text.md").write_text(FIELD_NOTES, encoding="utf-8")
    write_info(bundle, {
        "version": 2,
        "type": "net.daringfireball.markdown",
        "transient": False,
        "creatorIdentifier": "com.example.fieldnotes",
        # Another app's own keys: a reader saving the bundle keeps them.
        "com.example.fieldnotes": {"pinned": True, "tags": ["walks", "birds"], "colour": "moss"},
    })
    assets = bundle / "assets"
    save_webp(resized(FIELD / "heron.jpg", 1200), assets / "heron.webp")
    save_heic(FIELD / "fern.jpg", assets / "fern.heic", 1000)
    save_jpeg(resized(FIELD / "stone-wall.jpg", 1200), assets / "Café wall.jpg")
    save_png(FIELD / "walk-map.png", assets / "sketches" / "walk-map.png", 1200)
    # In the bundle, but not in the text.
    save_jpeg(resized(FIELD / "stone-wall.jpg", 400), assets / "unused.jpg")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    notes = OUT / "Field Notes.textbundle"
    field_notes(notes)
    pack(notes, OUT / "Field Notes.textpack")
    pack(notes, OUT / "Flat.textpack", inside_folder=False)
    # As the Finder's Compress writes one: the folder, plus a __MACOSX/ folder
    # of AppleDouble files (`._name`) beside it.
    apple_double = b"\x00\x05\x16\x07\x00\x02\x00\x00Mac OS X        " + bytes(10)
    finder = entries_of(notes, notes.name + "/")
    finder += [("__MACOSX/", None), (f"__MACOSX/{notes.name}/", None),
               (f"__MACOSX/{notes.name}/._text.md", apple_double), (f"__MACOSX/{notes.name}/._info.json", apple_double)]
    write_zip(OUT / "Finder.textpack", finder)

    article = fresh(OUT / "Clipped Article.textbundle")
    (article / "text.md").write_text(CLIPPED_ARTICLE, encoding="utf-8")
    write_info(article, {
        "version": 2,
        "type": "net.daringfireball.markdown",
        "creatorIdentifier": "com.example.clipper",
        "sourceURL": "https://example.com/articles/the-last-keepers",
    })
    save_jpeg(resized(COAST / "lighthouse-dusk.jpg", 1600), article / "assets" / "lighthouse-dusk.jpg")

    plain = fresh(OUT / "Plain Notes.textbundle")
    (plain / "text.txt").write_text(PLAIN_NOTES, encoding="utf-8")
    write_info(plain, {"version": 2, "type": "public.plain-text", "creatorIdentifier": "com.example.notes"})

    no_info = fresh(OUT / "No Info.textbundle")
    (no_info / "text.md").write_text(NO_INFO, encoding="utf-8")

    broken = OUT / "Broken.textpack"
    broken.write_bytes(b"This is not a zip file, whatever its name says.\n")

    tiny = io.BytesIO()
    Image.new("RGB", (8, 8), (200, 40, 40)).save(tiny, "PNG")
    write_zip(OUT / "Unsafe.textpack", [
        ("Unsafe.textbundle/", None),
        ("Unsafe.textbundle/info.json", json.dumps({"version": 2, "type": "net.daringfireball.markdown"}, indent=2).encode() + b"\n"),
        ("Unsafe.textbundle/text.md", UNSAFE.encode()),
        ("Unsafe.textbundle/assets/", None),
        ("../escape.png", tiny.getvalue()),
        ("/abs.png", tiny.getvalue()),
    ])

    # Large: twelve photos enlarged to 3,072 px on the long side, for timing
    # opening and unzipping. Built in a temporary folder: only the pack is kept.
    with tempfile.TemporaryDirectory() as tmp:
        journal = Path(tmp) / "Travel Journal.textbundle"
        journal.mkdir()
        (journal / "text.md").write_text(travel_text(), encoding="utf-8")
        write_info(journal, {"version": 2, "type": "net.daringfireball.markdown", "creatorIdentifier": "com.example.journal"})
        for _, image, _ in TRAVEL:
            save_jpeg(resized(COAST / f"{image}.jpg", 3072), journal / "assets" / f"{image}.jpg", quality=92)
        pack(journal, OUT / "Travel Journal.textpack")


if __name__ == "__main__":
    main()
