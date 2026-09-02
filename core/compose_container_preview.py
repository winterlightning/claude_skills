#!/usr/bin/env python3
"""Compose a non-shipping filled container preview from two editable sources.

The manifest keeps the shipping container and the candidate sub icon separate.
Only the rendered preview pair is produced; no flattened editable document is
created because such a document is not a valid icon type and must never enter
the shipping validation path.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
from typing import Any

from icon_geometry import Command, resolve_icon, sample, svg
from icon_profiles import (
    token_named,
    validate_container_slot,
    validate_document_profile,
)
from keyfit import circle_overflow, matches, token_box


MANIFEST_KIND = "container-filled-preview"
MANIFEST_SCHEMA_VERSION = 1
KEBAB_CASE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def _read_json(path: Path, label: str) -> dict[str, Any]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as error:
        raise ValueError(f"missing {label}: {path}") from error
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON in {label} {path}: {error}") from error
    if not isinstance(document, dict):
        raise ValueError(f"{label} must contain a JSON object: {path}")
    return document


def _referenced_json(manifest_path: Path, manifest: dict[str, Any], field: str) -> tuple[Path, dict[str, Any]]:
    raw = manifest.get(field)
    if not isinstance(raw, str) or not raw.strip():
        raise ValueError(f"preview manifest requires a relative {field!r} JSON path")
    reference = Path(raw)
    if reference.is_absolute():
        raise ValueError(f"preview manifest {field!r} path must be relative")
    path = (manifest_path.parent / reference).resolve()
    if path.suffix.lower() != ".json":
        raise ValueError(f"preview manifest {field!r} must reference a JSON file")
    return path, _read_json(path, f"{field} source")


def _validate_sub_keyshape(document: dict[str, Any], paths: list[dict], target_name: str) -> None:
    """Keep a preview candidate honest about the accepted painted boundary."""
    target = token_named(target_name, "sub")
    if target is None:
        raise ValueError(f"unknown sub keyshape target {target_name!r}")
    points = [
        point
        for path in paths
        for point in sample(path["commands"])[0]
    ]
    if not points:
        raise ValueError("sub source has no painted geometry")
    stroke = float(document.get("strokeWidth", 4))
    radius = stroke / 2.0
    actual = (
        min(x for x, _ in points) - radius,
        min(y for _, y in points) - radius,
        max(x for x, _ in points) + radius,
        max(y for _, y in points) + radius,
    )
    expected = token_box(target["width"], target["height"], "sub")
    if not matches(expected, actual, 1e-3):
        raise ValueError(
            f"sub painted bounds {actual} do not match declared {target_name} bounds {expected}"
        )
    if target["shape"] == "circle":
        overflow = circle_overflow(points, stroke, "sub")
        if overflow > 1e-3:
            raise ValueError(
                f"sub painted geometry exceeds {target_name} by {overflow:.4g}u"
            )


def _translated(paths: list[dict], dx: float, dy: float) -> list[dict]:
    translated = []
    for path in paths:
        commands = [
            Command(
                command.type,
                [(x + dx, y + dy) for x, y in command.points],
                command.arc,
            )
            for command in path["commands"]
        ]
        translated.append({**path, "commands": commands})
    return translated


def compose(manifest_path: Path, output_dir: Path) -> tuple[Path, Path]:
    """Validate one manifest and write its design/ship preview pair."""
    manifest_path = manifest_path.expanduser().resolve()
    manifest = _read_json(manifest_path, "preview manifest")
    if manifest.get("schemaVersion") != MANIFEST_SCHEMA_VERSION:
        raise ValueError(
            f"preview manifest schemaVersion must be {MANIFEST_SCHEMA_VERSION}"
        )
    if manifest.get("kind") != MANIFEST_KIND:
        raise ValueError(f"preview manifest kind must be {MANIFEST_KIND!r}")
    name = manifest.get("name", manifest_path.stem)
    if not isinstance(name, str) or KEBAB_CASE.fullmatch(name) is None:
        raise ValueError("preview name must be kebab-case")

    container_path, container = _referenced_json(
        manifest_path, manifest, "container"
    )
    sub_path, sub = _referenced_json(manifest_path, manifest, "sub")
    container_type, container_profile = validate_document_profile(container)
    sub_type, sub_profile = validate_document_profile(sub)
    if container_type != "container":
        raise ValueError(
            f"container source must declare iconType 'container': {container_path}"
        )
    if sub_type != "sub":
        raise ValueError(f"sub source must declare iconType 'sub': {sub_path}")

    slot = validate_container_slot(container, container_profile)
    target_name = (sub.get("keyfitCheck") or {}).get("targetToken")
    if not isinstance(target_name, str) or not target_name:
        raise ValueError("sub source requires keyfitCheck.targetToken")
    accepted_name = slot["acceptedToken"]["name"]
    if target_name != accepted_name:
        raise ValueError(
            f"container accepts {accepted_name}, but sub declares {target_name}"
        )
    if slot["w"] != sub_profile["designCanvas"] or slot["h"] != sub_profile["designCanvas"]:
        raise ValueError("container slot dimensions must equal the sub design canvas")

    container_paths = resolve_icon(container)
    sub_paths = resolve_icon(sub)
    _validate_sub_keyshape(sub, sub_paths, target_name)
    paths = [
        *container_paths,
        *_translated(sub_paths, float(slot["x"]), float(slot["y"])),
    ]

    design_canvas = container_profile["designCanvas"]
    ship_canvas = container_profile["shipCanvas"]
    design_stroke = container_profile["designStroke"]
    ship_stroke = container_profile["shipStroke"]
    scale = ship_canvas / design_canvas
    if scale != 0.5 or ship_stroke / design_stroke != 0.5:
        raise ValueError("filled previews require exact half-scale ship geometry")

    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    design_path = output_dir / f"{name}-design.svg"
    ship_path = output_dir / f"{name}.svg"
    design_path.write_text(
        svg(paths, design_canvas, design_stroke), encoding="utf-8"
    )
    ship_path.write_text(
        svg(paths, ship_canvas, ship_stroke, scale), encoding="utf-8"
    )
    return design_path, ship_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    design_path, ship_path = compose(args.manifest, args.out_dir)
    print(
        "NON-SHIPPING preview emitted to "
        f"{design_path} and {ship_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
