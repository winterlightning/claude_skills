#!/usr/bin/env python3
"""Prepare a folder of SVGs for an agent to look at and reconstruct.

    python3 icon_set/scripts/prepare_references.py container_icons/svg --out work/containers

Rasterizing first is the point. An icon's geometry says what coordinates it has;
a picture of it says what it *is*, and an agent reconstructing an icon needs the
second. Fitting arcs to the source's own coordinates produces something
mechanically close to the reference and frequently wrong for this system -- it
inherits an exporter's fragmentation, its stroke ratio and its accidents, none
of which survive a 64-unit canvas with a fixed 4-unit stroke.

So this writes, per icon:

    png/<name>.png        the icon rendered large enough to read
    png/<name>@64.png     the same at the target's native size
    briefs/<name>.md      concept, description and tags from the manifest
    sheets/sheet-NN.png   contact sheets, for triaging many at once
    index.html            browsable worklist with every render
    index.md              the same list, for reading in the terminal

Then the agent reads a brief, looks at the render, and authors the icon through
`icon_set/skills/icon-design/SKILL.md` like any other reference-backed request.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

PREVIEW = 320
FAMILY_NATIVE = {"sub": 32, "solo": 48, "container": 64}
SHEET_COLUMNS = 6
SHEET_CELL = 190
SHEET_PER_PAGE = 36


def _render(svg_text: str, out: Path, size: int, background: str = "#ffffff") -> None:
    import cairosvg

    out.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(bytestring=svg_text.encode("utf-8"), write_to=str(out),
                     output_width=size, output_height=size, background_color=background)


def _inline(svg_text: str) -> tuple[str, str]:
    """Inner markup and viewBox, for compositing into a contact sheet."""
    root = ET.fromstring(svg_text)
    inner = "".join(ET.tostring(e, encoding="unicode") for e in root)
    for prefix in ("ns0:", "ns1:"):
        inner = inner.replace(prefix, "")
    inner = inner.replace(' xmlns:ns0="http://www.w3.org/2000/svg"', "")
    inner = inner.replace(' xmlns:ns1="http://www.w3.org/2000/svg"', "")
    return inner, (root.get("viewBox") or "0 0 1024 1024")


def _sheet(entries: list[tuple[str, str]], out: Path, title: str) -> None:
    import cairosvg

    rows = math.ceil(len(entries) / SHEET_COLUMNS)
    width = SHEET_COLUMNS * SHEET_CELL
    height = rows * (SHEET_CELL + 26) + 34
    cells = [f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
             f'<text x="12" y="22" font-size="13" font-family="monospace" fill="#141413">{title}</text>']
    for index, (label, svg_text) in enumerate(entries):
        inner, view = _inline(svg_text)
        column, row = index % SHEET_COLUMNS, index // SHEET_COLUMNS
        x, y = column * SHEET_CELL, row * (SHEET_CELL + 26) + 34
        short = label if len(label) <= 26 else label[:24] + "…"
        cells.append(
            f'<rect x="{x+4}" y="{y+4}" width="{SHEET_CELL-8}" height="{SHEET_CELL-8}" '
            f'fill="#fbfbfa" stroke="#e5e3dd" rx="8"/>'
            f'<svg x="{x+18}" y="{y+16}" width="{SHEET_CELL-36}" height="{SHEET_CELL-46}" '
            f'viewBox="{view}" fill="none" stroke="#141413" stroke-linecap="round" '
            f'stroke-linejoin="round">{inner}</svg>'
            f'<text x="{x+SHEET_CELL/2}" y="{y+SHEET_CELL-4}" text-anchor="middle" '
            f'font-size="9" font-family="monospace" fill="#6b6963">{short}</text>')
    out.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(
        bytestring=(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" '
                    f'height="{height}">{"".join(cells)}</svg>').encode(),
        write_to=str(out), scale=1.25)


def _index_html(rows, folder: str) -> str:
    import html as _html

    cards = "".join(
        f'<article data-name="{_html.escape(concept.lower())} {_html.escape(stem.lower())}">'
        f'<div class="art"><img src="png/{stem}.png" alt="{_html.escape(concept)}" loading="lazy"></div>'
        f'<div class="native"><img src="png/{stem}@{native}.png" alt="" width="{native}" height="{native}"></div>'
        f'<h3>{_html.escape(concept)}</h3>'
        f'<a href="briefs/{stem}.md">brief</a></article>'
        for stem, concept, _tags, native in rows)
    return f"""<!doctype html>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Reconstruction worklist — {_html.escape(folder)}</title>
