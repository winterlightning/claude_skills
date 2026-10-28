"""Run the existing smart region-fill algorithm on side-sub SVGs for review.

This is a mechanical first pass, not an approval or a semantic fill decision.
It reads the source folder on every run and never pins or changes those sources.
"""

from __future__ import annotations

from .paths import DATA, FILL_ENGINE, WORK  # noqa: F401
import argparse
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
import hashlib
import html
import json
import math
from pathlib import Path
import sys
import tempfile
import xml.etree.ElementTree as ET

ROOT = WORK
WORKSPACE = DATA
sys.path.insert(0, str(FILL_ENGINE))
from fill_utils import assemble_polygon, geometry_to_svg, stroke_to_polygon  # noqa: E402
from step_2_fill_refactor_enhance import process_svg  # noqa: E402
from shapely.ops import unary_union  # noqa: E402


DEFAULT_SOURCE = DATA / "data/latest-side-sub-32"
DEFAULT_OUTPUT = WORK / "sub32-region-fill-review"
DEFAULT_DECISIONS = DATA / "data/sub32-region-fill-review-decisions.json"
DEFAULT_MARKS = DATA / "data/sub32-user-review-marks.json"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def effective_decision(name: str, decisions: dict, marks: dict) -> dict | None:
    mark = marks.get(name, {})
    if mark.get("action") == "retain":
        return {
            "action": "retain_original",
            "source_sha256": mark["source_sha256"],
            "reason": "User marked Retain: output is the original source SVG.",
        }
    return decisions.get(name)


def process_with_source_bound_closure(source: Path, decision: dict | None):
    """Add only a reviewed native endpoint edge (or a zero-length close flag)."""
    closure = decision.get("source_bound_closure") if decision else None
    if not closure:
        return process_svg(str(source), algo="smart_fill", edge_close=False)

    original_row, _, _, _ = process_svg(str(source), algo="smart_fill", edge_close=False)
    shapes = {item["source_id"]: item for item in original_row["shapes"]}
    root = ET.fromstring(source.read_bytes())
    namespace = root.tag.split("}")[0] + "}" if root.tag.startswith("{") else ""
    if closure["kind"] == "connect_endpoints":
        endpoints = []
        for key, end_key in (("from_source", "from_end"), ("to_source", "to_end")):
            source_id = closure[key]
            if source_id not in shapes:
                raise ValueError(f"Closure source path missing: {source_id}")
            # Which native endpoint of that path: "last" (default) or "first".
            end = closure.get(end_key, "last")
            if end not in ("first", "last"):
                raise ValueError(f"Closure {end_key} must be first or last: {end}")
            endpoints.append(shapes[source_id]["coords"][0 if end == "first" else -1])
        ET.SubElement(root, f"{namespace}path", {
            "id": "review-source-bound-closure",
            "d": f"M{endpoints[0][0]:.12g} {endpoints[0][1]:.12g}"
                 f"L{endpoints[1][0]:.12g} {endpoints[1][1]:.12g}",
        })
    elif closure["kind"] == "close_at_existing_endpoint":
        source_id = closure["source_id"]
        shape = shapes.get(source_id)
        if shape is None or len(shape["coords"]) < 2:
            raise ValueError(f"Closure source path missing: {source_id}")
        start, end = shape["coords"][0], shape["coords"][-1]
        if max(abs(start[i] - end[i]) for i in (0, 1)) > 1e-6:
            raise ValueError(f"Closure endpoints differ: {source_id}")
        element = next((item for item in root.iter() if item.get("id") == source_id), None)
        if element is None or not element.tag.endswith("path"):
            raise ValueError(f"Closure SVG path missing: {source_id}")
        element.set("d", element.get("d", "") + "Z")
    else:
        raise ValueError(f"Unsupported closure kind: {closure['kind']}")

    with tempfile.TemporaryDirectory(prefix="sub32-native-closure-") as temp_dir:
        virtual_source = Path(temp_dir) / source.name
        virtual_source.write_bytes(ET.tostring(root, encoding="utf-8"))
        return process_svg(str(virtual_source), algo="smart_fill", edge_close=False)


