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
        if destination.name != f"{sid}_rework.svg" or destination.parent.name != sid:
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
    destination = generated_path(pack, row["destination"], rows)
    ship = generated_path(pack, row["ship"], rows)
    source = scoped_path(pack, str(row["editable"].relative_to(pack)))
    if hashlib.sha256(source.read_bytes()).hexdigest() != row["sourceSha256"]:
        raise ValueError("editable source changed after validation; rebuild and review")
    if hashlib.sha256(ship.read_bytes()).hexdigest() != row["shipSha256"]:
        raise ValueError("emitted geometry changed after validation; rebuild and review")
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
        os.replace(staged, destination)
    finally:
        if staged is not None and staged.exists():
            staged.unlink()


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


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
        if path and Path(path).is_file():
            png = cairosvg.svg2png(url=str(path), output_width=72, output_height=72)
            icon = Image.open(io.BytesIO(png)).convert("RGBA")
            sheet.paste(icon, (x + 74, y + 20), icon)
            size = row.get("shipSize", 24)
            tiny = Image.open(io.BytesIO(cairosvg.svg2png(url=str(path), output_width=size, output_height=size))).convert("RGBA")
            sheet.paste(tiny, (x + (cell_w - size) // 2, y + 102), tiny)
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


def build(pack: Path, rows: list[dict], skip_qa: bool = False) -> int:
    from icon_geometry import resolve_icon, svg
    from icon_profiles import validate_document_profile
    import check_keyfit
    import check_svg_grid
    import qa_overlays
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
    for gate in ("structural", "grid", "keyshape", "holes", "overlap"):
        (qa / gate).mkdir(parents=True, exist_ok=True)
    all_grid, all_keyshape, all_holes = [], [], []
    for row in rows:
        source, doc = sources[row["sid"]]
        row["editable"] = source
        row["references"] = (doc.get("sourceAnalysis") or {}).get("lucideReferences", [])
        row["failures"] = reference_evidence(doc)
        row["status"] = "draft" if skip_qa else "fail"
        try:
            icon_type, profile = validate_document_profile(doc)
            row["iconType"], row["shipSize"] = icon_type, profile["shipCanvas"]
            paths = resolve_icon(doc)
            design = generated_path(pack, output / f"{doc['name']}-design.svg", rows)
            ship = generated_path(pack, output / f"{doc['name']}.svg", rows)
            row["design"], row["ship"] = design, ship
            design.write_text(svg(paths, profile["designCanvas"], profile["designStroke"]))
            ship.write_text(svg(paths, profile["shipCanvas"], profile["shipStroke"], profile["shipCanvas"] / profile["designCanvas"]))
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
            # A documented geometric exception is hash-locked to this exact SVG.
            exceptions_path = pack / "grid-exceptions.json"
            if exceptions_path.is_file():
                grid = check_svg_grid.apply_exceptions(grid, design, json.loads(exceptions_path.read_text()).get("files", {}))
            keyshape = check_keyfit.process(ship, qa / "keyshape", 32, 2 / 32,
                                           doc["keyfitCheck"]["targetToken"], icon_type, doc["keyfitCheck"])
            holes = qa_overlays.process(ship, qa / "holes", 32, 1, 1, icon_type)
            grid["keyfit"] = keyshape
            grid["overallStatus"] = "pass" if grid["status"] == keyshape["status"] == "pass" else "fail"
            all_grid.append(grid)
            all_keyshape.append(keyshape)
            all_holes.append(holes)
            for gate, report in (("grid", grid), ("keyshape", keyshape), ("holes", holes)):
                if report["status"] != "pass":
                    row["failures"].append(f"{gate}: {report.get('reason') or report.get('issues') or report['status']}")
            if (doc.get("sourceAnalysis") or {}).get("spacingChecks"):
                overlap = subprocess.run([sys.executable, "-B", str(ROOT / "core" / "render_overlap_audit.py"),
                                          str(source), str(qa / "overlap" / f"{doc['name']}.svg")], capture_output=True, text=True, cwd=ROOT)
                if overlap.returncode:
                    row["failures"].append("overlap: " + overlap.stdout + overlap.stderr)
            review = (doc.get("sourceAnalysis") or {}).get("visualReview") or {}
            if review.get("status") != "pass" or not review.get("notes") or review.get("shipSize") != profile["shipCanvas"]:
                row["failures"].append("requires recorded true-size visual review (status, shipSize, notes)")
            if review.get("geometrySha256") != row["shipSha256"]:
                row["failures"].append("visual review is missing or stale for the emitted geometry")
            if icon_type == "container":
                row["failures"].append("container delivery requires separate filled-preview evidence; use the container workflow")
            row["status"] = "pass" if not row["failures"] else "fail"
        except Exception as error:
            row["failures"].append(str(error))
        print(f"{row['sid']}: {row['status'].upper()}" + (" — " + "; ".join(row["failures"])[:220] if row["failures"] else ""), flush=True)
    if not skip_qa:
        check_svg_grid.write_report(all_grid, qa / "grid")
        check_keyfit.write_aggregate(all_keyshape, qa / "keyshape")
        qa_overlays.write_aggregate(all_holes, qa / "holes", 1, 1)
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
        new = f'<img src="{link(ship)}" width="88" height="88" alt="{html.escape(row["name"])}">' if ship else "Not emitted"
        size = row.get("shipSize", 24)
        tiny = f'<img src="{link(ship)}" width="{size}" height="{size}" alt="Actual size">' if ship else ""
        references = row.get("references", [])
        if not isinstance(references, list):
            references = []
        refs = " · ".join(f'<a href="{link(ROOT / "references/lucide/original" / (ref["name"] + ".svg"))}">{html.escape(ref["name"])}</a> <a href="{link(ROOT / "references/lucide/atomic-debug" / (ref["name"] + ".svg"))}">(atoms)</a>'
                          for ref in references if isinstance(ref, dict) and isinstance(ref.get("name"), str) and ICON_NAME.fullmatch(ref["name"]))
        downloads = f'<a href="{link(row["editable"])}">Editable JSON</a> · <a href="{link(ship)}">SVG</a>' if ship else ""
        failures = html.escape("; ".join(row.get("failures", [])))
        qa_details = ("Diagnostic draft only: automated QA and visual-review verification were skipped. Nothing delivered."
                      if draft else failures or "All required automated checks and recorded visual review passed.")
        cards.append(f'<article><div class="title"><h2>{html.escape(row["name"])}</h2><span class="{row.get("status", "draft")}">{row.get("status", "draft")}</span></div><p class="id">{row["sid"]} · {row.get("iconType", "normal")}</p><div class="pair"><figure><img src="{link(row["prototype"])}" width="88" height="88" alt="Prototype"><figcaption>Prototype</figcaption></figure><figure>{new}<figcaption>Rework</figcaption></figure></div><div class="actual">{tiny}<span>{size}px actual size</span></div><p>{html.escape(row["brief"])}</p><p class="links">{downloads}</p><p class="refs">References: {refs}</p><details><summary>QA details</summary><p>{qa_details}</p></details></article>')
    passed = sum(row.get("status") == "pass" for row in rows)
    label = "Diagnostic drafts — not delivered" if draft else f"{passed} of {len(rows)} passed and delivered locally"
    qa_links = "" if draft else (f' · <a href="{link(qa / "grid/grid-report.html")}">Grid</a>'
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
