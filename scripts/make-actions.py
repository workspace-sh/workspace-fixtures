#!/usr/bin/env python3
"""Write Fixtures/actions/: every kind of Workspace action, in every format that holds one.

Actions are specified in workspace-protocol's docs/actions/ (reference.md
names every trigger, request and result; in-files.md says where each format
keeps them). This writes one document that uses all of them, the same as a
TextBundle and a TextPack, a JSON Canvas and a .table, and the files they
read. Each value says when it last ran, so whether an action ran can be seen
at a glance.

Run it again rather than editing a fixture by hand. It writes the same bytes
on every run (the TextPack's dates are fixed).

    python3 scripts/make-actions.py
"""

import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Fixtures" / "actions"

# A fixed time for the zip's entries, so the pack is the same bytes each run.
ZIP_TIME = (2026, 11, 28, 0, 0, 0)


def action(edn: str) -> str:
    """An action block, as a Markdown document holds one."""
    return f"<!--action\n{edn.strip()}\n-->"


def kept(ref: str, shown: str) -> str:
    """A place an action keeps a value, not run yet."""
    return f"<!--[kept {ref}]-->{shown}<!--[/kept]-->"


# Each section: a heading, what it shows, the places, and the actions they use.
# `bundle` False: left out of the TextBundle and TextPack, which can't read the
# files beside the folder they're in.
SECTIONS = [
    {
        "heading": "When the document opens",
        "about": "Runs once each time the document opens. Needs nothing, so nothing is asked.",
        "places": [
            ("Opened", kept("demo/opened", "not run yet")),
            ("Budget", kept("demo/total {:items [14400 4863 920]}", "not run yet")),
            ("Count", kept("demo/count {:items [3 1 4 1 5 9 2 6]}", "not run yet")),
        ],
        "actions": [
            '{:id :demo/opened :on :open\n :fn (fn [_ env ctx] {:keep (str "ran at " (env/now))})}',
            '{:id :demo/total :on :open\n :fn (fn [{:keys [items]} env ctx]\n       {:keep (str (env/format :currency (sum items)) " across " (count items) " · ran at " (env/now))})}',
            '{:id :demo/count :on :open\n :fn (fn [{:keys [items]} env ctx]\n       {:keep (str (env/format :number (sum items)) " from " (count items) " numbers · ran at " (env/now))})}',
        ],
    },
    {
        "heading": "Kept for a while",
        "about": "`:fresh \"PT2M\"`: runs on opening only when its value is more than two minutes old. Open, close and reopen within two minutes: the time doesn't change.",
        "places": [("Fresh", kept("demo/fresh", "not run yet"))],
        "actions": ['{:id :demo/fresh :on :open :fresh "PT2M"\n :fn (fn [_ env ctx] {:keep (str "ran at " (env/now))})}'],
    },
    {
        "heading": "From the web, once allowed",
        "about": "Asks first: one action, used in three places, each with its own input. Until it's allowed, each value shows what it last kept.",
        "places": [
            ("Dublin", kept('demo/place {:q "Dublin"}', "not looked up yet")),
            ("Lisbon", kept('demo/place {:q "Lisbon"}', "not looked up yet")),
            ("Kyoto", kept('demo/place {:q "Kyoto"}', "not looked up yet")),
        ],
        "actions": [
            '{:id :demo/place :on :open\n :needs {:fetch ["nominatim.openstreetmap.org"]}\n :fn (fn [{:keys [q]} env ctx]\n       (let [r (first (env/fetch "https://nominatim.openstreetmap.org/search" {:q q :format "json" :limit 1}))]\n         {:keep (str (get r :lat) ", " (get r :lon) " · fetched at " (env/now))}))}',
        ],
    },
    {
        "heading": "When you tap it",
        "about": "`:on :tap`: runs only when its value is tapped while reading.",
        "places": [("Tapped", kept("demo/tapped", "tap me"))],
        "actions": ['{:id :demo/tapped :on :tap\n :fn (fn [_ env ctx] {:keep (str "tapped at " (env/now))})}'],
    },
    {
        "heading": "On a clock",
        "about": "Runs while the document is open, when its time comes. A plain cron string, a cron map, and a single moment.",
        "places": [
            ("Every minute", kept("demo/minute", "not run yet")),
            ("Every five minutes", kept("demo/five", "not run yet")),
            ("Once, at midnight on 1 Jan 2027 in London", kept("demo/once", "waiting for 1 Jan 2027")),
        ],
        "actions": [
            '{:id :demo/minute :on [:cron "* * * * *"]\n :fn (fn [_ env ctx] {:keep (str "ticked at " (env/now))})}',
            '{:id :demo/five :on [:cron {:minute "*/5"} :tz "Europe/London"]\n :fn (fn [_ env ctx] {:keep (str "ticked at " (env/now))})}',
            '{:id :demo/once :on [:at "2027-01-01T00:00:00+00:00[Europe/London]"]\n :fn (fn [_ env ctx] {:keep (str "rang at " (env/now))})}',
        ],
    },
    {
        "heading": "When another file changes",
        "about": "Reads a file beside this one, and runs again when it changes. Asks first. Edit `Packing.txt` or `Budget.table` and come back.",
        "bundle": False,
        "places": [
            ("Packing list", kept("demo/packing", "not read yet")),
            ("Budget table", kept("demo/budget", "not read yet")),
            ("Canvas", kept("demo/canvas", "not read yet")),
        ],
        "actions": [
            '{:id :demo/packing :on [:change "Packing.txt"]\n :needs {:read ["Packing.txt"]}\n :fn (fn [_ env ctx] {:keep (str (env/read "Packing.txt") " · read at " (env/now))})}',
            '{:id :demo/budget :on [:change "Budget.table"]\n :needs {:read ["Budget.table"]}\n :fn (fn [_ env ctx]\n       (let [t (env/read "Budget.table")]\n         {:keep (str (env/format :currency (sum (map (fn [r] (get r :amount)) (get t :rows)))) " in " (count (get t :rows)) " rows · read at " (env/now))}))}',
            '{:id :demo/canvas :on [:change "Every Action.canvas"]\n :needs {:read ["Every Action.canvas"]}\n :fn (fn [_ env ctx] {:keep (str (count (get (env/read "Every Action.canvas") :nodes)) " nodes · read at " (env/now))})}',
        ],
    },
    {
        "heading": "Live, not saved",
        "about": "`{:show …}`: drawn on this device only, never written into the file. The file keeps what's between the markers; Workspace shows the live value over it.",
        "places": [
            ("Now", kept("demo/live", "shown live in Workspace")),
            ("Both", kept("demo/both", "kept, and shown live")),
        ],
        "actions": [
            '{:id :demo/live :on [:cron "* * * * *"]\n :fn (fn [_ env ctx] {:show (str "live at " (env/now))})}',
            '{:id :demo/both :on :open\n :fn (fn [_ env ctx] {:keep (str "kept at " (env/now)) :show (str "shown at " (env/now))})}',
        ],
    },
    {
        "heading": "What fails, and how",
        "about": "Each of these fails on purpose. Its value stays as it was, marked stale, and the reason is reported.",
        "places": [
            ("An expired certificate (error)", kept("demo/expired", "not fetched yet")),
            ("A host it didn't declare (refused)", kept("demo/undeclared", "not fetched yet")),
            ("A misspelt function (failed, with a suggestion)", kept("demo/typo {:items [1 2 3]}", "not run yet")),
            ("Too much work (limit or timeout)", kept("demo/forever", "not run yet")),
            ("Where this device is (denied: not answered yet)", kept("demo/where", "not located yet")),
            ("A question for you (denied: not answered yet)", kept("demo/ask", "not asked yet")),
        ],
        "actions": [
            '{:id :demo/expired :on :open\n :needs {:fetch ["expired.badssl.com"]}\n :fn (fn [_ env ctx] {:keep (str (env/fetch "https://expired.badssl.com/") " · fetched at " (env/now))})}',
            '{:id :demo/undeclared :on :open\n :needs {:fetch ["example.org"]}\n :fn (fn [_ env ctx] {:keep (str (env/fetch "https://example.com/") " · fetched at " (env/now))})}',
            '{:id :demo/typo :on :open\n :fn (fn [{:keys [items]} env ctx] {:keep (str (cuont items) " items")})}',
            '{:id :demo/forever :on :open\n :fn (fn [_ env ctx] {:keep (str (reduce + (range 100000000)))})}',
            '{:id :demo/where :on :open\n :needs {:locate true}\n :fn (fn [_ env ctx] {:keep (str (env/locate) " · located at " (env/now))})}',
            '{:id :demo/ask :on :open\n :needs {:ask true}\n :fn (fn [_ env ctx] {:keep (str (env/ask "Which colour?" ["red" "green"]) " · answered at " (env/now))})}',
        ],
    },
]

