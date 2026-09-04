#!/usr/bin/env python3
"""Check the clearance between disconnected centerline components in native SVGs.

Splits M-separated drawable subpaths, including those inside a single path.
Uses continuous segment distances and bounded curve approximation, not distances
between element boxes or sampled points. Actual centerline connections form one
component; touching/overlapping ink alone never exempts a too-close pair.

  python3 core/check_svg_spacing.py icon.svg --output-dir qa/spacing
  python3 core/check_svg_spacing.py output --icon-type normal --json

The default normal profile is 48px with 4px stroke and an 8u centerline minimum
(4u clear ink gap). Settings resolve from icon_profiles.json. Other profiles must
be selected explicitly; this command never scales an SVG or edits its geometry.
Exit 0: every selected file passes; 1: violation, uncertainty, or input/report
error; 2: CLI misuse. A spacing pass is not complete icon/visual approval.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET

MAX_INPUT_BYTES = 4 * 1024 * 1024
PALETTE = ("#2563eb", "#9333ea", "#087f5b", "#c2410c", "#be185d", "#0e7490")
REPAIR = "Repair the editable geometry, regenerate both SVG aliases, and rerun spacing and all affected QA; do not lower thresholds to hide a failure."
NOTICE = (
    "Measures disconnected centerline components, not internal gaps within a connected shape. "
    "Geometric connections are not semantic approval; structural relationships, holes/pinches, "
    "keyshapes, grid and native-size visual review remain separate requirements."
)


def _read_bytes(path: Path) -> bytes:
    if not path.is_file() or path.stat().st_size > MAX_INPUT_BYTES:
        raise ValueError(f"input must be a regular SVG no larger than {MAX_INPUT_BYTES} bytes: {path}")
    data = path.read_bytes()
    if len(data) > MAX_INPUT_BYTES:
        raise ValueError("SVG exceeds the input byte limit")
    return data


def _result(source: Path | None) -> dict:
    return {"file": source.name if source else None, "source": str(source) if source else None,
            "ok": False, "status": "error", "iconType": None, "canvas": None,
            "strokeWidth": None, "requiredCenterline": None, "requiredInkClearance": None,
            "contours": [], "components": [], "pairs": [], "connectedPairs": [],
            "errors": [], "svgSha256": None, "profileSha256": None,
            "reportPath": None, "overlayPath": None, "notice": NOTICE, "repair": REPAIR}


def _failure(result: dict, error: object) -> None:
    result.update(ok=False, status="error")
    result["errors"].append(str(error))


def _write(path: Path, data: str, protected=()) -> None:
    """Replace a QA file atomically, never a selected source or symlink target."""
    if path.is_symlink() or path.exists() and not path.is_file():
        raise ValueError(f"unsafe report target: {path}")
    for original in protected:
        original = Path(original).expanduser().absolute()
        if path.resolve() == original.resolve() or (
            path.exists() and original.exists() and path.samefile(original)
        ):
            raise ValueError(f"report would overwrite an input: {path}")
    staged = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=".spacing-", delete=False) as handle:
            staged = Path(handle.name)
            handle.write(data)
        os.replace(staged, path)
    finally:
        if staged is not None and staged.exists():
            staged.unlink()


def _json(value) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n"


def _directory(path: Path) -> Path:
    path = Path(path).expanduser().absolute()
    if path.is_symlink():
        raise ValueError("QA output directory cannot be a symlink")
    path.mkdir(parents=True, exist_ok=True)
    return path


def overlay_svg(result: dict) -> str:
    """A native-size diagnostic only: component colors and shortest-gap markers."""
    canvas, stroke = result["canvas"], result["strokeWidth"]
    colors = {component["id"]: PALETTE[index % len(PALETTE)]
              for index, component in enumerate(result["components"])}
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas}" height="{canvas}" viewBox="0 0 {canvas} {canvas}">',
             '<title>Disconnected stroke spacing: colored components and failing nearest pairs</title>']
    for contour in result["contours"]:
        color = colors.get(contour.get("componentId"), "#64748b")
        parts.append(f'<path d="{html.escape(contour["pathData"], quote=True)}" fill="none" '
                     f'stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"/>')
    for pair in result["pairs"]:
        if pair["status"] == "pass":
            continue
        (x1, y1), (x2, y2) = pair["nearestPoints"]
        parts.append(f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="#dc2626" stroke-width="0.5" stroke-dasharray="1 1"/>')
        for x, y in ((x1, y1), (x2, y2)):
            parts.append(f'<circle cx="{x}" cy="{y}" r="0.65" fill="white" stroke="#dc2626" stroke-width="0.35"/>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def check_file(path, *, icon_type="normal", output_dir=None) -> dict:
    """Read one actual SVG. A malformed/unsupported file always fails closed."""
    source = Path(path).expanduser().absolute()
    result, data = _result(source), None
    try:
        from icon_geometry import resolve_icon
        from icon_profiles import get_profile, svg_native_size_issues
        from profile_adaptation import read_design_svg
        from stroke_distance import analyze_paths

        profile = get_profile(icon_type)
        minimum = profile["validation"]["minimumDistinctCenterlineDistance"]
        result.update(iconType=icon_type, canvas=profile["canvas"], strokeWidth=profile["strokeWidth"],
                      requiredCenterline=minimum, requiredInkClearance=max(0, minimum - profile["strokeWidth"]),
                      geometryTolerance=profile["validation"]["geometryTolerance"],
                      profileSha256=hashlib.sha256(json.dumps(profile, sort_keys=True, separators=(",", ":"),
                                                             ensure_ascii=False, allow_nan=False).encode()).hexdigest())
        data = _read_bytes(source)
        result["source"] = str(source.resolve())
        result["svgSha256"] = hashlib.sha256(data).hexdigest()
        with tempfile.TemporaryDirectory(prefix="svg-spacing-input-") as temporary:
            snapshot = Path(temporary) / "input.svg"
            snapshot.write_bytes(data)
            parsed = read_design_svg(snapshot)
            root = ET.parse(snapshot).getroot()
            for field in ("width", "height"):
                if field not in root.attrib:
                    raise ValueError(f"native SVG must explicitly declare {field}")
            issues = svg_native_size_issues(root.attrib, icon_type)
            if issues:
                raise ValueError("; ".join(issue["detail"] for issue in issues))
            if parsed["canvas"] != profile["canvas"] or parsed["strokeWidth"] != profile["strokeWidth"]:
                raise ValueError(f"SVG must use {icon_type}'s native {profile['canvas']}px canvas and {profile['strokeWidth']}px stroke")
            paths = resolve_icon({"schemaVersion": 2, "elements": parsed["elements"]})
            measurement = analyze_paths(paths, minimum_distance=minimum, stroke_width=profile["strokeWidth"],
                                        tolerance=profile["validation"]["geometryTolerance"])
            result.update(measurement)
            if result.get("status") not in ("pass", "fail", "review") or not isinstance(result.get("errors"), list):
                raise ValueError("spacing engine returned an invalid result")
            result["ok"] = result["status"] == "pass" and not result["errors"]
    except Exception as error:
        _failure(result, f"{type(error).__name__}: {error}")
    finally:
        if data is not None:
            try:
                if _read_bytes(source) != data:
                    _failure(result, "SVG changed during measurement; rerun the checker")
            except (OSError, ValueError) as error:
                _failure(result, f"SVG became unreadable during measurement: {error}")
    if output_dir is not None:
        try:
            directory = _directory(output_dir)
            files = _directory(directory / "files")
            stem = re.sub(r"[^a-zA-Z0-9_-]+", "-", source.stem)[:70] or "icon"
            prefix = f"{stem}-{hashlib.sha256(str(source).encode()).hexdigest()[:12]}-"
            evidence = Path(tempfile.mkdtemp(prefix=prefix, dir=files)).resolve()
            result["reportPath"] = str(evidence / "spacing.json")
            if result["contours"]:
                result["overlayPath"] = str(evidence / "spacing.svg")
                _write(Path(result["overlayPath"]), overlay_svg(result), [source])
            _write(Path(result["reportPath"]), _json(result), [source])
        except Exception as error:
            _failure(result, f"report error: {error}")
    return result


def check_drawing(text, *, icon_type="normal") -> dict:
    """In-memory convenience API, with the same strict native-SVG contract."""
    try:
        data = text.encode("utf-8") if isinstance(text, str) else bytes(text)
        if len(data) > MAX_INPUT_BYTES:
            raise ValueError("SVG exceeds the input byte limit")
        with tempfile.TemporaryDirectory(prefix="svg-spacing-drawing-") as temporary:
            path = Path(temporary) / "icon.svg"
            path.write_bytes(data)
            result = check_file(path, icon_type=icon_type)
        result["source"] = None
        return result
    except Exception as error:
        result = _result(None)
        _failure(result, error)
        return result


def collect(inputs: list[str]) -> tuple[list[Path], list[dict]]:
    files, errors = set(), []
    for raw in inputs:
        path = Path(raw).expanduser().absolute()
        try:
            if path.is_dir():
                selected = [item for item in path.iterdir() if item.suffix.lower() == ".svg"]
                if not selected:
                    raise ValueError("folder contains no immediate SVG files")
                files.update(selected)
            elif path.suffix.lower() == ".svg":
                files.add(path)
            else:
                raise ValueError("input must be an SVG file or flat SVG folder")
        except (OSError, ValueError) as error:
            result = _result(path)
            _failure(result, error)
            errors.append(result)
    return sorted(files), errors


def _report_html(aggregate: dict, directory: Path) -> str:
    from urllib.parse import quote

    parts = ['<!doctype html><html lang="en"><meta charset="utf-8"><title>SVG spacing report</title>',
             '<style>body{font:14px system-ui;margin:24px;max-width:1100px;color:#18202c}table{border-collapse:collapse;width:100%;margin:12px 0}td,th{border:1px solid #ccd3dc;padding:6px;text-align:left}img{background:#f8fafc}code{overflow-wrap:anywhere}</style>',
             '<h1>Disconnected stroke spacing</h1>',
             f'<p>{aggregate["checked"]} files; {aggregate["failed"]} failing or requiring review. Native-size previews; not production artwork.</p>',
             f'<p>{html.escape(NOTICE)}</p>']
    for row in aggregate["rows"]:
        parts.append(f'<h2>{html.escape(row["file"] or "input")} — {html.escape(row["status"])}</h2>')
        if row.get("overlayPath"):
            href = quote(os.path.relpath(row["overlayPath"], directory), safe="/")
            parts.append(f'<img src="{href}" width="{row["canvas"]}" height="{row["canvas"]}" alt="Colored stroke components and failing gaps">')
        for error in row["errors"]:
            parts.append(f'<p>{html.escape(str(error))}</p>')
        if row["requiredCenterline"] is not None:
            parts.append(f'<p>Required centerline distance: {row["requiredCenterline"]:g}u. Required ink gap: {row["requiredInkClearance"]:g}u. '
                         f'{len(row["contours"])} contours in {len(row["components"])} connected components.</p>')
        if row["components"]:
            parts.append('<ul>')
            for index, component in enumerate(row["components"]):
                label = html.escape(component["id"] + ": " + ", ".join(component["contourIds"]))
                parts.append(f'<li style="color:{PALETTE[index % len(PALETTE)]}"><code>{label}</code></li>')
            parts.append('</ul>')
        if not row["pairs"]:
            parts.append('<p>No disconnected pairs measured; this does not assess internal gaps.</p>')
        else:
            parts.append('<table><tr><th>Closest contours</th><th>Centerline (u)</th><th>Ink clearance (u)</th><th>Verdict</th></tr>')
            for pair in row["pairs"]:
                label = html.escape(" ↔ ".join(pair["closestContours"]))
                reason = html.escape(str(pair.get("reason", "")))
                parts.append(f'<tr><td><code>{label}</code></td><td>{pair["centerlineDistance"]:.4f}</td>'
                             f'<td>{pair["inkClearance"]:.4f}</td><td>{html.escape(pair["status"])}: {reason}</td></tr>')
            parts.append('</table>')
    return "\n".join(parts + ['</html>']) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("inputs", nargs="+", metavar="SVG_OR_FOLDER")
    parser.add_argument("--icon-type", default="normal", help="configured profile (default normal); no automatic size inference")
    parser.add_argument("--output-dir", type=Path, help="write per-file JSON/overlay and aggregate JSON/HTML")
    parser.add_argument("--json", action="store_true", help="print machine-readable aggregate")
    parser.add_argument("--quiet", "-q", action="store_true", help="suppress human output")
    args = parser.parse_args(argv)
    files, rows = collect(args.inputs)
    rows.extend(check_file(path, icon_type=args.icon_type, output_dir=args.output_dir) for path in files)
    aggregate = {"ok": bool(rows) and all(row["ok"] for row in rows), "checked": len(rows),
                 "failed": sum(not row["ok"] for row in rows), "rows": rows, "repair": REPAIR}
    if args.output_dir is not None:
        try:
            from icon_profiles import PROFILE_SOURCE
            directory = _directory(args.output_dir)
            protected = [*files, PROFILE_SOURCE]
            _write(directory / "spacing-report.html", _report_html(aggregate, directory), protected)
            _write(directory / "spacing-results.json", _json(aggregate), protected)
        except Exception as error:
            aggregate.update(ok=False, reportError=str(error))
    if args.json:
        print(_json(aggregate), end="")
    elif not args.quiet:
        for row in rows:
            print(f"{row['status'].upper()} {row['file']}: {len(row['contours'])} contours / {len(row['components'])} components")
            for error in row["errors"]:
                print(f"  {error}")
            for pair in row["pairs"]:
                print(f"  {' / '.join(pair['closestContours'])}: {pair['centerlineDistance']:.4f}u centerline, "
                      f"{pair['inkClearance']:.4f}u ink gap — {pair['status']}")
        print(f"{aggregate['checked'] - aggregate['failed']}/{aggregate['checked']} passed spacing; not full icon approval.")
        if not aggregate["ok"]:
            print(aggregate.get("reportError", REPAIR))
    return 0 if aggregate["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
