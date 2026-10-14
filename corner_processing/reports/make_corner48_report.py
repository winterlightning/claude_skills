#!/usr/bin/env python3
"""make_corner48_report.py — self-contained review page for core/detect.py results.

Reads <dir>/corners48.json (+ the input 48x48 SVGs) and writes <dir>/corner48_report.html, <dir>
being outputs/solo48 (whole-set runs) or outputs/ (partial runs), whichever ran last: every
icon drawn with its strokes, centerlines and the detector's verdicts (sharp / round /
junction / kink / curve), filter chips, and a detail view per icon.

  python3 reports/make_corner48_report.py [--json outputs/solo48/corners48.json] [--out outputs/solo48/corner48_report.html]
"""

import os as _os
import sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))   # corner_processing/: import core
import argparse
import collections
import json
import os
import xml.etree.ElementTree as ET

from core.paths import ROOT
from core.svg_io import DEFAULT_INPUT, iter_skeleton_shapes, localname
from _shared import default_dir

GEOM_ATTRS = ("d", "x", "y", "width", "height", "rx", "ry", "cx", "cy", "r",
              "x1", "y1", "x2", "y2", "points")
LARGE_R = 8.0      # u — round corners above this get flagged for review


def shapes_of(path):
    """Geometry-only markup of every stroked element of an icon."""
    root = ET.parse(path).getroot()
    out = []
    for el in iter_skeleton_shapes(root):
        attrs = " ".join(f'{a}="{el.get(a)}"' for a in GEOM_ATTRS if el.get(a) is not None)
        out.append(f"<{localname(el.tag)} {attrs}/>")
    return out


def review_flags(v):
    flags = []
    if any(j["type"] == "meeting" and j["degree"] == 3 for j in v["junction"]):
        flags.append("3-arm meeting")
    if any(r["r"] > LARGE_R for r in v["round"]):
        flags.append("large radius")
    if any(not r["circular"] for r in v["round"]):
        flags.append("non-circular round")
    if any("curve" in s["arms"] for s in v["sharp"]):
        flags.append("curve-armed sharp")
    if v["kink"]:
        flags.append("kink")
    return flags


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="default: <dir>/corners48.json (outputs/solo48 or outputs/, whichever ran last)")
    ap.add_argument("--input", default=DEFAULT_INPUT)
    ap.add_argument("--out", help="default: corner48_report.html next to --json")
    ap.add_argument("--subtitle", default="")
    cfg = ap.parse_args(argv)
    cfg.json = cfg.json or os.path.join(default_dir(), "corners48.json")
    cfg.out = cfg.out or os.path.join(os.path.dirname(cfg.json), "corner48_report.html")

    res = {n: v for n, v in json.load(open(cfg.json)).items()     # leave out icons detected before
           if os.path.exists(os.path.join(cfg.input, n))}         # the input was re-fetched without them
    C = collections.Counter
    icons = []
    for name, v in sorted(res.items()):
        icons.append({"name": name, "shapes": shapes_of(os.path.join(cfg.input, name)),
                      "res": v, "flags": review_flags(v)})

    vals = list(res.values())
    summary = {
        "icons": len(res),
        "counts": {k: sum(len(v[k]) for v in vals)
                   for k in ("sharp", "round", "junction", "kink", "curve")},
        "sharp_arms": C("–".join(sorted(s["arms"])) for v in vals for s in v["sharp"]).most_common(),
        "sharp_where": C(s["where"] for v in vals for s in v["sharp"]).most_common(),
        "sharp_angle": C(f'{round(s["angle"])}°' for v in vals for s in v["sharp"]).most_common(8),
        "round_r": C(f'r {s["r"]:g}' for v in vals for s in v["round"]).most_common(8),
        "round_shape": C(("arc" if s["shape"] == "arc" else "cubic") + (" · circular" if s["circular"] else " · not circular")
                         for v in vals for s in v["round"]).most_common(),
        "curve_why": C(c["why"] for v in vals for c in v["curve"]).most_common(),
        "junction": C(j["type"] for v in vals for j in v["junction"]).most_common(),
        "flags": C(f for i in icons for f in i["flags"]).most_common(),
        "no_corner": sum(1 for v in vals if not v["sharp"] and not v["round"]),
    }
    data = json.dumps({"icons": icons, "summary": summary, "subtitle": cfg.subtitle},
                      separators=(",", ":"))
    html = TEMPLATE.replace("__DATA__", data.replace("</", "<\\/")).replace(
        "__SRC__", os.path.relpath(cfg.input, ROOT).replace("&", "&amp;").replace("<", "&lt;"))
    with open(cfg.out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"wrote {cfg.out} ({len(icons)} icons, {len(html) // 1024} KB)")