CODE_SECTION = """## Never run: written about, in code

A marker or an action inside code is text about actions, so it shows as written and nothing runs:

```markdown
Total: <!--[kept demo/total {:items [1 2]}]-->?<!--[/kept]-->
```

And inline: `<!--[kept demo/opened]-->not run<!--[/kept]-->`."""


def document(title: str, in_bundle: bool) -> str:
    parts = [
        f"# {title}",
        "Every kind of action Workspace runs, one section each. Every value says when it last ran, so it's clear whether its action ran. "
        "An action that's stopped leaves its last value in the file: a kept value is part of the document.",
    ]
    defs = []
    for s in SECTIONS:
        if not in_bundle or s.get("bundle", True):
            parts.append(f"## {s['heading']}")
            parts.append(s["about"])
            parts.extend(f"{label}: {place}" for label, place in s["places"])
            defs.extend(s["actions"])
    parts.append(CODE_SECTION)
    parts.extend(action(d) for d in defs)
    return "\n\n".join(parts) + "\n"


def canvas() -> dict:
    """A canvas whose text nodes keep values (in-files.md, JSON Canvas)."""
    node = lambda i, x, y, text, act=None: {
        "id": i,
        "type": "text",
        "x": x,
        "y": y,
        "width": 360,
        "height": 100,
        "text": text,
        **({"x-action": act} if act else {}),
    }
    return {
        "nodes": [
            node("title", 0, -160, "# Every action, on a canvas\nEach box below is kept by an action."),
            node("opened", 0, 0, "Opened: not run yet", "canvas/opened"),
            node("place", 400, 0, "Dublin: not looked up yet", "canvas/place"),
            node("minute", 0, 140, "Every minute: not run yet", "canvas/minute"),
            node("packing", 400, 140, "Packing list: not read yet", "canvas/packing"),
        ],
        "edges": [{"id": "e1", "fromNode": "title", "fromSide": "bottom", "toNode": "opened", "toSide": "top"}],
        "x-actions": {
            "canvas/opened": '{:id :canvas/opened :on :open :fn (fn [_ env ctx] {:keep (str "Opened: ran at " (env/now))})}',
            "canvas/place": '{:id :canvas/place :on :open :needs {:fetch ["nominatim.openstreetmap.org"]} :fn (fn [_ env ctx] (let [r (first (env/fetch "https://nominatim.openstreetmap.org/search" {:q "Dublin" :format "json" :limit 1}))] {:keep (str "Dublin: " (get r :lat) ", " (get r :lon) " · fetched at " (env/now))}))}',
            "canvas/minute": '{:id :canvas/minute :on [:cron "* * * * *"] :fn (fn [_ env ctx] {:keep (str "Every minute: ticked at " (env/now))})}',
            "canvas/packing": '{:id :canvas/packing :on [:change "Packing.txt"] :needs {:read ["Packing.txt"]} :fn (fn [_ env ctx] {:keep (str "Packing list: " (env/read "Packing.txt") " · read at " (env/now))})}',
        },
    }


