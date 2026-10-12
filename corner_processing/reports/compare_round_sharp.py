#!/usr/bin/env python3
"""compare_round_sharp.py - how alike is each icon's sharp output to its round output?

Renders the round output and the sharp output (with the review's current proposal applied, if the icon has one)
at 96 px and measures the share of ink they do not share. Writes a page sorted from most identical to least, so the
icons whose sharp version adds nothing over the round one come first.

  python3 reports/compare_round_sharp.py                      # all icons -> outputs/solo48/compare-round-sharp.html
  python3 reports/compare_round_sharp.py --max-diff 5         # only icons differing by under 5 %
  python3 reports/compare_round_sharp.py --status ok --limit 300
  (400 icons per page: compare-round-sharp.html, compare-round-sharp-2.html, ...; --per-page to change)

identical rate = 100 - diff, where diff = pixels inked in only one of the two / pixels inked in either (in %).
Needs rsvg-convert, numpy and Pillow (use /opt/homebrew/bin/python3).
"""
import argparse
import base64
import html
import json
import os
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

import numpy as np
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "outputs", "solo48")


def load_review():
    st = {i["icon"]: i for i in json.load(open(os.path.join(ROOT, "review", "status.json")))["icons"]}
    last = {}
    for line in open(os.path.join(ROOT, "review", "decisions.jsonl")):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        last[r["icon"]] = r
    return st, last


def apply(svg, paths):
    for v in (paths or {}).values():
        if "old" not in v:
            continue
        for o in (v["old"], v["old"].replace("Z", " Z")):
            if f'd="{o}"' in svg:
                svg = svg.replace(f'd="{o}"', f'd="{v["new"]}"', 1)
                break
    return svg


def raster(svg, size=96):
    png = subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size), "-b", "white"],
                         input=svg.encode(), capture_output=True).stdout
    return np.asarray(Image.open(BytesIO(png)).convert("L")) < 128


def clean(svg):
    svg = re.sub(r"<\?xml.*?\?>", "", svg)
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    return re.sub(r"<title>.*?</title>", "", svg, flags=re.S).strip()


def measure(icon, st, last):
    try:
        sharp = clean(open(os.path.join(OUT, "sharp", icon)).read())
        rnd = clean(open(os.path.join(OUT, "round", icon)).read())
    except FileNotFoundError:
        return None
    status = st.get(icon, {}).get("status", "-")
    if status in ("proposed", "decided") and icon in last:
        sharp = apply(sharp, last[icon].get("paths"))
    a, b = raster(sharp), raster(rnd)
    union = int((a | b).sum())
    diff = 100.0 * int((a ^ b).sum()) / max(union, 1)
    return {"icon": icon, "status": status, "diff": round(diff, 2), "sharp": sharp, "round": rnd}


