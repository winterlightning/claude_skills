#!/usr/bin/env python3
"""Build output_png/report.html: original PNG, raw (vectorized) SVG and redrawn SVG per run,
next to the current (disapproved) gallery SVG of the run's source_icon_id.

Usage: python3 new-pipeline-test/build_report.py [output_png_dir]
Paths in the report are relative, so open it straight from disk.
"""
import html
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / "output_png"
RUN_RE = re.compile(r"^(\d{8})-(\d{4})-(.+)$")
REPO = Path(__file__).resolve().parent.parent
UUID_RE = re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", re.I)


def current_icons(source_ids):
    """source_icon_id -> (icon key, current published SVG) from the local gallery catalog.

    Matches the model's SOURCE_ICON_ID first, then the UUID in the original source's file name."""
    wanted = {sid.lower() for sid in source_ids if sid}
    if not wanted:
        return {}
    try:
        data = json.loads((REPO / "published" / "gallery" / "icons.json").read_text())
    except (OSError, ValueError):
        return {}
    items = data if isinstance(data, list) else data.get("icons", data)
    items = list(items.values()) if isinstance(items, dict) else items
    found = {}  # source id -> [(icon key, svg)], model SOURCE_ICON_ID matches first
    for icon in items:
        svg = REPO / "published" / "gallery" / (icon.get("preview_url") or "")
        if not icon.get("preview_url") or not svg.resolve().is_file():
            continue
        entry = (icon["key"], svg.resolve())
        module = REPO / ((icon.get("python_source") or {}).get("path") or "")
        if module.suffix == ".py" and module.is_file():
            m = re.search(r"^SOURCE_ICON_ID\s*=\s*['\"]([^'\"]+)['\"]", module.read_text(), re.M)
            if m and m.group(1).lower() in wanted:
                found.setdefault(m.group(1).lower(), []).insert(0, entry)
        for source in icon.get("original_sources") or []:
            m = UUID_RE.search(source.get("source_path") or "")
            if m and m.group(0).lower() in wanted and entry not in found.get(m.group(0).lower(), []):
                found.setdefault(m.group(0).lower(), []).append(entry)
    return found


def pick_current(candidates, slug):
    """Several icons can share one original; prefer the one named like the run."""
    for match in (lambda name: name == slug, lambda name: name.startswith(slug)):
        for key, svg in candidates:
            if match(key.split("/")[-1]):
                return key, svg
    return candidates[0] if candidates else (None, None)


def load_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return {}


def collect():
    runs = []
    for d in sorted(ROOT.iterdir()):
        m = RUN_RE.match(d.name)
        if not d.is_dir() or not m:
            continue
        slug = m.group(3)
        under = slug.replace("-", "_")
        choice = load_json(d / "choice.json")
        metrics = load_json(d / f"{slug}_metrics.json")

        def pick(*names):
            for n in names:
                if (d / n).exists():
                    return f"{d.name}/{n}"
            return None

        runs.append({
            "source_icon_id": choice.get("source_icon_id"),
            "dir": d.name,
            "slug": slug,
            "when": datetime.strptime(m.group(1) + m.group(2), "%Y%m%d%H%M").strftime("%b %d, %H:%M"),
            "subject": choice.get("subject") or slug.replace("-", " "),
            "parts": choice.get("parts", ""),
            "shape": choice.get("shape", ""),
            "attempts": choice.get("attempts"),
            "reference": pick("reference.svg", "reference.png"),
            "png": pick(f"{slug}.png"),
            "raw": pick(f"{slug}_raw.svg"),
            "redraw": pick(f"{slug}_redraw.svg"),
            "redraw_py": pick(f"{under}_redraw.py", f"{slug}_redraw.py"),
            "keyshape": (metrics.get("keyshape") or {}).get("suggested"),
            "summary": metrics.get("summary") or {},
        })
    return runs


def esc(s):
    return html.escape(str(s), quote=True)