def source_fragment_polygon(shape: dict, selector: dict, viewbox: list[float]):
    """Stroke a hash-bound interval of one original centerline, without new points."""
    coords = shape["coords"]
    indices = []
    for endpoint in ("start", "end"):
        point = selector[endpoint]
        matches = [i for i, xy in enumerate(coords)
                   if max(abs(xy[axis] - point[axis]) for axis in (0, 1)) < 1e-4]
        if not matches:
            raise ValueError(f"Source fragment endpoint missing: {shape['source_id']} {point}")
        occurrence = selector.get(f"{endpoint}_occurrence", 0)
        indices.append(matches[occurrence])
    first, last = indices
    if first >= last:
        raise ValueError(f"Source fragment is not forward: {shape['source_id']} {first}:{last}")
    fragment = {key: value for key, value in shape.items()
                if key not in {"native_path", "source_coords"}}
    fragment["coords"] = coords[first:last + 1]
    fragment["closed"] = False
    if "width" in selector:
        width = float(selector["width"])
        if not 0 < width <= shape["stroke_width"]:
            raise ValueError(f"Invalid source fragment cut width: {shape['source_id']}")
        fragment["stroke_width"] = width
    return stroke_to_polygon([fragment], viewbox)


def extended_source_cut(shape: dict, length: float, viewbox: list[float], end: str = "first"):
    """Continue an explicitly named source line outward from its first (or last) endpoint."""
    coords = shape["coords"]
    if len(coords) != 2 or not 0 < length <= max(viewbox[2:]) or end not in {"first", "last"}:
        raise ValueError(f"Source line extension is invalid: {shape['source_id']}")
    start, inner = coords if end == "first" else coords[::-1]
    dx, dy = start[0] - inner[0], start[1] - inner[1]
    distance = math.hypot(dx, dy)
    if distance < 1e-6:
        raise ValueError(f"Source line has no direction: {shape['source_id']}")
    outer = (start[0] + length * dx / distance,
             start[1] + length * dy / distance)
    fragment = {key: value for key, value in shape.items()
                if key not in {"native_path", "source_coords"}}
    fragment["coords"] = [outer, start]
    fragment["closed"] = False
    return stroke_to_polygon([fragment], viewbox)


def kept_hole_islands(regions):
    """The drawing inside each hole a decision keeps open (a phone screen's glyph), or None.

    assemble_polygon subtracts the children of filled holes but drops the children of kept holes.
    Each child exterior is assembled as its own subtree with the same per-region treatments, so a
    kept screen still shows its content as source strokes, with the content's own holes as decided.
    """
    parts = []
    kept = regions[(regions.ring == "hole") & (regions.fill == "keep")]
    for _, hole in kept.iterrows():
        for _, island in regions[(regions.parent_id == hole.region_id) & (regions.ring == "exterior")].iterrows():
            subtree, frontier = [island.region_id], [island.region_id]
            while frontier:
                children = list(regions[regions.parent_id.isin(frontier)].region_id)
                subtree.extend(children)
                frontier = children
            part = regions[regions.region_id.isin(subtree)].copy()
            part["level"] = part["level"] - (island.level - 1)
            if part.loc[part.region_id == island.region_id, "fill"].iloc[0] == "cutout":
                part.loc[part.region_id == island.region_id, "fill"] = "keep"
            assembled = assemble_polygon(part)
            if assembled is not None and not assembled.is_empty:
                parts.append(assembled)
            nested = kept_hole_islands(part)
            if nested is not None:
                parts.append(nested)
    return unary_union(parts) if parts else None


