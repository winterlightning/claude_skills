#!/usr/bin/env python3
"""Try profile-aware SVG adaptation, writing new unapproved drafts and QA.

Folder inputs select only immediate *-design.svg files. Source geometry always
comes from those SVGs, never from a companion JSON. Matching JSON may supply
verified keyshape/optical intent and semantic relationships, not old approval.
Exit 0 means the experiment completed, not that its icons are ready to ship.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import html
import io
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import quote

from icon_geometry import finite_number, path_data, primitive_commands, resolve_icon, sample, spacing_pair, svg
from icon_profiles import get_profile, profile_names, source_document, validate_document_profile
from profile_adaptation import adapt_geometry, read_design_svg


CORE = Path(__file__).resolve().parent
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SAMPLES = 32


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")


def select_sources(path: Path) -> list[Path]:
    if path.is_symlink():
        raise ValueError("Select a real SVG file or folder, not a symlink")
    if path.is_dir():
        files = sorted(path.glob("*-design.svg"))
    elif path.is_file() and path.suffix.lower() == ".svg":
        files = [path]
    else:
        raise ValueError("Input must be an SVG file or a folder of *-design.svg files")
    if not files:
        raise ValueError("No *-design.svg files found in the selected folder")
    for item in files:
        if item.is_symlink() or not item.is_file():
            raise ValueError(f"Source is not a regular SVG file: {item}")
        if not NAME.fullmatch(item.stem.removesuffix("-design")):
            raise ValueError(f"Source needs a safe kebab-case filename: {item.name}")
    return files


def prepare_output(path: Path, sources: list[Path], metadata_dir: Path | None) -> Path:
    absolute = path.absolute()
    if any(item.is_symlink() for item in (absolute, *absolute.parents)):
        raise ValueError("Output folder and its parents must not be symlinks")
    if absolute.exists():
        raise ValueError("Use a new output folder; adaptation never overwrites an existing trial")
    # Do not put generated artifacts in the selected source or metadata folder.
    for protected in {item.parent.resolve() for item in sources} | ({metadata_dir.resolve()} if metadata_dir else set()):
        if absolute.resolve().is_relative_to(protected):
            raise ValueError("Output must be separate from source SVG and metadata folders")
    absolute.mkdir(parents=True)
    return absolute


def token_named(profile: dict, name: str) -> dict:
    matches = [token for token in profile["keyshapes"] if token["name"] == name]
    if len(matches) != 1:
        raise ValueError(f"Unknown profile keyshape: {name!r}")
    return deepcopy(matches[0])


def matching_token(source_token: dict, target_profile: dict, explicit: str | None = None) -> dict:
    if explicit:
        return token_named(target_profile, explicit)
    matches = [token for token in target_profile["keyshapes"]
               if token["shape"] == source_token["shape"] and token["orientation"] == source_token["orientation"]]
    if len(matches) != 1:
        raise ValueError("Target keyshape is missing or ambiguous; supply --target-keyshape")
    return deepcopy(matches[0])


def verified_metadata(path: Path, source: dict, source_type: str) -> dict:
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"Missing regular companion metadata: {path}")
    document = json.loads(path.read_text(encoding="utf-8"))
    icon_type, profile = validate_document_profile(document)
    if icon_type != source_type or document.get("schemaVersion") != 2:
        raise ValueError("Companion metadata must be schema v2 and declare the selected source profile")
    if profile["canvas"] != source["canvas"] or profile["strokeWidth"] != source["strokeWidth"]:
        raise ValueError("Companion metadata canvas/stroke differs from the actual source SVG")
    expected = [path_data(item["commands"]) for item in resolve_icon(document)]
    actual = [path_data(primitive_commands(item["tag"], item["attrs"])) for item in source["elements"]]
    if actual != expected:
        raise ValueError("Companion metadata geometry/order does not match the selected design SVG")
    check = document.get("keyfitCheck")
    if not isinstance(check, dict) or not isinstance(check.get("targetToken"), str):
        raise ValueError("Companion metadata must declare a keyshape")
    if check.get("mode", "exact") not in {"exact", "optical"}:
        raise ValueError("Companion metadata keyfit mode is unsupported")
    if check.get("mode") == "optical" and not str(check.get("rationale", "")).strip():
        raise ValueError("A source optical fit needs its original semantic rationale")
    return document


def geometry_samples(document: dict) -> list[dict]:
    return [{**item, "points": sample(item["commands"])[0]} for item in resolve_icon(document)]


def measured_painted_bounds(document: dict) -> list[float]:
    points = [point for item in geometry_samples(document) for point in item["points"]]
    if not points:
        raise ValueError("Adaptation has no visible geometry")
    radius = document["strokeWidth"] / 2
    return [min(x for x, _ in points) - radius, min(y for _, y in points) - radius,
            max(x for x, _ in points) + radius, max(y for _, y in points) + radius]


def refreshed_relationships(metadata: dict | None, document: dict) -> list[dict]:
    """Retain verified semantic pair labels, never old distances or verdicts."""
    if metadata is None:
        return []
    from validate_icon import minimum_distance
    sampled = geometry_samples(document)
    by_order = {item["order"]: item for item in sampled}
    checks = []
    for previous in (metadata.get("sourceAnalysis") or {}).get("spacingChecks", []):
        left, right = spacing_pair(previous, sampled)
        relation = previous.get("relation")
        if relation not in {"connected", "intentional-overlap", "ordinary-distinct", "visual-opening"}:
            raise ValueError(f"Unrecognized source spacing relation: {relation!r}")
        distance = minimum_distance(by_order[left]["points"], by_order[right]["points"])
        check = {"elements": [by_order[left]["elementId"], by_order[right]["elementId"]],
                 "relation": relation, "centerlineDistance": round(distance, 6),
                 "paintedClearance": round(distance - document["strokeWidth"], 6),
                 "reviewStatus": "pending"}
        if relation == "visual-opening":
            if "minimumCenterline" in previous:
                source_stroke = validate_document_profile(metadata)[1]["strokeWidth"]
                minimum = finite_number(previous["minimumCenterline"], "source minimum centerline") - source_stroke
            else:
                minimum = finite_number(previous.get("minimum", 3), "source minimum visual opening")
            if minimum < 0:
                raise ValueError("A minimum visual opening cannot be negative")
            check.update(minimum=minimum, minimumCenterline=document["strokeWidth"] + minimum)
        checks.append(check)
    return checks


def make_draft(name: str, source: dict, source_profile: dict, target_profile: dict,
               source_type: str, target_type: str, source_token: dict, target_token: dict,
               metadata: dict | None, provenance: dict) -> tuple[dict, dict]:
    source = deepcopy(source)
    # IDs/roles are safe to retain only after SVG-to-metadata parity verification.
    if metadata:
        for element, original in zip(source["elements"], metadata["elements"], strict=True):
            element["id"] = original["id"]
            if "role" in original:
                element["role"] = original["role"]
    result = adapt_geometry(source, source_profile, target_profile, source_token, target_token)
    mode = (metadata or {}).get("keyfitCheck", {}).get("mode", "exact")
    document = {
        "schemaVersion": 2, "name": name, "iconType": target_type,
        "canvas": target_profile["canvas"], "strokeWidth": target_profile["strokeWidth"],
        "cornerStyle": "round", "elements": result["elements"],
        "keyfitCheck": {"targetToken": target_token["name"], "mode": mode},
        "sourceAnalysis": {"sourceOrigin": "profile-adaptation-trial", "incomplete": True,
            "mappings": [{"sourceElements": [index], "elements": [element["id"]],
                          "decision": "adapt-draft", "reason": "Profile fit and grid adjustment; native-size review is pending."}
                         for index, element in enumerate(result["elements"])],
            "relationships": [], "spacingChecks": [],
            "visualReview": {"status": "pending", "shipSize": target_profile["canvas"]}},
        "adaptation": {"status": "draft", "sourceProfile": source_type, "targetProfile": target_type,
            "sourceKeyshape": source_token["name"], "targetKeyshape": target_token["name"],
            "provenance": provenance, "metrics": result["metrics"], "warnings": result["warnings"],
            "pendingReview": ["Native silhouette and curve joins", "Connections and painted clearance",
                              "Optical balance", "All required production QA and source analysis"]},
    }
    if mode == "optical":
        document["keyfitCheck"].update(
            rationale="Draft adaptation retaining the source's sparse/narrow subject: " + metadata["keyfitCheck"]["rationale"]
                      + " Target optical fit still requires independent review.",
            paintedBounds=measured_painted_bounds(document))
    checks = refreshed_relationships(metadata, document)
    document["sourceAnalysis"]["spacingChecks"] = checks
    document["sourceAnalysis"]["relationships"] = [{"elements": item["elements"], "relation": item["relation"],
                                                    "reviewStatus": "pending"} for item in checks]
    return document, result


def authored_ink_diagnostics(path: Path, profile: dict) -> dict:
    """Supplement the standard narrowed-stroke QA without changing its policy."""
    import qa_overlays as holes
    view = (0.0, 0.0, float(profile["canvas"]), float(profile["canvas"]))
    ink = holes.render_ink_mask(path, view[2], view[3], SAMPLES, 0)
    labels, components = holes.enclosed_components(ink)
    measured = holes.measure_holes(labels, components, view, SAMPLES,
        profile["validation"]["minimumEnclosedRadius"], profile["canvas"], profile["canvas"])
    pinches = holes.find_pinches(path, ink, view, SAMPLES,
        profile["validation"]["minimumSolidFillDepth"], 0, profile["canvas"])
    return {"strokeWidth": profile["strokeWidth"], "holeCount": len(measured),
            "holes": measured, "pinches": pinches,
            "status": "fail" if any(item["status"] != "pass" for item in measured) or pinches else "pass",
            "note": "Supplementary authored-stroke raster diagnostic; not a visual approval."}


def run_qa(document: dict, editable: Path, emitted: Path, source_path: Path,
           source_type: str, source_profile: dict, target_type: str, target_profile: dict, output: Path) -> dict:
    import check_keyfit as keyfit
    import check_svg_grid as grid
    import qa_overlays as holes
    for name in ("grid", "keyshape", "holes", "structure", "authored-ink"):
        (output / "qa" / name).mkdir(parents=True, exist_ok=True)
    grid_result = grid.inspect(emitted, "design", target_type)
    write_json(output / "qa/grid" / f"{document['name']}.json", grid_result)
    keyfit_result = keyfit.process(emitted, output / "qa/keyshape", SAMPLES, None,
        document["keyfitCheck"]["targetToken"], target_type, document["keyfitCheck"])
    hole_result = holes.process(emitted, output / "qa/holes", SAMPLES, None, None, target_type)
    structure = subprocess.run([sys.executable, "-B", str(CORE / "validate_icon.py"), str(editable),
                                "--dir", str(emitted.parent)], capture_output=True, text=True)
    structure_text = structure.stdout + structure.stderr
    (output / "qa/structure" / f"{document['name']}.txt").write_text(structure_text, encoding="utf-8")
    structural_issues = [line.strip()[5:] for line in structure_text.splitlines() if line.strip().startswith("FAIL ")]
    geometry_issues = [issue for issue in structural_issues if not issue.startswith("sourceAnalysis is marked incomplete;")]
    if structure.returncode not in (0, 1) or (structure.returncode and not structural_issues):
        raise RuntimeError(f"Structural validator could not check the draft: {structure_text}")
    source_ink = authored_ink_diagnostics(source_path, source_profile)
    target_ink = authored_ink_diagnostics(emitted, target_profile)
    topology_changed = source_ink["holeCount"] != target_ink["holeCount"]
    collapsed_segments = document.get("adaptation", {}).get("metrics", {}).get("collapsedSegments", [])
    write_json(output / "qa/authored-ink" / f"{document['name']}.json",
               {"source": source_ink, "target": target_ink, "holeCountChanged": topology_changed,
                "note": "A changed count is a review signal, not proof that all topology changes are detected."})
    mechanical_pass = (grid_result["status"] == keyfit_result["status"] == hole_result["status"]
                       == target_ink["status"] == "pass" and not geometry_issues and not topology_changed
                       and not collapsed_segments)
    return {"grid": grid_result, "keyshape": keyfit_result, "holes": hole_result,
            "structure": {"status": "blocked-draft", "exitCode": structure.returncode,
                          "issues": structural_issues, "geometryIssues": geometry_issues},
            "authoredInk": {"source": source_ink, "target": target_ink, "holeCountChanged": topology_changed},
            "adaptationStructure": {"status": "review" if collapsed_segments else "pass", "collapsedSegments": collapsed_segments},
            "mechanicalChecksPassed": mechanical_pass, "visualApproval": "pending"}


def write_reviews(rows: list[dict], output: Path, source_profile: dict, target_profile: dict,
                  originals_unchanged: bool = True) -> None:
    import cairosvg
    from PIL import Image, ImageDraw, ImageFont
    cards = []
    native_source, native_target = source_profile["canvas"], target_profile["canvas"]
    columns, cell_w = 4, max(248, native_source + native_target + 96)
    cell_h = max(native_source, native_target) + 126
    sheet = Image.new("RGB", (columns * cell_w, math.ceil(len(rows) / columns) * cell_h), "white")
    drawing, font = ImageDraw.Draw(sheet), ImageFont.load_default()
    for index, row in enumerate(rows):
        name = row["name"]
        x, y = index % columns * cell_w, index // columns * cell_h
        drawing.rectangle((x, y, x + cell_w - 1, y + cell_h - 1), outline="#d9e1e5")
        drawing.text((x + 12, y + 10), name[:32], fill="#253638", font=font)
        if row.get("error"):
            message = "Unable to adapt: " + row["error"]
            drawing.text((x + 12, y + 44), "Unable to adapt - see report", fill="#ae2929", font=font)
            cards.append(f'<article><h2>{html.escape(name)}</h2><p class="issue">{html.escape(message)}</p></article>')
            continue
        qa = row["qa"]
        badge = "Numeric checks passed / DRAFT" if qa["mechanicalChecksPassed"] else "Geometry review needed / DRAFT"
        images = []
        for label, relative, size, offset in (("Source", row["sourceCopy"], native_source, 32),
                                               ("Adapted", row["svg"], native_target, cell_w // 2 + 24)):
            pixels = cairosvg.svg2png(bytestring=(output / relative).read_bytes(), output_width=size, output_height=size)
            icon = Image.open(io.BytesIO(pixels)).convert("RGBA")
            sheet.paste(icon, (x + offset, y + 36 + (max(native_source, native_target) - size) // 2), icon)
            drawing.text((x + offset - 7, y + 44 + max(native_source, native_target)), f"{label} {size}px", fill="#57686b", font=font)
            images.append(f'<figure><div><img src="{quote(relative)}" width="{size}" height="{size}" alt="{html.escape(name)} {label.lower()}"></div><figcaption>{label} {size}×{size}</figcaption></figure>')
        drawing.text((x + 12, y + cell_h - 42), badge, fill="#285e48" if qa["mechanicalChecksPassed"] else "#ae2929", font=font)
        gate_text = f"Grid: {qa['grid']['status']} · keyshape: {qa['keyshape']['status']} · holes: {qa['holes']['status']}"
        drawing.text((x + 12, y + cell_h - 24), gate_text.replace(" · ", " / "), fill="#57686b", font=font)
        details = [*row["warnings"], *qa["structure"]["geometryIssues"]]
        if qa["keyshape"]["status"] != "pass":
            details.append("Keyshape: " + str(qa["keyshape"].get("reason", "failed")))
        if qa["holes"]["status"] != "pass":
            details.append(f"Negative space: {qa['holes']['failed_hole_count']} failing hole(s), {qa['holes']['pinch_count']} pinch(es)")
        if qa["authoredInk"]["holeCountChanged"]:
            details.append(f"Authored-stroke hole count changed: {qa['authoredInk']['source']['holeCount']} → {qa['authoredInk']['target']['holeCount']}")
        if qa["authoredInk"]["target"]["pinches"]:
            details.append(f"Supplementary authored-stroke diagnostic: {len(qa['authoredInk']['target']['pinches'])} pinch(es)")
        entries = "".join(f"<li>{html.escape(item)}</li>" for item in details)
        cards.append(f'<article><h2>{html.escape(name)}</h2><p class="badge">{badge}</p><div class="pair">{"".join(images)}</div>'
                     f'<p>{html.escape(gate_text)}</p><p><code>{html.escape(row["sourceToken"])} → {html.escape(row["targetToken"])}</code></p>'
                     f'<p><a href="{quote(row["svg"])}">Draft SVG</a> · <a href="{quote(row["editable"])}">Editable JSON</a> · '
                     f'<a href="qa/keyshape/{quote(name)}_keyfit.png">Keyshape overlay</a> · <a href="qa/holes/{quote(name)}_holes.png">Hole overlay</a></p>'
                     f'<details><summary>Geometry notes ({len(details)})</summary><ul>{entries}</ul></details></article>')
    sheet.save(output / "comparison.png")
    success = sum(row.get("qa", {}).get("mechanicalChecksPassed", False) for row in rows)
    input_status = ("Originals and profile configuration are unchanged." if originals_unchanged else
                    "Warning: an input or the profile configuration changed during this trial; see changedInputs in the report and rerun.")
    content = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Profile adaptation trial</title><style>
body{{font:14px system-ui,sans-serif;color:#203431;background:#f0f4f1;margin:0}}main{{max-width:1400px;padding:32px;margin:auto}}
h1{{font-size:30px;margin:0 0 12px}}.notice{{padding:16px;background:#fff1d8;border:1px solid #e6bf6d;border-radius:8px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:18px;margin-top:24px}}article{{background:white;border:1px solid #d6dfd8;border-radius:10px;padding:18px}}
h2{{font-size:15px;overflow-wrap:anywhere;margin:0 0 12px}}.pair{{display:flex;justify-content:space-around}}figure{{margin:12px;text-align:center}}
figure div{{height:{max(native_source, native_target) + 20}px;display:flex;align-items:center;justify-content:center}}img{{display:block;max-width:none}}figcaption{{color:#54645e;font-size:12px}}
.badge{{font-size:12px;color:#795000}}.issue{{color:#a22}}a{{color:#19674e}}code{{font-size:12px}}li{{margin:8px 0}}summary{{cursor:pointer}}
</style></head><body><main><h1>{native_source}px → {native_target}px adaptation trial</h1>
<p class="notice">All results are unapproved drafts. {success}/{len(rows)} pass the trial's numeric and topology checks. Native visual review and complete source analysis remain required for every icon. {input_status}</p>
<p>Actual design SVG paths → uniform stroke-aware fit → target grid adjustment → new editable geometry and fresh QA. Preview icons below use their native dimensions, with no 24px review.</p>
<p><a href="summary.json">Full report</a> · <a href="comparison.png">Native-size comparison sheet</a></p><section class="cards">{"".join(cards)}</section></main></body></html>'''
    (output / "review.html").write_text(content, encoding="utf-8")


def run_trial(args: argparse.Namespace) -> dict:
    sources = select_sources(args.input)
    source_profile, target_profile = get_profile(args.from_profile), get_profile(args.to_profile)
    if source_profile.get("containerSlot") or target_profile.get("containerSlot"):
        raise ValueError("This draft adapter does not adapt container slots; use independent container authoring")
    if args.from_profile == args.to_profile:
        raise ValueError("Choose a different target profile")
    if args.source_keyshape:
        token_named(source_profile, args.source_keyshape)
    if args.target_keyshape:
        token_named(target_profile, args.target_keyshape)
    original_hashes = {path.resolve(): sha256(path.read_bytes()) for path in sources}
    config_path = CORE / "icon_profiles.json"
    original_hashes[config_path] = sha256(config_path.read_bytes())
    if args.metadata_dir:
        if args.metadata_dir.is_symlink() or not args.metadata_dir.is_dir():
            raise ValueError("Metadata directory must be a real existing folder")
        for path in sources:
            metadata_path = args.metadata_dir / f"{path.stem.removesuffix('-design')}.json"
            if metadata_path.is_file() and not metadata_path.is_symlink():
                original_hashes[metadata_path.resolve()] = sha256(metadata_path.read_bytes())
    output = prepare_output(args.out_dir, sources, args.metadata_dir)
    for folder in ("sources", "editable", "output", "qa"):
        (output / folder).mkdir()
    write_json(output / "profile-snapshot.json", source_document())
    rows = []
    for path in sources:
        base = path.stem.removesuffix("-design")
        name = f"{base}-{args.to_profile}"
        row = {"name": name, "source": str(path.resolve()), "sourceSha256": original_hashes[path.resolve()]}
        try:
            source = read_design_svg(path)
            metadata_path = args.metadata_dir / f"{base}.json" if args.metadata_dir else None
            metadata = verified_metadata(metadata_path, source, args.from_profile) if metadata_path else None
            source_token = token_named(source_profile, metadata["keyfitCheck"]["targetToken"] if metadata else args.source_keyshape)
            target_token = matching_token(source_token, target_profile, args.target_keyshape)
            content = path.read_bytes()
            if sha256(content) != row["sourceSha256"]:
                raise ValueError("Source changed while the trial was running")
            source_copy = output / "sources" / path.name
            source_copy.write_bytes(content)
            provenance = {"sourceSvg": "../sources/" + path.name, "sourceSha256": row["sourceSha256"],
                          "profileConfigurationSha256": original_hashes[config_path]}
            if metadata_path:
                provenance.update(sourceMetadata=str(metadata_path.resolve()),
                                  sourceMetadataSha256=original_hashes[metadata_path.resolve()],
                                  metadataGeometryVerified=True)
            document, adapted = make_draft(name, source, source_profile, target_profile, args.from_profile,
                args.to_profile, source_token, target_token, metadata, provenance)
            editable = output / "editable" / f"{name}.json"
            emitted = output / "output" / f"{name}.svg"
            write_json(editable, document)
            generated = svg(resolve_icon(document), target_profile["canvas"], target_profile["strokeWidth"])
            emitted.write_text(generated, encoding="utf-8")
            emitted.with_name(f"{name}-design.svg").write_text(generated, encoding="utf-8")
            qa = run_qa(document, editable, emitted, source_copy, args.from_profile, source_profile,
                        args.to_profile, target_profile, output)
            row.update(sourceCopy=str(source_copy.relative_to(output)), svg=str(emitted.relative_to(output)),
                       editable=str(editable.relative_to(output)), sourceToken=source_token["name"],
                       targetToken=target_token["name"], fitMode=document["keyfitCheck"]["mode"],
                       warnings=adapted["warnings"], metrics=adapted["metrics"], qa=qa,
                       status="draft-numeric-pass" if qa["mechanicalChecksPassed"] else "draft-needs-geometry-review")
            print(f"{base}: {row['status']} (grid {qa['grid']['status']}, keyshape {qa['keyshape']['status']}, holes {qa['holes']['status']})", flush=True)
        except Exception as error:
            row.update(status="error", error=str(error))
            print(f"{base}: ERROR — {error}", file=sys.stderr, flush=True)
        rows.append(row)
    changed_inputs = [str(path) for path, digest in original_hashes.items()
                      if not path.is_file() or sha256(path.read_bytes()) != digest]
    report = {"status": "trial-complete" if not changed_inputs and all("error" not in row for row in rows) else "trial-error",
              "sourceProfile": args.from_profile, "targetProfile": args.to_profile,
              "sourceCount": len(sources), "draftCount": sum("qa" in row for row in rows),
              "numericPassCount": sum(row.get("qa", {}).get("mechanicalChecksPassed", False) for row in rows),
              "approvedCount": 0, "originalsUnchanged": not changed_inputs, "changedInputs": changed_inputs,
              "notice": "Numeric success is not production approval. Every output is a draft requiring independent native-size review and source-analysis completion.",
              "files": rows}
    write_json(output / "summary.json", report)
    write_reviews(rows, output, source_profile, target_profile, originals_unchanged=not changed_inputs)
    print(f"Trial report: {output / 'review.html'}", flush=True)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--from-profile", required=True, choices=profile_names())
    parser.add_argument("--to-profile", required=True, choices=profile_names())
    source_intent = parser.add_mutually_exclusive_group(required=True)
    source_intent.add_argument("--metadata-dir", type=Path, help="verified companion v2 JSON intent, never the geometry source")
    source_intent.add_argument("--source-keyshape", help="explicit source token when no companion metadata is available")
    parser.add_argument("--target-keyshape", help="explicit target token if same-orientation matching is ambiguous")
    parser.add_argument("--out-dir", type=Path, required=True, help="new, separate trial folder; never overwritten")
    args = parser.parse_args()
    try:
        report = run_trial(args)
    except (ValueError, OSError, ImportError) as error:
        parser.error(str(error))
    return 0 if report["status"] == "trial-complete" else 1


if __name__ == "__main__":
    raise SystemExit(main())
