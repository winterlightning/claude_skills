#!/usr/bin/env python3
"""Fail-closed native canvas, stroke and declared painted-keyshape verification.

The numerical authority is core/icon_profiles.json, not a second size table.
Editable metadata supplies the expected profile and keyfitCheck.targetToken;
the actual SVG supplies geometry. No keyshape is inferred from an output.
Exact and documented optical fit use the existing stroke-inclusive raster gate.

Run from the repository root:
  python3 core/validate_icon_keyshapes.py output/icon.svg --editable editable/icon.json
  python3 core/validate_icon_keyshapes.py output --expected-editable-dir editable --output-dir qa/canvas-keyshape

Exit 0 means every selected SVG passed this gate, not production approval.
Exit 1 means validation, input, dependency or report failure; 2 is CLI misuse.
Only explicitly requested QA reports and temporary measurement files are written.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET

MAX_INPUT_BYTES = 4 * 1024 * 1024
MAX_RASTER_PIXELS = 32 * 1024 * 1024
REPAIR = (
    "Repair the editable geometry, regenerate canonical SVG and its design alias, "
    "recheck prerequisites, then restart distance -> holes -> keyshape. If exact proportions distort the subject, "
    "the AI may approve the documented optical keyshape exception with rationale and measured paintedBounds; "
    "the exceptional centerline width and height must each be divisible by 4, and the rationale must record that size. "
    "Containment and all other gates still apply. Do not change profile thresholds or edit reports to obtain a pass."
)


def _json_bytes(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _issue(result: dict, code: str, detail: str) -> None:
    result["issues"].append({"code": code, "detail": detail})
    result["errors"].append(detail)
    result["ok"], result["status"] = False, "fail"
    if result["fault"] is None:
        result["fault"] = code


def _result(path: Path | None = None) -> dict:
    return {
        "ok": False, "status": "fail", "file": path.name if path else None,
        "source": str(path) if path else None, "iconType": None,
        "canvas": None, "stroke": None, "keyshape": None, "key": None,
        "fitMode": None, "keyfit": None, "painted": None,
        "svgSha256": None, "editableSha256": None, "profileSha256": None,
        "evidenceDirectory": None, "keyfitReport": None, "keyfitOverlay": None,
        "fault": None, "issues": [], "errors": [], "repair": REPAIR,
        "notice": "This gate does not replace structural/grid/spacing/hole QA or native-size visual acceptance.",
    }


def _read_bytes(path: Path) -> bytes:
    if not path.is_file():
        raise ValueError(f"not a readable regular file: {path}")
    if path.stat().st_size > MAX_INPUT_BYTES:
        raise ValueError(f"input exceeds the {MAX_INPUT_BYTES}-byte limit: {path}")
    data = path.read_bytes()
    if len(data) > MAX_INPUT_BYTES:
        raise ValueError(f"input exceeds the {MAX_INPUT_BYTES}-byte limit: {path}")
    return data


def _unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON member: {key}")
        result[key] = value
    return result


def _invalid_constant(value):
    raise ValueError(f"non-finite JSON number: {value}")


def _read_document(editable):
    if editable is None:
        raise ValueError("expected editable metadata is required; use --editable or --expected-editable-dir (no inferred keyshape)")
    if isinstance(editable, dict):
        document = deepcopy(editable)
        return document, _json_bytes(document), None
    path = Path(editable).expanduser().absolute()
    data = _read_bytes(path)
    document = json.loads(data.decode("utf-8-sig"), object_pairs_hook=_unique_object,
                          parse_constant=_invalid_constant)
    if not isinstance(document, dict):
        raise ValueError("editable metadata must be a JSON object")
    return document, data, path


def _expected(document: dict, icon_type: str | None):
    from icon_profiles import validate_document_profile, token_named

    if type(document.get("schemaVersion")) is not int or document["schemaVersion"] != 2:
        raise ValueError("expected metadata must declare schemaVersion: 2")
    for field in ("iconType", "canvas", "strokeWidth"):
        if field not in document:
            raise ValueError(f"expected metadata must explicitly declare {field}")
    if not isinstance(document["iconType"], str):
        raise ValueError("iconType must be a configured profile name")
    if icon_type is not None and icon_type != document["iconType"]:
        raise ValueError(f"--icon-type {icon_type!r} conflicts with declared iconType {document['iconType']!r}")
    name, profile = validate_document_profile(document)
    check = document.get("keyfitCheck")
    if not isinstance(check, dict) or not isinstance(check.get("targetToken"), str):
        raise ValueError("expected metadata must declare keyfitCheck.targetToken")
    token = token_named(check["targetToken"], name)
    if token is None:
        raise ValueError(f"unknown declared keyshape {check['targetToken']!r} for {name}")
    if check.get("mode", "exact") not in ("exact", "optical"):
        raise ValueError("keyfitCheck.mode must be exact or optical")
    return name, profile, token, deepcopy(check)


def _report_directory(output_dir: Path, source: Path) -> Path:
    output_dir = Path(output_dir).expanduser().absolute()
    if output_dir.is_symlink():
        raise ValueError("QA output directory cannot be a symlink")
    output_dir.mkdir(parents=True, exist_ok=True)
    files = output_dir / "files"
    if files.is_symlink():
        raise ValueError("QA files directory cannot be a symlink")
    files.mkdir(exist_ok=True)
    stem = re.sub(r"[^a-zA-Z0-9_-]+", "-", source.stem)[:70] or "icon"
    prefix = f"{stem}-{_sha(str(source).encode())[:12]}-"
    # Fresh exclusive directories cannot reuse stale raster evidence.
    return Path(tempfile.mkdtemp(prefix=prefix, dir=files)).resolve()


def _write_json(path: Path, value, protected=()) -> None:
    if path.is_symlink() or path.exists() and not path.is_file():
        raise ValueError(f"unsafe QA report target: {path}")
    for original in protected:
        original = Path(original).expanduser()
        if path.resolve() == original.resolve() or (
            path.exists() and original.exists() and path.samefile(original)
        ):
            raise ValueError(f"QA report would overwrite an input: {path}")
    staged = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", prefix=".keyshape-", dir=path.parent,
                                         delete=False) as handle:
            staged = Path(handle.name)
            handle.write(json.dumps(value, indent=2, ensure_ascii=False,
                                    allow_nan=False).encode("utf-8") + b"\n")
        os.replace(staged, path)
    finally:
        if staged is not None and staged.exists():
            staged.unlink()


def _measure(snapshot: Path, source: Path, document: dict, name: str,
             profile: dict, token: dict, check: dict, evidence: Path | None,
             result: dict) -> None:
    # Missing dependencies are caught by check_file and cannot grant a pass.
    import check_keyfit
    from icon_geometry import resolve_icon, sample
    from icon_profiles import svg_native_size_issues, validate_container_slot
    from keyfit import circle_overflow
    from profile_adaptation import read_design_svg
    from validate_icon import container_paint_overlap

    parsed = read_design_svg(snapshot)
    root = ET.parse(snapshot).getroot()
    for field in ("width", "height"):
        if field not in root.attrib:
            _issue(result, "missing-native-size", f"canonical SVG must explicitly declare native {field}")
    for item in svg_native_size_issues(root.attrib, name):
        _issue(result, item["code"], item["detail"])
    if parsed["canvas"] != profile["canvas"]:
        _issue(result, "wrong-canvas", f"SVG canvas must equal {name}'s {profile['canvas']}px canvas")
    if parsed["strokeWidth"] != profile["strokeWidth"]:
        _issue(result, "wrong-stroke", f"SVG stroke must equal {name}'s {profile['strokeWidth']}px stroke")
    if result["errors"]:
        return

    paths = resolve_icon({"schemaVersion": 2, "elements": parsed["elements"]})
    points = [point for item in paths for point in sample(item["commands"])[0]]
    if not points:
        raise ValueError("SVG has no measurable outline geometry")
    radius = profile["strokeWidth"] / 2
    canvas = profile["canvas"]
    bounds = [min(x for x, _ in points) - radius,
              min(y for _, y in points) - radius,
              max(x for x, _ in points) + radius,
              max(y for _, y in points) + radius]
    result["sampledPaintedBounds"] = bounds
    tolerance = profile["validation"]["geometryTolerance"]
    # A fragment entirely outside the padded raster viewport must not disappear
    # from measurement and grant a false pass.
    if min(bounds[:2]) < -tolerance or max(bounds[2:]) > canvas + tolerance:
        _issue(result, "canvas-overflow", f"stroke-inclusive geometry extends outside the native canvas: {bounds}")
    if token["shape"] == "circle":
        excess = circle_overflow(points, profile["strokeWidth"], name, token)
        if excess > profile["validation"]["keyshapeTolerance"]:
            _issue(result, "circle-overflow", f"paint exceeds declared circular keyshape by {excess:.4g}u")
    if profile.get("containerSlot"):
        slot = validate_container_slot(document, profile)
        if container_paint_overlap(points, slot, profile["strokeWidth"], tolerance):
            _issue(result, "container-slot", "container paint enters its protected clearance region")

    samples = check_keyfit.DEFAULT_SAMPLES_PER_UNIT
    if math.ceil((canvas + 2 * profile["strokeWidth"]) * samples) ** 2 > MAX_RASTER_PIXELS:
        raise ValueError("profile exceeds the bounded raster verification budget")
    raster_dir = evidence or snapshot.parent / "measurement"
    raster_dir.mkdir(exist_ok=True)
    measured = check_keyfit.process(snapshot, raster_dir, samples, None,
                                   token["name"], name, check)
    if not isinstance(measured, dict) or measured.get("status") not in ("pass", "fail"):
        raise ValueError("painted-keyshape checker returned no valid verdict")
    measured.update(file=source.name, source=str(source))
    result["keyfit"] = measured
    result["painted"] = measured.get("paintedBoundsDesign")
    if evidence is not None:
        report = evidence / f"{source.stem}.keyfit.json"
        overlay = evidence / f"{source.stem}_keyfit.png"
        if not report.is_file() or not overlay.is_file():
            raise ValueError("painted-keyshape checker did not produce required evidence")
        _write_json(report, measured)
        result.update(keyfitReport=str(report), keyfitOverlay=str(overlay))
    if measured["status"] != "pass":
        _issue(result, "keyshape", "painted-keyshape check failed: " + str(measured.get("reason", "unknown failure")))
    result["ok"] = not result["errors"]
    result["status"] = "pass" if result["ok"] else "fail"


def check_file(path, *, editable=None, icon_type=None, output_dir=None) -> dict:
    """Measure one actual SVG against explicit metadata; never change inputs.

    Metadata may be a Path or dictionary. It need not duplicate the geometry:
    full editable/SVG parity belongs to the separate structural gate.
    """
    source = Path(path).expanduser().absolute()
    result = _result(source)
    evidence = None
    source_data = metadata_data = None
    metadata_path = None
    try:
        source_data = _read_bytes(source)
        result["svgSha256"] = _sha(source_data)
        document, metadata_data, metadata_path = _read_document(editable)
        result["editableSha256"] = _sha(metadata_data)
        name, profile, token, check = _expected(document, icon_type)
        result.update(iconType=name, canvas=profile["canvas"], stroke=profile["strokeWidth"],
                      keyshape=token, key=token["orientation"], fitMode=check.get("mode", "exact"),
                      profileSha256=_sha(_json_bytes(profile)))
        if output_dir is not None:
            evidence = _report_directory(Path(output_dir), source)
            result["evidenceDirectory"] = str(evidence)
        with tempfile.TemporaryDirectory(prefix="icon-keyshape-check-") as temporary:
            snapshot = Path(temporary) / source.name
            snapshot.write_bytes(source_data)
            _measure(snapshot, source, document, name, profile, token, check, evidence, result)
    except Exception as error:
        _issue(result, "verification-error", f"{type(error).__name__}: {error}")
    finally:
        for original, data in ((source, source_data), (metadata_path, metadata_data)):
            if original is not None and data is not None:
                try:
                    if _read_bytes(original) != data:
                        _issue(result, "changed-input", f"input changed during verification: {original}; rerun")
                except (OSError, ValueError) as error:
                    _issue(result, "changed-input", f"input became unreadable during verification: {original}: {error}")
    if evidence is not None:
        try:
            _write_json(evidence / "canvas-keyshape.json", result)
        except (OSError, ValueError) as error:
            _issue(result, "report-error", str(error))
    return result


def check_drawing(text, *, document=None, icon_type=None) -> dict:
    """In-memory convenience API. Explicit profile/keyshape metadata is required."""
    try:
        data = text.encode("utf-8") if isinstance(text, str) else bytes(text)
        if len(data) > MAX_INPUT_BYTES:
            raise ValueError("SVG exceeds the input limit")
        with tempfile.TemporaryDirectory(prefix="icon-drawing-check-") as temporary:
            path = Path(temporary) / "icon.svg"
            path.write_bytes(data)
            result = check_file(path, editable=document, icon_type=icon_type)
        result["source"] = None
        if result["keyfit"]:
            result["keyfit"]["source"] = None
        return result
    except Exception as error:
        result = _result()
        _issue(result, "verification-error", f"{type(error).__name__}: {error}")
        return result


def collect(inputs: list[str]) -> tuple[list[Path], list[dict]]:
    files, failures = set(), []
    for raw in inputs:
        path = Path(raw).expanduser().absolute()
        try:
            if path.is_dir():
                selected = sorted(p for p in path.iterdir() if p.suffix.lower() == ".svg")
                if not selected:
                    raise ValueError("input folder contains no immediate SVG files")
                files.update(selected)
            elif path.suffix.lower() == ".svg":
                files.add(path)  # missing files receive a failed row, never skip
            else:
                raise ValueError("input must be an SVG file or a flat SVG folder")
        except (OSError, ValueError) as error:
            result = _result(path)
            _issue(result, "input-error", str(error))
            failures.append(result)
    return sorted(files), failures


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("inputs", nargs="+", metavar="SVG_OR_FOLDER")
    metadata = parser.add_mutually_exclusive_group()
    metadata.add_argument("--editable", type=Path, help="explicit expected JSON for exactly one SVG")
    metadata.add_argument("--expected-editable-dir", type=Path, help="matching editable JSON folder (required unless --editable)")
    parser.add_argument("--icon-type", help="assert expected configured profile; must match metadata")
    parser.add_argument("--output-dir", type=Path, help="write fresh QA and canvas-keyshape-results.json")
    parser.add_argument("--json", action="store_true", help="machine-readable aggregate")
    parser.add_argument("--quiet", "-q", action="store_true", help="suppress human output")
    args = parser.parse_args(argv)
    files, rows = collect(args.inputs)
    if args.editable is not None and (len(files) != 1 or len(args.inputs) != 1 or Path(args.inputs[0]).expanduser().is_dir()):
        parser.error("--editable requires exactly one explicit SVG; use --expected-editable-dir for a folder or batch")
    protected = list(files)
    for path in files:
        editable = args.editable
        if args.expected_editable_dir is not None:
            stem = path.stem.removesuffix("-design")
            editable = args.expected_editable_dir / f"{stem}.json"
        if editable is not None:
            protected.append(editable)
        rows.append(check_file(path, editable=editable, icon_type=args.icon_type,
                               output_dir=args.output_dir))
    aggregate = {"ok": bool(rows) and all(row["ok"] is True for row in rows),
                 "checked": len(rows), "failed": sum(row["ok"] is not True for row in rows),
                 "rows": rows, "repair": REPAIR}
    if args.output_dir is not None:
        try:
            directory = args.output_dir.expanduser().absolute()
            if directory.is_symlink():
                raise ValueError("QA output directory cannot be a symlink")
            directory.mkdir(parents=True, exist_ok=True)
            from icon_profiles import PROFILE_SOURCE
            _write_json(directory / "canvas-keyshape-results.json", aggregate,
                        [*protected, PROFILE_SOURCE])
        except Exception as error:
            aggregate["ok"] = False
            aggregate["reportError"] = f"{type(error).__name__}: {error}"
    if args.json:
        print(json.dumps(aggregate, indent=2, ensure_ascii=False, allow_nan=False))
    elif not args.quiet:
        for row in rows:
            label = "PASS" if row["ok"] else "FAIL"
            print(f"{label} {row['file']}: " + (f"{row['iconType']} / {row['keyshape']['name']}" if row["ok"] else "; ".join(row["errors"])))
        print(f"{aggregate['checked'] - aggregate['failed']}/{aggregate['checked']} passed this gate; not visual acceptance.")
        if not aggregate["ok"]:
            print(aggregate.get("reportError", REPAIR))
    return 0 if aggregate["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