def table(path: Path) -> None:
    """A .table whose fields keep values (in-files.md, .table): a lookup on an edit, and a time on opening."""
    t = path / "tables" / "places"
    (t / "rows").mkdir(parents=True)
    meta = {
        "format": "table",
        "formatVersion": 3,
        "title": "Every Action",
        "description": "Places whose coordinates are looked up when their city is edited, and a time kept as the table opens.",
        "tables": ["places"],
        "created_at": "2026-11-28T00:00:00Z",
        "modified_at": "2026-11-28T00:00:00Z",
    }
    schema = {
        "fields": [
            {"id": "f8city", "name": "city", "type": "string", "constraints": {"required": True}},
            {"id": "f8coords", "name": "coords", "type": "string", "x-action": "places/coords"},
            {"id": "f8opened", "name": "opened", "type": "string", "x-action": "places/opened"},
        ],
        "x-actions": {
            "places/coords": '{:id :places/coords :on [:edit "city"] :fresh "P30D" :needs {:fetch ["nominatim.openstreetmap.org"]} :fn (fn [{:keys [city]} env ctx] (let [r (first (env/fetch "https://nominatim.openstreetmap.org/search" {:q city :format "json" :limit 1}))] {:keep (str (get r :lat) ", " (get r :lon))}))}',
            "places/opened": '{:id :places/opened :on :open :fn (fn [_ env ctx] {:keep (str "ran at " (env/now))})}',
        },
    }
    rows = [
        {"id": "r1dublin", "city": "Dublin"},
        {"id": "r2lisbon", "city": "Lisbon"},
        {"id": "r3kyoto", "city": "Kyoto"},
    ]
    write(path / "meta.json", json.dumps(meta, indent=2) + "\n")
    write(t / "meta.json", json.dumps({"name": "places", "title": "Places"}, indent=2) + "\n")
    write(t / "schema.json", json.dumps(schema, indent=2, ensure_ascii=False) + "\n")
    write(t / "rows" / "0001.ndjson", "".join(json.dumps(r, separators=(",", ":")) + "\n" for r in rows))


