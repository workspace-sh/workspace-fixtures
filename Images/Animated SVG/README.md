# Animated SVG

Animated SVGs for testing renderers that play CSS animation and SMIL: the files the [`Animated SVG` TextBundles](../../Fixtures/textbundle/) show. [`scripts/make-animated-svg.py`](../../scripts/make-animated-svg.py) writes `Feature tests/` and the bundles; everything else here is kept exactly as it came from its source.

Unlike the rest of this repository, most of these files were not made for it. They are here because a renderer is only tested properly against SVGs written by other people, and every one is under a permissive licence that allows redistribution, with its licence beside it. Each bundle carries the licences of what it holds in `assets/licences/` and credits them in its text.

| Folder | Files | Source | Licence |
|---|---|---|---|
| `Feature tests/` | 19 | Written for this repository by the script: one animation feature each, labelled with what should be seen. Three test what must **not** happen: a tap starting an animation, `:hover`, and `<script>`. | Same as this repository |
| `Complex/` | 3 | Written for this repository by the script: an orrery (nested orbits, a moon, a breathing halo, twinkling stars), an equaliser (18 bars on eased splines and a morphing waveform) and an assembly (an outline drawing itself, a fill, a tick and a caption in sequence). Supported features only, so all three should move throughout. | Same as this repository |
| `SVG Spinners/SMIL/`, `SVG Spinners/CSS/` | 46 + 46 | [n3r4zzurr0/svg-spinners](https://github.com/n3r4zzurr0/svg-spinners) at `abfa05c` (6 Mar 2023): the same spinners animated with SMIL and with CSS | MIT, `SVG Spinners/LICENSE` |
| `SVG Loaders/` | 12 | [SamHerbert/SVG-Loaders](https://github.com/SamHerbert/SVG-Loaders) at `561eaca` (2 Jan 2025): white on transparent | MIT, `SVG Loaders/LICENSE.md` |
| `Meteocons/fill`, `line`, `flat`, `monochrome` | 475 each | [Meteocons](https://github.com/basmilius/weather-icons), the npm package `@meteocons/svg` 0.1.0 (the repository builds them; the package is what it publishes) | MIT, `Meteocons/LICENSE` (from the repository at `70dfb1d`) |
| `W3C SVG 1.1/` | 74 | The `animate-*` tests of the [W3C SVG 1.1 Second Edition test suite](https://www.w3.org/Graphics/SVG/Test/20110816/) (archive of 16 Aug 2011) that use no `<script>`; the four that do were left out | [W3C 3-clause BSD](https://www.w3.org/Consortium/Legal/2008/03-bsd-license), `W3C SVG 1.1/LICENSE.txt`. W3C offers its test suites under it for software development and testing; each file keeps its copyright notice |

## Still, and why

The bundles sort every set into up to three groups, and say which: **Animated**; **Waits for a tap or hover**, files that start an animation on a click, a hover or focus (`begin="click"`), which an image in a page never gets, on GitHub or here, so some or all of each stays still; and **Still by design**, files with nothing in them to animate (Meteocons' flags, units and its crossed-out "not available" icon, N/A). The script decides from the file's text.

## What the parser makes of them

Measured on 26 Nov 2026 with the markdown library's `svganim` crate, parsing each file and drawing frames:

- **Feature tests:** 16 animate. The three out-of-scope tests stay still, as they should.
- **Complex:** all three animate.
- **SVG Spinners:** all 92 animate. A quarter of the SMIL ones start one animation off another's begin or end (`begin="a.end-0.5s"`), which svganim works out ahead, looping for ever where the chain loops.
- **SVG Loaders:** all 12 animate.
- **Meteocons:** 1,788 of 1,900 animate. The rest are drawn still by their author.
- **W3C:** 65 of 74 animate in part or whole; the nine that don't wait for an event. Many tests state what a pass looks like at a given second, so they are a coverage reference, not a pass list.
