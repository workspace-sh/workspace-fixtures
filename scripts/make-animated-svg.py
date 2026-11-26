#!/usr/bin/env python3
"""
Writes the animated SVG fixtures: the feature tests in
Images/Animated SVG/Feature tests/, then TextBundles in Fixtures/textbundle/
that show them and the openly licensed sets beside them in
Images/Animated SVG/. See Images/Animated SVG/README.md.

    python3 scripts/make-animated-svg.py

Needs nothing beyond Python 3. The output is the same on every run.

Images go in as HTML <img> tags, as READMEs write them: a renderer that
animates SVG has to do it there, and a markdown image is the plainer case.
"""

import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "Images" / "Animated SVG"
TESTS = SRC / "Feature tests"
OUT = ROOT / "Fixtures" / "textbundle"

# ---------- Feature tests (ours) ----------
#
# One feature each, labelled with what should be seen. 240 x 120, with a
# caption band, so a still frame says what was meant to move.


def card(title: str, expect: str, body: str, style: str = "") -> str:
    css = f"<style>{style}</style>" if style else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="240" height="120" viewBox="0 0 240 120">
{css}<rect width="240" height="120" rx="10" fill="#1f2433"/>
<rect y="92" width="240" height="28" rx="0" fill="#2b3245"/>
<text x="10" y="104" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="600" fill="#e8ecf4">{html.escape(title)}</text>
<text x="10" y="115" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="#9aa6bd">{html.escape(expect)}</text>
{body}
</svg>
"""


FEATURES = {
    # CSS animation
    "css-rotate": card(
        "CSS @keyframes: transform rotate",
        "The bar turns once every 2 s.",
        '<rect class="spin" x="70" y="42" width="100" height="10" rx="5" fill="#6ea8fe"/>',
        ".spin{transform-origin:120px 47px;animation:spin 2s linear infinite}"
        "@keyframes spin{to{transform:rotate(360deg)}}",
    ),
    "css-opacity": card(
        "CSS @keyframes: opacity",
        "The dot fades out and back every 1.5 s.",
        '<circle class="pulse" cx="120" cy="46" r="22" fill="#f78c6c"/>',
        ".pulse{animation:pulse 1.5s ease-in-out infinite}"
        "@keyframes pulse{50%{opacity:.1}}",
    ),
    "css-stroke-draw": card(
        "CSS: stroke-dashoffset (a line drawing itself)",
        "The wave draws from left to right, then starts again.",
        '<path class="draw" d="M20 60 Q50 10 80 50 T140 50 T200 40 T220 50" fill="none" '
        'stroke="#c3e88d" stroke-width="4" stroke-linecap="round" stroke-dasharray="300" stroke-dashoffset="300"/>',
        ".draw{animation:draw 2.5s ease-in-out infinite}"
        "@keyframes draw{to{stroke-dashoffset:0}}",
    ),
    "css-steps": card(
        "CSS: steps() timing",
        "The square jumps across in 5 steps, no glide.",
        '<rect class="step" x="20" y="34" width="24" height="24" fill="#c792ea"/>',
        ".step{animation:step 2s steps(5) infinite}"
        "@keyframes step{to{transform:translateX(175px)}}",
    ),
    "css-alternate": card(
        "CSS: cubic-bezier, alternate, delay",
        "Slides right and back, easing at each end; starts after 0.5 s.",
        '<circle class="slide" cx="30" cy="46" r="14" fill="#89ddff"/>',
        ".slide{animation:slide 1.2s cubic-bezier(.65,0,.35,1) .5s infinite alternate}"
        "@keyframes slide{to{transform:translateX(180px)}}",
    ),
    "css-fill-colour": card(
        "CSS @keyframes: fill colour",
        "The heart goes red, gold, blue and back every 3 s.",
        '<path class="tint" d="M120 78 L94 52 A15 15 0 0 1 120 30 A15 15 0 0 1 146 52 Z" fill="#ff5370"/>',
        ".tint{animation:tint 3s linear infinite}"
        "@keyframes tint{33%{fill:#ffcb6b}66%{fill:#82aaff}}",
    ),
    "css-reduced-motion": card(
        "CSS: prefers-reduced-motion",
        "Spins, unless Reduce Motion is on: then it stays still.",
        '<rect class="rm" x="100" y="26" width="40" height="40" rx="6" fill="#ffcb6b"/>',
        ".rm{transform-origin:120px 46px;animation:rm 1.5s linear infinite}"
        "@keyframes rm{to{transform:rotate(360deg)}}"
        "@media (prefers-reduced-motion: reduce){.rm{animation:none}}",
    ),
    # SMIL
    "smil-animate": card(
        "SMIL <animate>: an attribute (r, cx)",
        "The circle grows and moves right, then repeats.",
        '<circle cx="40" cy="46" r="8" fill="#6ea8fe">'
        '<animate attributeName="r" values="8;24;8" dur="2s" repeatCount="indefinite"/>'
        '<animate attributeName="cx" values="40;200;40" dur="4s" repeatCount="indefinite"/>'
        "</circle>",
    ),
    "smil-set": card(
        "SMIL <set>: visibility",
        "The text appears 1 s in and stays (fill=freeze).",
        '<text x="120" y="54" text-anchor="middle" font-family="system-ui, sans-serif" font-size="22" '
        'font-weight="700" fill="#c3e88d" visibility="hidden">Hello'
        '<set attributeName="visibility" to="visible" begin="1s" fill="freeze"/></text>',
    ),
    "smil-transform": card(
        "SMIL <animateTransform>: scale and rotate",
        "The star pulses in size while it turns.",
        '<g transform="translate(120 46)"><g>'
        '<path d="M0 -26 L7 -8 L26 -8 L11 4 L16 22 L0 11 L-16 22 L-11 4 L-26 -8 L-7 -8 Z" fill="#ffcb6b"/>'
        '<animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="4s" repeatCount="indefinite"/>'
        '</g><animateTransform attributeName="transform" type="scale" values="1;1.4;1" dur="1s" '
        'additive="sum" repeatCount="indefinite"/></g>',
    ),
    "smil-motion": card(
        "SMIL <animateMotion>: along a path, rotate=auto",
        "The arrow follows the loop and points the way it goes.",
        '<path id="loop" d="M40 46 C40 0 200 0 200 46 C200 92 40 92 40 46 Z" fill="none" stroke="#3a4257" stroke-width="2"/>'
        '<path d="M-9 -6 L9 0 L-9 6 Z" fill="#f78c6c">'
        '<animateMotion dur="4s" repeatCount="indefinite" rotate="auto"><mpath xlink:href="#loop"/></animateMotion></path>',
    ),
    "smil-keysplines": card(
        "SMIL: calcMode=spline, keySplines",
        "The ball drops and bounces with easing, not at a constant speed.",
        '<circle cx="120" cy="16" r="10" fill="#89ddff">'
        '<animate attributeName="cy" values="16;78;16" keyTimes="0;0.5;1" calcMode="spline" '
        'keySplines="0.5 0 1 1;0 0 0.5 1" dur="1.2s" repeatCount="indefinite"/></circle>',
    ),
    "smil-discrete": card(
        "SMIL: calcMode=discrete",
        "The colour changes in hard steps: red, green, blue.",
        '<rect x="90" y="20" width="60" height="52" rx="8" fill="#ff5370">'
        '<animate attributeName="fill" values="#ff5370;#c3e88d;#82aaff" calcMode="discrete" '
        'dur="3s" repeatCount="indefinite"/></rect>',
    ),
    "smil-accumulate": card(
        "SMIL: additive=sum, accumulate=sum",
        "Moves right in 4 hops of 40, each starting where the last ended.",
        '<rect x="20" y="34" width="24" height="24" fill="#c792ea">'
        '<animate attributeName="x" by="40" dur="0.75s" additive="sum" accumulate="sum" repeatCount="4" '
        'fill="freeze"/></rect>',
    ),
    "smil-begin-freeze": card(
        "SMIL: begin offset, fill=freeze",
        "Waits 1 s, slides right over 1 s, then stays there.",
        '<circle cx="30" cy="46" r="14" fill="#c3e88d">'
        '<animate attributeName="cx" from="30" to="210" begin="1s" dur="1s" fill="freeze"/></circle>',
    ),
    "smil-morph": card(
        "SMIL: path d morph",
        "A square turns into a diamond and back.",
        '<path fill="#82aaff" d="M95 21 L145 21 L145 71 L95 71 Z">'
        '<animate attributeName="d" dur="2s" repeatCount="indefinite" '
        'values="M95 21 L145 21 L145 71 L95 71 Z;M120 14 L152 46 L120 78 L88 46 Z;M95 21 L145 21 L145 71 L95 71 Z"/></path>',
    ),
    # Out of scope, as on GitHub: these show what a renderer should NOT do.
    "out-click-begin": card(
        "Out of scope: SMIL begin=click",
        "Stays still: no animation starts from a tap.",
        '<circle cx="120" cy="46" r="20" fill="#6c7891">'
        '<animate attributeName="r" values="20;30;20" begin="click" dur="1s" repeatCount="indefinite"/></circle>',
    ),
    "out-hover": card(
        "Out of scope: CSS :hover",
        "Grey, with no change on hover or tap.",
        '<rect class="hov" x="90" y="22" width="60" height="48" rx="8" fill="#6c7891"/>',
        ".hov:hover{fill:#ff5370}",
    ),
    "out-script": card(
        "Out of scope: <script>",
        "Grey. If it turns red, script ran, and it must not.",
        '<circle id="s" cx="120" cy="46" r="22" fill="#6c7891"/>'
        "<script>document.getElementById('s').setAttribute('fill','#ff5370')</script>",
    ),
}

# ---------- Bundles ----------

INFO = {"version": 2, "type": "net.daringfireball.markdown", "transient": False}


def img(src: str, alt: str, width: int) -> str:
    return f'<img src="assets/{src}" width="{width}" alt="{alt}" title="{alt}">'


def grid(files: list[tuple[str, str]], width: int, per_row: int) -> str:
    """Rows of images, one HTML paragraph per row."""
    rows = []
    for i in range(0, len(files), per_row):
        cells = " ".join(img(src, alt, width) for src, alt in files[i : i + per_row])
        rows.append(f"<p>\n{cells}\n</p>")
    return "\n\n".join(rows)


def name(path: Path) -> str:
    return path.stem.replace("-", " ")


def bundle(title: str, text: str, assets: dict[str, Path]) -> None:
    out = OUT / f"{title}.textbundle"
    if out.exists():
        shutil.rmtree(out)
    (out / "assets").mkdir(parents=True)
    (out / "info.json").write_text(json.dumps(INFO, indent=2) + "\n")
    (out / "text.md").write_text(text)
    for dest, src in sorted(assets.items()):
        target = out / "assets" / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, target)


SPINNERS = SRC / "SVG Spinners"
LOADERS = SRC / "SVG Loaders"
METEO = SRC / "Meteocons"
W3C = SRC / "W3C SVG 1.1"

CREDITS = {
    "spinners": "[SVG Spinners](https://github.com/n3r4zzurr0/svg-spinners) by Utkarsh Verma, MIT (`assets/licences/SVG Spinners.txt`)",
    "loaders": "[SVG Loaders](https://github.com/SamHerbert/SVG-Loaders) by Sam Herbert, MIT (`assets/licences/SVG Loaders.txt`)",
    "meteocons": "[Meteocons](https://github.com/basmilius/weather-icons) by Bas Milius, MIT (`assets/licences/Meteocons.txt`)",
    "w3c": "[W3C SVG 1.1 Second Edition test suite](https://www.w3.org/Graphics/SVG/Test/20110816/), W3C 3-clause BSD licence (`assets/licences/W3C.txt`); each file keeps its own copyright notice",
}
LICENCES = {
    "spinners": SPINNERS / "LICENSE",
    "loaders": LOADERS / "LICENSE.md",
    "meteocons": METEO / "LICENSE",
    "w3c": W3C / "LICENSE.txt",
}
LICENCE_NAMES = {"spinners": "SVG Spinners", "loaders": "SVG Loaders", "meteocons": "Meteocons", "w3c": "W3C"}


def licence_assets(*keys: str) -> dict[str, Path]:
    return {f"licences/{LICENCE_NAMES[k]}.txt": LICENCES[k] for k in keys}


def credits(*keys: str) -> str:
    return "## Credits\n\n" + "\n".join(f"- {CREDITS[k]}" for k in keys) + "\n"


def main() -> None:
    # Feature tests.
    TESTS.mkdir(parents=True, exist_ok=True)
    for key, svg in FEATURES.items():
        (TESTS / f"{key}.svg").write_text(svg)

    tests = sorted(TESTS.glob("*.svg"))
    smil = sorted((SPINNERS / "SMIL").glob("*.svg"))
    css = sorted((SPINNERS / "CSS").glob("*.svg"))
    loaders = sorted(LOADERS.glob("*.svg"))
    styles = ["fill", "line", "flat", "monochrome"]
    meteo = {s: sorted((METEO / s).glob("*.svg")) for s in styles}
    w3c = sorted(W3C.glob("*.svg"))

    # 1. The showcase: a few of the best, and every feature test.
    weather = ["clear-day", "partly-cloudy-day-rain", "thunderstorms-rain", "snow", "wind", "fog",
               "clear-night", "hurricane", "tornado", "sunrise", "umbrella", "starry-night"]
    spin = ["90-ring-with-bg", "270-ring-with-bg", "12-dots-scale-rotate", "8-dots-rotate", "3-dots-rotate",
            "gooey-balls-1", "gooey-balls-2", "dot-revolve", "ring-resize", "tadpole", "wind-toy", "clock"]
    load = ["audio", "ball-triangle", "grid", "hearts", "oval", "puff", "rings", "spinning-circles",
            "tail-spin", "three-dots", "bars", "circles"]
    assets: dict[str, Path] = {}
    for n in weather:
        assets[f"weather/{n}.svg"] = METEO / "fill" / f"{n}.svg"
    for n in spin:
        assets[f"spinners/{n}.svg"] = SPINNERS / "SMIL" / f"{n}.svg"
    for n in load:
        assets[f"loaders/{n}.svg"] = LOADERS / f"{n}.svg"
    for t in tests:
        assets[f"tests/{t.name}"] = t
    assets.update(licence_assets("spinners", "loaders", "meteocons"))
    feature_rows = "\n\n".join(
        f"<p>\n{img(f'tests/{t.name}', t.stem, 240)}\n</p>" for t in tests
    )
    text = f"""# Animated SVG