def uri(svg):
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def page(rows, title, start=0, nav=""):
    cards = []
    for n, r in enumerate(rows, start + 1):
        same = 100 - r["diff"]
        cards.append(
            f'<article class="card" data-s="{html.escape(r["status"])}"><h3><span class="n">{n}</span>{html.escape(r["icon"][:-4])}</h3>'
            f'<div class="row"><figure><img loading="lazy" src="{uri(r["round"])}" width="88" height="88" alt=""><figcaption>round</figcaption></figure>'
            f'<figure><img loading="lazy" src="{uri(r["sharp"])}" width="88" height="88" alt=""><figcaption>sharp</figcaption></figure>'
            f'<div class="tiny"><img loading="lazy" src="{uri(r["round"])}" width="32" height="32" alt=""><img loading="lazy" src="{uri(r["sharp"])}" width="32" height="32" alt=""></div></div>'
            f'<p class="m"><b>{same:.1f}%</b> identical · {html.escape(r["status"])}</p></article>')
    return f"""<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Round vs Sharp</title>
<style>
:root{{--bg:#f6f5f1;--card:#fff;--fg:#1d1c19;--mute:#6d6a62;--line:#e2dfd6;--acc:#b5482f}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#17171a;--card:#212125;--fg:#ecebe6;--mute:#9c9a92;--line:#34343a;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#17171a;--card:#212125;--fg:#ecebe6;--mute:#9c9a92;--line:#34343a;color-scheme:dark}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);font:14px/1.45 system-ui,-apple-system,sans-serif;padding-inline:16px;padding-block:0 48px}}
h1{{font-size:19px;margin:16px 0 4px}}.lead{{color:var(--mute);max-width:75ch;margin:0 0 14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px;min-width:0}}
h3{{font-size:12.5px;margin:0 0 6px;word-break:break-all}}.n{{color:var(--mute);font-family:ui-monospace,Menlo,monospace;margin-right:6px}}
.row{{display:flex;gap:6px;align-items:end;flex-wrap:wrap}}figure{{margin:0;text-align:center}}figcaption{{font-size:11px;color:var(--mute)}}
.tiny{{display:flex;flex-direction:column;gap:4px}}img{{display:block;background:#fff;border-radius:4px;max-width:100%}}
nav{{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}}nav a{{color:var(--fg);border:1px solid var(--line);background:var(--card);border-radius:6px;padding:3px 8px;text-decoration:none;font-size:12.5px}}nav a.on{{border-color:var(--acc);color:var(--acc)}}
.m{{margin:6px 0 0;font-size:12px;color:var(--mute);font-variant-numeric:tabular-nums}}.m b{{color:var(--acc)}}
</style>
<h1>{html.escape(title)}</h1>
{nav}<p class="lead">Icons {start + 1}-{start + len(rows)}, most identical first. Identical rate = the share of ink the round and sharp outputs have in common at 96 px; the sharp side includes the review's current proposal.</p>
<div class="grid">{"".join(cards)}</div>"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--max-diff", type=float, default=100, help="keep icons whose diff is under this %% (default all)")
    ap.add_argument("--status", help="only icons with this review status (ok, proposed, ...)")
    ap.add_argument("--limit", type=int, help="at most this many icons on the page")
    ap.add_argument("--per-page", type=int, default=400, help="icons per page (pages: NAME.html, NAME-2.html, ...)")
    ap.add_argument("--out", default=os.path.join(OUT, "compare-round-sharp.html"))
    ap.add_argument("--json", help="also write the measurements (icon, status, diff) here")
    a = ap.parse_args()
    st, last = load_review()
    icons = sorted(f for f in os.listdir(os.path.join(OUT, "sharp")) if f.endswith(".svg"))
    if a.status:
        icons = [i for i in icons if st.get(i, {}).get("status") == a.status]
    with ThreadPoolExecutor(10) as ex:
        rows = [r for r in ex.map(lambda i: measure(i, st, last), icons) if r and r["diff"] < a.max_diff]
    rows.sort(key=lambda r: (r["diff"], r["icon"]))
    if a.json:
        json.dump([{k: r[k] for k in ("icon", "status", "diff")} for r in rows], open(a.json, "w"), indent=0)
    if a.limit:
        rows = rows[:a.limit]
    base = a.out[:-5] if a.out.endswith(".html") else a.out
    name = lambda k: f"{base}.html" if k == 0 else f"{base}-{k + 1}.html"
    chunks = [rows[i:i + a.per_page] for i in range(0, len(rows), a.per_page)] or [[]]
    for k, chunk in enumerate(chunks):
        lo = lambda j: chunks[j][0]["diff"] if chunks[j] else 0
        nav = "<nav>" + "".join(f'<a href="{os.path.basename(name(j))}"{" class=on" if j == k else ""}>{j * a.per_page + 1}+ ({100 - lo(j):.0f}%)</a>'
                                for j in range(len(chunks))) + "</nav>"
        open(name(k), "w").write(page(chunk, "Round vs sharp: most identical first", k * a.per_page, nav))
    print(f"{len(rows)} icons on {len(chunks)} page(s) -> {name(0)}")


if __name__ == "__main__":
    main()
