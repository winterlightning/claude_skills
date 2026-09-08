#!/usr/bin/env python3
"""Compose a container icon and a sub icon into one validated CONTAINER64 icon.

Ported from the previous system's ``compose_container_preview.py``, onto the
current model. The mechanics that script hand-rolled -- integer translation,
element-id namespacing, flattening -- already live in ``CombinedIcon``, so what
remains here is resolving two registered icons, placing them at the positions
the frozen ``CONTAINER_COMBINE`` template dictates, and running the full
validator chain over the result.

The original produced a deliberately non-shipping preview because its manifest
had nowhere to put a combined icon. This one produces a real, validated icon:
the template is frozen, so the composition either satisfies every locked rule or
reports exactly which element and coordinate does not.

    python3 icon_set/scripts/compose.py --host container-circle --sub plus
    python3 icon_set/scripts/compose.py --host container-square --sub heart --png

``--class`` selects the frozen template, which owns both child positions, so a
caller chooses only the two participants.

Since the protected slot was withdrawn a container no longer promises to fit
anything, so this is also the tool that answers whether a particular pair
works: it runs the full validator over the flattened composition and reports
the measured clearance between the two participants' real ink.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model import contracts  # noqa: E402
from icon_set.model.icons.combined import CombinedIcon  # noqa: E402
from icon_set.model.icons.registry import create, icon_ids  # noqa: E402
from icon_set.model.keyshapes import Keyshape, resolve_token  # noqa: E402
from icon_set.model.position import Position  # noqa: E402

PACKAGE_ROOT = REPO_ROOT / "icon_set"
DEFAULT_DIST = PACKAGE_ROOT / "dist" / "compositions"
DEFAULT_CLASS = "CONTAINER_COMBINE"


def frozen_classes() -> list[str]:
    return sorted(
        name for name, row in contracts.composition_templates()["classes"].items()
        if row.get("frozen") and "children" in row
    )


def template(composition_class: str = DEFAULT_CLASS) -> dict:
    classes = contracts.composition_templates()["classes"]
    if composition_class not in classes:
        raise ValueError(
            f"unknown composition class: {composition_class!r}; "
            f"available: {sorted(classes)}"
        )
    spec = classes[composition_class]
    if not spec.get("frozen") or "children" not in spec:
        raise ValueError(
            f"{composition_class} has no frozen arrangement in this release; "
            f"available: {frozen_classes()}"
        )
    return spec


def compose(
    host_id: str,
    sub_id: str,
    *,
    composition_class: str = DEFAULT_CLASS,
    icon_id: str | None = None,
    keyshape: Keyshape | None = None,
) -> CombinedIcon:
    """Build the combined icon at the template's dictated positions.

    The template owns both child positions, so a caller chooses only the two
    participants and which arrangement to use. Whether they clear each other
    is measured by the validator, not guaranteed by the template.
    """
    spec = template(composition_class)
    host = create(host_id)
    sub = create(sub_id)
    positions = [Position(*child["position"]) for child in spec["children"]]
    combined = CombinedIcon(
        icon_id or f"{host_id}-{sub_id}",
        composition_class,
        keyshape or host.keyshape,
        icons=[host, sub],
        positions=positions,
    )
    combined.semantic_kind = host.semantic_kind
    combined.semantic_role = host.semantic_role
    combined.category = "compositions"
    combined.keywords = tuple(dict.fromkeys(host.keywords + sub.keywords))
    return combined


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--host", "--container", dest="host",
        help="registered container-family (CONTAINER64) icon id (child 0)",
    )
    parser.add_argument("--sub", help="registered sub-family (SUB32) icon id (child 1)")
    parser.add_argument(
        "--class", dest="composition_class", default=DEFAULT_CLASS,
        help=f"frozen composition template (default: {DEFAULT_CLASS})",
    )
    parser.add_argument("--name", help="icon id for the result (default: <container>-<sub>)")
    parser.add_argument(
        "--keyshape",
        help="outer keyshape token (default: the container's own)",
    )
    parser.add_argument("--dist", type=Path, default=DEFAULT_DIST)
    parser.add_argument("--png", action="store_true", help="also write a native PNG")
    parser.add_argument("--list", action="store_true", help="list registered icon ids and exit")
    args = parser.parse_args(argv)

    if args.list:
        print("frozen composition classes:", ", ".join(frozen_classes()))
        print("registered icons:")
        for name in icon_ids():
            print(f"  {name}")
        return 0

    missing = [flag for flag, value in (("--host", args.host), ("--sub", args.sub)) if not value]
    if missing:
        parser.error(f"missing required argument(s): {', '.join(missing)}")

    try:
        keyshape = resolve_token(args.keyshape) if args.keyshape else None
        combined = compose(
            args.host, args.sub,
            composition_class=args.composition_class,
            icon_id=args.name, keyshape=keyshape,
        )
    except (KeyError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    report = combined.validate_icon()
    if not report.ok:
        print(f"{combined.icon_id}: {report.status}")
        for line in report.errors:
            print(f"  ERROR  {line}")
        for line in report.warnings:
            print(f"  WARN   {line}")
        return 1

    target = args.dist / f"{combined.icon_id}.svg"
    combined.export_icon_to(target)
    record = combined.to_record()
    record["svg_path"] = str(target.relative_to(PACKAGE_ROOT))
    record["validation"] = {"status": report.status, "checks_run": list(report.checks_run)}
    (args.dist / f"{combined.icon_id}.json").write_text(
        json.dumps(record, indent=2) + "\n", encoding="utf-8"
    )
    print(f"{combined.icon_id}: valid -> {target.relative_to(PACKAGE_ROOT)}")
    if args.png:
        preview = combined.export_icon_to(target.with_suffix(".png"))
        print(f"  png -> {preview.relative_to(PACKAGE_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