def draft_one(args: tuple[str, str, dict | None]) -> dict:
    source_name, output_dir, decision = args
    source = Path(source_name)
    target = Path(output_dir) / "svg" / source.name
    result = {"name": source.stem, "source": str(source), "output": f"svg/{source.name}"}
    try:
        original_bytes = source.read_bytes()
        result["source_sha256_at_run"] = sha(original_bytes)
        active_decision = decision if not decision or decision["source_sha256"] == result["source_sha256_at_run"] else None
        row, filled, regions, distance = process_with_source_bound_closure(source, active_decision)
        ink = row["polygon"]
        if ink is None or ink.is_empty or not ink.is_valid:
            raise ValueError("Source has no valid visible paint")
        if filled is None or filled.is_empty or not filled.is_valid:
            raise ValueError("Region-fill algorithm returned no valid geometry")

        holes = regions[regions.ring == "hole"] if not regions.empty else regions
        selected = holes[holes.fill == "fill"] if not holes.empty else holes
        result["enclosed_regions"] = len(holes)
        result["selected_regions"] = len(selected)
        result["selected_region_ids"] = [int(value) for value in selected.region_id]
        result["algorithm_decisions"] = (
            {str(key): int(value) for key, value in regions["fill"].value_counts().items()}
            if not regions.empty else {}
        )
        result["small_detail_cutouts"] = row.get("small_detail_cutouts", [])
        result["adjacency_distance"] = distance
        result["viewbox"] = row["viewbox"]
        result["source_area"] = round(ink.area, 6)
        if decision:
            result["review_action"] = decision["action"]
            result["review_note"] = decision["reason"]
            if decision["source_sha256"] != result["source_sha256_at_run"]:
                result["review_action"] = "stale"
                result["review_note"] = "Source changed since visual review; inspect this draft again."
            else:
                if decision.get("source_bound_closure"):
                    result["source_bound_closure"] = decision["source_bound_closure"]
                region_overrides = decision.get("region_overrides", {})
                if region_overrides:
                    for region_id, treatment in region_overrides.items():
                        matches = regions.index[regions.region_id == int(region_id)]
                        if len(matches) != 1 or treatment not in {"fill", "keep", "cutout"}:
                            raise ValueError(f"Invalid region override: {region_id}={treatment}")
                        regions.loc[matches, "fill"] = treatment
                    result["selected_region_ids"] = [int(value) for value in regions.loc[
                        (regions.ring == "hole") & (regions.fill == "fill"), "region_id"]]
                    result["selected_regions"] = len(result["selected_region_ids"])
                    stroke_result = assemble_polygon(regions)
                    native_fill = row.get("filled_polygon")
                    islands = kept_hole_islands(regions) if decision.get("keep_hole_islands") else None
                    parts = [part for part in (stroke_result, islands, native_fill)
                             if part is not None and not part.is_empty]
                    filled = unary_union(parts)
                cut_ids = set(decision.get("cut_source_strokes", []))
                restore_ids = set(decision.get("restore_source_strokes", []))
                cut_widths = decision.get("cut_source_stroke_widths", {})
                cut_fragments = decision.get("cut_source_fragments", [])
                restore_fragments = decision.get("restore_source_fragments", [])
                extensions = decision.get("extend_source_stroke_cuts", [])
                if cut_ids or restore_ids or cut_fragments or restore_fragments or extensions:
                    vb = [float(value) for value in row["viewbox"].strip("()").replace(",", " ").split()]
                    by_id = {item["source_id"]: item for item in row["shapes"]}
                    found = {item["source_id"] for item in row["shapes"] if item["source_id"] in cut_ids | restore_ids}
                    if found != cut_ids | restore_ids:
                        raise ValueError(f"Source stroke IDs changed: expected {sorted(cut_ids | restore_ids)}, found {sorted(found)}")
                    if set(cut_widths) - cut_ids:
                        raise ValueError("Cut widths must name selected source strokes")
                    cuts = []
                    for item in row["shapes"]:
                        if item["source_id"] not in cut_ids:
                            continue
                        width = float(cut_widths.get(item["source_id"], item["stroke_width"]))
                        if not 0 < width <= item["stroke_width"]:
                            raise ValueError(f"Invalid source stroke cut width: {item['source_id']}")
                        cuts.append(stroke_to_polygon([item], vb, stroke_width=width))
                    cuts.extend(source_fragment_polygon(by_id[item["source_id"]], item, vb)
                                for item in cut_fragments)
                    cuts.extend(extended_source_cut(by_id[item["source_id"]],
                                                    float(item["length"]), vb, item.get("end", "first"))
                                for item in extensions)
                    if cuts:
                        filled = filled.difference(unary_union(cuts))
                    restore = [stroke_to_polygon([item], vb) for item in row["shapes"] if item["source_id"] in restore_ids]
                    restore.extend(source_fragment_polygon(by_id[item["source_id"]], item, vb)
                                   for item in restore_fragments)
                    if restore:
                        filled = unary_union([filled, *restore])
                    result["cut_source_strokes"] = sorted(cut_ids)
                    result["cut_source_stroke_widths"] = cut_widths
                    result["restore_source_strokes"] = sorted(restore_ids)
                    result["cut_source_fragments"] = cut_fragments
                    result["extend_source_stroke_cuts"] = extensions
                    result["restore_source_fragments"] = restore_fragments
            if result["review_action"] == "cut_source_filled_shape":
                ids = set(decision["source_ids"])
                shapes = [item for item in row.get("filled_shapes", []) if item.get("source_id") in ids]
                found = {item.get("source_id") for item in shapes}
                if found != ids:
                    raise ValueError(f"Native detail source IDs changed: expected {sorted(ids)}, found {sorted(found)}")
                for item in shapes:
                    detail = item["geometry"]
                    if filled.intersection(detail).area < detail.area * 0.95:
                        raise ValueError(f"Native detail {item['source_id']} is not inside the selected fill")
                    filled = filled.difference(detail)
                if filled.is_empty or not filled.is_valid:
                    raise ValueError("Native detail subtraction produced invalid geometry")
                result["detail_source_ids"] = sorted(ids)
        if filled is None or filled.is_empty or not filled.is_valid:
            raise ValueError("Review treatment produced invalid geometry")
        result["paint_added_area"] = round(filled.difference(ink).area, 6)
        result["paint_removed_area"] = round(ink.difference(filled).area, 6)

        action = result.get("review_action")
        if action in {"retain_original", "hold_original_for_repair"}:
            output_bytes = original_bytes
            result["status"] = "retained_original" if action == "retain_original" else "held_for_repair"
        elif filled.symmetric_difference(ink).area > 1e-6:
            output_bytes = geometry_to_svg(
                filled, row["viewbox"], row["width"], row["height"]
            ).encode("utf-8")
            result["status"] = "filled_with_detail_cut" if action == "cut_source_filled_shape" else "filled"
        else:
            output_bytes = original_bytes
            result["status"] = "unchanged"
        if active_decision and active_decision.get("needs_followup"):
            result["status"] = "needs_repair"

        ET.fromstring(output_bytes)
        target.write_bytes(output_bytes)
        result["output_sha256"] = sha(output_bytes)
    except Exception as exc:
        result.update(status="error", error=f"{type(exc).__name__}: {exc}")
        result.pop("output", None)
    return result


