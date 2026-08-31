#!/usr/bin/env python3
"""Audit final SVGs for canvas consistency, atomic-grid placement, and line angles."""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import math
import re
import shutil
import sys
from urllib.parse import quote
from pathlib import Path
import xml.etree.ElementTree as ET

from icon_geometry import parse_path

DESIGN_CANVAS = 48.0
ANGLE_STEP = 15.0
TOLERANCE = 1e-3
AXIS_GRID_ANGLES = (0, 45, 90, 135)


def collect(inputs: list[str]) -> list[Path]:
    files: set[Path] = set()
    for raw in inputs:
        path = Path(raw).expanduser().resolve()
        if path.is_dir():
            files.update(item for item in path.glob("*.svg") if item.is_file())
        elif path.is_file() and path.suffix.lower() == ".svg":
            files.add(path)
        else:
            print(f"warn: skipping missing/non-SVG input: {path}", file=sys.stderr)
    return sorted(files)


def number(value: str | None, fallback: float) -> float:
    if not value:
        return fallback
    match = re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", value)
    return float(match.group()) if match else fallback


def fractional(value: float) -> bool:
    return abs(value - round(value)) > TOLERANCE


def normalized_view(root: ET.Element) -> tuple[float, float, float]:
    values = [float(item) for item in root.get("viewBox", "0 0 48 48").replace(",", " ").split()]
    if len(values) != 4 or values[2] <= 0 or values[3] <= 0 or abs(values[2] - values[3]) > TOLERANCE:
        raise ValueError("viewBox must be a positive square")
    return values[2], values[3], DESIGN_CANVAS / values[2]


def inspect(path: Path, expected: str) -> dict:
    root = ET.parse(path).getroot()
    view_w, view_h, scale = normalized_view(root)
    stroke = number(root.get("stroke-width"), 0) * scale
    issues: list[dict] = []
    fractional_values = 0
    fractional_axis_segments = 0
    off_angle_segments = 0

    expected_canvas = {"design": 48.0, "ship": 24.0}.get(expected)
    if expected_canvas is not None and abs(view_w - expected_canvas) > TOLERANCE:
        issues.append({"code": "wrong-canvas", "detail": f"expected {expected_canvas:g}x{expected_canvas:g}, found {view_w:g}x{view_h:g}"})
    if expected == "either" and all(abs(view_w - size) > TOLERANCE for size in (24.0, 48.0)):
        issues.append({"code": "wrong-canvas", "detail": f"expected 24x24 or 48x48, found {view_w:g}x{view_h:g}"})
    if abs(stroke - 4.0) > TOLERANCE:
        issues.append({"code": "wrong-stroke", "detail": f"stroke normalizes to {stroke:g}u instead of 4u"})

    paths = root.findall(".//{*}path")
    other = [node.tag.rsplit("}", 1)[-1] for node in root.iter() if node is not root and node.tag.rsplit("}", 1)[-1] != "path"]
    if other:
        issues.append({"code": "non-path-geometry", "detail": f"unsupported final geometry tags: {sorted(set(other))}"})

    for path_index, node in enumerate(paths):
        data = node.get("d", "")
        if re.search(r"[CcSs]", data):
            issues.append({"code": "cubic", "detail": f"path {path_index} contains a cubic command"})
            continue
        try:
            commands = parse_path(data)
        except Exception as error:
            issues.append({"code": "parse-error", "detail": f"path {path_index}: {error}"})
            continue
        cursor = start = None
        for command_index, command in enumerate(commands):
            values = [coordinate * scale for point in command.points for coordinate in point]
            if command.arc:
                values.extend([command.arc[0] * scale, command.arc[1] * scale])
            fractional_values += sum(fractional(value) for value in values)
            if command.type == "M":
                cursor = start = command.points[0]
                continue
            if command.type == "L":
                end = command.points[0]
            elif command.type == "Z" and cursor is not None and start is not None:
                end = start
            else:
                if command.points:
                    cursor = command.points[-1]
                continue
            if cursor is None:
                issues.append({"code": "path-order", "detail": f"path {path_index} command {command_index} has no start point"})
                continue
            dx = (end[0] - cursor[0]) * scale
            dy = (end[1] - cursor[1]) * scale
            if math.hypot(dx, dy) > TOLERANCE:
                angle = (math.degrees(math.atan2(dy, dx)) + 360) % 180
                nearest = round(angle / ANGLE_STEP) * ANGLE_STEP
                if abs(angle - nearest) > 0.01:
                    off_angle_segments += 1
                endpoints = [cursor[0] * scale, cursor[1] * scale, end[0] * scale, end[1] * scale]
                if int(round(nearest)) in AXIS_GRID_ANGLES and any(fractional(value) for value in endpoints):
                    fractional_axis_segments += 1
            cursor = end

    if off_angle_segments:
        issues.append({"code": "off-angle", "detail": f"{off_angle_segments} straight segment(s) leave the 15-degree grid"})
    if fractional_axis_segments:
        issues.append({"code": "fractional-grid-lines", "detail": f"{fractional_axis_segments} axis/45-degree segment(s) use avoidable fractional design coordinates"})

    failure_codes = {"wrong-canvas", "wrong-stroke", "non-path-geometry", "cubic", "parse-error", "path-order", "off-angle", "fractional-grid-lines"}
    status = "fail" if any(issue["code"] in failure_codes for issue in issues) else ("review" if fractional_values else "pass")
    return {
        "file": path.name,
        "source": str(path),
        "status": status,
        "viewBox": [0, 0, view_w, view_h],
        "normalizedStroke": round(stroke, 4),
        "fractionalDesignValues": fractional_values,
        "fractionalAxisOr45Segments": fractional_axis_segments,
        "offAngleSegments": off_angle_segments,
        "issues": issues,
        "documentedExceptions": [],
    }