def panel(label, src, kind, note="", caption=""):
    if not src:
        return (f'<figure class="panel missing"><div class="stage"><span>not yet</span></div>'
                f'<figcaption><b>{label}</b><span>{note or "missing"}</span></figcaption></figure>')
    small = f'<img class="px48 {kind}" src="{esc(src)}" alt="" width="48" height="48">'
    return (f'<figure class="panel"><a class="stage" href="{esc(src)}" target="_blank">'
            f'<img class="{kind}" src="{esc(src)}" alt="{esc(label)}" loading="lazy"></a>'
            f'<figcaption><b>{label}</b><span class="at48">{small}48px</span></figcaption>'
            + (f'<div class="cap">{esc(caption)}</div>' if caption else "") + '</figure>')


def card(r):
    s = r["summary"]
    chips = []
    if r["keyshape"]:
        chips.append(f'<span class="chip">{esc(r["keyshape"])}</span>')
    if r["shape"]:
        chips.append(f'<span class="chip">{esc(r["shape"])}</span>')
    if s:
        chips.append(f'<span class="chip err">{s.get("errors", 0)} err</span>'
                     f'<span class="chip warn">{s.get("warnings", 0)} warn</span>')
    status = "done" if r["redraw"] else "pending"
    chips.append(f'<span class="chip {status}">{"redrawn" if r["redraw"] else "awaiting redraw"}</span>')
    panels = []
    if r["reference"]:
        panels.append(panel("Reference", r["reference"], "svg"))
    if r["source_icon_id"]:
        panels.append(panel("Disapproved (current)", r["current"], "svg",
                            "not in local gallery", r["current_key"] or ""))
    panels.append(panel("Original PNG", r["png"], "png"))
    panels.append(panel("Raw SVG", r["raw"], "svg", "not vectorized"))
    panels.append(panel("Redrawn SVG", r["redraw"], "svg", "not redrawn"))
    py = f' · <a href="{esc(r["redraw_py"])}">model</a>' if r["redraw_py"] else ""
    return f'''<article class="run" data-status="{status}" data-name="{esc(r["subject"].lower())}">
  <header><div><h2>{esc(r["subject"])}</h2>
  <p class="meta">{esc(r["when"])} · <a href="{esc(r["dir"])}/">{esc(r["dir"])}</a>{py}</p></div>
  <div class="chips">{"".join(chips)}</div></header>
  {f'<p class="parts">{esc(r["parts"])}</p>' if r["parts"] else ""}
  <div class="panels cols{len(panels)}">{"".join(panels)}</div>
</article>'''