def gallery(records: list[dict], source: Path, output: Path,
            output_only: bool = False) -> str:
    source_prefix = Path("../../data/latest-side-sub-32") if source == DEFAULT_SOURCE else source
    cards = []
    for row in records:
        name = row["name"]
        source_url = html.escape(str(source_prefix / f"{name}.svg"), quote=True)
        output_path = row.get("output", "")
        output_url = html.escape(
            f'{output_path}?v={row["output_sha256"][:12]}' if output_path else "",
            quote=True,
        )
        title = html.escape(name)
        status = row["status"]
        proposal = (
            f'<img data-output-image loading="lazy" src="{output_url}" alt="Filled {title}">' if row.get("output")
            else '<span class="missing">No proposal</span>'
        )
        if output_only:
            artwork = (
                '<div class="output-artwork">'
                f'<div class="output-large">{proposal}</div>'
                f'<div class="output-native">32px output <img data-output-image loading="lazy" src="{output_url}" alt="" width="32" height="32"></div>'
                '</div>'
            )
        else:
            artwork = (
                '<div class="comparison">'
                f'<figure><div class="large"><img loading="lazy" src="{source_url}" alt="Original {title}"></div>'
                f'<figcaption>Original <img loading="lazy" src="{source_url}" alt="" width="32" height="32"></figcaption></figure>'
                f'<figure><div class="large">{proposal}</div>'
                f'<figcaption>Algorithm proposal {proposal}</figcaption></figure>'
                '</div>'
                '<div class="darkrow">'
                f'<img loading="lazy" src="{source_url}" alt="Original on dark">'
                + (f'<img data-output-image loading="lazy" src="{output_url}" alt="Fill on dark">' if output_url else '')
                + '</div>'
            )
        cards.append(
            f'<article data-status="{status}" data-name="{title}" data-source-hash="{row.get("source_sha256_at_run", "")}">'
            f'<h2>{title}</h2>'
            + (artwork if output_only else '')
            + f'<p class="badge">{status.replace("_", " ")} · '
            f'{row.get("selected_regions", 0)} of {row.get("enclosed_regions", 0)} regions selected</p>'
            + (f'<p class="note {"warning" if status in {"held_for_repair", "needs_repair", "error"} else "resolved"}">{html.escape(row["review_note"])}</p>' if row.get("review_note") else '')
            + '<div class="mark-controls"><button type="button" data-action="retain">Retain</button>'
            '<button type="button" data-action="fix_small_dot">Fix small dot</button>'
            '<button type="button" data-action="clear" class="clear">Clear</button>'
            '<span class="mark-state">Unmarked</span></div>'
            '<div class="feedback-controls"><label>Feedback'
            '<textarea rows="2" maxlength="2000" placeholder="Describe what should change for this icon"></textarea></label>'
            '<button type="button" data-action="save_feedback">Save feedback</button></div>'
            + ('' if output_only else artwork)
            + (f'<p class="error">{html.escape(row["error"])}</p>' if row.get("error") else '')
            + '</article>'
        )
    counts = Counter(row["status"] for row in records)
    summary = " · ".join(f"{status}: {count}" for status, count in sorted(counts.items()))
    grid_columns = "repeat(auto-fill,minmax(230px,1fr))" if output_only else "repeat(auto-fill,minmax(330px,1fr))"
    page_title = "Side sub 32 · outputs" if output_only else "Side sub 32 · region-fill proposals"
    mode_link = '<a href="compare.html">Compare with originals</a>' if output_only else '<a href="index.html">Outputs only</a>'
    return f"""<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{page_title}</title>
<style>
*{{box-sizing:border-box}}body{{margin:0;background:#edf1f3;color:#18252e;font:14px system-ui}}
header{{position:sticky;top:0;background:#fff;padding:18px 24px;box-shadow:0 2px 12px #0002;z-index:2}}
h1{{font-size:22px;margin:0 0 6px}}p{{line-height:1.4}}header p{{margin:3px 0 10px}}
input{{padding:9px 12px;width:min(480px,100%);border:1px solid #aab8c0;border-radius:6px}}
main{{padding:20px;display:grid;grid-template-columns:{grid_columns};gap:16px}}
article{{background:white;border-radius:9px;padding:14px;min-width:0;box-shadow:0 1px 5px #0001}}
article[hidden]{{display:none}}h2{{font-size:15px;overflow-wrap:anywhere;margin:0 0 5px}}
.badge{{color:#566b78;margin:0 0 10px}}.comparison{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}
figure{{margin:0;text-align:center;min-width:0}}.large{{height:145px;background:#f5f7f7;display:grid;place-items:center}}
.large img{{width:128px;height:128px;object-fit:contain}}figcaption{{min-height:40px;display:flex;align-items:center;justify-content:center;gap:8px;font-size:12px}}
figcaption img{{width:32px;height:32px;object-fit:contain}}.darkrow{{background:#142129;display:flex;justify-content:space-around;padding:8px;margin-top:8px}}
.darkrow img{{width:32px;height:32px;object-fit:contain;filter:brightness(0) invert(1)}}
.output-artwork{{margin:8px 0 12px;text-align:center}}
.output-large{{height:150px;background:#f5f7f7;display:grid;place-items:center}}
.output-large img{{width:128px;height:128px;object-fit:contain}}
.output-native{{display:flex;align-items:center;justify-content:center;gap:8px;margin-top:5px;font-size:12px;color:#516572}}
.output-native img{{object-fit:contain}}
.error{{color:#a12323;overflow-wrap:anywhere}}.missing{{color:#a12323}}
.note{{padding:6px 8px;border-radius:4px;margin:0 0 8px}}
.note.warning{{color:#763f18;background:#fff4e8}}.note.resolved{{color:#225b3d;background:#eaf5ee}}
.mark-controls{{display:flex;align-items:center;gap:5px;flex-wrap:wrap;margin:8px 0 10px}}
.mark-controls button{{padding:6px 8px;background:#f7fafb;border:1px solid #9baeb8;border-radius:5px;cursor:pointer;color:#18252e}}
.mark-controls button[aria-pressed="true"]{{background:#164c67;color:#fff;border-color:#164c67}}
.mark-controls button.clear{{font-size:12px}}.mark-state{{color:#516572;font-size:12px}}
.feedback-controls{{display:flex;align-items:flex-end;gap:7px;margin:0 0 10px}}
.feedback-controls label{{flex:1;font-size:12px;color:#516572}}.feedback-controls textarea{{display:block;width:100%;resize:vertical;min-height:43px;padding:6px;border:1px solid #9baeb8;border-radius:5px;font:13px system-ui;color:#18252e}}
.feedback-controls button{{padding:7px 9px;background:#f7fafb;border:1px solid #9baeb8;border-radius:5px;cursor:pointer;white-space:nowrap}}
article[data-user-mark="fix_small_dot"]{{outline:2px solid #b86c1b}}
article[data-user-mark="retain"]{{outline:2px solid #164c67}}
article[data-has-feedback="true"] .feedback-controls textarea{{border-color:#337458}}
</style>
<header><h1>{page_title}</h1>
<p>{len(records)} script proposals · {summary}</p>
<p>Showing your commented icons in the grid. {mode_link} · Use the filter to see all icons or your other marks.</p>
<input id="search" type="search" placeholder="Search icon name or status" aria-label="Search icons">
<select id="mark-filter" aria-label="Filter by your mark"><option value="feedback" selected>Commented icons</option><option value="all">All icons</option><option value="unmarked">Unmarked</option><option value="retain">Retain</option><option value="fix_small_dot">Fix small dot</option></select>
<span id="shown"></span><span id="save-status" role="status"></span></header>
<main>{''.join(cards)}</main>
<script src="../../sub32-review.js"></script></html>"""


