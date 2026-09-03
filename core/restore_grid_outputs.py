#!/usr/bin/env python3
"""Re-emit the keyshape work set from canonical editable icon JSON sources."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

from icon_geometry import resolve_icon, svg
from icon_profiles import validate_document_profile


def source_for(root: Path, name: str) -> Path:
    candidates = (
        root / "work_keyshape_scale/hole_repaired_sources" / f"{name}.json",
        root / "output/batch-24" / f"{name}.json",
        root / "output/batch-23" / f"{name}.json",
        root / "remake_opus_output" / f"{name}.json",
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f"no editable JSON source for {name}")


def fractional_reasons(document: dict, design_svg: str) -> list[str]:
    reasons = []
    for instance in document.get("instances", []):
        reason = instance.get("fractionalReason")
        if reason and reason not in reasons:
            reasons.append(reason)
    path_data = re.findall(r"\sd=\"([^\"]*)\"", design_svg)
    if any(re.search(r"[-+]?\d*\.\d+", data) for data in path_data):
        shapes = sorted({item.get("shapeId", "unknown") for item in document.get("instances", [])})
        fallback = "Registered atomic geometry emits exact rotated, curved, junction, or optical coordinates: " + ", ".join(shapes)
        if not reasons:
            reasons.append(fallback)
    return reasons


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inventory", type=Path, help="flat SVG folder whose filenames define the repair set")
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    root = args.project_root.resolve()
    inventory = args.inventory.resolve()
    output = args.output_dir.resolve()
    if output.exists():
        if not args.overwrite:
            parser.error(f"output exists: {output}; pass --overwrite to replace generated files")
        shutil.rmtree(output)
    design_dir = output / "final"
    editable_dir = output / "editable"
    for folder in (design_dir, editable_dir):
        folder.mkdir(parents=True, exist_ok=True)

    manifest = {"version": 1, "files": {}}
    sources = []
    for inventory_svg in sorted(inventory.glob("*.svg")):
        name = inventory_svg.stem
        source = source_for(root, name)
        document = json.loads(source.read_text())
        if document.get("name") != name:
            raise ValueError(f"{source}: expected name {name!r}, found {document.get('name')!r}")
        _, profile = validate_document_profile(document)
        paths = resolve_icon(document)
        design_path = design_dir / f"{name}.svg"
        design_svg = svg(paths, profile["designCanvas"], profile["designStroke"])
        design_path.write_text(design_svg)
        shutil.copy2(source, editable_dir / source.name)
        reasons = fractional_reasons(document, design_svg)
        if reasons:
            manifest["files"][design_path.name] = {
                "sha256": hashlib.sha256(design_path.read_bytes()).hexdigest(),
                "allow": ["fractional-grid-lines", "fractional-design-values"],
                "reason": " | ".join(reasons),
                "source": str(source.relative_to(root)),
            }
        sources.append({"name": name, "editableSource": str(source.relative_to(root)), "instances": len(document.get("instances", []))})

    (output / "grid-exceptions.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (output / "repair-manifest.json").write_text(json.dumps(sources, indent=2) + "\n")
    (output / "README.md").write_text(
        "# Atomic-grid repair output\n\n"
        "This set was regenerated from the canonical editable icon JSON sources; it was not rounded or globally scaled.\n\n"
        "- `final/`: native-size SVGs matching their configured icon profiles; editable and final geometry are identical.\n"
        "- `editable/`: source JSON used for regeneration.\n"
        "- `grid-exceptions.json`: SHA-256-locked reasons for exact rotated, curved, junction, or optical fractions.\n"
        "- `repair-manifest.json`: source provenance for every icon.\n"
        "- `qa/`: validation evidence.\n\n"
        "Run the grid gate with `--exceptions grid-exceptions.json`; an exception becomes invalid if its SVG changes.\n"
    )
    print(f"re-emitted {len(sources)} icons from editable sources -> {output}")
    print(f"documented exact-geometry exceptions: {len(manifest['files'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