def budget(path: Path) -> None:
    """A small .table the document reads, and runs again when it changes."""
    t = path / "tables" / "budget"
    (t / "rows").mkdir(parents=True)
    write(path / "meta.json", json.dumps({
        "format": "table", "formatVersion": 3, "title": "Budget", "tables": ["budget"],
        "created_at": "2026-11-28T00:00:00Z", "modified_at": "2026-11-28T00:00:00Z",
    }, indent=2) + "\n")
    write(t / "meta.json", json.dumps({"name": "budget", "title": "Budget"}, indent=2) + "\n")
    write(t / "schema.json", json.dumps({"fields": [
        {"id": "b8item", "name": "item", "type": "string"},
        {"id": "b8amount", "name": "amount", "type": "number"},
    ]}, indent=2) + "\n")
    rows = [("b1", "Flights", 412.5), ("b2", "Hotel", 690), ("b3", "Rail pass", 129)]
    write(t / "rows" / "0001.ndjson", "".join(json.dumps({"id": i, "item": n, "amount": a}, separators=(",", ":")) + "\n" for i, n, a in rows))


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def textpack(bundle: Path, pack: Path) -> None:
    with zipfile.ZipFile(pack, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(bundle.rglob("*")):
            if f.is_file():
                info = zipfile.ZipInfo(f"{bundle.name}/{f.relative_to(bundle).as_posix()}", ZIP_TIME)
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, f.read_bytes())


def main() -> None:
    # Everything but the README is made here, so it's made afresh.
    OUT.mkdir(parents=True, exist_ok=True)
    for f in OUT.iterdir():
        if f.name != "README.md":
            shutil.rmtree(f) if f.is_dir() else f.unlink()
    write(OUT / "Every Action.md", document("Every Action", in_bundle=False))
    # One line and no newline at its end: an action keeps what it reads as it is, and a newline would split the line it's kept in.
    write(OUT / "Packing.txt", "passport, charger, rain jacket")
    budget(OUT / "Budget.table")
    write(OUT / "Every Action.canvas", json.dumps(canvas(), indent=2, ensure_ascii=False) + "\n")
    table(OUT / "Every Action.table")
    bundle = OUT / "Every Action.textbundle"
    write(bundle / "info.json", json.dumps({"version": 2, "type": "net.daringfireball.markdown"}, indent=2) + "\n")
    write(bundle / "text.md", document("Every Action, in a TextBundle", in_bundle=True))
    textpack(bundle, OUT / "Every Action.textpack")
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