def apply_exceptions(result: dict, path: Path, entries: dict[str, dict]) -> dict:
    """Apply hash-locked, human-readable geometry exceptions to one result."""
    entry = entries.get(path.name)
    if not entry:
        return result
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != entry.get("sha256"):
        result["issues"].append({
            "code": "stale-exception",
            "detail": "documented exception hash does not match this SVG",
        })
        result["status"] = "fail"
        return result
    allowed = set(entry.get("allow", []))
    retained = []
    waived = []
    for issue in result["issues"]:
        if issue["code"] in allowed:
            waived.append(issue)
        else:
            retained.append(issue)
    if result["status"] == "review" and "fractional-design-values" in allowed:
        waived.append({
            "code": "fractional-design-values",
            "detail": f"{result['fractionalDesignValues']} fractional design value(s) are documented",
        })
    result["issues"] = retained
    if waived:
        result["documentedExceptions"] = [{
            "codes": sorted({item["code"] for item in waived}),
            "reason": entry.get("reason", "documented exact geometry"),
            "source": entry.get("source"),
        }]
    failure_codes = {"wrong-canvas", "wrong-stroke", "non-path-geometry", "cubic", "parse-error", "path-order", "off-angle", "fractional-grid-lines", "stale-exception"}
    result["status"] = "fail" if any(issue["code"] in failure_codes for issue in retained) else "pass"
    return result