def build(source: Path, output: Path, workers: int, limit: int | None = None,
          decisions_path: Path = DEFAULT_DECISIONS) -> dict:
    source = source.resolve()
    output = output.resolve()
    if output == source or output.is_relative_to(source):
        raise ValueError("Output must be separate from source")
    files = sorted(source.glob("*.svg"))
    if limit is not None:
        files = files[:limit]
    if not files:
        raise ValueError(f"No source SVGs in {source}")
    (output / "svg").mkdir(parents=True, exist_ok=True)
    decisions = json.loads(decisions_path.read_text()).get("decisions", {}) if decisions_path.exists() else {}
    marks = (json.loads(DEFAULT_MARKS.read_text()).get("marks", {})
             if source == DEFAULT_SOURCE.resolve() and DEFAULT_MARKS.exists() else {})
    jobs = [(str(path), str(output), effective_decision(path.stem, decisions, marks))
            for path in files]
    with ProcessPoolExecutor(max_workers=workers) as pool:
        records = list(pool.map(draft_one, jobs, chunksize=4))
    counts = Counter(row["status"] for row in records)
    summary = {
        "schema": "sub32-smart-region-fill-review/v2",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_folder": str(source),
        "output_folder": str(output),
        "source_policy": "Read current files on every run; source hashes are recorded, not frozen.",
        "method": "Existing step_2_fill_refactor_enhance.process_svg(algo='smart_fill') on native SVGs; no inferred closures.",
        "review_status": "AI_screened_drafts; held items require repair; no human approval",
        "review_decisions": str(decisions_path.resolve()),
        "total": len(records),
        "counts": dict(counts),
        "records": records,
    }
    (output / "manifest.json").write_text(json.dumps(summary, indent=2) + "\n")
    (output / "errors.json").write_text(json.dumps([row for row in records if row["status"] == "error"], indent=2) + "\n")
    (output / "index.html").write_text(gallery(records, source, output, output_only=True))
    (output / "compare.html").write_text(gallery(records, source, output))
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--decisions", type=Path, default=DEFAULT_DECISIONS)
    args = parser.parse_args()
    if args.workers < 1 or args.limit is not None and args.limit < 1:
        parser.error("workers and limit must be positive")
    report = build(args.source, args.out, args.workers, args.limit, args.decisions)
    print(json.dumps({key: report[key] for key in ("total", "counts", "output_folder")}, indent=2))


if __name__ == "__main__":
    main()
