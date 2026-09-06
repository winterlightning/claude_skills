#!/usr/bin/env python3
"""Inspect, prepare, and verify local manifest-based symbol rework packs.

This tool does not choose a design, author geometry, or upload anything. Authors
write schema-v2 sources in PACK/editable with sourceAnalysis.symbolId. Build
emits those sources, runs the existing QA gates, and delivers only passing,
visually reviewed outputs to the manifest's exact local rework destinations.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import html
import io
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
SID = re.compile(r"sym_[0-9]+\Z")
ICON_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
DELIVERY_LABEL = re.compile(r"[a-z0-9]+(?:[-_][a-z0-9]+)*\Z")


def scoped_path(pack: Path, value: str) -> Path:
    """Manifest paths are local paths, never shell commands or remote URLs."""
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError("manifest path must be a nonempty relative path")
    candidate = pack / value
    if candidate.is_symlink() or pack.resolve() not in candidate.resolve().parents:
        raise ValueError(f"manifest path escapes its pack: {value}")
    for parent in candidate.parents:
        if parent == pack:
            break
        if parent.is_symlink():
            raise ValueError(f"manifest path crosses a symlink: {value}")
    return candidate


def load_pack(pack: Path) -> list[dict]:
    pack = pack.resolve()
    manifest = json.loads((pack / "manifest.json").read_text())
    symbols = manifest.get("symbols")
    if not isinstance(symbols, list) or not symbols:
        raise ValueError("manifest must contain a nonempty symbols list")
    # Rework packs deliver `<sid>_rework.svg`; generation packs name their
    # delivery after the manifest's upload label (for example `_generated`).
    label = (manifest.get("api") or {}).get("label")
    suffixes = {"rework"} | ({label} if isinstance(label, str) and DELIVERY_LABEL.fullmatch(label) else set())
    seen = set()
    rows = []
    for symbol in symbols:
        sid = symbol.get("sid", "")
        if not SID.fullmatch(sid) or sid in seen:
            raise ValueError(f"invalid or duplicate symbol ID: {sid!r}")
        seen.add(sid)
        source = scoped_path(pack, (symbol.get("files") or {}).get("prototype"))
        destination = scoped_path(pack, symbol.get("upload"))
        if source.suffix != ".svg" or not source.is_file():
            raise ValueError(f"missing SVG prototype for {sid}")
        if destination.name not in {f"{sid}_{suffix}.svg" for suffix in suffixes} or destination.parent.name != sid:
            raise ValueError(f"unexpected rework destination for {sid}: {destination}")
        if destination == source:
            raise ValueError("rework must never overwrite its prototype")
        rows.append({"sid": sid, "name": symbol.get("name") or sid,
                     "brief": symbol.get("minimal_description") or symbol.get("description") or symbol.get("name") or "",
                     "context": symbol.get("icons", []), "wrong": bool(symbol.get("wrong")),
                     "prototype": source, "destination": destination})
    prototypes = {row["prototype"].resolve() for row in rows}
    if any(row["destination"].resolve() in prototypes for row in rows):
        raise ValueError("rework must never overwrite any pack prototype")
    return rows


def generated_path(pack: Path, path: Path, rows: list[dict]) -> Path:
    """Check every generated file, not just its parent output directory."""
    checked = scoped_path(pack, str(path.relative_to(pack)))
    if checked.exists() and not checked.is_file():
        raise ValueError(f"generated file target is not a regular file: {path}")
    if any(checked.resolve() == row["prototype"].resolve()
           or (checked.exists() and checked.samefile(row["prototype"])) for row in rows):
        raise ValueError(f"generated output must never overwrite a prototype: {path}")
    return checked


def publish_file(pack: Path, row: dict, rows: list[dict], qa: Path) -> None:
    """Stage beside the exact destination; leave old output intact on failure."""
    from icon_profiles import get_profile

    destination = generated_path(pack, row["destination"], rows)
    ship = generated_path(pack, row["ship"], rows)
    source = scoped_path(pack, str(row["editable"].relative_to(pack)))
    if hashlib.sha256(source.read_bytes()).hexdigest() != row["sourceSha256"]:
        raise ValueError("editable source changed after validation; rebuild and review")
    if hashlib.sha256(ship.read_bytes()).hexdigest() != row["shipSha256"]:
        raise ValueError("emitted geometry changed after validation; rebuild and review")

    def verify_gate_evidence() -> None:
        if row.get("profileConfigurationSha256") != profile_configuration_sha256():
            raise ValueError("profile configuration changed after validation; rebuild all gates")
        spacing_path = row.get("spacingReport")
        if not isinstance(spacing_path, str):
            raise ValueError("spacing evidence is incomplete at delivery")
        spacing = json.loads(generated_path(pack, Path(spacing_path), rows).read_text())
        verify_spacing_evidence(spacing, ship, get_profile(row["iconType"]), qa / "spacing")
        hole_path = row.get("holeReport")
        if not isinstance(hole_path, str):
            raise ValueError("holes evidence is incomplete at delivery")
        holes = json.loads(generated_path(pack, Path(hole_path), rows).read_text())
        verify_hole_evidence(holes, ship, get_profile(row["iconType"]), qa / "holes")
        evidence = row.get("canvasKeyshapeReports")
        emitted_files = (ship, generated_path(pack, row["design"], rows))
        if any(hashlib.sha256(path.read_bytes()).hexdigest() != row["shipSha256"] for path in emitted_files):
            raise ValueError("canvas/keyshape svgSha256 is stale or aliases lost canonical parity")
        if not isinstance(evidence, dict) or set(evidence) != {path.name for path in emitted_files}:
            raise ValueError("canvas/keyshape evidence is incomplete at delivery")
        for emitted in emitted_files:
            report_path = generated_path(pack, Path(evidence[emitted.name]), rows)
            report = json.loads(report_path.read_text())
            failure = canvas_keyshape_failure(report)
            if failure:
                raise ValueError("canvas/keyshape evidence is no longer passing: " + failure)
            verify_canvas_keyshape_evidence(report, emitted, source, get_profile(row["iconType"]),
                                            qa / "canvas-keyshape")

    verify_gate_evidence()
    if destination.is_file() and destination.read_bytes() != ship.read_bytes():
        previous = generated_path(pack, qa / "previous-delivery" / destination.name, rows)
        previous.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(destination, previous)
    destination.parent.mkdir(parents=True, exist_ok=True)
    staged = None
    try:
        with tempfile.NamedTemporaryFile(mode="wb", prefix=".rework-delivery-", suffix=".svg", dir=destination.parent, delete=False) as output:
            staged = Path(output.name)
            with ship.open("rb") as emitted:
                shutil.copyfileobj(emitted, output)
            output.flush()
            os.fsync(output.fileno())
        # Check again immediately before replacing a destination that may have
        # changed since the initial manifest read.
        generated_path(pack, destination, rows)
        if hashlib.sha256(staged.read_bytes()).hexdigest() != row["shipSha256"]:
            raise ValueError("staged geometry differs from the visually reviewed output")
        if hashlib.sha256(source.read_bytes()).hexdigest() != row["sourceSha256"]:
            raise ValueError("editable source changed during delivery; rebuild and review")
        verify_gate_evidence()
        os.replace(staged, destination)
    finally:
        if staged is not None and staged.exists():
            staged.unlink()


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def profile_configuration_sha256() -> str:
    """Detect configuration edits even while imported profiles remain cached."""
    return hashlib.sha256((ROOT / "core/icon_profiles.json").read_bytes()).hexdigest()


def native_review_size(row: dict) -> int:
    """Review at the profile canvas, never at a historical half-size hint."""
    from icon_profiles import get_profile
    return int(get_profile(row.get("iconType"))["designCanvas"])


def render_sheet(rows: list[dict], output: Path, sources: bool = False) -> None:
    import cairosvg
    from PIL import Image, ImageDraw, ImageFont
    cols, cell_w, cell_h = 5, 220, 188
    sheet = Image.new("RGB", (cols * cell_w, math.ceil(len(rows) / cols) * cell_h), "#fafaf9")
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 13)
        small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 11)
    except OSError:
        font = small = ImageFont.load_default()
    for i, row in enumerate(rows):
        x, y = (i % cols) * cell_w, (i // cols) * cell_h
        draw.rounded_rectangle((x + 7, y + 7, x + cell_w - 7, y + cell_h - 7), radius=10, fill="white", outline="#e5e5e0")
        path = row["prototype"] if sources else row.get("ship")
        size = native_review_size(row)
        if path and Path(path).is_file():
            png = cairosvg.svg2png(url=str(path), output_width=size, output_height=size)
            icon = Image.open(io.BytesIO(png)).convert("RGBA")
            sheet.paste(icon, (x + (cell_w - size) // 2, y + 14 + (96 - size) // 2), icon)
        size_label = "source comparison" if sources else "native output"
        draw.text((x + 17, y + 112), f"{size}×{size}px · {size_label}", font=small, fill="#59645f")
        draw.text((x + 17, y + 139), row["name"][:29], font=font, fill="#17211e")
        draw.text((x + 17, y + 158), row["sid"] + (" · prototype" if sources else " · " + row.get("status", "draft")), font=small, fill="#59645f")
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)


def prepare(pack: Path, rows: list[dict]) -> None:
    from detect_svg_shapes import analyze_svg, render_detection_plot
    detection = scoped_path(pack, "detection")
    contact = generated_path(pack, pack / "prototype-contact-sheet.png", rows)
    for row in rows:
        generated_path(pack, detection / f"{row['sid']}-shapes.json", rows)
        generated_path(pack, detection / f"{row['sid']}-preflight.png", rows)
    detection.mkdir(parents=True, exist_ok=True)
    for row in rows:
        source = row["prototype"].read_text()
        report = analyze_svg(source, row["prototype"].name)
        save_json(detection / f"{row['sid']}-shapes.json", report)
        render_detection_plot(source, report, detection / f"{row['sid']}-preflight.png")
        print(f"{row['sid']}: source analyzed", flush=True)
    render_sheet(rows, contact, sources=True)


def authored_sources(pack: Path, rows: list[dict]) -> dict[str, tuple[Path, dict]]:
    expected = {row["sid"] for row in rows}
    sources = {}
    names = set()
    editable = scoped_path(pack, "editable")
    for path in sorted(editable.glob("*.json")):
        if path.is_symlink():
            raise ValueError(f"editable source cannot be a symlink: {path}")
        doc = json.loads(path.read_text())
        sid = (doc.get("sourceAnalysis") or {}).get("symbolId")
        if sid not in expected:
            raise ValueError(f"editable source is not mapped to a pack symbol: {path}")
        if sid in sources:
            raise ValueError(f"multiple editable sources for {sid}")
        if doc.get("schemaVersion") != 2 or "elements" not in doc or "instances" in doc:
            raise ValueError(f"new reworks require schema-v2 elements: {path}")
        name = doc.get("name", "")
        if not ICON_NAME.fullmatch(name) or name in names or path.stem != name:
            raise ValueError(f"editable filename/name must be a unique kebab-case name: {path}")
        names.add(name)
        sources[sid] = (path, doc)
    missing = expected - set(sources)
    if missing:
        raise ValueError("missing editable sources: " + ", ".join(sorted(missing)))
    return sources


def reference_evidence(doc: dict) -> list[str]:
    from lucide_reference import reference_paths
    problems = []
    analysis = doc.get("sourceAnalysis") or {}
    refs = analysis.get("lucideReferences")
    if not isinstance(refs, list) or not refs:
        return ["missing Lucide reference/construction evidence"]
    for ref in refs:
        try:
            reference_paths(ref.get("name", ""))
        except (ValueError, AttributeError) as error:
            problems.append(str(error))
            continue
        if not ref.get("reason") or not ref.get("principles"):
            problems.append("each Lucide reference needs a reason and construction principles")
    return problems


def verify_spacing_evidence(report: object, emitted: Path, profile: dict, output_dir: Path) -> None:
    """Require a fresh, persisted passing distance result for this exact SVG."""
    if (not isinstance(report, dict) or report.get("ok") is not True
            or report.get("status") != "pass" or report.get("errors") != []
            or not isinstance(report.get("pairs"), list)
            or any(not isinstance(pair, dict) or pair.get("status") != "pass" for pair in report["pairs"])):
        raise ValueError("spacing result is missing, malformed, failed, or requires review")
    if report.get("file") != emitted.name or report.get("svgSha256") != hashlib.sha256(emitted.read_bytes()).hexdigest():
        raise ValueError("spacing SVG evidence is missing or stale")
    snapshot = json.dumps(profile, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()
    if report.get("profileSha256") != hashlib.sha256(snapshot).hexdigest():
        raise ValueError("spacing profile evidence is missing or stale")
    for field in ("reportPath", "overlayPath"):
        path = report.get(field)
        if (not isinstance(path, str) or not Path(path).is_file() or Path(path).is_symlink()
                or not Path(path).resolve().is_relative_to(output_dir.resolve())):
            raise ValueError(f"spacing {field} artifact is missing or outside this run")
    if json.loads(Path(report["reportPath"]).read_text()) != report:
        raise ValueError("spacing persisted report is inconsistent")


def verify_hole_evidence(report: object, emitted: Path, profile: dict, output_dir: Path) -> None:
    """Require complete, current negative-space metrics and their zone overlay."""
    if (not isinstance(report, dict) or report.get("status") != "pass"
            or report.get("processingErrors", []) != []
            or report.get("nativeSizeIssues") != []
            or not isinstance(report.get("holes"), list)
            or report.get("pinches") != []
            or any(type(report.get(key)) is not int for key in ("hole_count", "failed_hole_count", "pinch_count"))
            or report["hole_count"] != len(report["holes"])
            or report["failed_hole_count"] != 0 or report["pinch_count"] != 0
            or any(not isinstance(hole, dict) or hole.get("status") != "pass" for hole in report["holes"])):
        raise ValueError("holes result is missing, malformed, failed, or contradicts its zone counts")
    if report.get("file") != emitted.name or report.get("svgSha256") != hashlib.sha256(emitted.read_bytes()).hexdigest():
        raise ValueError("holes SVG evidence is missing or stale")
    snapshot = json.dumps(profile, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()
    if report.get("profileSha256") != hashlib.sha256(snapshot).hexdigest():
        raise ValueError("holes profile evidence is missing or stale")
    for field, setting in (("configuredMinimumRadiusDesignUnits", "minimumEnclosedRadius"),
                           ("configuredMinimumFillDepthDesignUnits", "minimumSolidFillDepth")):
        if type(report.get(field)) not in (int, float) or report[field] != profile["validation"][setting]:
            raise ValueError("holes thresholds do not match the selected profile")
    metrics = output_dir / f"{emitted.stem}.metrics.json"
    overlay = output_dir / f"{emitted.stem}_holes.png"
    for path in (metrics, overlay):
        if not path.is_file() or path.is_symlink() or not path.resolve().is_relative_to(output_dir.resolve()):
            raise ValueError("holes metrics or overlay is missing or outside this run")
    if json.loads(metrics.read_text()) != report:
        raise ValueError("holes persisted metrics are inconsistent")


def canvas_keyshape_failure(report: object) -> str | None:
    """A missing, malformed, or errored gate result is never passing evidence."""
    if not isinstance(report, dict):
        return "missing or malformed canvas/keyshape report"
    if (report.get("ok") is True and report.get("status") == "pass"
            and isinstance(report.get("errors"), list) and not report["errors"]
            and isinstance(report.get("keyfit"), dict)
            and report["keyfit"].get("status") == "pass"):
        return None
    errors = report.get("errors")
    if isinstance(errors, list) and errors:
        return "; ".join(str(error) for error in errors)
    return str(report.get("reason") or f"incomplete or unsuccessful canvas/keyshape report (status={report.get('status')!r})")


def verify_canvas_keyshape_evidence(report: dict, emitted: Path, source: Path, profile: dict, output_dir: Path) -> None:
    """Bind a gate's passing verdict and its raster evidence to these inputs."""
    if report.get("file") != emitted.name:
        raise ValueError("canvas/keyshape result does not identify the emitted file")
    for key, path in (("svgSha256", emitted), ("editableSha256", source)):
        if report.get(key) != hashlib.sha256(path.read_bytes()).hexdigest():
            raise ValueError(f"canvas/keyshape {key} evidence is missing or stale")
    snapshot = json.dumps(profile, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    if report.get("profileSha256") != hashlib.sha256(snapshot).hexdigest():
        raise ValueError("canvas/keyshape profile evidence is missing or stale")
    evidence_directory = report.get("evidenceDirectory")
    if (not isinstance(evidence_directory, str) or not Path(evidence_directory).is_dir()
            or not Path(evidence_directory).resolve().is_relative_to(output_dir.resolve())):
        raise ValueError("canvas/keyshape evidence directory is missing or outside this run")
    evidence = Path(evidence_directory) / "canvas-keyshape.json"
    if not evidence.is_file() or evidence.is_symlink() or json.loads(evidence.read_text()) != report:
        raise ValueError("canvas/keyshape persisted report is missing or inconsistent")
    for key in ("keyfitReport", "keyfitOverlay"):
        artifact = report.get(key)
        if (not isinstance(artifact, str) or not Path(artifact).is_file() or Path(artifact).is_symlink()
                or not Path(artifact).resolve().is_relative_to(Path(evidence_directory).resolve())):
            raise ValueError(f"canvas/keyshape {key} artifact is missing")


def build(pack: Path, rows: list[dict], skip_qa: bool = False) -> int:
    from icon_geometry import resolve_icon, svg
    from icon_profiles import validate_document_profile
    import check_keyfit
    import check_svg_grid
    import check_svg_spacing
    import qa_overlays
    import validate_icon_keyshapes
    configuration_sha256 = profile_configuration_sha256()
    sources = authored_sources(pack, rows)
    output = scoped_path(pack, "output")
    qa_root = scoped_path(pack, "qa")
    # Preflight all predictable writes before emitting anything. Existing
    # symlinks and manifest prototypes are not disposable build artifacts.
    for target in (pack / "rework-results.json", pack / "contact-sheet.png", pack / "review.html"):
        generated_path(pack, target, rows)
    for source, doc in sources.values():
        for name in (f"{doc['name']}-design.svg", f"{doc['name']}.svg"):
            generated_path(pack, output / name, rows)
    for row in rows:
        generated_path(pack, row["destination"], rows)
    output.mkdir(parents=True, exist_ok=True)
    # Every run gets new evidence. A failed tool cannot reuse an old passing JSON.
    run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    qa = qa_root / run
    for gate in ("structural", "grid", "spacing", "canvas-keyshape", "keyshape", "holes", "overlap"):
        (qa / gate).mkdir(parents=True, exist_ok=True)
    all_grid, all_keyshape, all_holes = [], [], []
    all_canvas_keyshape = []
    all_spacing = []
    for row in rows:
        source, doc = sources[row["sid"]]
        row["editable"] = source
        row["references"] = (doc.get("sourceAnalysis") or {}).get("lucideReferences", [])
        row["failures"] = reference_evidence(doc)
        row["status"] = "draft" if skip_qa else "fail"
        row["profileConfigurationSha256"] = configuration_sha256
        try:
            icon_type, profile = validate_document_profile(doc)
            row["iconType"], row["shipSize"] = icon_type, profile["designCanvas"]
            paths = resolve_icon(doc)
            design = generated_path(pack, output / f"{doc['name']}-design.svg", rows)
            ship = generated_path(pack, output / f"{doc['name']}.svg", rows)
            row["design"], row["ship"] = design, ship
            # Both retained filenames refer to the same native output, not two
            # production sizes. Keep the alias for existing QA/wrapper callers.
            native_svg = svg(paths, profile["designCanvas"], profile["designStroke"])
            design.write_text(native_svg)
            ship.write_text(native_svg)
            row["sourceSha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
            row["shipSha256"] = hashlib.sha256(ship.read_bytes()).hexdigest()
            if skip_qa:
                print(f"{row['sid']}: DRAFT emitted, delivery untouched", flush=True)
                continue
            command = [sys.executable, "-B", str(ROOT / "core" / "validate_icon.py"), str(source), "--dir", str(output)]
            result = subprocess.run(command, capture_output=True, text=True, cwd=ROOT)
            (qa / "structural" / f"{doc['name']}.log").write_text(result.stdout + result.stderr)
            if result.returncode:
                row["failures"].append("structural: " + (result.stdout + result.stderr).strip())
            grid = check_svg_grid.inspect(design, "design", icon_type)
            exceptions_path = pack / "grid-exceptions.json"
            if exceptions_path.is_file():
                grid = check_svg_grid.apply_exceptions(grid, design, json.loads(exceptions_path.read_text()).get("files", {}))
            if (doc.get("sourceAnalysis") or {}).get("spacingChecks"):
                overlap = subprocess.run([sys.executable, "-B", str(ROOT / "core" / "render_overlap_audit.py"),
                                          str(source), str(qa / "overlap" / f"{doc['name']}.svg")], capture_output=True, text=True, cwd=ROOT)
                if overlap.returncode:
                    row["failures"].append("overlap: " + overlap.stdout + overlap.stderr)
            # Ordered acceptance gates: distance, negative-space zones, keyshape.
            # Continue collecting diagnostics, but no non-pass can be delivered.
            spacing = None
            try:
                spacing = check_svg_spacing.check_file(ship, icon_type=icon_type, output_dir=qa / "spacing")
                verify_spacing_evidence(spacing, ship, profile, qa / "spacing")
                row["spacingReport"] = spacing["reportPath"]
            except Exception as error:
                row["failures"].append("spacing: " + str(error))
                if not isinstance(spacing, dict):
                    spacing = {"file": ship.name, "ok": False, "status": "error", "errors": [str(error)]}
                elif spacing.get("ok") is True:
                    spacing = {**spacing, "ok": False, "status": "error", "errors": [str(error)]}
            all_spacing.append(spacing)
            holes = qa_overlays.process(ship, qa / "holes", 32, None, None, icon_type)
            try:
                verify_hole_evidence(holes, ship, profile, qa / "holes")
                row["holeReport"] = str(qa / "holes" / f"{ship.stem}.metrics.json")
            except (OSError, ValueError, TypeError) as error:
                row["failures"].append("holes: " + str(error))
                if (not isinstance(holes, dict) or not isinstance(holes.get("holes"), list)
                        or not isinstance(holes.get("pinches"), list)
                        or any(type(holes.get(key)) is not int for key in ("hole_count", "failed_hole_count", "pinch_count"))):
                    holes = {"file": ship.name, "source": str(ship), "iconType": icon_type,
                             "status": "fail", "holes": [], "pinches": [], "nativeSizeIssues": [],
                             "hole_count": 0, "failed_hole_count": 0, "pinch_count": 0,
                             "processingErrors": [str(error)]}
                elif holes.get("status") == "pass":
                    holes = {**holes, "status": "fail", "processingErrors": [str(error)]}
            # Both filenames are native-size deliverables. Checking only the
            # canonical SVG leaves the upload alias outside the mandatory gate.
            keyshape = None
            row["canvasKeyshapeReports"] = {}
            for emitted in (ship, design):
                try:
                    canvas_keyshape = validate_icon_keyshapes.check_file(
                        emitted, editable=source, icon_type=icon_type,
                        output_dir=qa / "canvas-keyshape")
                    failure = canvas_keyshape_failure(canvas_keyshape)
                    if failure is None:
                        verify_canvas_keyshape_evidence(canvas_keyshape, emitted, source, profile, qa / "canvas-keyshape")
                        row["canvasKeyshapeReports"][emitted.name] = str(Path(canvas_keyshape["evidenceDirectory"]) / "canvas-keyshape.json")
                    if emitted == ship and isinstance(canvas_keyshape, dict):
                        keyshape = canvas_keyshape.get("keyfit")
                        # Keep the existing HTML/CSV painted-bounds report and
                        # its sibling links without running a third raster pass.
                        if isinstance(keyshape, dict):
                            for field, name in (("keyfitReport", f"{ship.stem}.keyfit.json"),
                                                ("keyfitOverlay", f"{ship.stem}_keyfit.png")):
                                artifact = canvas_keyshape.get(field)
                                if not isinstance(artifact, str) or not Path(artifact).is_file():
                                    raise ValueError(f"canvas/keyshape {field} artifact is missing")
                                shutil.copy2(artifact, qa / "keyshape" / name)
                except Exception as error:
                    canvas_keyshape = {"file": emitted.name, "ok": False,
                                       "status": "fail", "errors": [str(error)],
                                       "issues": [{"code": "gate-error", "detail": str(error)}]}
                failure = canvas_keyshape_failure(canvas_keyshape)
                if not isinstance(canvas_keyshape, dict):
                    canvas_keyshape = {"file": emitted.name, "ok": False, "status": "fail",
                                       "errors": [failure], "issues": []}
                all_canvas_keyshape.append(canvas_keyshape)
                if failure:
                    row["failures"].append(f"canvas/keyshape ({emitted.name}): {failure}")
            if not isinstance(keyshape, dict):
                keyshape = {"file": ship.name, "source": str(ship), "iconType": icon_type,
                            "status": "fail", "reason": "missing-canvas-keyshape-raster-evidence"}
            grid["keyfit"] = keyshape
            grid["overallStatus"] = "pass" if grid["status"] == keyshape["status"] == "pass" else "fail"
            all_grid.append(grid)
            all_keyshape.append(keyshape)
            all_holes.append(holes)
            for gate, report in (("grid", grid), ("keyshape", keyshape), ("holes", holes)):
                if report["status"] != "pass":
                    row["failures"].append(f"{gate}: {report.get('reason') or report.get('issues') or report['status']}")
            review = (doc.get("sourceAnalysis") or {}).get("visualReview") or {}
            if review.get("status") != "pass" or not review.get("notes") or review.get("shipSize") != profile["designCanvas"]:
                size = profile["designCanvas"]
                row["failures"].append(f"requires recorded native-size visual review at {size}×{size}px (status, shipSize, notes)")
            if review.get("geometrySha256") != row["shipSha256"]:
                row["failures"].append("visual review is missing or stale for the emitted geometry")
            if profile.get("containerSlot"):
                row["failures"].append("container delivery requires separate filled-preview evidence; use the container workflow")
            if profile_configuration_sha256() != configuration_sha256:
                row["failures"].append("profile configuration changed during validation; rebuild all gates")
            row["status"] = "pass" if not row["failures"] else "fail"
        except Exception as error:
            row["failures"].append(str(error))
        print(f"{row['sid']}: {row['status'].upper()}" + (" — " + "; ".join(row["failures"])[:220] if row["failures"] else ""), flush=True)
    if not skip_qa:
        spacing_failed = sum(report.get("ok") is not True or report.get("status") != "pass" for report in all_spacing)
        save_json(qa / "spacing" / "spacing-results.json", {
            "checked": len(all_spacing), "failed": spacing_failed,
            "ok": len(all_spacing) == len(rows) and spacing_failed == 0, "rows": all_spacing,
        })
        canvas_failed = sum(canvas_keyshape_failure(report) is not None for report in all_canvas_keyshape)
        save_json(qa / "canvas-keyshape" / "canvas-keyshape-results.json", {
            "checked": len(all_canvas_keyshape), "failed": canvas_failed,
            "ok": len(all_canvas_keyshape) == 2 * len(rows) and canvas_failed == 0,
            "rows": all_canvas_keyshape,
        })
        check_svg_grid.write_report(all_grid, qa / "grid")
        check_keyfit.write_aggregate(all_keyshape, qa / "keyshape")
        qa_overlays.write_aggregate(all_holes, qa / "holes", None, None)
    # Publish only after all required checks for that icon, with old output backed up.
    for row in rows:
        row["delivered"] = False
        if skip_qa or row["status"] != "pass":
            continue
        try:
            publish_file(pack, row, rows, qa)
            row["delivered"] = True
        except (OSError, ValueError) as error:
            row["status"] = "fail"
            row["failures"].append("delivery: " + str(error))
            print(f"{row['sid']}: FAIL — delivery: {error}", flush=True)
    results = {"run": run, "qaDirectory": str(qa), "diagnosticOnly": skip_qa, "uploaded": False,
               "symbols": [{k: str(v) if isinstance(v, Path) else v for k, v in row.items()} for row in rows]}
    save_json(qa / "results.json", results)
    save_json(generated_path(pack, pack / "rework-results.json", rows), results)
    render_sheet(rows, generated_path(pack, pack / "contact-sheet.png", rows))
    write_gallery(pack, rows, qa, skip_qa)
    return 0 if not skip_qa and all(row["status"] == "pass" for row in rows) else 1


def write_gallery(pack: Path, rows: list[dict], qa: Path, draft: bool) -> None:
    def link(path):
        return quote(os.path.relpath(path, pack).replace(os.sep, "/"), safe="/")
    cards = []
    for row in rows:
        ship = row.get("ship")
        size = native_review_size(row)
        new = f'<img src="{link(ship)}" width="{size}" height="{size}" alt="{html.escape(row["name"])}">' if ship else "Not emitted"
        references = row.get("references", [])
        if not isinstance(references, list):
            references = []
        refs = " · ".join(f'<a href="{link(ROOT / "references/lucide/original" / (ref["name"] + ".svg"))}">{html.escape(ref["name"])}</a> <a href="{link(ROOT / "references/lucide/atomic-debug" / (ref["name"] + ".svg"))}">(atoms)</a>'
                          for ref in references if isinstance(ref, dict) and isinstance(ref.get("name"), str) and ICON_NAME.fullmatch(ref["name"]))
        downloads = f'<a href="{link(row["editable"])}">Editable JSON</a> · <a href="{link(ship)}">SVG</a>' if ship else ""
        failures = html.escape("; ".join(row.get("failures", [])))
        qa_details = ("Diagnostic draft only: automated QA and visual-review verification were skipped. Nothing delivered."
                      if draft else failures or "All required automated checks and recorded visual review passed.")
        cards.append(f'<article><div class="title"><h2>{html.escape(row["name"])}</h2><span class="{row.get("status", "draft")}">{row.get("status", "draft")}</span></div><p class="id">{row["sid"]} · {row.get("iconType", "normal")}</p><div class="pair"><figure><img src="{link(row["prototype"])}" width="{size}" height="{size}" alt="Prototype"><figcaption>Prototype comparison</figcaption></figure><figure>{new}<figcaption>Native rework</figcaption></figure></div><div class="actual"><span>{size}×{size}px native size · 1:1</span></div><p>{html.escape(row["brief"])}</p><p class="links">{downloads}</p><p class="refs">References: {refs}</p><details><summary>QA details</summary><p>{qa_details}</p></details></article>')
    passed = sum(row.get("status") == "pass" for row in rows)
    label = "Diagnostic drafts — not delivered" if draft else f"{passed} of {len(rows)} passed and delivered locally"
    qa_links = "" if draft else (f' · <a href="{link(qa / "spacing/spacing-results.json")}">Distance gate</a>'
                                  f' · <a href="{link(qa / "canvas-keyshape/canvas-keyshape-results.json")}">Canvas + keyshape gate</a>'
                                  f' · <a href="{link(qa / "grid/grid-report.html")}">Grid</a>'
                                  f' · <a href="{link(qa / "keyshape/keyfit-report.html")}">Painted bounds</a>'
                                  f' · <a href="{link(qa / "holes/hole-radius-report.html")}">Negative space</a>')
    document = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lucide-guided rework review</title><style>
    *{{box-sizing:border-box}}body{{margin:0;background:#f4f5f2;color:#1e3027;font:14px system-ui,sans-serif}}header,main{{max-width:1320px;margin:auto;padding:32px}}header{{padding-bottom:12px}}h1{{font-size:32px;letter-spacing:-1px;margin:8px 0}}.eyebrow{{text-transform:uppercase;letter-spacing:2px;color:#6a7c70;font-size:11px}}.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px}}article{{background:white;border:1px solid #dfe5dc;border-radius:14px;padding:20px}}h2{{font-size:16px;margin:0}}.title{{display:flex;justify-content:space-between;gap:8px}}.title span{{font-size:10px;text-transform:uppercase;border-radius:12px;padding:3px 8px;white-space:nowrap}}.pass{{background:#e7f4e7;color:#22652f}}.fail{{background:#ffebe5;color:#b3401b}}.draft{{background:#fff5da;color:#8e6524}}.id,.refs,figcaption{{font-size:11px;color:#748177}}.pair{{display:flex;justify-content:space-around;border-bottom:1px solid #eef1eb;margin:22px 0 12px;padding-bottom:16px}}figure{{margin:0;text-align:center}}figcaption{{margin-top:10px}}.actual{{display:flex;align-items:center;justify-content:center;gap:12px;min-height:35px;font-size:11px;color:#728074}}p{{line-height:1.5}}a{{color:#247248;text-decoration:none}}a:hover{{text-decoration:underline}}details{{font-size:11px;overflow-wrap:anywhere}}summary{{cursor:pointer}}.links{{font-size:12px}}header p{{color:#69796d}}
    </style><header><div class="eyebrow">Unlimited Shapes · construction study</div><h1>Lucide-guided reworks</h1><p>{html.escape(label)}. Sources preserved. Nothing uploaded.</p><p><a href="contact-sheet.png">Contact sheet</a> · <a href="rework-results.json">Results</a>{qa_links}</p></header><main><div class="grid">{"".join(cards)}</div></main></html>'''
    generated_path(pack, pack / "review.html", rows).write_text(document)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("inspect", "prepare", "build"))
    parser.add_argument("pack", type=Path, help="one folder containing manifest.json")
    parser.add_argument("--skip-qa", action="store_true", help="build drafts only; never write manifest rework destinations")
    args = parser.parse_args()
    pack = args.pack.resolve()
    try:
        rows = load_pack(pack)
        if args.command == "inspect":
            for row in rows:
                print(f"{row['sid']} | {row['name']} | {row['brief']}")
            return 0
        if args.command == "prepare":
            prepare(pack, rows)
            return 0
        return build(pack, rows, args.skip_qa)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"rework error: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
