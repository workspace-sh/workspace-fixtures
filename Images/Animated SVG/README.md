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

## Still, and not yet

The bundles sort every set into three groups, and say which: **Animated**; **Not animated yet**, files that start one animation from another's beginning or end (`begin="a.end"`) or from a tap or hover, which the iOS player doesn't do yet, so some or all of each stays still; and **Still by design**, files with nothing in them to animate (Meteocons' flags, units and its crossed-out "not available" icon, N/A). The script decides from the file's text; the parser's own count below agrees with it except for a few W3C tests and one spinner that is only partly chained.

## What the current parser makes of them

Measured on 26 Nov 2026 with the markdown library's `svganim` crate (workspace-sh/markdown#481), parsing each file and drawing one frame:

- **Feature tests:** 16 animate. The three out-of-scope tests stay still, as they should.
- **SVG Spinners:** 69 of 92 animate. The other 23 start one animation from another's (`begin="a.end-0.5s"`, `begin="b.begin+0.1s"`), which the parser doesn't evaluate yet, so they are drawn still: `3-dots-bounce`, `3-dots-fade`, `3-dots-move`, `3-dots-scale`, `6-dots-scale`, `6-dots-scale-middle`, `bars-fade`, `bars-scale`, `bars-scale-fade`, `bars-scale-middle`, `blocks-scale`, `blocks-shuffle-2`, `blocks-shuffle-3`, `blocks-wave`, `bouncing-ball`, `pulse-2`, `pulse-3`, `pulse-multiple`, `pulse-rings-2`, `pulse-rings-3`, `pulse-rings-multiple`, `wifi` and `wifi-fade`.
- **SVG Loaders:** all 12 animate.
- **Meteocons:** 1,788 of 1,900 animate. The rest are drawn still by their author (flags, °C and °F, a beanie and so on).
- **W3C:** many tests chain animations the same way (`begin="0s; a.end + 1s"`), and many state what a pass looks like at a given second, so they are a coverage reference, not a pass list.
