#!/usr/bin/env python3
"""make_toggle48_report.py — INPUT -> CORNER DETECT -> ALL ROUND | ALL SHARP review page.

Reads <dir>/corners48.json (core/detect.py), <dir>/toggle.json and the round/ + sharp/ SVGs
(core/toggle.py) plus the input icons, and writes <dir>/toggle48_report.html: one row of four
panels per icon, with markers for what changed. <dir> is outputs/solo48 (whole-set runs) or
outputs/ (partial runs), whichever ran last; round_corner_processing.py and
sharp_corner_processing.py rebuild the page at the end of every run.

  python3 reports/make_toggle48_report.py
  python3 reports/make_toggle48_report.py --dir outputs --input input/solo48/svg
"""

import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))   # corner_processing/: import core
import argparse
import json
import os
import tempfile
import xml.etree.ElementTree as ET

from core.paths import ROOT
from core import locks
from core.svg_io import DEFAULT_INPUT, iter_skeleton_shapes, localname
from _shared import default_dir, filled_markup

GEOM_ATTRS = ("d", "x", "y", "width", "height", "rx", "ry", "cx", "cy", "r",
              "x1", "y1", "x2", "y2", "points", "stroke-linecap",   # per-path caps (sharp output)
              "stroke-miterlimit")


def shapes_of(path, uid=None):
    """The drawing's shapes as SVG strings. A sharp output's own mitre limit and its tip-cut clip
    path (--miter keyshape) are kept: a <g> around the shapes, the clip renamed per page (uid)."""
    root = ET.parse(path).getroot()
    clip = next((el for el in root.iter() if localname(el.tag) == "clipPath"), None)
    in_clip = set(clip.iter()) if clip is not None else set()
    skel = [el for el in iter_skeleton_shapes(root) if el not in in_clip]
    out = filled_markup(root, {id(el) for el in skel}, GEOM_ATTRS, in_clip)     # under the strokes
    for el in skel:
        attrs = " ".join(f'{a}="{el.get(a)}"' for a in GEOM_ATTRS if el.get(a) is not None)
        out.append(f"<{localname(el.tag)} {attrs}/>")
    g = {}
    if root.get("stroke-miterlimit") not in (None, "2"):
        g["stroke-miterlimit"] = root.get("stroke-miterlimit")
    if clip is not None and uid:
        cp = next(el for el in clip.iter() if localname(el.tag) == "path")
        out.insert(0, f'<clipPath id="cut-{uid}"><path d="{cp.get("d")}" clip-rule="evenodd"/></clipPath>')
        g["clip-path"] = f"url(#cut-{uid})"
    if g:
        head = " ".join(f'{k}="{v}"' for k, v in g.items())
        out = [s for s in out if s.startswith("<clipPath")] + [f"<g {head}>"] + \
              [s for s in out if not s.startswith("<clipPath")] + ["</g>"]
    return out


REVIEW_DIR = os.path.join(ROOT, "review")
DECISION_COL = {"redraw input": "input", "adjust round output": "round", "adjust sharp output": "sharp",
                "keep": "sharp", "corner": "sharp", "round or sharp": "sharp"}


def load_review():
    """{icon: review entry} from review/status.json, each with its latest decision from decisions.jsonl."""
    out = {}
    sp = os.path.join(REVIEW_DIR, "status.json")
    if os.path.exists(sp):
        for e in json.load(open(sp, encoding="utf-8"))["icons"]:
            if e["status"] != "todo":
                out[e["icon"]] = {k: e.get(k) for k in ("status", "note", "claim", "reviewed")}
    dp = os.path.join(REVIEW_DIR, "decisions.jsonl")
    if os.path.exists(dp):
        for line in open(dp, encoding="utf-8"):
            if line.strip():
                d = json.loads(line)
                out.setdefault(d["icon"], {"status": "proposed", "note": d.get("why", "")})["decision"] = d
    for e in out.values():          # ok = the outputs stay as processed: an earlier proposal no longer holds
        if e["status"] == "ok":
            e.pop("decision", None)
    return out