Animated SVGs as a README shows them, in HTML `<img>` tags. Everything below should move, except the three in **Out of scope**, which test that a renderer does not run script or react to a tap or hover (GitHub doesn't either).

Larger sets, for stress and coverage: `Animated SVG Spinners`, the four `Animated SVG Weather` bundles and `Animated SVG W3C Tests`.

## Weather

{grid([(f"weather/{n}.svg", n.replace("-", " ")) for n in weather], 96, 4)}

## Spinners

{grid([(f"spinners/{n}.svg", n.replace("-", " ")) for n in spin], 48, 6)}

## Loaders

These are white on transparent: on a light page they are hard to see, which is part of the test.

{grid([(f"loaders/{n}.svg", n.replace("-", " ")) for n in load], 56, 6)}

## Feature tests

Each names the feature it uses and what should be seen. A still frame is a failure, except where it says so.

{feature_rows}

{credits("meteocons", "spinners", "loaders")}
The feature tests were written for this repository.
"""
    bundle("Animated SVG", text, assets)

    # 2. Every spinner and loader.
    assets = {f"smil/{p.name}": p for p in smil}
    assets.update({f"css/{p.name}": p for p in css})
    assets.update({f"loaders/{p.name}": p for p in loaders})
    assets.update(licence_assets("spinners", "loaders"))
    text = f"""# Animated SVG Spinners

{len(smil)} spinners animated with SMIL, the same {len(css)} animated with CSS, and {len(loaders)} loaders. Every one should move.

## SVG Spinners, SMIL

{grid([(f"smil/{p.name}", name(p)) for p in smil], 48, 6)}

## SVG Spinners, CSS

The same shapes again, driven by `@keyframes` instead.

{grid([(f"css/{p.name}", name(p)) for p in css], 48, 6)}

## SVG Loaders

White on transparent.

{grid([(f"loaders/{p.name}", name(p)) for p in loaders], 56, 6)}

{credits("spinners", "loaders")}"""
    bundle("Animated SVG Spinners", text, assets)

    # 3. Every weather icon, one bundle per style: hundreds of moving images
    # in one document, for timing and memory.
    for style in styles:
        files = meteo[style]
        assets = {p.name: p for p in files}
        assets.update(licence_assets("meteocons"))
        text = f"""# Animated SVG Weather, {style}

All {len(files)} Meteocons weather icons in the {style} style. Every one is animated with SMIL. A stress test: only what is on screen should be drawing.

{grid([(p.name, name(p)) for p in files], 64, 5)}

{credits("meteocons")}"""
        bundle(f"Animated SVG Weather {style.capitalize()}", text, assets)

    # 4. The W3C SVG 1.1 animation tests that use no script.
    assets = {p.name: p for p in w3c}
    assets.update(licence_assets("w3c"))
    rows = "\n\n".join(f"### {p.stem}\n\n<p>\n{img(p.name, p.stem, 320)}\n</p>" for p in w3c)
    text = f"""# Animated SVG W3C Tests

The {len(w3c)} animation tests from the W3C SVG 1.1 Second Edition test suite that use no script (`animate-*`). Each was written for a browser: many say what a pass looks like in the image itself, often at a given second, and some rely on fonts or events a document view doesn't have. A coverage reference, not a pass list.

{rows}

{credits("w3c")}"""
    bundle("Animated SVG W3C Tests", text, assets)


if __name__ == "__main__":
    main()