TEMPLATE = r"""<title>Corner48 Sample Review</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Condensed:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: drafting-table review sheet — summary ledger on top, then a contact sheet of
   48-grid plates; each plate opens a detail sheet with the corner table. */
:root {
  --bg: #eef1f4; --panel: #ffffff; --ink: #18202b; --muted: #5b6676; --line: #d5dbe3;
  --grid: #e3e8ee; --stroke: #c9d1db; --accent: #1f5fbf;
  --sharp: #d23a2f; --round: #0f8a6c; --junction: #5c6b80; --kink: #c77a00; --curve: #7b4fc9;
  --chip: #e6ebf1;
  --f-display: "IBM Plex Sans Condensed", "Arial Narrow", system-ui, sans-serif;
  --f-body: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --f-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
}
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) {
  --bg: #11161d; --panel: #18202a; --ink: #e4e9f0; --muted: #94a0b1; --line: #2a3442;
  --grid: #202a36; --stroke: #3a4656; --accent: #6ea4ff;
  --sharp: #ff6b5f; --round: #3fcf9f; --junction: #9aabc2; --kink: #f0a531; --curve: #a888f0;
  --chip: #222c38; color-scheme: dark } }
:root[data-theme="dark"] {
  --bg: #11161d; --panel: #18202a; --ink: #e4e9f0; --muted: #94a0b1; --line: #2a3442;
  --grid: #202a36; --stroke: #3a4656; --accent: #6ea4ff;
  --sharp: #ff6b5f; --round: #3fcf9f; --junction: #9aabc2; --kink: #f0a531; --curve: #a888f0;
  --chip: #222c38; color-scheme: dark }
* { box-sizing: border-box }
body { background: var(--bg); color: var(--ink); font: 14px/1.5 var(--f-body); margin: 0 }
.wrap { max-width: 1240px; margin: 0 auto; padding-inline: 20px; padding-block: 28px 64px;
        display: grid; gap: 28px }
h1, h2 { font-family: var(--f-display); font-weight: 600; text-wrap: balance; margin: 0 }
h1 { font-size: 30px; letter-spacing: -.01em }
h2 { font-size: 18px }
.eyebrow { font: 500 11px/1 var(--f-mono); letter-spacing: .08em; text-transform: uppercase; color: var(--muted) }
.lede { color: var(--muted); max-width: 72ch; margin: 6px 0 0 }
header { display: grid; gap: 8px }
.num { font-variant-numeric: tabular-nums; font-family: var(--f-mono) }

/* summary ledger */
.ledger { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1px;
          background: var(--line); border: 1px solid var(--line); border-radius: 8px; overflow: hidden }
.tile { background: var(--panel); padding: 14px 16px; display: grid; gap: 4px }
.tile .v { font: 600 26px/1 var(--f-mono); font-variant-numeric: tabular-nums }
.tile .k { display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--muted) }
.sw { width: 10px; height: 10px; border-radius: 50%; flex: none }
.sw.sq { border-radius: 2px }
.tile .d { font-size: 12px; color: var(--muted) }

.cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 16px }
.box { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 16px; display: grid; gap: 10px; align-content: start; min-width: 0 }
.bars { display: grid; gap: 6px }
.bar { display: grid; grid-template-columns: minmax(0, 1fr) 44px; gap: 8px; align-items: center; font-size: 13px }
.bar .lab { display: grid; gap: 3px; min-width: 0 }
.bar .lab span { overflow: hidden; text-overflow: ellipsis; white-space: nowrap }
.bar .track { height: 6px; background: var(--chip); border-radius: 3px; overflow: hidden }
.bar .fill { height: 100%; border-radius: 3px; background: var(--accent) }
.bar .n { text-align: right; font: 500 13px var(--f-mono); font-variant-numeric: tabular-nums }
.note { font-size: 13px; color: var(--muted); margin: 0 }
.flow { display: grid; gap: 8px; font-size: 13px }
.flow div { display: flex; justify-content: space-between; gap: 12px; border-bottom: 1px dashed var(--line); padding-bottom: 6px }

/* review list */
.review { display: grid; gap: 10px; margin: 0; padding: 0; list-style: none }
.review li { display: grid; grid-template-columns: 160px minmax(0, 1fr); gap: 12px; padding: 10px 12px;
             background: var(--panel); border: 1px solid var(--line); border-left: 3px solid var(--kink); border-radius: 6px }
.review b { font-family: var(--f-display); font-weight: 600 }
.review p { margin: 0; color: var(--muted) }
@media (max-width: 560px) { .review li { grid-template-columns: 1fr } }

/* controls */
.controls { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; position: sticky;
            top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--bg); padding-block: 10px }
.chipbtn { font: 500 13px var(--f-body); color: var(--ink); background: var(--chip); border: 1px solid transparent;
           border-radius: 999px; padding: 5px 12px; cursor: pointer }
.chipbtn[aria-pressed="true"] { background: var(--ink); color: var(--panel) }
.chipbtn:focus-visible, .card:focus-visible, input:focus-visible, .close:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }
.controls input { font: 13px var(--f-body); color: var(--ink); background: var(--panel); border: 1px solid var(--line);
                  border-radius: 6px; padding: 6px 10px; min-width: 0; flex: 1 1 180px; max-width: 280px }
.legend { display: flex; flex-wrap: wrap; gap: 14px; font-size: 12px; color: var(--muted); margin-left: auto }
.legend span { display: inline-flex; align-items: center; gap: 6px }

/* contact sheet */
.sheet { display: grid; grid-template-columns: repeat(auto-fill, minmax(196px, 1fr)); gap: 12px }
/* pager */
.pager { display: flex; flex-wrap: wrap; align-items: center; gap: 6px; padding-block: 8px; font-size: 13px; color: var(--muted) }
.pager .pg { font: 500 13px var(--f-mono); font-variant-numeric: tabular-nums; min-width: 34px; color: var(--ink); background: var(--chip);
             border: 1px solid transparent; border-radius: 6px; padding: 4px 9px; cursor: pointer }
.pager .pg[aria-current="page"] { background: var(--ink); color: var(--panel) }
.pager .pg:disabled { opacity: .4; cursor: default }
.pager .pg:focus-visible, .pager select:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px }
.pager .gap { padding-inline: 2px }
.pager .info { margin-left: auto; font-variant-numeric: tabular-nums }
.pager select { font: 13px var(--f-body); color: var(--ink); background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 3px 6px }

.card { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 10px; display: grid; gap: 8px;
        cursor: pointer; text-align: left; font: inherit; color: inherit; min-width: 0 }
.card:hover { border-color: var(--accent) }
.card svg { width: 100%; height: auto; aspect-ratio: 1; display: block; max-width: 100% }
.card .nm { font: 500 12px var(--f-mono); overflow: hidden; text-overflow: ellipsis; white-space: nowrap }
.card .ct { display: flex; flex-wrap: wrap; gap: 4px 10px; font: 12px var(--f-mono); color: var(--muted) }
.card .ct i { font-style: normal; display: inline-flex; align-items: center; gap: 4px }
.card .fl { display: flex; flex-wrap: wrap; gap: 4px }
.tag { font: 500 11px var(--f-body); background: var(--chip); color: var(--muted); border-radius: 4px; padding: 1px 6px }
.empty { color: var(--muted); padding: 24px 0 }

/* icon drawing */
.g-grid { stroke: var(--grid); stroke-width: .08 }
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
.g-lab { font: 600 2.1px var(--f-mono); paint-order: stroke; stroke: var(--panel); stroke-width: .5 }

/* detail dialog */
dialog { border: 1px solid var(--line); border-radius: 10px; background: var(--panel); color: var(--ink);
         width: min(980px, calc(100vw - 32px)); max-height: calc(100vh - 48px); padding: 0 }
dialog::backdrop { background: rgb(10 14 20 / .55) }
.dhead { display: flex; justify-content: space-between; align-items: center; gap: 12px; padding: 14px 18px; border-bottom: 1px solid var(--line) }
.dhead h2 { font-size: 17px; overflow-wrap: anywhere }
.close { font: 500 13px var(--f-body); background: var(--chip); color: var(--ink); border: 0; border-radius: 6px; padding: 6px 12px; cursor: pointer }
.dbody { display: grid; grid-template-columns: minmax(0, 380px) minmax(0, 1fr); gap: 18px; padding: 18px; overflow: auto; max-height: calc(100vh - 120px) }
@media (max-width: 760px) { .dbody { grid-template-columns: 1fr } }
.dbody svg { width: 100%; height: auto; aspect-ratio: 1; display: block; border: 1px solid var(--line); border-radius: 6px }
.tables { display: grid; gap: 14px; min-width: 0 }
.tw { overflow-x: auto }
table { border-collapse: collapse; width: 100%; font: 12px var(--f-mono); font-variant-numeric: tabular-nums }
th { text-align: left; font: 600 11px var(--f-body); letter-spacing: .04em; text-transform: uppercase; color: var(--muted); padding: 4px 8px; border-bottom: 1px solid var(--line); white-space: nowrap }
td { padding: 4px 8px; border-bottom: 1px solid var(--line); white-space: nowrap }
caption { text-align: left; font: 600 13px var(--f-display); padding-bottom: 4px; caption-side: top }
@media (prefers-reduced-motion: reduce) { * { transition: none !important } }
</style>

<div class="wrap">
  <header>
    <span class="eyebrow">core/detect.py · __SRC__ · 48×48 · <span id="sub"></span></span>
    <h1>Corner48 Sample Review</h1>
    <p class="lede">The segment-based corner detector run on a random sample of the 48×48 icon set.
      Every corner is reported in the state it is drawn in, <b>sharp</b> or <b>round</b>, with the apex
      the sharp version would have and the radius the round version has, so either state can be produced later.</p>
  </header>

  <section class="ledger" id="ledger" aria-label="Totals"></section>

  <section class="cols" id="breakdowns" aria-label="Breakdowns"></section>

  <section style="display:grid;gap:12px" aria-labelledby="rv">
    <h2 id="rv">Open questions in this sample</h2>
    <ul class="review" id="review"></ul>
  </section>

  <section style="display:grid;gap:4px" aria-labelledby="ic">
    <h2 id="ic">Icons</h2>
    <div class="controls">
      <div id="chips" style="display:flex;flex-wrap:wrap;gap:6px"></div>
      <input id="q" type="search" placeholder="Filter by name" aria-label="Filter icons by name">
      <div class="legend" aria-hidden="true">
        <span><i class="sw" style="background:var(--sharp)"></i>sharp</span>
        <span><i class="sw" style="background:var(--round)"></i>round · apex ◇</span>
        <span><i class="sw sq" style="background:var(--junction)"></i>junction</span>
        <span><i class="sw" style="background:var(--kink)"></i>kink</span>
        <span><i class="sw sq" style="background:var(--curve)"></i>curve</span>
      </div>
    </div>
    <nav class="pager" aria-label="Pages"></nav>
    <div class="sheet" id="sheet"></div>
    <nav class="pager" aria-label="Pages"></nav>
  </section>
</div>

<dialog id="dlg" aria-labelledby="dt">
  <div class="dhead"><h2 id="dt"></h2><button class="close" id="dclose" type="button">Close</button></div>
  <div class="dbody"><div id="dsvg"></div><div class="tables" id="dtab"></div></div>
</dialog>

<script>
const DATA = __DATA__;
const S = DATA.summary, ICONS = DATA.icons;
const $ = id => document.getElementById(id);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const f = (x, d = 2) => (x === null || x === undefined) ? "–" : (+x).toFixed(d).replace(/\.?0+$/, "");
$("sub").textContent = DATA.subtitle || `${S.icons} random icons`;

// ---- ledger
const K = [
  ["sharp", "Sharp corners", "var(--sharp)", "", "two arms meet at a point"],
  ["round", "Round corners", "var(--round)", "", "a curve bridges two arms"],
  ["junction", "Junctions", "var(--junction)", "sq", "3+ arms, not toggleable"],
  ["kink", "Kinks", "var(--kink)", "", "2–25° bends"],
  ["curve", "Curves", "var(--curve)", "sq", "shape curves, never corners"],
];
$("ledger").innerHTML = `<div class="tile"><span class="k">Icons</span><span class="v">${S.icons}</span><span class="d">${S.no_corner} with no sharp or round corner</span></div>` +
  K.map(([k, lab, c, sq, d]) => `<div class="tile"><span class="k"><i class="sw ${sq}" style="background:${c}"></i>${lab}</span><span class="v">${S.counts[k]}</span><span class="d">${d}</span></div>`).join("");

// ---- breakdowns
function bars(title, rows, color, note) {
  const max = Math.max(1, ...rows.map(r => r[1]));
  return `<div class="box"><h2>${title}</h2><div class="bars">` + rows.map(([l, n]) =>
    `<div class="bar"><div class="lab"><span title="${esc(l)}">${esc(l)}</span><div class="track"><div class="fill" style="width:${(100 * n / max).toFixed(1)}%;background:${color}"></div></div></div><span class="n">${n}</span></div>`).join("") +
    `</div>${note ? `<p class="note">${note}</p>` : ""}</div>`;
}
let bh = "";
bh += bars("Sharp corners by arm type", S.sharp_arms, "var(--sharp)", `${(S.sharp_where.find(r => r[0] === "between strokes") || [0, 0])[1]} of them are two separate strokes meeting end to end; the rest are joins inside one path.`);
bh += bars("Sharp corner angles", S.sharp_angle, "var(--sharp)", "Interior angle between the two arms (top 8).");
bh += bars("Round corner radius", S.round_r, "var(--round)", "Fitted from the tangent legs; exact for arcs (top 8).");
bh += bars("Round corner shape", S.round_shape, "var(--round)", "Circular = within 0.05 u of a true circle.");
bh += bars("Why a curve is not a corner", S.curve_why, "var(--curve)", "cap/loop: turns more than 170°. no straight arm: neither end flows into a line. inflection: S-bend.");
bh += bars("Junction types", S.junction, "var(--junction)", "T: a stroke ends on another stroke. meeting: 3+ stroke ends at one point.");
$("breakdowns").innerHTML = bh;

// ---- review list
const flagCount = Object.fromEntries(S.flags);
const REVIEW = [
  ["3-arm meeting", "Arrow tips and similar", "Two head arms meet at the tip and the shaft ends at the same point, so the tip is a 3-arm junction and not toggleable. Decide whether the head's two arms should count as one sharp corner with a stroke ending on it."],
  ["large radius", "Very large round corners", "Round corners with r > 8 (e.g. a shield's curved sides, r ≈ 23). Geometrically they are a rounding between two arms; a designer may read them as shape curves. A radius cap would turn them into curves."],
  ["non-circular round", "Round corners that are not circles", "Drawn with a cubic or an elliptical arc whose legs differ (e.g. 3 and 4). Their apex is exact; toggling to round with a true arc would change the drawn shape slightly."],
  ["curve-armed sharp", "Sharp corners with a curved arm", "One or both arms leave on a curve (a neck opening meeting a shoulder). There is no straight run to trim, so r_max is 0 here; rounding them needs a trim along the curve."],
  ["kink", "Kinks", "2-arm joins turning 2–25° (interior 155–178°). Reported, not treated as corners."],
];
$("review").innerHTML = REVIEW.filter(r => flagCount[r[0]]).map(([k, t, p]) =>
  `<li><b>${t}<br><span class="num" style="font-weight:400;color:var(--muted)">${flagCount[k]} icon${flagCount[k] > 1 ? "s" : ""}</span></b><p>${p}</p></li>`).join("");

// ---- drawing
function drawIcon(ic, big) {
  const r = ic.res;
  let g = "";
  for (let i = 0; i <= 48; i += 4) g += `<line class="g-grid" x1="${i}" y1="0" x2="${i}" y2="48"/><line class="g-grid" x1="0" y1="${i}" x2="48" y2="${i}"/>`;
  const shapes = ic.shapes.join("");
  let o = `<g class="g-ink">${shapes}</g><g class="g-cl">${shapes}</g>`;
  for (const c of r.curve) o += `<path class="g-curve" d="${c.segs.join("")}"><title>curve (${esc(c.why)}) · turns ${f(c.turn, 0)}°</title></path>`;
  r.round.forEach((c, i) => {
    const [ax, ay] = c.apex, [sx, sy] = c.start, [ex, ey] = c.end;
    if (c.centre) o += `<circle class="g-circ" cx="${c.centre[0]}" cy="${c.centre[1]}" r="${c.r}"/>`;
    o += `<path class="g-leg" d="M${sx} ${sy}L${ax} ${ay}L${ex} ${ey}"/>`;
    o += `<path class="g-roundarc" d="${c.segs.join("")}"><title>R${i + 1} round · ${f(c.angle, 1)}° · r ${f(c.r)}${c.circular ? "" : " (not circular)"}</title></path>`;
    o += `<path class="g-apex" d="M${ax} ${ay - .9}L${ax + .9} ${ay}L${ax} ${ay + .9}L${ax - .9} ${ay}Z"><title>R${i + 1} apex (${ax}, ${ay})</title></path>`;
    if (big) o += `<text class="g-lab" x="${ax + 1.2}" y="${ay - 1}" fill="var(--round)">R${i + 1}</text>`;
  });
  r.junction.forEach(j => { const [x, y] = j.p; o += `<rect class="g-junc" x="${x - .75}" y="${y - .75}" width="1.5" height="1.5"><title>junction · ${j.type} · ${j.degree} arms</title></rect>`; });
  r.kink.forEach(k => { const [x, y] = k.p; o += `<circle class="g-kink" cx="${x}" cy="${y}" r=".65"><title>kink · ${f(k.angle, 1)}°</title></circle>`; });
  r.sharp.forEach((s, i) => {
    const [x, y] = s.p;
    o += `<circle class="g-sharp" cx="${x}" cy="${y}" r=".95"><title>S${i + 1} sharp · ${f(s.angle, 1)}° · r_max ${f(s.r_max)}</title></circle>`;
    if (big) o += `<text class="g-lab" x="${x + 1.2}" y="${y - 1}" fill="var(--sharp)">S${i + 1}</text>`;
  });
  return `<svg viewBox="-2 -2 52 52" role="img" aria-label="${esc(ic.name)}">${g}${o}</svg>`;
}

// ---- filters + sheet
const FILTERS = [
  ["all", "All", () => true],
  ["round", "Has round", ic => ic.res.round.length > 0],
  ["sharp", "Has sharp", ic => ic.res.sharp.length > 0],
  ["review", "Open question", ic => ic.flags.length > 0],
  ["none", "No corners", ic => !ic.res.sharp.length && !ic.res.round.length],
];
let cur = "all";
try { cur = localStorage.getItem("c48f") || "all"; } catch (e) {}
if (!FILTERS.some(x => x[0] === cur)) cur = "all";
function renderChips() {
  $("chips").innerHTML = FILTERS.map(([k, l, fn]) =>
    `<button type="button" class="chipbtn" data-k="${k}" aria-pressed="${k === cur}">${l} <span class="num">${ICONS.filter(fn).length}</span></button>`).join("");
}
const PS_KEY = "c48ps", LIST_TOP = () => $("ic");
// ---- pager: one page of icons at a time
const PAGE_SIZES = [25, 50, 100, 200];
let page = 0, pageSize = 50;
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
  page = +b.dataset.p; pushNext = true; showPage(); LIST_TOP().scrollIntoView({ block: "start" });
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
  const per = +u.get("per");
  if (PAGE_SIZES.includes(per)) pageSize = per; else if (!initial) pageSize = 50;
  initialPage = Math.max(0, (parseInt(u.get("page"), 10) || 1) - 1);
}
function writeURL() {
  const u = new URLSearchParams();
  if (page > 0) u.set("page", page + 1);
  if (pageSize !== 50) u.set("per", pageSize);
  if (cur !== "all") u.set("filter", cur);
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
function renderSheet() {                   // filter / search changed: back to page 1
  const fn = FILTERS.find(x => x[0] === cur)[2], q = $("q").value.trim().toLowerCase();
  list = ICONS.filter(ic => fn(ic) && (!q || ic.name.toLowerCase().includes(q)));
  page = 0;
  showPage();
}
function showPage() {
  const pages = Math.max(1, Math.ceil(list.length / pageSize));
  page = Math.max(0, Math.min(page, pages - 1));
  const slice = list.slice(page * pageSize, (page + 1) * pageSize);
  drawPagers(list.length);
  writeURL();
  $("sheet").innerHTML = slice.length ? slice.map(ic => {
    const r = ic.res, n = k => r[k].length;
    const parts = [["sharp", "var(--sharp)"], ["round", "var(--round)"], ["junction", "var(--junction)"], ["kink", "var(--kink)"], ["curve", "var(--curve)"]]
      .filter(([k]) => n(k)).map(([k, c]) => `<i><span class="sw" style="background:${c};width:7px;height:7px"></span>${n(k)} ${k}</i>`).join("");
    return `<button type="button" class="card" data-n="${esc(ic.name)}">${drawIcon(ic, false)}
      <span class="nm" title="${esc(ic.name)}">${esc(ic.name.replace(/\.svg$/, ""))}</span>
      <span class="ct">${parts || "<i>no corners</i>"}</span>
      ${ic.flags.length ? `<span class="fl">${ic.flags.map(x => `<span class="tag">${esc(x)}</span>`).join("")}</span>` : ""}</button>`;
  }).join("") : `<p class="empty">No icons match this filter.</p>`;
}
$("chips").addEventListener("click", e => {
  const b = e.target.closest("button"); if (!b) return;
  cur = b.dataset.k; try { localStorage.setItem("c48f", cur); } catch (err) {}
  renderChips(); renderSheet();
});
$("q").addEventListener("input", renderSheet);

// ---- detail
function table(cap, cols, rows) {
  if (!rows.length) return "";
  return `<div class="tw"><table><caption>${cap}</caption><thead><tr>${cols.map(c => `<th>${c}</th>`).join("")}</tr></thead><tbody>` +
    rows.map(r => `<tr>${r.map(v => `<td>${v}</td>`).join("")}</tr>`).join("") + `</tbody></table></div>`;
}
$("sheet").addEventListener("click", e => {
  const b = e.target.closest(".card"); if (!b) return;
  const ic = ICONS.find(x => x.name === b.dataset.n), r = ic.res;
  $("dt").textContent = ic.name;
  $("dsvg").innerHTML = drawIcon(ic, true);
  const pt = p => `${f(p[0])}, ${f(p[1])}`;
  $("dtab").innerHTML =
    table("Sharp corners", ["#", "point", "angle", "arms", "reach", "r_max", "where"],
      r.sharp.map((s, i) => [`S${i + 1}`, pt(s.p), `${f(s.angle, 1)}°`, s.arms.join("–"), s.reach.map(x => f(x)).join(" / "), f(s.r_max), s.where])) +
    table("Round corners", ["#", "apex", "angle", "r", "drawn", "legs", "circle dev", "shape", "r_max"],
      r.round.map((s, i) => [`R${i + 1}`, pt(s.apex), `${f(s.angle, 1)}°`, f(s.r), s.r_drawn === null ? "–" : f(s.r_drawn), s.legs.map(x => f(x)).join(" / "), f(s.circle_dev, 3), s.shape, f(s.r_max)])) +
    table("Junctions", ["point", "type", "arms"], r.junction.map(j => [pt(j.p), j.type, j.degree])) +
    table("Kinks", ["point", "angle"], r.kink.map(k => [pt(k.p), `${f(k.angle, 1)}°`])) +
    table("Curves", ["from", "to", "turn", "why"], r.curve.map(c => [pt(c.start), pt(c.end), `${f(c.turn, 0)}°`, c.why])) +
    (!r.sharp.length && !r.round.length && !r.junction.length && !r.kink.length && !r.curve.length ? `<p class="note">Nothing to report: straight strokes only${r.circles ? `, ${r.circles} circle(s)` : ""}${r.dots ? `, ${r.dots} dot(s)` : ""}.</p>` : "");
  $("dlg").showModal();
});
$("dclose").addEventListener("click", () => $("dlg").close());
$("dlg").addEventListener("click", e => { if (e.target === $("dlg")) $("dlg").close(); });

const START = () => { renderSheet(); if (initialPage) { page = initialPage; initialPage = 0; showPage(); } };
readURL(true);
renderChips(); START();
</script>
"""

if __name__ == "__main__":
    main()