def proposed_shapes(path, paths, uid=None):
    """The drawing at `path` with a decision's path changes applied ({id: {old, new}}): its shapes, as shapes_of."""
    tree = ET.parse(path)
    done = 0
    by_d = {" ".join(c["old"].split()): c for c in paths.values() if c.get("old")}   # id-less shapes ("path#7")
    for el in tree.getroot().iter():
        c = paths.get(el.get("id") or "") or (by_d.get(" ".join(el.get("d", "").split())) if not el.get("id") else None)
        if c and el.get("d") is not None:
            el.set("d", c["new"])
            done += 1
    if not done:
        return None
    fd, tmp = tempfile.mkstemp(suffix=".svg")
    os.close(fd)
    try:
        tree.write(tmp)
        return shapes_of(tmp, uid)
    finally:
        os.remove(tmp)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None, help="the run's output folder (default: outputs/solo48 or "
                                                "outputs/, whichever ran last)")
    ap.add_argument("--input", default=DEFAULT_INPUT)
    ap.add_argument("--out", help="default: <dir>/toggle48_report.html")
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--names", help="only the icons listed in this file (one name per line), "
                                    "e.g. a smaller page to publish")
    ap.add_argument("--keyshapes", help="each icon's SOLO48 keyshape (core/keyshape.py), drawn as a dashed "
                                        "guide (default: <dir>/keyshapes.json)")
    ap.add_argument("--previous", help="outputs of the previous update (round/ sharp/): icons whose output differs "
                                       "get a 'Changed in last update' filter and a before plate (default: <dir>/previous)")
    cfg = ap.parse_args(argv)
    cfg.dir = cfg.dir or default_dir()
    cfg.out = cfg.out or os.path.join(cfg.dir, "toggle48_report.html")
    cfg.keyshapes = cfg.keyshapes or os.path.join(cfg.dir, "keyshapes.json")
    cfg.previous = cfg.previous or os.path.join(cfg.dir, "previous")

    det = json.load(open(os.path.join(cfg.dir, "corners48.json")))
    tog = json.load(open(os.path.join(cfg.dir, "toggle.json")))
    ks = json.load(open(cfg.keyshapes)) if os.path.exists(cfg.keyshapes) else {}
    icons, missing = [], []
    reviews = load_review()
    only = set(open(cfg.names).read().split()) if cfg.names else None
    for name, v in sorted(tog["icons"].items()):
        if only is not None and name not in only:
            continue
        built = [m for m in ("round", "sharp")
                 if m in v and os.path.exists(os.path.join(cfg.dir, m, name))]
        if name not in det or not built or not os.path.exists(os.path.join(cfg.input, name)):
            missing.append(name)                   # input re-fetched without it, or a half-finished run
            continue
        # round and sharp are separate runs here: an icon may have only one of them so far
        out = {m: (v[m] if m in built else {"log": [], "after": None, "check": None}) for m in ("round", "sharp")}
        icons.append({
            "name": name,
            "input": shapes_of(os.path.join(cfg.input, name)),
            "round": shapes_of(os.path.join(cfg.dir, "round", name)) if "round" in built else None,
            "sharp": shapes_of(os.path.join(cfg.dir, "sharp", name), name[:-4]) if "sharp" in built else None,
            "res": det[name], "rlog": out["round"]["log"], "slog": out["sharp"]["log"],
            "before": v["before"], "rafter": out["round"]["after"], "safter": out["sharp"]["after"],
            "check": {m: out[m]["check"]["status"] if out[m]["check"] else "none" for m in out},
            "detail": {m: out[m]["check"] for m in out},
            "fp": locks.fingerprint(name, cfg.input, cfg.dir),
            "ks": ks.get(name),
            "keep": v.get("shared_keep", []),
        })
        rv = reviews.get(name)
        if rv:
            dec = rv.get("decision") or {}
            col = DECISION_COL.get(dec.get("decision"))
            if col and dec.get("paths"):
                src = os.path.join(cfg.input, name) if col == "input" else os.path.join(cfg.dir, col, name)
                rv["fix"] = {"col": col, "shapes": proposed_shapes(src, dec["paths"], name[:-4] + "-fix" if col == "sharp" else None)}
            icons[-1]["review"] = rv
        prev = {}
        for m in built:
            old = os.path.join(cfg.previous, m, name)
            if os.path.exists(old) and open(old, "rb").read() != \
                    open(os.path.join(cfg.dir, m, name), "rb").read():
                prev[m] = shapes_of(old)
        if prev:
            icons[-1]["prev"] = prev
    data = json.dumps({"icons": icons, "bands": tog["bands"], "fallback": tog["fallback"],
                       "group_tol": tog["group_tol"], "corner_max_r": tog.get("corner_max_r", 8),
                       "miter": tog.get("miter", "slice"), "subtitle": cfg.subtitle,
                       "input": os.path.relpath(cfg.input, ROOT), "dir": os.path.relpath(cfg.dir, ROOT),
                       "locks": locks.load()},
                      separators=(",", ":"))
    html = TEMPLATE.replace("__DATA__", data.replace("</", "<\\/"))
    with open(cfg.out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {cfg.out} ({len(icons)} icons, {len(html) // 1024} KB)")
    if missing:
        print(f"  left out {len(missing)} icon(s) in toggle.json without their input or output SVG: "
              f"{', '.join(missing[:5])}{' ...' if len(missing) > 5 else ''}")
    locks.warn(locks.changed_locks(names={ic["name"] for ic in icons}, input_dir=cfg.input,
                                   out_dir=cfg.dir))


TEMPLATE = r"""<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Corner48 Round and Sharp</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: a pipeline strip per icon — four 48-grid plates left to right (input, detect,
   all round, all sharp) under a sticky column header; summary ledger and rules on top. */
:root {
  --bg: #eef1f4; --panel: #ffffff; --ink: #18202b; --muted: #5b6676; --line: #d5dbe3;
  --grid: #e6eaef; --stroke: #c9d1db; --ghost: #9fb4d6; --accent: #1f5fbf;
  --sharp: #d23a2f; --round: #0f8a6c; --junction: #5c6b80; --kink: #c77a00; --curve: #7b4fc9;
  --chip: #e6ebf1; --ok: #0f8a6c; --warn: #b26a00; --bad: #c02f25; --keyshape: #e8760c;
  --f-display: "IBM Plex Sans Condensed", "Arial Narrow", system-ui, sans-serif;
  --f-body: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --f-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #11161d; --panel: #18202a; --ink: #e4e9f0; --muted: #94a0b1; --line: #2a3442;
  --grid: #1f2833; --stroke: #3a4656; --ghost: #4d6a96; --accent: #6ea4ff;
  --sharp: #ff6b5f; --round: #3fcf9f; --junction: #9aabc2; --kink: #f0a531; --curve: #a888f0;
  --chip: #222c38; --ok: #3fcf9f; --warn: #f0a531; --bad: #ff6b5f; --keyshape: #ff9a3d; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #11161d; --panel: #18202a; --ink: #e4e9f0; --muted: #94a0b1; --line: #2a3442;
  --grid: #1f2833; --stroke: #3a4656; --ghost: #4d6a96; --accent: #6ea4ff;
  --sharp: #ff6b5f; --round: #3fcf9f; --junction: #9aabc2; --kink: #f0a531; --curve: #a888f0;
  --chip: #222c38; --ok: #3fcf9f; --warn: #f0a531; --bad: #ff6b5f; --keyshape: #ff9a3d; color-scheme: dark }
* { box-sizing: border-box }
body { background: var(--bg); color: var(--ink); font: 14px/1.5 var(--f-body); margin: 0 }
.wrap { max-width: 1180px; margin: 0 auto; padding-inline: 20px; padding-block: 28px 64px; display: grid; gap: 26px }
h1, h2, h3 { font-family: var(--f-display); font-weight: 600; text-wrap: balance; margin: 0 }
h1 { font-size: 30px; letter-spacing: -.01em }
h2 { font-size: 18px }
h3 { font-size: 15px }
.eyebrow { font: 500 11px/1 var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted) }
.lede { color: var(--muted); max-width: 74ch; margin: 6px 0 0 }
.lede code { font: 12px var(--f-mono); color: var(--ink) }
header { display: grid; gap: 8px }
.num { font-family: var(--f-mono); font-variant-numeric: tabular-nums }

.stages { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px }
@media (max-width: 820px) { .stages { grid-template-columns: repeat(2, minmax(0, 1fr)) } }
.stage { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 14px 16px; display: grid; gap: 8px; align-content: start; min-width: 0 }
.stage .k { font: 500 11px var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted) }
.stage .v { font: 600 26px/1 var(--f-mono); font-variant-numeric: tabular-nums }
.stage ul { margin: 0; padding: 0; list-style: none; display: grid; gap: 4px; font-size: 13px; color: var(--muted) }
.stage li { display: flex; justify-content: space-between; gap: 10px }
.stage li b { color: var(--ink); font: 500 13px var(--f-mono); font-variant-numeric: tabular-nums }

.rules { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 12px }
.rule { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 14px 16px; display: grid; gap: 6px; align-content: start }
.rule p { margin: 0; color: var(--muted); font-size: 13px }

.controls { display: flex; flex-wrap: wrap; gap: 8px; align-items: center }
.chipbtn { font: 500 13px var(--f-body); color: var(--ink); background: var(--chip); border: 1px solid transparent; border-radius: 999px; padding: 5px 12px; cursor: pointer }
.chipbtn[aria-pressed="true"] { background: var(--ink); color: var(--panel) }
.chipbtn:focus-visible, input:focus-visible, label:focus-within { outline: 2px solid var(--accent); outline-offset: 2px }
.controls input[type=search] { font: 13px var(--f-body); color: var(--ink); background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 6px 10px; min-width: 0; flex: 1 1 160px; max-width: 240px }
.sw { display: inline-flex; align-items: center; gap: 6px; font-size: 13px; color: var(--muted); cursor: pointer; border-radius: 6px; padding: 2px 4px }
.legend { display: flex; flex-wrap: wrap; gap: 14px; font-size: 12px; color: var(--muted) }
.legend span { display: inline-flex; align-items: center; gap: 6px }
.dot { width: 9px; height: 9px; border-radius: 50%; flex: none; display: inline-block }
.ring { width: 10px; height: 10px; border-radius: 50%; flex: none; display: inline-block; border: 2px solid }

.colhead { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; position: sticky; top: env(safe-area-inset-top, 0px);
           z-index: 4; background: var(--bg); padding-block: 8px; border-bottom: 1px solid var(--line) }
.colhead div { font: 600 12px var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted); display: flex; gap: 8px; align-items: center }
.colhead div::after { content: "→"; color: var(--line); margin-left: auto }
.colhead div:nth-child(2)::after { content: "⇉" }
.colhead div:nth-child(n+3)::after { content: "" }
.rows { display: grid; gap: 14px }
.row { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 12px; display: grid; gap: 10px; min-width: 0 }
.rowhead { display: flex; flex-wrap: wrap; gap: 6px 12px; align-items: baseline }
.rowhead .nm { font: 500 13px var(--f-mono); overflow-wrap: anywhere }
.tag { font: 500 11px var(--f-body); background: var(--chip); color: var(--muted); border-radius: 4px; padding: 1px 6px; white-space: nowrap }
.tag.ok { color: var(--ok) } .tag.warn { color: var(--warn) } .tag.bad { color: var(--bad) }
.plates { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px }
@media (max-width: 640px) { .colhead { display: none } }
.plate { display: grid; gap: 4px; min-width: 0 }
.plate svg { width: 100%; height: auto; aspect-ratio: 1; display: block; max-width: 100%; border: 1px solid var(--line); border-radius: 6px; background: var(--panel) }
.plate .cap { font: 12px var(--f-mono); color: var(--muted); font-variant-numeric: tabular-nums; min-height: 1.5em }
.plate .lbl { display: none; font: 600 11px var(--f-mono); letter-spacing: .06em; text-transform: uppercase; color: var(--muted) }
@media (max-width: 640px) { .plate .lbl { display: block } }
details.log summary { cursor: pointer; font-size: 12px; color: var(--muted) }
.tw { overflow-x: auto }
table { border-collapse: collapse; width: 100%; font: 12px var(--f-mono); font-variant-numeric: tabular-nums; margin-top: 6px }
th { text-align: left; font: 600 11px var(--f-body); letter-spacing: .04em; text-transform: uppercase; color: var(--muted); padding: 3px 8px; border-bottom: 1px solid var(--line); white-space: nowrap }
td { padding: 3px 8px; border-bottom: 1px solid var(--line); white-space: nowrap }
.empty { color: var(--muted); padding: 24px 0 }
/* pager */
/* grid view: one tile per icon - original, round, final sharp */
.rows.tiles { grid-template-columns: repeat(auto-fill, minmax(min(100%, var(--tile, 210px)), 1fr)); gap: 10px }
body:not(.view-grid) .gridctl { display: none }
.view-grid .rowctl, .view-grid .legend { display: none }
.rows.tiles.one .tp, .rows.tiles.one .tl { grid-template-columns: minmax(0, 1fr) }
.rows.tiles.show-input .tp > :not(:nth-child(1)), .rows.tiles.show-input .tl > :not(:nth-child(1)),
.rows.tiles.show-round .tp > :not(:nth-child(2)), .rows.tiles.show-round .tl > :not(:nth-child(2)),
.rows.tiles.show-sharp .tp > :not(:nth-child(3)), .rows.tiles.show-sharp .tl > :not(:nth-child(3)) { display: none }
.rows.tiles.small .tl, .rows.tiles.small .tg { display: none }
.rows.tiles.small .tile { padding: 5px; gap: 4px }
.rows.tiles.small .tile .tn { font-size: 10px; min-height: 2.6em }
.tile { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 8px; display: grid; gap: 6px; min-width: 0; cursor: pointer }
.tile:hover, .tile:focus-visible { border-color: var(--accent) }
.tile .tn { font: 500 11.5px var(--f-mono); overflow-wrap: anywhere; color: var(--ink); min-height: 2.8em; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden }
.tile .tp { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px }
.tile .tp svg { width: 100%; height: auto; aspect-ratio: 1; display: block; border: 1px solid var(--line); border-radius: 4px; background: var(--panel) }
.tile .tp .fx svg { border: 2px solid var(--accent) }
.tile .tl { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4px; font: 10px var(--f-mono); color: var(--muted); text-align: center }
.tile .tg { display: flex; flex-wrap: wrap; gap: 4px }
.tile .tg .tag { font-size: 10.5px }
.view-grid .colhead { display: none }
.pager { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; padding-block: 8px; font-size: 13px; color: var(--muted) }
.pager .pg { font: 500 13px var(--f-mono); font-variant-numeric: tabular-nums; min-width: 34px; color: var(--ink); background: var(--chip);
             border: 1px solid transparent; border-radius: 6px; padding: 4px 9px; cursor: pointer }
.pager .pg[aria-current="page"] { background: var(--ink); color: var(--panel) }
.pager .pg:disabled { opacity: .4; cursor: default }
.pager .pg:focus-visible, .pager select:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }
.pager .gap { padding-inline: 2px }
.pager .info { margin-left: auto; font-variant-numeric: tabular-nums }
.pager select { font: 13px var(--f-body); color: var(--ink); background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 3px 6px }

/* drawing */
.g-grid { stroke: var(--grid); stroke-width: .08 }
.g-ks { fill: none; stroke: var(--keyshape); stroke-width: .25; stroke-dasharray: 1 .8; opacity: .9 }
.hide-ks .g-ks { display: none }
.tag.ks { color: var(--keyshape); background: transparent; border: 1px dashed var(--keyshape); font-family: var(--f-mono) }
.tag.ksover { color: var(--keyshape); background: transparent; border: 1px solid var(--keyshape); font-weight: 600 }
.sw select { font: 13px var(--f-body); color: var(--ink); background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 3px 6px }
.tag.ks.none { color: var(--muted); border-color: var(--line) }
.g-icon { fill: none; stroke: var(--ink); stroke-width: 4; stroke-linecap: round; stroke-linejoin: round }
.g-icon.sharp { stroke-linecap: butt; stroke-linejoin: miter; stroke-miterlimit: 2 }
.g-ghost { fill: none; stroke: var(--ghost); stroke-width: .35; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: .9 .6 }
.g-ink { fill: none; stroke: var(--stroke); stroke-width: 4; stroke-linecap: round; stroke-linejoin: round }
.g-cl { fill: none; stroke: var(--ink); stroke-width: .22; stroke-linecap: round; stroke-linejoin: round; opacity: .55 }
.g-curve { fill: none; stroke: var(--curve); stroke-width: .7; stroke-linecap: round; opacity: .85 }
.g-circ { fill: none; stroke: var(--round); stroke-width: .22; stroke-dasharray: .7 .5 }
.g-leg { fill: none; stroke: var(--round); stroke-width: .2; stroke-dasharray: .5 .4 }
.g-roundarc { fill: none; stroke: var(--round); stroke-width: .9; stroke-linecap: round }
.g-apex { fill: var(--panel); stroke: var(--round); stroke-width: .3 }
.g-sharp { fill: var(--sharp); stroke: var(--panel); stroke-width: .3 }
.g-junc { fill: var(--junction); stroke: var(--panel); stroke-width: .25 }
.g-kink { fill: var(--kink); stroke: var(--panel); stroke-width: .25 }
.m-rounded { fill: none; stroke: var(--round); stroke-width: .45 }
.m-reduced { fill: none; stroke: var(--warn); stroke-width: .45 }
.m-skipped { fill: none; stroke: var(--bad); stroke-width: .45; stroke-linecap: round }
.m-kept { fill: none; stroke: var(--muted); stroke-width: .3; stroke-dasharray: .5 .4 }
.m-sharp { fill: var(--sharp); stroke: var(--panel); stroke-width: .3 }
.m-lab { font: 600 2.1px var(--f-mono); text-anchor: middle; fill: var(--round); paint-order: stroke; stroke: var(--panel); stroke-width: .45 }
.m-lab.warn { fill: var(--warn) }
.m-lab.kept { fill: var(--muted) }
.hide-markers .mk { display: none }
.hide-radius .m-lab { display: none }
/* lock in */
.lockbar { display: flex; flex-wrap: wrap; gap: 8px 14px; align-items: center; font-size: 13px; color: var(--muted);
           background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 10px 14px }
.lockbar.alert { border-color: var(--bad); color: var(--ink) }
.lockbar .warnt { color: var(--bad); font-weight: 600 }
.lockbar .mode { font: 12px var(--f-mono) }
.lockbar code { font: 12px var(--f-mono); background: var(--chip); border-radius: 4px; padding: 1px 5px }
.lbtn { font: 500 12px var(--f-body); color: var(--ink); background: var(--chip); border: 1px solid var(--line); border-radius: 6px; padding: 3px 10px; cursor: pointer }
.lbtn.primary { background: var(--ok); border-color: var(--ok); color: var(--panel) }
.lbtn.danger { color: var(--bad) }
.lbtn:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }
.lbtn:disabled { opacity: .5; cursor: default }
.lockctl { margin-left: auto; display: inline-flex; gap: 6px; align-items: center; flex-wrap: wrap }
.tag.lock { color: var(--ok); background: transparent; border: 1px solid var(--ok) }
.row.locked { border-color: var(--ok) }
.row.pending { border-color: var(--warn); box-shadow: inset 4px 0 0 var(--warn) }
.tag.pend { color: var(--warn); background: transparent; border: 1px solid var(--warn) }
.lbtn.warnb { color: var(--warn) }
.pendnote { display: flex; gap: 6px; font-size: 13px; color: var(--warn); background: color-mix(in srgb, var(--warn) 10%, var(--panel)); border-radius: 6px; padding: 6px 10px }
.prevrow { padding-top: 8px; border-top: 1px dashed var(--line) }
.revrow { display: grid; gap: 8px; padding-top: 10px; border-top: 1px dashed var(--line) }
.revhead { display: flex; flex-wrap: wrap; gap: 6px 10px; align-items: baseline; font-size: 13px }
.revhead .who { font: 12px var(--f-mono); color: var(--muted) }
.revnote { margin: 0; font-size: 13px; color: var(--ink); max-width: 90ch }
.revcorners { margin: 0; padding-left: 18px; font: 12px var(--f-mono); color: var(--muted) }
.tag.rv-ok { color: var(--ok); background: transparent; border: 1px solid var(--ok) }
.tag.rv-proposed { color: var(--accent); background: transparent; border: 1px solid var(--accent) }
.tag.rv-needs-user { color: var(--panel); background: var(--warn) }
.tag.rv-decided, .tag.rv-applied { color: var(--panel); background: var(--ok) }
.tag.rv-reviewing { color: var(--muted); background: transparent; border: 1px dashed var(--muted) }
.row.rv-needs-user { box-shadow: inset 4px 0 0 var(--warn) }
.row.rv-proposed { box-shadow: inset 4px 0 0 var(--accent) }
.plate.fix svg { border: 2px solid var(--accent) }
.plate.fix.none { visibility: hidden }
.chipbtn.st-rv { box-shadow: inset 0 0 0 1px var(--accent) }
.g-dec { fill: none; stroke: var(--accent); stroke-width: .5 }
.plate.prev svg { opacity: .8; border-style: dashed }
.hide-prevsharp .plate.prev.p-sharp { visibility: hidden }
.hide-prevsharp .prevrow.only-sharp { display: none }
.plate.prev.none { align-content: center; justify-items: center; border: 1px dashed var(--line); border-radius: 6px; aspect-ratio: 1 }
.prevnote { font: 12px var(--f-body); color: var(--accent); align-self: center }
.tag.chg { color: var(--accent); background: transparent; border: 1px solid var(--accent) }
.chipbtn.st-lastchange, .chipbtn.st-lastready { box-shadow: inset 0 0 0 1px var(--accent) }
.chipsep { width: 1px; align-self: stretch; background: var(--line); margin-inline: 4px }
.chipbtn.st-ready { box-shadow: inset 0 0 0 1px var(--muted) }
.chipbtn.st-locked { box-shadow: inset 0 0 0 1px var(--ok) }
.chipbtn.st-pending { box-shadow: inset 0 0 0 1px var(--warn) }
.chipbtn.st-changed { box-shadow: inset 0 0 0 1px var(--bad) }
.totop { position: fixed; right: 20px; bottom: calc(20px + env(safe-area-inset-bottom, 0px)); z-index: 10;
         font: 600 13px var(--f-body); color: var(--panel); background: var(--ink); border: 0; border-radius: 999px;
         padding: 10px 16px; cursor: pointer; box-shadow: 0 4px 14px rgba(0,0,0,.25); opacity: .92 }
.totop:hover { opacity: 1 }
.totop:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px }
.row.clickable { cursor: pointer }
.row.clickable:hover { border-color: var(--accent) }
.row.locked.clickable:hover { border-color: var(--ok); box-shadow: 0 0 0 1px var(--ok) }
.row:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }
.row.changed { border-color: var(--bad); box-shadow: inset 4px 0 0 var(--bad) }
.lockwarn { display: flex; flex-wrap: wrap; gap: 6px 12px; align-items: center; font-size: 13px; color: var(--bad);
            background: color-mix(in srgb, var(--bad) 10%, var(--panel)); border-radius: 6px; padding: 6px 10px }
.lockwarn b { font-weight: 600 }
@media (prefers-reduced-motion: reduce) { * { transition: none !important } }
</style>

<div class="wrap">
  <header>
    <span class="eyebrow">core/detect.py → core/toggle.py · <span id="src"></span> · whole-number radii · <span id="sub"></span></span>
    <h1>Corner48 Round and Sharp</h1>
    <p class="lede">Each icon goes through the pipeline left to right: the input as drawn, the corners the detector finds,
      then two outputs built from those corners: every corner made round (<code>round_corner_processing.py</code>) and every
      corner made sharp (<code>sharp_corner_processing.py</code>). The two are separate runs, so an icon can have one of them
      only. Both outputs are run through the detector again to check them; <code>core/publish.py</code> sends them to the
      review site as the <code>--round</code> / <code>--sharp</code> Style records, where a failed check lands in the Failed tab.</p>
  </header>

  <section class="stages" id="stages" aria-label="Pipeline totals"></section>

  <section class="rules" aria-label="Rules used">
    <div class="rule"><h3>All round</h3><p id="r-round"></p></div>
    <div class="rule"><h3>All sharp</h3><p id="r-sharp"></p></div>
    <div class="rule"><h3>Never touched</h3><p>Junctions (3+ arms), kinks (2–25° bends) and shape curves (loops, caps, S-bends, free-end curves) stay exactly as drawn in both outputs. Filled shapes (a window dot, an arrowhead, a white backdrop) are copied into both outputs as drawn, under the strokes; the sharp output turns a round dot into a square.</p></div>
    <div class="rule"><h3>One decision per round corner</h3><p>Round and sharp decide each drawn round corner together: it is either a corner (re-rounded with its band radius, and sharpened) or kept as drawn in both. A round corner either output keeps (too large for a corner, no room to re-round, a sharp point crossing a stroke, no corner left to re-round) is kept in the other too. The <b>Kept as drawn in both</b> filter lists them; the big ones are what a reviewer may later turn back into corners.</p></div>
    <div class="rule"><h3>Re-detect check</h3><p>Both outputs go through the detector again and are compared junction by junction. An output <b>fails</b> when a junction of the input disappears (a stroke came loose), a new crossing appears (an arc cuts through a stroke), or a corner is left in the wrong state. A <b>new contact</b> is allowed: a sharpened leg that now runs along another stroke creates a new T. Arcs that merge with a curve or with each other are not failures.</p></div>
  </section>

  <section style="display:grid;gap:10px" aria-labelledby="ic">
    <h2 id="ic">Icons</h2>
    <div class="lockbar" id="lockbar" role="status" aria-live="polite"></div>
    <div class="controls">
      <div id="chips" style="display:flex;flex-wrap:wrap;gap:6px"></div>
      <input id="q" type="search" placeholder="Search icons by name" aria-label="Search icons by name">
      <label class="sw">View <select id="view" aria-label="View"><option value="grid">grid</option><option value="rows">rows</option></select></label>
      <label class="sw gridctl">Show <select id="show" aria-label="Drawings in each tile"><option value="all">original · round · sharp</option><option value="input">original only</option><option value="round">round only</option><option value="sharp">sharp only</option></select></label>
      <label class="sw gridctl">Size <input id="tsize" type="range" min="60" max="420" step="10" value="210" aria-label="Tile size"></label>
      <label class="sw">Sort <select id="sort" aria-label="Sort icons">
        <option value="name">name</option>
        <option value="input">ink outside keyshape · input</option>
        <option value="round">ink outside keyshape · all round</option>
        <option value="sharp">ink outside keyshape · all sharp</option>
        <option value="any">ink outside keyshape · most of the three</option>
      </select></label>
      <label class="sw rowctl"><input type="checkbox" id="mk" checked> Markers</label>
      <label class="sw rowctl"><input type="checkbox" id="rl" checked> Radius numbers</label>
      <label class="sw rowctl"><input type="checkbox" id="gh"> Ghost of input</label>
      <label class="sw rowctl"><input type="checkbox" id="ks" checked> Keyshape</label>
      <label class="sw rowctl"><input type="checkbox" id="ps"> Previous sharp</label>
    </div>
    <div class="legend" aria-hidden="true">
      <span><i class="ring" style="border-color:var(--keyshape);border-style:dashed;border-radius:2px"></i>keyshape: SOLO48 visible-ink envelope, detected from the input's ink</span>
      <span><i class="dot" style="background:var(--sharp)"></i>sharp corner / sharpened apex</span>
      <span><i class="dot" style="background:var(--round)"></i>round corner</span>
      <span><i class="ring" style="border-color:var(--round)"></i>rounded at its band radius (number = r)</span>
      <span><i class="ring" style="border-color:var(--warn)"></i>rounded below its band radius (no room)</span>
      <span><i class="ring" style="border-color:var(--bad)"></i>left sharp (no room)</span>
      <span><i class="ring" style="border-color:var(--muted);border-style:dashed"></i>kept as drawn (round corner with a curved side, or a corner between two curves)</span>
    </div>
    <div class="colhead" aria-hidden="true"><div>Original</div><div>Round</div><div>Sharp (final)</div></div>
    <nav class="pager" aria-label="Pages"></nav>
    <div class="rows" id="rows"></div>
    <nav class="pager" aria-label="Pages"></nav>
  </section>
</div>

<button type="button" class="totop" id="totop" hidden aria-label="Scroll to top">↑ Top</button>
<script>
const DATA = __DATA__, ICONS = DATA.icons;
// ---- lock in: an icon marked good; a warning when its files change afterwards.
// Saved to locks.json through serve_report.py; opened as a plain file, edits stay in this
// browser (LS_LOCKS) until the page is served again.
const LS_LOCKS = "t48locks", PARTS = ["input", "round", "sharp"];
let LOCKS = {}, MODE = "file", BUSY = false;
const nowStamp = () => new Date().toISOString().slice(0, 16).replace("T", " ") + " UTC";
function browserEdits() { try { return JSON.parse(localStorage.getItem(LS_LOCKS) || "{}"); } catch (e) { return {}; } }
function setBrowserEdits(m) { try { localStorage.setItem(LS_LOCKS, JSON.stringify(m)); } catch (e) {} }
function merged(base, edits) {                // newer edit wins; {unlocked:true} removes a lock
  const out = { ...base };
  for (const [n, e] of Object.entries(edits)) {
    if (base[n] && base[n].at > e.at) continue;
    if (e.unlocked) delete out[n]; else out[n] = e;
  }
  return out;
}
// status: "none" = ready (not reviewed), "locked" = reviewed OK, "pending" = reviewed not OK,
// "changed" = locked but its files changed since
function lockState(ic) {
  const rec = LOCKS[ic.name]; if (!rec) return { s: "none" };
  const parts = PARTS.filter(p => rec.fp[p] !== ic.fp[p]);
  if ((rec.status || "locked") === "pending") return { s: "pending", parts, rec };
  return parts.length ? { s: "changed", parts, rec } : { s: "locked", rec };
}
const editFor = (action, fp, at) => action === "unlock" ? { unlocked: true, at }
  : { fp, at, status: action === "pending" ? "pending" : "locked" };
async function initLocks() {
  LOCKS = merged(DATA.locks || {}, browserEdits());
  if (location.protocol.startsWith("http")) {
    try {
      const r = await fetch("/api/locks", { cache: "no-store" });
      if (r.ok) { LOCKS = await r.json(); MODE = "server"; }
    } catch (e) {}
  }
  renderChips(); refilter(); drawLockbar();
}
async function setLock(name, action) {
  const ic = ICONS.find(i => i.name === name); if (!ic || BUSY) return;
  if (MODE === "server") {
    BUSY = true;
    try {
      const r = await fetch("/api/locks", { method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, action, fp: ic.fp }) });
      if (!r.ok) throw new Error((await r.json()).error || r.status);
      LOCKS = await r.json();
    } catch (e) { drawLockbar(`Could not save: ${e.message}. Is serve_report.py still running?`); BUSY = false; return; }
    BUSY = false;
  } else {
    const edits = browserEdits();
    edits[name] = editFor(action, ic.fp, nowStamp());
    setBrowserEdits(edits);
    LOCKS = merged(DATA.locks || {}, edits);
  }
  renderChips(); refilter(); drawLockbar();
}
let LAST_BULK = null;                             // {names, action} of the last page lock, for Undo
async function setMany(names, action) {          // action: "lock" | "unlock"
  const items = names.map(n => ({ name: n, fp: ICONS.find(i => i.name === n).fp }));
  if (!items.length || BUSY) return false;
  if (MODE === "server") {
    BUSY = true;
    try {
      const r = await fetch("/api/locks", { method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ action: action + "_many", items }) });
      if (!r.ok) throw new Error((await r.json()).error || r.status);
      LOCKS = await r.json();
    } catch (e) { BUSY = false; drawLockbar(`Could not save: ${e.message}. Is serve_report.py still running?`); return false; }
    BUSY = false;
  } else {
    const edits = browserEdits(), at = nowStamp();
    for (const it of items) edits[it.name] = editFor(action, it.fp, at);
    setBrowserEdits(edits);
    LOCKS = merged(DATA.locks || {}, edits);
  }
  return true;
}
function pageSlice() { return list.slice(page * pageSize, (page + 1) * pageSize); }
async function lockPage() {
  const slice = pageSlice();
  const todo = slice.filter(ic => lockState(ic).s === "none").map(ic => ic.name);
  const skipped = slice.filter(ic => lockState(ic).s === "changed").length;
  if (!todo.length) { drawLockbar(); return; }
  if (await setMany(todo, "lock")) {
    LAST_BULK = { names: todo, skipped };
    renderChips(); refilter(); drawLockbar();
  }
}
async function undoBulk() {
  if (!LAST_BULK) return;
  if (await setMany(LAST_BULK.names, "unlock")) { LAST_BULK = null; renderChips(); refilter(); drawLockbar(); }
}
async function pushBrowserEdits() {             // serve mode: save edits made while opened as a file
  const edits = browserEdits();
  for (const [name, e] of Object.entries(edits)) {
    const ic = ICONS.find(i => i.name === name); if (!ic) continue;
    if (LOCKS[name] && LOCKS[name].at > e.at) continue;
    await fetch("/api/locks", { method: "POST", headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, action: e.unlocked ? "unlock" : (e.status === "pending" ? "pending" : "lock"), fp: e.unlocked ? ic.fp : e.fp }) });
  }
  setBrowserEdits({});
  const r = await fetch("/api/locks", { cache: "no-store" }); if (r.ok) LOCKS = await r.json();
  renderChips(); refilter(); drawLockbar();
}
function drawLockbar(err) {
  const n = Object.values(LOCKS).filter(r => (r.status || "locked") === "locked").length;
  const np = Object.keys(LOCKS).length - n;
  const changed = ICONS.filter(ic => lockState(ic).s === "changed");
  const pending = MODE === "server" ? Object.keys(browserEdits()).length : 0;
  const where = MODE === "server" ? `saved to the project (<code>locks.json</code>)`
    : `saved in this browser only. To save them to the project, run <code>python3 reports/serve_report.py</code> (in corner_processing/) and use the page it opens`;
  let h = `<span><b class="num">${n}</b> locked · <b class="num" style="color:var(--warn)">${np}</b> pending · <span class="mode">${where}</span></span>`;
  if (changed.length) h = `<span class="warnt">⚠ ${changed.length} locked icon${changed.length > 1 ? "s" : ""} changed since lock-in</span> ` +
    `<button type="button" class="lbtn" data-showchanged>Show them</button>` + h;
  const open = typeof list !== "undefined" ? pageSlice().filter(ic => lockState(ic).s === "none").length : 0;
  h += ` <button type="button" class="lbtn primary" data-lockpage${open ? "" : " disabled"}>Lock in this page${open ? ` (${open})` : ""}</button>`;
  if (LAST_BULK) h += ` <span class="mode">Locked ${LAST_BULK.names.length} on this page` +
    `${LAST_BULK.skipped ? ` · skipped ${LAST_BULK.skipped} changed since lock-in` : ""}</span>` +
    ` <button type="button" class="lbtn" data-undobulk>Undo</button>`;
  if (pending) h += ` <button type="button" class="lbtn primary" data-push>Save ${pending} browser-only change${pending > 1 ? "s" : ""} to the project</button>`;
  if (err) h += ` <span class="warnt">${esc(err)}</span>`;
  $("lockbar").innerHTML = h;
  $("lockbar").classList.toggle("alert", !!changed.length || !!err);
}
// a click on the card itself toggles its lock (not on its buttons, the corner log, or while
// selecting text); a card that changed since lock-in needs its Accept / Unlock button
function cardToggle(row) {
  const ic = ICONS.find(i => i.name === row.dataset.name); if (!ic) return;
  const st = lockState(ic).s;
  if (st === "none") setLock(ic.name, "lock");
  else if (st === "locked") setLock(ic.name, "unlock");
}
document.addEventListener("click", e => {
  const b = e.target.closest("[data-lock]");
  if (b) { setLock(b.dataset.name, b.dataset.lock); return; }
  const row = e.target.closest(".row.clickable");
  if (row && !e.target.closest("button, a, input, select, label, summary, details") &&
      !(window.getSelection && String(window.getSelection()).length)) { cardToggle(row); return; }
  if (e.target.closest("[data-push]")) { pushBrowserEdits(); return; }
  if (e.target.closest("[data-lockpage]")) { lockPage(); return; }
  if (e.target.closest("[data-undobulk]")) { undoBulk(); return; }
  if (e.target.closest("[data-showchanged]")) {
    cur = "changed"; try { localStorage.setItem("t48f", cur); } catch (err) {}
    renderChips(); render(); $("ic").scrollIntoView({ block: "start" });
  }
});
const BANDS = DATA.bands.split(",").map(s => s.split(":").map(Number));
const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const f = (x, d = 2) => (x === null || x === undefined) ? "–" : (+x).toFixed(d).replace(/\.?0+$/, "");
const sum = fn => ICONS.reduce((a, ic) => a + fn(ic), 0);
const cnt = (log, st) => log.filter(e => e.status === st).length;
$("sub").textContent = DATA.subtitle || `${ICONS.length} icons`;
$("src").textContent = `${DATA.input} → ${DATA.dir}`;
const bandTxt = BANDS.map(([b, r], i) => `${i === 0 ? "≤" : "<"} ${b}° → r ${r}`).join(", ");
$("r-round").innerHTML = `Every straight-sided corner is first made sharp, then rounded with a whole-number radius, so it stays on the 48 grid. Round corners with a curved side keep their drawn shape, and a corner between two curves (a lens shape's point) is left as drawn. The icon's corner angles are grouped (within ${f(DATA.group_tol)}° of the group's average), and each group's average angle picks its radius: <b>${esc(bandTxt)}</b>. ` +
  (DATA.fallback === "reduce" ? `A corner whose sides are too short for its radius gets the largest whole number that fits; below 1 it stays sharp.` : `A corner whose sides are too short for its radius stays sharp.`) +
  ` On a curved side the arc's touch point is found on the curve. A drawn round too large for a corner (bigger than r 6, unless its sharp point sits within 1 u of the curve; always above r ${f(DATA.corner_max_r)}) is a designed curve and keeps its shape, as in the sharp output; so does one with no room to re-round.`;
const MITER = { slice: "Ink that leaves the keyshape is sliced flat along the keyshape edge; each side may reach as far as the input does there.",
  shift: "A point that leaves the keyshape slides inward along its arms until it touches the keyshape, keeping its angle (sliced where it cannot move)." };
$("r-sharp").innerHTML = `Each round corner with two straight sides up to r 6 is replaced by two straight lines meeting at its apex; bigger ones (up to r 8) too when the point sits within 1 u of the drawn curve. A round corner with a curved side is part of a curve and stays. ` +
  `Mitre joins draw the points (limit 4, full points down to 29°). ${MITER[DATA.miter] || `Mitre mode: <b>${esc(DATA.miter)}</b>.`} ` +
  `Flat ends are lengthened up to 2 u (the reach of the round cap) but never past the keyshape; an end on another stroke, a dot or a circle stays flush. Dots become 4×4 squares. A sharpened corner another stroke would cross stays round.`;

// ---- stage totals
const det = k => sum(ic => ic.res[k].length);
const rounded = sum(ic => cnt(ic.rlog, "rounded")), reduced = sum(ic => ic.rlog.filter(e => e.reduced).length);
const onCurve = sum(ic => ic.rlog.filter(e => e.status === "rounded" && e.curved).length);
const rCount = {}; ICONS.forEach(ic => ic.rlog.forEach(e => { if (e.status === "rounded") rCount[e.r] = (rCount[e.r] || 0) + 1; }));
const reshaped = sum(ic => ic.rlog.filter(e => e.status === "rounded" && e.was_round !== null && Math.abs(e.was_round - e.r) > 1e-6).length);
const skipped = sum(ic => cnt(ic.rlog, "skipped"));
const built = m => ICONS.filter(ic => ic[m]).length, nR = built("round"), nS = built("sharp");
const notBuilt = (m, n) => n < ICONS.length ? li("not built yet", ICONS.length - n) : "";
const sharpened = sum(ic => cnt(ic.slog, "sharpened"));
const keptS = sum(ic => cnt(ic.slog, "kept round")), keptR = sum(ic => cnt(ic.rlog, "kept round"));
const keptCC = sum(ic => cnt(ic.rlog, "kept sharp"));
const chk = (mode, v) => ICONS.filter(ic => ic.check[mode] === v).length;
const li = (k, v) => `<li><span>${k}</span><b>${v}</b></li>`;
$("stages").innerHTML = `
  <div class="stage"><span class="k">1 · Input</span><span class="v">${ICONS.length}</span><ul>${li("icons", ICONS.length)}${li("48×48, stroke 4", "")}</ul></div>
  <div class="stage"><span class="k">2 · Corner detect</span><span class="v">${det("sharp") + det("round")}</span><ul>${li("sharp corners", det("sharp"))}${li("round corners", det("round"))}${li("junctions", det("junction"))}${li("curves", det("curve"))}</ul></div>
  <div class="stage"><span class="k">3 · All round</span><span class="v">${rounded}</span><ul>${li("rounded", rounded)}${Object.keys(rCount).sort((a, b) => a - b).map(r => li(`· r ${r}`, rCount[r])).join("")}${li("· on a curved side", onCurve)}${li("· below band radius (no room)", reduced)}${li("· was drawn round, radius changed", reshaped)}${li("left sharp: no room", skipped)}${li("kept sharp: two curved sides", keptCC)}${li("kept round as drawn", keptR)}${li("check passed", `${chk("round", "ok") + chk("round", "contact")}/${nR}`)}${li("· new contact point", chk("round", "contact"))}${li("check failed", chk("round", "fail"))}${notBuilt("round", nR)}</ul></div>
  <div class="stage"><span class="k">4 · All sharp</span><span class="v">${sharpened}</span><ul>${li("sharpened", sharpened)}${li("kept round as drawn", keptS)}${li("already sharp", det("sharp"))}${li("check passed", `${chk("sharp", "ok") + chk("sharp", "contact")}/${nS}`)}${li("· new contact point", chk("sharp", "contact"))}${li("check failed", chk("sharp", "fail"))}${notBuilt("sharp", nS)}</ul></div>`;

// ---- drawing
const GRID = (() => { let g = ""; for (let i = 0; i <= 48; i += 4) g += `<line class="g-grid" x1="${i}" y1="0" x2="${i}" y2="48"/><line class="g-grid" x1="0" y1="${i}" x2="48" y2="${i}"/>`; return g; })();
// the icon's SOLO48 keyshape (visible-ink envelope) as a dashed guide under the ink
function ksShape(ic) {
  const k = ic && ic.ks;
  if (!k || !k.keyshape) return "";
  const [l, t, r, b] = k.bounds;
  return k.r ? `<circle class="g-ks" cx="${(l + r) / 2}" cy="${(t + b) / 2}" r="${k.r}"/>`
             : `<rect class="g-ks" x="${l}" y="${t}" width="${r - l}" height="${b - t}"/>`;
}
const svg = (inner, label, ic) => `<svg viewBox="-2 -2 52 52" role="img" aria-label="${esc(label)}">${GRID}${ksShape(ic)}${inner}</svg>`;
const ghost = ic => `<g class="g-ghost gh">${ic.input.join("")}</g>`;
function plateInput(ic) { return svg(`<g class="g-icon">${ic.input.join("")}</g>`, `${ic.name} input`, ic); }
function plateDetect(ic) {
  const r = ic.res, sh = ic.input.join("");
  let o = `<g class="g-ink">${sh}</g><g class="g-cl">${sh}</g>`;
  for (const c of r.curve) o += `<path class="g-curve" d="${c.segs.join("")}"><title>curve (${esc(c.why)})</title></path>`;
  for (const c of r.round) {
    const [ax, ay] = c.apex, [sx, sy] = c.start, [ex, ey] = c.end;
    if (c.centre) o += `<circle class="g-circ" cx="${c.centre[0]}" cy="${c.centre[1]}" r="${c.r}"/>`;
    o += `<path class="g-leg" d="M${sx} ${sy}L${ax} ${ay}L${ex} ${ey}"/><path class="g-roundarc" d="${c.segs.join("")}"><title>round · ${f(c.angle, 1)}° · r ${f(c.r)}</title></path>`;
    o += `<path class="g-apex" d="M${ax} ${ay - .9}L${ax + .9} ${ay}L${ax} ${ay + .9}L${ax - .9} ${ay}Z"/>`;
  }
  for (const j of r.junction) o += `<rect class="g-junc" x="${j.p[0] - .75}" y="${j.p[1] - .75}" width="1.5" height="1.5"><title>junction · ${j.type}</title></rect>`;
  for (const k of r.kink) o += `<circle class="g-kink" cx="${k.p[0]}" cy="${k.p[1]}" r=".65"><title>kink · ${f(k.angle, 1)}°</title></circle>`;
  for (const s of r.sharp) o += `<circle class="g-sharp" cx="${s.p[0]}" cy="${s.p[1]}" r=".95"><title>sharp · ${f(s.angle, 1)}° · r_max ${f(s.r_max)}</title></circle>`;
  return svg(o, `${ic.name} detected corners`, ic);
}
const notYet = (ic, m) => `<svg viewBox="-2 -2 52 52" role="img" aria-label="${esc(ic.name)} ${m}: not built">${GRID}${ksShape(ic)}${ghost(ic).replace(' gh"', '"')}` +
  `<text class="m-lab kept" x="24" y="25" style="font-size:3.2px">not built yet</text></svg>`;
function plateRound(ic) {
  if (!ic.round) return notYet(ic, "all round");
  let o = ghost(ic) + `<g class="g-icon">${ic.round.join("")}</g><g class="mk">`;
  for (const e of ic.rlog) {
    const [x, y] = e.p;
    if (e.status === "rounded") {
      o += `<circle class="${e.reduced ? "m-reduced" : "m-rounded"}" cx="${x}" cy="${y}" r="2.2"><title>rounded · r ${f(e.r)} (band r ${e.band}, group ${f(e.group, 1)}°)${e.reduced ? " · reduced to fit" : ""}${e.was_round !== null ? ` · was drawn r ${f(e.was_round)}` : ""}${e.curved ? " · on a curved side" : ""}${e.consumed ? " · used the whole straight" : ""}</title></circle>`;
      o += `<text class="m-lab ${e.reduced ? "warn" : ""}" x="${x}" y="${y + .75}">${f(e.r)}</text>`;
    }
    else if (e.status === "skipped") o += `<path class="m-skipped" d="M${x - 1.2} ${y - 1.2}L${x + 1.2} ${y + 1.2}M${x + 1.2} ${y - 1.2}L${x - 1.2} ${y + 1.2}"><title>left sharp · ${esc(e.why)}</title></path>`;
    else if (e.status === "kept sharp") o += `<circle class="m-kept" cx="${x}" cy="${y}" r="2.2"><title>kept as drawn: corner between two curves</title></circle>`;
    else {
      o += `<circle class="m-kept" cx="${x}" cy="${y}" r="2.2"><title>kept as drawn (curved side) · r ${f(e.r)}</title></circle>`;
      o += `<text class="m-lab kept" x="${x}" y="${y + .75}">${f(e.r)}</text>`;
    }
  }
  return svg(o + "</g>" + decisionMarks(ic, "round"), `${ic.name} all round`, ic);
}
function plateSharp(ic) {
  if (!ic.sharp) return notYet(ic, "all sharp");
  let o = ghost(ic) + `<g class="g-icon sharp">${ic.sharp.join("")}</g><g class="mk">`;
  for (const e of ic.slog) {
    if (e.status === "sharpened") o += `<circle class="m-sharp" cx="${e.p[0]}" cy="${e.p[1]}" r=".95"><title>sharpened · ${f(e.angle, 1)}° (was r ${f(e.r)})</title></circle>`;
    else if (e.status === "kept round") o += `<circle class="m-kept" cx="${e.p[0]}" cy="${e.p[1]}" r="2.2"><title>kept round (curved side) · r ${f(e.r)}</title></circle>`;
  }
  return svg(o + "</g>" + decisionMarks(ic, "sharp"), `${ic.name} all sharp`, ic);
}

// the final drawing of an output: the AI review's proposal when it changes this output, else the processed output
function plateFinal(ic, m) {
  const fix = ic.review && ic.review.fix;
  if (fix && fix.col === m && fix.shapes)
    return [svg(`<g class="g-icon${m === "sharp" ? " sharp" : ""}">${fix.shapes.join("")}</g>`, `${ic.name} ${m} (final)`, ic), true];
  if (!ic[m]) return [notYet(ic, m), false];
  return [svg(`<g class="g-icon${m === "sharp" ? " sharp" : ""}">${ic[m].join("")}</g>`, `${ic.name} ${m}`, ic), false];
}
// grid view tile: original, round and final sharp, small; a click opens the icon's row
const tsvg = (inner, label) => `<svg viewBox="-2 -2 52 52" role="img" aria-label="${esc(label)}">${inner}</svg>`;
function tileShapes(ic, m) {
  const fix = ic.review && ic.review.fix;
  if (fix && fix.col === m && fix.shapes) return [fix.shapes.join(""), true];
  return [ic[m] ? ic[m].join("") : "", false];
}
function tile(ic) {
  const [r, rf] = tileShapes(ic, "round"), [sh, sf] = tileShapes(ic, "sharp"), nm = esc(ic.name.replace(/\.svg$/, ""));
  const rv = ic.review ? tag("rv-" + ic.review.status, RV_LABEL[ic.review.status] || ic.review.status) : "";
  return `<article class="tile" tabindex="0" data-open="${nm}" title="${nm}: open its row"><span class="tn">${nm}</span>` +
    `<div class="tp"><div>${tsvg(`<g class="g-icon">${ic.input.join("")}</g>`, nm + " original")}</div>` +
    `<div${rf ? ' class="fx"' : ""}>${tsvg(`<g class="g-icon">${r}</g>`, nm + " round")}</div>` +
    `<div${sf ? ' class="fx"' : ""}>${tsvg(`<g class="g-icon sharp">${sh}</g>`, nm + " sharp (final)")}</div></div>` +
    `<div class="tl"><span>original</span><span>round</span><span>sharp${sf ? " · AI" : ""}</span></div>` +
    (rv ? `<div class="tg">${rv}</div>` : "") + `</article>`;
}
let VIEW = "grid", SHOW = "all", TSIZE = 210;
try { const g = JSON.parse(localStorage.getItem("t48grid") || "{}"); if (["all", "input", "round", "sharp"].includes(g.show)) SHOW = g.show; if (g.size >= 60 && g.size <= 420) TSIZE = g.size; } catch (e) {}
function applyGrid() {
  const r = $("rows"), one = SHOW !== "all";
  r.style.setProperty("--tile", TSIZE + "px");
  r.classList.toggle("one", one);
  for (const k of ["input", "round", "sharp"]) r.classList.toggle("show-" + k, SHOW === k);
  r.classList.toggle("small", (one ? TSIZE : TSIZE / 3) < 70);
  $("show").value = SHOW; $("tsize").value = TSIZE;
  try { localStorage.setItem("t48grid", JSON.stringify({ show: SHOW, size: TSIZE })); } catch (e) {}
}
try { VIEW = localStorage.getItem("t48view") || "grid"; } catch (e) {}
// previous update's output under the new one, for the outputs that changed
function prevPlate(ic, m) {
  const sh = ic.prev[m];
  if (!sh) return `<div class="plate prev none p-${m}"><span class="cap">${m}: unchanged</span></div>`;
  return `<div class="plate prev p-${m}"><span class="lbl">previous ${m}</span>` +
    svg(`<g class="g-icon${m === "sharp" ? " sharp" : ""}">${sh.join("")}</g>`, `${ic.name} previous ${m}`, ic) +
    `<span class="cap">previous ${m}</span></div>`;
}
// ---- AI review (review/status.json + decisions.jsonl): status, decision, proposed drawing
const RV_LABEL = { reviewing: "AI reviewing", ok: "AI: ok", proposed: "AI proposed", "needs-user": "needs you",
                   decided: "decided", applied: "applied" };
function reviewRow(ic) {
  const rv = ic.review; if (!rv) return "";
  const dec = rv.decision || {};
  const who = dec.reviewer || (rv.reviewed && rv.reviewed.by) || (rv.claim && rv.claim.by) || "";
  const at = dec.at || (rv.reviewed && rv.reviewed.at) || (rv.claim && rv.claim.at) || "";
  const plates = "";                          // the proposal is drawn in the grid's final plates
  const corners = (dec.corners || []).map(k => `<li>${esc(k.decision)} at ${esc(k.p.join(", "))}${k.why ? " · " + esc(k.why) : ""}</li>`).join("");
  return `<div class="revrow"><div class="revhead">${tag("rv-" + rv.status, RV_LABEL[rv.status] || rv.status)}` +
    (dec.decision ? `<b>${esc(dec.decision)}</b>${dec.case ? ` <span class="tag">${esc(dec.case)}</span>` : ""}` : "") +
    `<span class="who">${esc(who)}${at ? " · " + esc(at) : ""}</span></div>` +
    ((rv.note || dec.why) ? `<p class="revnote">${esc(rv.note || dec.why)}</p>` : "") +
    (corners ? `<ul class="revcorners">${corners}</ul>` : "") + plates + `</div>`;
}
function decisionMarks(ic, col) {             // corner / keep decisions drawn on the round and sharp plates
  const dec = ic.review && ic.review.decision;
  if (!dec || !dec.corners || !["round", "sharp"].includes(col)) return "";
  return dec.corners.map(k => `<circle class="g-dec" cx="${k.p[0]}" cy="${k.p[1]}" r="3.2"><title>${esc(k.decision)}: ${esc(k.why || "")}</title></circle>`).join("");
}
function prevRow(ic) {
  return `<div class="plates prevrow${ic.prev.round ? "" : " only-sharp"}"><div class="prevnote">Changed in the last update. Above: now · below: before</div>` +
    prevPlate(ic, "round") + prevPlate(ic, "sharp") + `</div>`;
}

// ink past the icon's keyshape (u), per drawing: input / round / sharp (core/keyshape.py)
const overOf = (ic, p) => (ic.ks && ic.ks.over) ? (p === "any" ? Math.max(0, ...Object.values(ic.ks.over)) : (ic.ks.over[p] || 0)) : 0;
let SORT = "name";
// ink box centre vs the canvas centre (24, 24), from the rendered input: [dx, dy]
const offc = ic => { const k = ic.ks; if (!k || !k.ink) return null; const [l, t, r, b] = k.ink;
  const d = [(l + r) / 2 - 24, (t + b) / 2 - 24].map(v => Math.round(v * 10) / 10); return Math.max(...d.map(Math.abs)) > .05 ? d : null; };
// SOLO48 legacy names are the same box as the L sizes (HRECT_XL = HRECT_L)
const ksDiffers = k => !!(k && k.keyshape && k.declared && k.declared.replace("_XL", "_L") !== k.keyshape);
const sorted = l => SORT === "name" ? l : l.slice().sort((a, b) => overOf(b, SORT) - overOf(a, SORT) || (a.name < b.name ? -1 : 1));

// ---- rows
const FILTERS = [
  ["all", "All", () => true],
  ["rounded", "Gets rounded", ic => cnt(ic.rlog, "rounded") > 0],
  ["sharpened", "Gets sharpened", ic => cnt(ic.slog, "sharpened") > 0],
  ["reduced", "Below band radius", ic => ic.rlog.some(e => e.reduced)],
  ["reshaped", "Drawn radius changed", ic => ic.rlog.some(e => e.status === "rounded" && e.was_round !== null && Math.abs(e.was_round - e.r) > 1e-6)],
  ["curved", "Curved side", ic => ic.rlog.some(e => e.status === "rounded" && e.curved)],
  ["kept", "Kept round (curved)", ic => ic.slog.some(e => e.status === "kept round")],
  ["shared", "Kept as drawn in both", ic => ic.keep.length > 0, true],
  ["skipped", "Left sharp", ic => ic.rlog.some(e => e.status === "skipped")],
  ["contact", "New contact", ic => ic.check.round === "contact" || ic.check.sharp === "contact"],
  ["mismatch", "Check failed", ic => ic.check.round === "fail" || ic.check.sharp === "fail"],
  ["checkissue", "Check failed + new contact", ic => ["fail", "contact"].includes(ic.check.round) || ["fail", "contact"].includes(ic.check.sharp)],
  ["none", "No change", ic => ic.round && ic.sharp && !cnt(ic.rlog, "rounded") && !cnt(ic.slog, "sharpened")],
  ["noround", "Round not built", ic => !ic.round, true],
  ["nosharp", "Sharp not built", ic => !ic.sharp, true],
  ["lastchange", "Changed in last update", ic => !!ic.prev, true],
  ["lastready", "Changed · not reviewed", ic => !!ic.prev && lockState(ic).s === "none", true],
  ["ready", "Ready", ic => lockState(ic).s === "none"],
  ["locked", "Locked", ic => ["locked", "changed"].includes(lockState(ic).s)],
  ["pending", "Pending", ic => lockState(ic).s === "pending"],
  ["ksout", "Outside keyshape (drawing)", ic => overOf(ic, "input") > 0 || overOf(ic, "round") > 0],
  ["offc", "Off-centre", ic => !!offc(ic)],
  ["ksdiff", "Keyshape ≠ model", ic => ksDiffers(ic.ks)],
  ["changed", "Changed since lock-in", ic => lockState(ic).s === "changed", true],   // shown only when any
  ["rv-any", "AI reviewed", ic => !!ic.review && ic.review.status !== "reviewing", true],
  ["rv-proposed", "AI proposed", ic => !!ic.review && ic.review.status === "proposed", true],
  ["rv-needs-user", "Needs you", ic => !!ic.review && ic.review.status === "needs-user", true],
  ["rv-decided", "Decided", ic => !!ic.review && ["decided", "applied"].includes(ic.review.status), true],
  ["rv-ok", "AI: ok", ic => !!ic.review && ic.review.status === "ok", true],
];
let cur = "all";
try { cur = localStorage.getItem("t48f") || "all"; } catch (e) {}
if (!FILTERS.some(x => x[0] === cur)) cur = "all";
function renderChips() {
  $("chips").innerHTML = FILTERS.map(([k, l, fn, onlyIfAny]) => {
    const n = ICONS.filter(fn).length;
    if (onlyIfAny && !n && k !== cur) return "";
    const sep = (k === "lastchange" || k === "rv-any" || (k === "ready" && !ICONS.some(i => i.prev))) ? `<span class="chipsep" aria-hidden="true"></span>` : "";
    return `${sep}<button type="button" class="chipbtn${["ready", "locked", "pending", "changed", "lastchange", "lastready"].includes(k) ? " st-" + k : k.startsWith("rv-") ? " st-rv" : ""}" data-k="${k}" aria-pressed="${k === cur}">${l} <span class="num">${n}</span></button>`;
  }).join("");
}
function radii(ic) {
  const c = {}; ic.rlog.forEach(e => { if (e.status === "rounded") c[e.r] = (c[e.r] || 0) + 1; });
  return Object.keys(c).sort((a, b) => a - b).map(r => `r${r}×${c[r]}`).join(" · ");
}
const tag = (cls, t) => `<span class="tag ${cls}">${t}</span>`;
function row(ic) {
  const r = ic.res, rr = cnt(ic.rlog, "rounded"), red = ic.rlog.filter(e => e.reduced).length, sk = cnt(ic.rlog, "skipped"), sp = cnt(ic.slog, "sharpened");
  const tags = [];
  const why = d => [d.lost.length ? `${d.lost.length} junction lost` : "", d.crossings.length ? `${d.crossings.length} new crossing` : "", d.wrong_state ? `${d.wrong_state} corner in wrong state` : ""].filter(Boolean).join(", ");
  for (const m of ["round", "sharp"]) {
    const s = ic.check[m], d = ic.detail[m];
    tags.push(s === "none" ? tag("", `${m} not built`) : s === "ok" ? tag("ok", `${m} ✓`) : s === "contact" ? tag("warn", `${m} ✓ · new contact`) : tag("bad", `${m} ✗ ${why(d)}`));
  }
  const k = ic.ks;
  if (k) tags.push(k.keyshape
    ? `<span class="tag ks" title="keyshape detected from the input's ink: ${esc(k.keyshape)} ${k.bounds.join(", ")} · ink box ${(k.ink || []).join(", ")} · aspect ${k.aspect} · roundness ${k.roundness}${k.declared ? ` · model declares ${esc(k.declared)}` : ""}">${esc(k.keyshape)} ${esc(k.size)}</span>` +
      (ksDiffers(k) ? `<span class="tag ks none" title="the claude_skills model declares a different keyshape">model: ${esc(k.declared)}</span>` : "")
    : `<span class="tag ks none">no keyshape</span>`);
  if (k && k.over && Object.values(k.over).some(v => v > 0)) {
    const PN = {input: "input", round: "round", sharp: "sharp"};
    const parts = Object.keys(PN).filter(p => k.over[p] > 0).map(p => `${PN[p]} +${k.over[p]}${k.sides && k.sides[p] && k.sides[p].length ? ` ${k.sides[p].join("/")}` : ""}`);
    tags.push(`<span class="tag ksover" title="ink reaches past the keyshape by this many units (rendered ink, caps and joins included)">outside keyshape · ${esc(parts.join(" · "))}</span>`);
  }
  const oc = offc(ic);
  if (oc) tags.push(`<span class="tag ksover" title="the input's ink box centre is off the canvas centre (24, 24) by this much (u, + is right / down)">off-centre ${oc[0] > 0 ? "+" : ""}${oc[0]}, ${oc[1] > 0 ? "+" : ""}${oc[1]}</span>`);
  if (ic.keep.length) {
    const why = {}; ic.keep.forEach(k => { why[k.why] = (why[k.why] || 0) + 1; });
    tags.push(`<span class="tag warn" title="round corners kept as drawn in BOTH outputs (one decision for round and sharp): ${esc(ic.keep.map(k => `${k.p.join(", ")} ${k.why}`).join(" · "))}">kept in both · ${esc(Object.entries(why).map(([w, n]) => `${n} ${w}`).join(" · "))}</span>`);
  }
  if (ic.prev) tags.push(tag("chg", `changed in last update: ${Object.keys(ic.prev).join(", ")}`));
  const rows = [...ic.rlog.map(e => [e.p, e.angle, "round", e.status + (e.reduced ? ` (band r ${e.band})` : "") + (e.curved && e.status === "rounded" ? " · curved side" : "") + (e.consumed ? " · whole straight" : ""), e.r, (e.was_round !== null ? `was r ${f(e.was_round)} · ` : "") + `group ${f(e.group, 1)}°` + (e.why ? ` · ${e.why}` : "")]),
                ...ic.slog.filter(e => e.status === "sharpened").map(e => [e.p, e.angle, "sharp", "sharpened", e.r, ""])];
  const log = rows.length ? `<details class="log"><summary>Corner log (${rows.length})</summary><div class="tw"><table><thead><tr><th>point</th><th>angle</th><th>output</th><th>result</th><th>r</th><th>note</th></tr></thead><tbody>${rows.map(([p, a, m, s, rad, w]) => `<tr><td>${f(p[0])}, ${f(p[1])}</td><td>${f(a, 1)}°</td><td>${m}</td><td>${esc(s)}</td><td>${f(rad)}</td><td>${esc(w)}</td></tr>`).join("")}</tbody></table></div></details>` : "";
  const L = lockState(ic), nm = esc(ic.name), fr = plateFinal(ic, "round"), fs = plateFinal(ic, "sharp");
  let lockctl, lockwarn = "";
  const notOk = `<button type="button" class="lbtn warnb" data-lock="pending" data-name="${nm}">Not OK</button>`;
  if (L.s === "none") {
    lockctl = notOk + `<button type="button" class="lbtn primary" data-lock="lock" data-name="${nm}">Lock in</button>`;
  } else if (L.s === "locked") {
    tags.push(tag("lock", `locked · ${esc(L.rec.at)}`));
    lockctl = notOk + `<button type="button" class="lbtn" data-lock="unlock" data-name="${nm}">Unlock</button>`;
  } else if (L.s === "pending") {
    tags.push(tag("pend", `pending · not OK · ${esc(L.rec.at)}`));
    lockctl = `<button type="button" class="lbtn primary" data-lock="lock" data-name="${nm}">OK, lock in</button>` +
              `<button type="button" class="lbtn" data-lock="unlock" data-name="${nm}">Clear</button>`;
    if (L.parts.length) lockwarn = `<div class="pendnote">↻ <span>Its <b>${L.parts.join(", ")}</b> ${L.parts.length > 1 ? "have" : "has"} ` +
      `changed since it was marked not OK on ${esc(L.rec.at)}. Re-check it.</span></div>`;
  } else {
    tags.push(tag("bad", "changed since lock-in"));
    lockctl = `<button type="button" class="lbtn primary" data-lock="lock" data-name="${nm}">Accept new version</button>` +
              `<button type="button" class="lbtn danger" data-lock="unlock" data-name="${nm}">Unlock</button>`;
    lockwarn = `<div class="lockwarn">⚠ <span>Locked in as good on ${esc(L.rec.at)}, but its <b>${L.parts.join(", ")}</b> ` +
               `${L.parts.length > 1 ? "have" : "has"} changed since. Check it, then accept the new version or unlock it.</span></div>`;
  }
  const hint = L.s === "none" ? "Click the card to lock it in" : L.s === "locked" ? "Click the card to unlock it" : "";
  if (ic.review) tags.push(tag("rv-" + ic.review.status, RV_LABEL[ic.review.status] || ic.review.status));
  return `<article class="row${L.s === "none" ? "" : " " + L.s}${ic.review ? " rv-" + ic.review.status : ""}${hint ? " clickable" : ""}" data-name="${nm}"${hint ? ` tabindex="0" title="${hint}"` : ""}>
    <div class="rowhead"><span class="nm">${esc(ic.name.replace(/\.svg$/, ""))}</span>${tags.join("")}<span class="lockctl">${lockctl}</span></div>${lockwarn}
    <div class="plates">
      <div class="plate"><span class="lbl">Original</span>${plateInput(ic)}<span class="cap">as drawn</span></div>
      <div class="plate"><span class="lbl">Round</span>${fr[0]}<span class="cap">${fr[1] ? "AI proposal" : !ic.round ? "run round_corner_processing.py" : rr ? radii(ic) : "0 rounded"}</span></div>
      <div class="plate${fs[1] ? " fix" : ""}"><span class="lbl">Sharp (final)</span>${fs[0]}<span class="cap">${fs[1] ? "AI proposal applied" : ic.sharp ? `as processed · ${sp} sharpened` : "run sharp_corner_processing.py"}</span></div>
    </div>${ic.prev ? prevRow(ic) : ""}${reviewRow(ic)}${log}</article>`;
}
const PS_KEY = "t48ps50", LIST_TOP = () => $("ic");
// ---- pager: one page of icons at a time
const PAGE_SIZES = [20, 50, 100, 200], DEFAULT_PS = 50;
let page = 0, pageSize = DEFAULT_PS;
try { const s = +localStorage.getItem(PS_KEY); if (PAGE_SIZES.includes(s)) pageSize = s; } catch (e) {}
function pagerHTML(total) {
  const pages = Math.max(1, Math.ceil(total / pageSize));
  const from = total ? page * pageSize + 1 : 0, to = Math.min(total, (page + 1) * pageSize);
  const want = new Set([0, pages - 1, page - 2, page - 1, page, page + 1, page + 2].filter(p => p >= 0 && p < pages));
  let nums = "", last = -1;
  [...want].sort((a, b) => a - b).forEach(p => {
    if (last >= 0 && p > last + 1) nums += `<span class="gap">…</span>`;
    nums += `<button type="button" class="pg" data-p="${p}"${p === page ? ' aria-current="page"' : ""}>${p + 1}</button>`;
    last = p;
  });
  return `<button type="button" class="pg" data-p="${page - 1}"${page === 0 ? " disabled" : ""}>‹ Prev</button>${nums}` +
    `<button type="button" class="pg" data-p="${page + 1}"${page >= pages - 1 ? " disabled" : ""}>Next ›</button>` +
    `<span class="info">${total ? `Showing ${from.toLocaleString()}–${to.toLocaleString()} of ${total.toLocaleString()}` : "No icons"}</span>` +
    `<label>Per page <select data-ps>${PAGE_SIZES.map(s => `<option${s === pageSize ? " selected" : ""}>${s}</option>`).join("")}</select></label>`;
}
function drawPagers(total) {
  document.querySelectorAll(".pager").forEach(el => el.innerHTML = pagerHTML(total));
}
document.addEventListener("click", e => {
  const b = e.target.closest(".pager .pg"); if (!b || b.disabled) return;
  page = +b.dataset.p; pushNext = true; LAST_BULK = null; showPage(); LIST_TOP().scrollIntoView({ block: "start" });
});
// ---- view state in the URL: ?page=3&per=50&filter=round&q=arrow (page counted from 1)
let pushNext = false, initialPage = 0;
function readURL(initial) {
  // a parameter missing from the URL means its default — except on first open, where the
  // remembered filter / page size stay (a bare file link reopens the last view)
  const u = new URLSearchParams(location.search);
  const fl = u.get("filter");
  if (fl && FILTERS.some(x => x[0] === fl)) cur = fl; else if (!initial) cur = "all";
  $("q").value = u.get("q") || "";
  const vw = u.get("view");
  if (["grid", "rows"].includes(vw)) VIEW = vw; else if (!initial) VIEW = "grid";
  $("view").value = VIEW;
  const sw = u.get("show"); if (["all", "input", "round", "sharp"].includes(sw)) SHOW = sw; else if (!initial) SHOW = "all";
  const sz = +u.get("size"); if (sz >= 60 && sz <= 420) TSIZE = sz; else if (!initial) TSIZE = 210;
  const so = u.get("sort");
  SORT = ["input", "round", "sharp", "any"].includes(so) ? so : "name"; $("sort").value = SORT;
  const per = +u.get("per");
  if (PAGE_SIZES.includes(per)) pageSize = per; else if (!initial) pageSize = DEFAULT_PS;
  initialPage = Math.max(0, (parseInt(u.get("page"), 10) || 1) - 1);
}
function writeURL() {
  const u = new URLSearchParams();
  if (page > 0) u.set("page", page + 1);
  if (pageSize !== DEFAULT_PS) u.set("per", pageSize);
  if (cur !== "all") u.set("filter", cur);
  if (SORT !== "name") u.set("sort", SORT);
  if (VIEW !== "grid") u.set("view", VIEW);
  if (SHOW !== "all") u.set("show", SHOW);
  if (TSIZE !== 210) u.set("size", TSIZE);
  const q = $("q").value.trim();
  if (q) u.set("q", q);
  const url = location.pathname + (u.toString() ? "?" + u : "") + location.hash;
  try { (pushNext ? history.pushState : history.replaceState).call(history, null, "", url); } catch (e) {}
  pushNext = false;
}
window.addEventListener("popstate", () => { readURL(); renderChips(); START(); });
document.addEventListener("change", e => {
  if (!e.target.matches(".pager select[data-ps]")) return;
  pageSize = +e.target.value; page = 0;
  try { localStorage.setItem(PS_KEY, pageSize); } catch (err) {}
  showPage();
});

let list = [];
function refilter() {                      // lock state changed: same page, list rebuilt
  const fn = FILTERS.find(x => x[0] === cur)[2], q = $("q").value.trim().toLowerCase();
  list = sorted(ICONS.filter(ic => fn(ic) && (!q || ic.name.toLowerCase().includes(q))));
  showPage();
}
function render() {                        // filter / search changed: back to page 1
  LAST_BULK = null;
  const fn = FILTERS.find(x => x[0] === cur)[2], q = $("q").value.trim().toLowerCase();
  list = sorted(ICONS.filter(ic => fn(ic) && (!q || ic.name.toLowerCase().includes(q))));
  page = 0;
  showPage();
}
function showPage() {
  const pages = Math.max(1, Math.ceil(list.length / pageSize));
  page = Math.max(0, Math.min(page, pages - 1));
  const slice = list.slice(page * pageSize, (page + 1) * pageSize);
  const grid = VIEW === "grid";
  $("rows").classList.toggle("tiles", grid); document.body.classList.toggle("view-grid", grid); applyGrid();
  $("rows").innerHTML = slice.length ? slice.map(grid ? tile : row).join("") : `<p class="empty">No icons match this filter.</p>`;
  drawPagers(list.length);
  writeURL();
  if (typeof drawLockbar === "function" && $("lockbar").innerHTML) drawLockbar();
  applyToggles();
}
function applyToggles() {
  $("rows").classList.toggle("hide-markers", !$("mk").checked);
  $("rows").classList.toggle("hide-radius", !$("rl").checked);
  $("rows").classList.toggle("hide-ks", !$("ks").checked);
  $("rows").classList.toggle("hide-prevsharp", !$("ps").checked);
  $("rl").disabled = !$("mk").checked;
  try { localStorage.setItem("t48v", JSON.stringify({mk: $("mk").checked, rl: $("rl").checked, gh: $("gh").checked, ks: $("ks").checked, ps: $("ps").checked})); } catch (e) {}
  document.querySelectorAll(".gh").forEach(g => g.style.display = $("gh").checked ? "" : "none");
}
$("chips").addEventListener("click", e => {
  const b = e.target.closest("button"); if (!b) return;
  cur = b.dataset.k; try { localStorage.setItem("t48f", cur); } catch (err) {}
  renderChips(); render();
});
$("q").addEventListener("input", render);
$("sort").addEventListener("change", e => { SORT = e.target.value; render(); });
function setView(v) { VIEW = v; $("view").value = v; try { localStorage.setItem("t48view", v); } catch (e) {} }
$("view").addEventListener("change", e => { setView(e.target.value); pushNext = true; showPage(); });
$("show").addEventListener("change", e => {        // one drawing per tile: a smaller default size fits more
  const was = SHOW; SHOW = e.target.value;
  if ((was === "all") !== (SHOW === "all")) TSIZE = SHOW === "all" ? 210 : 110;
  applyGrid(); writeURL();
});
$("tsize").addEventListener("input", e => { TSIZE = +e.target.value; applyGrid(); });
$("tsize").addEventListener("change", writeURL);
function openTile(t) { setView("rows"); $("q").value = t.dataset.open; pushNext = true; render(); LIST_TOP().scrollIntoView({ block: "start" }); }
$("rows").addEventListener("click", e => { const t = e.target.closest(".tile"); if (t) openTile(t); });
// back to top: shown once the page is scrolled past the first screen
(() => {
  const btn = $("totop");
  const sync = () => { btn.hidden = window.scrollY < window.innerHeight * 0.8; };
  window.addEventListener("scroll", sync, { passive: true });
  sync();
  btn.addEventListener("click", () => {
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
    $("q").focus({ preventScroll: true });
  });
})();
$("rows").addEventListener("keydown", e => {
  if ((e.key === "Enter" || e.key === " ") && e.target.matches(".tile")) { e.preventDefault(); openTile(e.target); return; }
  if ((e.key === "Enter" || e.key === " ") && e.target.matches(".row.clickable")) { e.preventDefault(); cardToggle(e.target); }
});
$("mk").addEventListener("change", applyToggles);
$("gh").addEventListener("change", applyToggles);
$("rl").addEventListener("change", applyToggles);
$("ks").addEventListener("change", applyToggles);
$("ps").addEventListener("change", applyToggles);
try { const v = JSON.parse(localStorage.getItem("t48v") || "{}"); ["mk", "rl", "gh", "ks", "ps"].forEach(k => { if (typeof v[k] === "boolean") $(k).checked = v[k]; }); } catch (e) {}
const START = () => { render(); if (initialPage) { page = initialPage; initialPage = 0; showPage(); } };
readURL(true);
LOCKS = merged(DATA.locks || {}, browserEdits());
renderChips(); START(); drawLockbar(); initLocks();
</script>
"""

if __name__ == "__main__":
    main()