<style>
:root {{ --bg:#faf9f7; --card:#fff; --ink:#141413; --muted:#6b6963; --line:#e5e3dd;
         color-scheme:light dark; }}
@media (prefers-color-scheme:dark) {{
  :root {{ --bg:#1a1a18; --card:#232320; --ink:#f2f1ec; --muted:#a3a19a; --line:#33322e; }}
  .art img, .native img {{ filter:invert(1); }}
}}
*{{box-sizing:border-box}}
body {{ margin:0; background:var(--bg); color:var(--ink);
  font:14px/1.5 ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif; }}
header {{ padding:26px 30px 18px; border-bottom:1px solid var(--line); }}
h1 {{ margin:0 0 6px; font-size:19px; }}
p {{ margin:0; color:var(--muted); max-width:66ch; }}
.bar {{ position:sticky; top:0; z-index:2; background:var(--bg); padding:12px 30px;
  border-bottom:1px solid var(--line); }}
input {{ width:100%; max-width:420px; padding:8px 12px; border:1px solid var(--line);
  border-radius:8px; background:var(--card); color:var(--ink); font:inherit; }}
main {{ padding:20px 30px 60px; display:grid; gap:14px;
  grid-template-columns:repeat(auto-fill,minmax(200px,1fr)); }}
article {{ background:var(--card); border:1px solid var(--line); border-radius:12px;
  padding:12px; text-align:center; position:relative; }}
.art {{ aspect-ratio:1; display:grid; place-items:center; }}
.art img {{ max-width:100%; max-height:100%; }}
.native {{ position:absolute; right:12px; bottom:44px; opacity:.85; }}
h3 {{ margin:8px 0 4px; font-size:12px; font-weight:600; }}
a {{ font-size:11px; color:var(--muted); }}
.hidden {{ display:none }}
</style>
<header>
  <h1>Reconstruction worklist — {_html.escape(folder)}</h1>
  <p>{len(rows)} icons. Triage on the contact sheets in <code>sheets/</code>, then take one at a
  time: read its brief, look at the render, and author it through
  <code>icon_set/skills/icon-design/SKILL.md</code>. The small copy in each corner is the icon at
  its family's native size, which is the size it has to survive.</p>
</header>
<div class="bar"><input id="q" type="search" placeholder="filter…" aria-label="filter"></div>
<main id="grid">{cards}</main>
<script>
const cards=[...document.getElementById('grid').children];
document.getElementById('q').addEventListener('input',e=>{{
  const q=e.target.value.toLowerCase().trim();
  for(const c of cards) c.classList.toggle('hidden', q && !c.dataset.name.includes(q));
}});
</script>
"""


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--size", type=int, default=PREVIEW)
    parser.add_argument(
        "--native", type=int, default=64,
        help="native canvas to preview at when the manifest gives no family: "
             "32 for sub, 48 for solo, 64 for container (default 64)",
    )
    parser.add_argument("--limit", type=int)
    args = parser.parse_args(argv)

    folder = args.folder if args.folder.is_dir() else args.folder.parent
    manifest_path = args.manifest or (folder / "manifest.json")
    if not manifest_path.is_file() and folder.parent.is_dir():
        manifest_path = args.manifest or (folder.parent / "manifest.json")
    meta: dict[str, dict] = {}
    if manifest_path.is_file():
        try:
            for entry in json.loads(manifest_path.read_text(encoding="utf-8")):
                meta[entry["file"]] = entry
        except Exception as error:
            print(f"warning: could not read {manifest_path}: {error}", file=sys.stderr)

    if args.folder.is_dir():
        files = sorted(args.folder.glob("*.svg"))[: args.limit]
    else:
        files = [args.folder]
    if not files:
        print(f"error: no SVGs in {args.folder}", file=sys.stderr)
        return 1

    out = args.out
    rows, sheet_batch, sheet_index = [], [], 1
    for number, path in enumerate(files, 1):
        text = path.read_text(encoding="utf-8")
        entry = meta.get(path.name, {})
        concept = entry.get("concept", path.stem)
        native = FAMILY_NATIVE.get(entry.get("family"), args.native)
        try:
            _render(text, out / "png" / f"{path.stem}.png", args.size)
            _render(text, out / "png" / f"{path.stem}@{native}.png", native)
        except Exception as error:
            print(f"  skipped {path.name}: {error}", file=sys.stderr)
            continue

        tags = entry.get("tags") or []
        brief = [f"# {concept}", "",
                 f"- source: `{path.relative_to(REPO_ROOT) if REPO_ROOT in path.parents else path}`",
                 f"- render: `png/{path.stem}.png` (look at this first)",
                 f"- native {native}px: `png/{path.stem}@{native}.png`"]
        if entry.get("categories"):
            brief.append(f"- categories: {', '.join(entry['categories'])}")
        if tags:
            brief.append(f"- tags: {', '.join(tags[:12])}")
        family = entry.get("family")
        if family:
            brief.append(f"- family: {family} — author with `/icon-{family}`")
        if entry.get("icon_id"):
            brief.append(f"- proposed icon_id: `{entry['icon_id']}`")
        brief += ["", "## Description", "",
                  entry.get("description", "_none supplied; read the render._"), "",
                  "## To author", "",
                  (f"Run `/icon-{family}`, which reads" if family else "Pick the family skill, then read") +
                  " `icon_set/skills/icon-design/SKILL.md`, then the reference-backed",
                  "intake. Look at the render before choosing anything: name the subject in",
                  "one sentence, keep only what survives at native size, choose the keyshape,",
                  "and design backwards from its four extreme coordinates.", "",
                  "The reference sets the subject, not the grid, the stroke or the",
                  "proportions. Recompose on the profile; do not copy its coordinates.", "",
                  "## Reconstruct, do not trace", "",
                  "This reference is drawn at illustration scale — thin strokes and more",
                  f"detail than a {native}px canvas can hold. Regenerate it as a simpler icon:",
                  "fewer parts, the profile's stroke weight, larger gaps, geometry rebuilt on",
                  "the grid. Keep the meaning intact — the silhouette it is recognized by and",
                  "the parts that make it this subject and not a neighbouring one. Simplify",
                  "the drawing, never the meaning.", ""]
        brief_path = out / "briefs" / f"{path.stem}.md"
        brief_path.parent.mkdir(parents=True, exist_ok=True)
        brief_path.write_text("\n".join(brief), encoding="utf-8")

        rows.append((path.stem, concept, len(tags), native))
        sheet_batch.append((concept, text))
        if len(sheet_batch) == SHEET_PER_PAGE:
            _sheet(sheet_batch, out / "sheets" / f"sheet-{sheet_index:02d}.png",
                   f"{folder.name} — sheet {sheet_index}")
            sheet_batch, sheet_index = [], sheet_index + 1
        if number % 25 == 0:
            print(f"  {number}/{len(files)}", flush=True)
    if sheet_batch:
        _sheet(sheet_batch, out / "sheets" / f"sheet-{sheet_index:02d}.png",
               f"{folder.name} — sheet {sheet_index}")

    index = ["# Reconstruction worklist", "",
             f"{len(rows)} icons from `{args.folder}`.", "",
             "Triage on the contact sheets in `sheets/`, then take one icon at a time:",
             "read its brief, look at its render, and author it through",
             "`icon_set/skills/icon-design/SKILL.md`.", "",
             "| # | concept | brief | render |", "|--:|---|---|---|"]
    for number, (stem, concept, _tags, _native) in enumerate(rows, 1):
        index.append(f"| {number} | {concept} | [brief](briefs/{stem}.md) | "
                     f"![{concept}](png/{stem}.png) |")
    (out / "index.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    (out / "index.html").write_text(_index_html(rows, folder.name),
                                    encoding="utf-8")

    print(f"\n{len(rows)} icons prepared in {out.resolve()}")
    print(f"  renders  {out}/png/            ({args.size}px and each icon's native size)")
    print(f"  briefs   {out}/briefs/")
    print(f"  sheets   {out}/sheets/         ({sheet_index} sheet(s), {SHEET_PER_PAGE} per sheet)")
    print(f"  worklist {out}/index.html  and  {out}/index.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