CSS = """
:root{--bg:#f6f6f4;--card:#fff;--ink:#1b1b1a;--muted:#6b6a66;--line:#e3e2dd;--stage:#fff;
--err:#b3261e;--warn:#9a6700;--ok:#1a7f37;--chip:#efeee9}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#161615;--card:#1f1f1e;--ink:#ecebe6;
--muted:#9c9b95;--line:#33322f;--stage:#fff;--err:#ff8a80;--warn:#e3b341;--ok:#56d364;--chip:#2b2a28}}
:root[data-theme="dark"]{--bg:#161615;--card:#1f1f1e;--ink:#ecebe6;--muted:#9c9b95;--line:#33322f;--stage:#fff;
--err:#ff8a80;--warn:#e3b341;--ok:#56d364;--chip:#2b2a28}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
main{max-width:1180px;margin:0 auto;padding:28px 16px 64px}
h1{font-size:22px;margin:0 0 4px}.sub{color:var(--muted);margin:0 0 18px}
.bar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px}
.bar button,.bar input{font:inherit;border:1px solid var(--line);background:var(--card);color:var(--ink);
border-radius:8px;padding:6px 12px}.bar button[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
.bar input{flex:1;min-width:160px}
.run{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px;margin-bottom:16px}
.run header{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap}
h2{font-size:16px;margin:0;text-transform:capitalize}.meta{margin:2px 0 0;color:var(--muted);font-size:12px}
.meta a{color:inherit}.parts{color:var(--muted);margin:10px 0 0;font-size:13px}
.chips{display:flex;gap:6px;flex-wrap:wrap;align-items:flex-start}
.chip{background:var(--chip);border-radius:99px;padding:2px 9px;font-size:12px;white-space:nowrap}
.chip.err{color:var(--err)}.chip.warn{color:var(--warn)}.chip.done{color:var(--ok)}.chip.pending{color:var(--warn)}
.panels{display:grid;gap:12px;margin-top:14px;grid-template-columns:repeat(3,1fr)}
.panels.cols4{grid-template-columns:repeat(4,1fr)}.panels.cols5{grid-template-columns:repeat(5,1fr)}
.cap{padding:0 10px 8px;font:11px ui-monospace,monospace;color:var(--muted);overflow-wrap:anywhere}
.panel{margin:0;border:1px solid var(--line);border-radius:10px;overflow:hidden}
.stage{display:grid;place-items:center;aspect-ratio:1;background:var(--stage);
background-image:linear-gradient(45deg,#f2f2f2 25%,transparent 25%,transparent 75%,#f2f2f2 75%),
linear-gradient(45deg,#f2f2f2 25%,transparent 25%,transparent 75%,#f2f2f2 75%);background-size:16px 16px;
background-position:0 0,8px 8px}
.stage img{width:84%;height:84%;object-fit:contain}
.missing .stage{background:var(--chip);color:var(--muted)}
figcaption{display:flex;justify-content:space-between;align-items:center;padding:8px 10px;font-size:12px;gap:8px}
.at48{display:flex;align-items:center;gap:6px;color:var(--muted)}
.px48{width:48px;height:48px;background:#fff;border:1px solid var(--line);border-radius:4px;image-rendering:auto}
@media (max-width:960px){.panels.cols5{grid-template-columns:repeat(3,1fr)}}
@media (max-width:760px){.panels,.panels.cols4,.panels.cols5{grid-template-columns:repeat(2,1fr)}}
"""

JS = """
const q=document.getElementById('q'),btns=[...document.querySelectorAll('[data-f]')];let f='all';
function apply(){const t=q.value.toLowerCase();document.querySelectorAll('.run').forEach(r=>{
r.hidden=!((f==='all'||r.dataset.status===f)&&r.dataset.name.includes(t))})}
btns.forEach(b=>b.onclick=()=>{f=b.dataset.f;btns.forEach(x=>x.setAttribute('aria-pressed',x===b));apply()});
q.oninput=apply;
"""


def main():
    runs = collect()
    current = current_icons(r["source_icon_id"] for r in runs)
    for r in runs:
        key, svg = pick_current(current.get((r["source_icon_id"] or "").lower(), []), re.sub(r"-\d+$", "", r["slug"]))
        r["current_key"], r["current"] = key, (os.path.relpath(svg, ROOT) if svg else None)
    runs.sort(key=lambda r: r["dir"], reverse=True)
    done = sum(1 for r in runs if r["redraw"])
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>PNG Pipeline Report</title>
<style>{CSS}</style></head><body><main>
<h1>PNG → vectorize → redraw</h1>
<p class="sub">{len(runs)} runs · {done} redrawn · {len(runs) - done} awaiting redraw · built {datetime.now():%Y-%m-%d %H:%M}</p>
<div class="bar"><button data-f="all" aria-pressed="true">All</button><button data-f="done">Redrawn</button>
<button data-f="pending">Awaiting redraw</button><input id="q" type="search" placeholder="Filter by subject"></div>
{"".join(card(r) for r in runs)}
</main><script>{JS}</script></body></html>"""
    out = ROOT / "report.html"
    out.write_text(page)
    print(f"{out}  ({len(runs)} runs, {done} redrawn)")


if __name__ == "__main__":
    main()