def write_report(results: list[dict], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    icon_dir = output_dir / "icons"
    icon_dir.mkdir(exist_ok=True)
    for item in results:
        shutil.copy2(item["source"], icon_dir / item["file"])
    (output_dir / "grid-results.json").write_text(json.dumps(results, indent=2) + "\n")
    with (output_dir / "grid-results.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["file", "status", "grid_status", "keyshape_status", "keyshape_token", "painted_padding_left", "painted_padding_top", "painted_padding_right", "painted_padding_bottom", "viewBox", "fractional_design_values", "fractional_axis_or_45_segments", "off_angle_segments", "issues"])
        for item in results:
            keyfit = item.get("keyfit") or {}
            padding = keyfit.get("paintedPaddingDesign") or {}
            token = keyfit.get("assignedToken") or keyfit.get("targetToken") or {}
            writer.writerow([item["file"], item["overallStatus"], item["status"], keyfit.get("status", "not-run"), token.get("name", ""), padding.get("left", ""), padding.get("top", ""), padding.get("right", ""), padding.get("bottom", ""), item["viewBox"][2], item["fractionalDesignValues"], item["fractionalAxisOr45Segments"], item["offAngleSegments"], "; ".join(issue["detail"] for issue in item["issues"])])
    display_results = sorted(results, key=lambda item: (item["overallStatus"] != "fail", item["file"]))

    def target_token(item: dict) -> dict:
        keyfit = item.get("keyfit") or {}
        return keyfit.get("assignedToken") or keyfit.get("targetToken") or {
            "name": "square-40", "shape": "rect", "bounds": [4.0, 4.0, 44.0, 44.0]
        }

    def boundary_style(item: dict, centerline: bool = False) -> str:
        token = target_token(item)
        bounds = token.get("bounds", [4.0, 4.0, 44.0, 44.0])
        inset = 2.0 if centerline else 0.0
        left, top, right, bottom = (
            bounds[0] + inset, bounds[1] + inset,
            bounds[2] - inset, bounds[3] - inset,
        )
        style = (
            f"left:{left / 48 * 100:.6f}%;top:{top / 48 * 100:.6f}%;"
            f"width:{(right - left) / 48 * 100:.6f}%;height:{(bottom - top) / 48 * 100:.6f}%"
        )
        return style + (";border-radius:50%" if token.get("shape") == "circle" else "")

    def card_note(item: dict) -> str:
        keyfit = item.get("keyfit") or {}
        delta = keyfit.get("edgeDeltaToTarget") or {}
        adjustment = ", ".join(
            f"{side} {amount:+g}u" for side, amount in delta.items()
            if abs(amount) > 1e-6
        )
        if adjustment:
            return f"Target {target_token(item).get('name')}: {adjustment}"
        return keyfit.get("reason") or "; ".join(
            issue["detail"] for issue in item["issues"]
        ) or "; ".join(
            exception["reason"] for exception in item.get("documentedExceptions", [])
        ) or "Exact keyshape target and whole-unit grid geometry"

    cards = "".join(
        f'''<article class="icon-card status-{item['overallStatus']} keyfit-{(item.get('keyfit') or {}).get('status', 'not-run')}">
        <div class="preview" title="Target: {html.escape(target_token(item).get('name', 'unknown'), quote=True)}">
          <img src="icons/{quote(item['file'])}" alt="{html.escape(item['file'], quote=True)}">
          <span class="keyfit-boundary" style="{boundary_style(item)}" aria-hidden="true"></span>
          <span class="centerline-boundary" style="{boundary_style(item, True)}" aria-hidden="true"></span>
        </div>
        <div class="card-body">
          <div class="card-heading"><code>{html.escape(item['file'])}</code><span class="badge overall">{item['overallStatus']}</span></div>
          <div class="gate-row"><span class="gate grid-{item['status']}">Grid {item['status']}</span><span class="gate shape-{(item.get('keyfit') or {}).get('status', 'not-run')}">Keyshape {(item.get('keyfit') or {}).get('status', 'not-run')}</span></div>
          <div class="metrics">{html.escape(target_token(item).get('name', 'unknown'))} · {item['fractionalAxisOr45Segments']} fractional axis/45°</div>
          <div class="note">{html.escape(card_note(item))}</div>
        </div>
        </article>'''
        for item in display_results
    )
    rows = "".join(
        f"<tr><td><code>{html.escape(item['file'])}</code></td><td>{item['overallStatus']}</td><td>{item['status']}</td><td>{(item.get('keyfit') or {}).get('status', 'not-run')}</td><td>{html.escape(target_token(item).get('name', '—'))}</td><td>{item['viewBox'][2]:g}</td>"
        f"<td>{item['fractionalDesignValues']}</td><td>{item['fractionalAxisOr45Segments']}</td>"
        f"<td>{html.escape('; '.join(issue['detail'] for issue in item['issues']) or 'documented exact geometry')}</td>"
        f"<td>{html.escape('; '.join(exception['reason'] for exception in item.get('documentedExceptions', [])) or '—')}</td></tr>"
        for item in display_results
    ) or '<tr><td colspan="6">No grid failures or reviews.</td></tr>'
    document = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Unlimited Shapes visual grid audit</title>
<style>
:root{{--ink:#18202a;--muted:#667085;--line:#d9dee7;--major:#aeb8c7;--pass:#16794b;--review:#a56300;--fail:#c83232}}
*{{box-sizing:border-box}}body{{font:14px system-ui,-apple-system,sans-serif;margin:0;color:var(--ink);background:#f4f6f9}}
header{{position:sticky;top:0;z-index:10;padding:20px 28px;background:rgba(255,255,255,.94);border-bottom:1px solid var(--line);backdrop-filter:blur(10px)}}
h1{{font-size:24px;margin:0 0 6px}}header p{{margin:0;color:var(--muted)}}main{{padding:24px 28px 48px}}
.legend{{display:flex;flex-wrap:wrap;gap:14px;margin:0 0 20px;color:var(--muted)}}.legend span{{display:flex;align-items:center;gap:6px}}
.swatch{{width:18px;height:18px;border:1px solid var(--line);background-color:white;background-image:linear-gradient(to right,var(--major) 1px,transparent 1px),linear-gradient(to bottom,var(--major) 1px,transparent 1px);background-size:25% 25%}}
.key-swatch{{width:18px;height:18px;border:2px solid rgba(22,121,75,.7);background:#fff}}.center-swatch{{width:18px;height:18px;border:2px dashed rgba(37,99,235,.7);background:#fff}}
.gallery{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px}}
.icon-card{{overflow:hidden;border:1px solid var(--line);border-radius:12px;background:#fff;box-shadow:0 1px 2px rgba(16,24,40,.04)}}
.preview{{position:relative;aspect-ratio:1;overflow:hidden;background-color:#fff;background-image:linear-gradient(to right,rgba(72,85,105,.48) 1px,transparent 1px),linear-gradient(to bottom,rgba(72,85,105,.48) 1px,transparent 1px),linear-gradient(to right,rgba(121,134,153,.27) 1px,transparent 1px),linear-gradient(to bottom,rgba(121,134,153,.27) 1px,transparent 1px);background-size:calc(100% / 12) calc(100% / 12),calc(100% / 12) calc(100% / 12),calc(100% / 48) calc(100% / 48),calc(100% / 48) calc(100% / 48)}}
.preview img{{position:absolute;inset:0;width:100%;height:100%;display:block;z-index:2}}.keyfit-boundary{{position:absolute;z-index:3;pointer-events:none;border:2px solid rgba(22,121,75,.68)}}.centerline-boundary{{position:absolute;z-index:3;pointer-events:none;border:1px dashed rgba(37,99,235,.72)}}.keyfit-fail .keyfit-boundary{{border-color:rgba(200,50,50,.9);border-width:3px}}
.card-body{{padding:12px}}.card-heading{{display:flex;align-items:flex-start;justify-content:space-between;gap:8px}}code{{font-size:12px;overflow-wrap:anywhere}}.badge{{padding:2px 7px;border-radius:999px;font-size:10px;font-weight:750;text-transform:uppercase;background:#eaf7f0;color:var(--pass)}}
.status-review .badge{{background:#fff3dc;color:var(--review)}}.status-fail .badge{{background:#ffebeb;color:var(--fail)}}.gate-row{{display:flex;gap:6px;margin-top:9px;flex-wrap:wrap}}.gate{{font-size:10px;font-weight:700;padding:2px 6px;border-radius:5px;text-transform:uppercase;background:#edf1f5;color:var(--muted)}}.grid-pass,.shape-pass{{background:#eaf7f0;color:var(--pass)}}.grid-review{{background:#fff3dc;color:var(--review)}}.grid-fail,.shape-fail{{background:#ffebeb;color:var(--fail)}}.metrics{{margin-top:8px;font-size:12px;color:var(--muted)}}.note{{margin-top:5px;font-size:11px;line-height:1.35;color:var(--muted);display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}}
details{{margin-top:32px;background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px}}summary{{cursor:pointer;font-weight:650}}table{{margin-top:12px;border-collapse:collapse;width:100%;font-size:12px}}th,td{{border-bottom:1px solid #e5e7eb;padding:8px;text-align:left;vertical-align:top}}th{{background:#f5f6f8}}
@media(max-width:600px){{header,main{{padding-left:14px;padding-right:14px}}.gallery{{grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px}}}}
</style></head>
<body><header><h1>Visual grid + keyshape audit</h1><p>{len(results)} checked · {sum(x['overallStatus']=='pass' for x in results)} overall pass · {sum(x['overallStatus']=='review' for x in results)} review · {sum(x['overallStatus']=='fail' for x in results)} overall fail</p></header>
<main><div class="legend"><span><i class="swatch"></i>1u grid, heavier every 4u</span><span><i class="key-swatch"></i>selected exact painted-bounds target</span><span><i class="center-swatch"></i>target inset by the 2u stroke radius</span></div>
<section class="gallery">{cards}</section>
<details><summary>Open numeric audit table</summary><table><thead><tr><th>File</th><th>Overall</th><th>Grid</th><th>Keyshape</th><th>Token</th><th>Canvas</th><th>Fractional values</th><th>Fractional axis/45° lines</th><th>Issues</th><th>Documented exception</th></tr></thead><tbody>{rows}</tbody></table></details></main></body></html>"""
    (output_dir / "grid-report.html").write_text(document)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+")
    parser.add_argument("--expected", choices=("design", "ship", "either"), default="either")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--exceptions", type=Path, help="hash-locked JSON exceptions for exact rotated/arc geometry")
    parser.add_argument("--keyfit-results", type=Path, help="keyfit-results.json to include in the visual report and overall status")
    args = parser.parse_args()
    files = collect(args.inputs)
    if not files:
        parser.error("no SVG files found")
    entries: dict[str, dict] = {}
    if args.exceptions:
        document = json.loads(args.exceptions.read_text())
        entries = document.get("files", {})
    results = [apply_exceptions(inspect(path, args.expected), path, entries) for path in files]
    keyfits: dict[str, dict] = {}
    if args.keyfit_results:
        keyfit_document = json.loads(args.keyfit_results.read_text())
        if not isinstance(keyfit_document, list):
            parser.error("--keyfit-results must contain a JSON list")
        keyfits = {item.get("file", ""): item for item in keyfit_document}
    for result in results:
        keyfit = keyfits.get(result["file"])
        if args.keyfit_results and keyfit is None:
            keyfit = {"status": "fail", "reason": "missing-keyshape-result", "assignedToken": None}
        result["keyfit"] = keyfit
        keyfit_status = (keyfit or {}).get("status")
        result["overallStatus"] = "fail" if result["status"] == "fail" or keyfit_status == "fail" else ("review" if result["status"] == "review" or keyfit_status not in (None, "pass") else "pass")
    write_report(results, args.output_dir)
    for item in results:
        keyfit_status = (item.get("keyfit") or {}).get("status", "not-run")
        print(f"{item['file']}: {item['overallStatus'].upper()} (grid {item['status']}, keyshape {keyfit_status}; {item['fractionalAxisOr45Segments']} fractional grid-line segments, {item['offAngleSegments']} off-angle)")
    print(f"wrote {len(results)} grid reports to {args.output_dir}")
    return 1 if any(item["overallStatus"] == "fail" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
