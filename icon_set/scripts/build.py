#!/usr/bin/env python3
"""Validate every registered icon, then export SVG, PNG and a manifest per family.

Validate-then-export: nothing reaches ``dist/`` that has not passed the full
chain, and one failing icon fails the whole build with the element id and the
coordinates that caused it. Output is byte-stable, so a clean rebuild produces
an identical tree.

Each family ships to its own folder, named by the contract -- ``dist/sub32/``,
``dist/solo48/``, ``dist/container64/`` -- with its own ``manifest.json``. The
folders never mix: a family's manifest lists one profile, and the build refuses
an icon whose profile is not its family's before it writes anything.

    python3 icon_set/scripts/build.py                # all families
    python3 icon_set/scripts/build.py --family solo  # one family only
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from contextlib import ExitStack
from tempfile import TemporaryDirectory
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.model import contracts  # noqa: E402
from icon_set.model.icons.registry import icons_in  # noqa: E402
from icon_set.model.profiles import Profile  # noqa: E402
from icon_set.renderers.png import render_png  # noqa: E402
from icon_set.validation.library_qa import inspect_icon, artifact_key, save_evidence  # noqa: E402

PACKAGE_ROOT = REPO_ROOT / "icon_set"
DEFAULT_DIST = PACKAGE_ROOT / "dist"
DEFAULT_PNG = PACKAGE_ROOT / "assets" / "previews-png"
MANIFEST_VERSION = 2


def family_dist_name(family: str) -> str:
    """``dist/sub32`` -> ``sub32``: the contract names the folder."""
    return contracts.families()[family]["dist"].rsplit("/", 1)[-1]


def _prune(directory: Path, suffix: str, keep: set[str]) -> list[Path]:
    """Delete outputs for icons that no longer exist, so a rename cannot linger."""
    if not directory.is_dir():
        return []
    removed = []
    for path in sorted(directory.glob(f"*{suffix}")):
        if path.stem not in keep:
            path.unlink()
            removed.append(path)
    return removed


def _stage_family(
    family: str, dist: Path, png_dir: Path | None, *, write_png: bool, published_dist: Path,
    qa_rows: list, qa_dir: Path | None, debug: bool
) -> tuple[int, int]:
    """Write one family into staging. Returns (prepared, failed)."""
    profile = Profile.for_family(family)
    folder = family_dist_name(family)
    target_dir = dist / folder
    preview_dir = png_dir / folder if (write_png and png_dir is not None) else None

    icons = list(icons_in(family))
    failures: list[tuple[str, list[str]]] = []
    records: list[dict] = []

    for icon in icons:
        key = artifact_key(icon)
        qa = inspect_icon(icon, debug_dir=qa_dir / key if debug and qa_dir else None)
        qa['_key'] = key
        qa_rows.append(qa)
        if icon.profile is not profile or icon.family != family:
            failures.append((icon.icon_id, [
                f"family {family!r} ships {profile.name} only; this icon is "
                f"{icon.family!r} on {getattr(icon.profile, 'name', icon.profile)!r}"
            ]))
            continue
        if qa['status'] != 'pass':
            failures.append((icon.icon_id, qa['errors'] or qa['warnings']))
            continue
        try:
            document = qa['_svg']
            target = target_dir / f"{icon.icon_id}.svg"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(document, encoding="utf-8")

            record = icon.to_record()
            record["svg_path"] = os.path.relpath(published_dist / folder / target.name, PACKAGE_ROOT)
            record["svg_sha256"] = hashlib.sha256(document.encode("utf-8")).hexdigest()
            record["validation"] = {
                "status": "valid",
                "checks_run": qa['checks_run'] + ['holes/pinches'],
                "warnings": qa['warnings'],
                "negative_space": {key: value for key, value in qa['negative_space'].items()
                                   if key not in ('holes', 'pinches')},
                "rules_sha256": qa['rules_sha256'],
                "internal_spacing_advisory": qa.get("internal_spacing"),
            }
            records.append(record)

            if preview_dir is not None:
                preview = preview_dir / f"{icon.icon_id}.png"
                preview.parent.mkdir(parents=True, exist_ok=True)
                preview.write_bytes(render_png(icon))
        except (OSError, ValueError, TypeError, RuntimeError) as error:
            qa['status'] = 'error'
            qa['errors'].append(f'export: {type(error).__name__}: {error}')
            failures.append((icon.icon_id, qa['errors']))

    if failures:
        print(f"BUILD FAILED [{family}]: {len(failures)} of {len(icons)} icons did not validate\n")
        for icon_id, messages in failures:
            print(f"  {icon_id}")
            for message in messages:
                print(f"    {message}")
        return len(records), len(failures)

    keep = {record["icon_id"] for record in records}
    _prune(target_dir, ".svg", keep)
    if preview_dir is not None:
        _prune(preview_dir, ".png", keep)

    manifest = {
        "manifest_version": MANIFEST_VERSION,
        "family": family,
        "profile": profile.name,
        "canvas_size": profile.spec.canvas_size,
        "count": len(records),
        "icons": records,
    }
    target_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = target_dir / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=False) + "\n", encoding="utf-8"
    )
    return len(records), 0


def _publish(replacements: list[tuple[Path, Path]]) -> None:
    """Swap complete directories, rolling back earlier swaps on an I/O error.

    Each rename is on the destination filesystem. This protects ordinary failed
    builds; multiple output directories are not one crash-atomic transaction.
    """
    completed = []
    try:
        for staged, target in replacements:
            backup = staged.parent / (staged.name + '.previous')
            existed = target.exists()
            if existed:
                os.replace(target, backup)
            completed.append((target, backup, existed))
            os.replace(staged, target)
    except OSError:
        for target, backup, existed in reversed(completed):
            if target.exists():
                shutil.rmtree(target)
            if existed:
                os.replace(backup, target)
        raise


def _build_selected(families, dist, png_dir, *, write_png, debug=False, report=True):
    dist = dist.resolve()
    png_dir = png_dir.resolve() if write_png and png_dir is not None else None
    counts = []
    replacements = []
    with ExitStack() as stack:
        stages = {}
        for root in dict.fromkeys([dist] + ([png_dir] if png_dir is not None else [])):
            root.mkdir(parents=True, exist_ok=True)
            stage = Path(stack.enter_context(TemporaryDirectory(prefix='.icon-build-', dir=root)))
            stages[root] = stage
            for family in families:
                folder = family_dist_name(family)
                target = root / folder
                if target.exists():
                    shutil.copytree(target, stage / folder)
                else:
                    (stage / folder).mkdir()
                replacements.append((stage / folder, target))
        qa_rows = []
        qa_dir = stages[dist] / 'qa' if debug or report else None
        if qa_dir is not None:
            qa_dir.mkdir()
        for family in families:
            counts.append(_stage_family(
                family, stages[dist], stages.get(png_dir),
                write_png=write_png, published_dist=dist,
                qa_rows=qa_rows, qa_dir=qa_dir, debug=debug,
            ))
        if qa_dir is not None:
            # A filtered build still shows the complete current library. Only
            # selected families determine whether this release can be published.
            from icon_set.model.icons.registry import all_icons
            for icon in all_icons():
                if icon.family in families:
                    continue
                key = artifact_key(icon)
                row = inspect_icon(icon, debug_dir=qa_dir / key if debug else None, selected=False)
                row['_key'] = key
                qa_rows.append(row)
            save_evidence(qa_rows, qa_dir, debug=debug, report=report)
            _publish([(qa_dir, dist / 'qa')])
            print(f"QA evidence -> {dist / 'qa' / ('index.html' if report else 'results.json')}")
        failed = sum(bad for _, bad in counts)
        if failed:
            return 0, failed
        _publish(replacements)
    for family, (count, _) in zip(families, counts):
        print(f"[{family}] validated and exported {count} {Profile.for_family(family).name} icons "
              f"-> {dist / family_dist_name(family)}")
    return sum(count for count, _ in counts), 0


def build_family(
    family: str, dist: Path, png_dir: Path | None, *, write_png: bool,
    debug: bool = False, report: bool = True,
) -> tuple[int, int]:
    """Publish one complete family only after validation and rendering succeed."""
    return _build_selected([family], dist, png_dir, write_png=write_png, debug=debug, report=report)


def build(
    dist: Path = DEFAULT_DIST, png_dir: Path | None = DEFAULT_PNG, *, write_png: bool = True,
    only: list[str] | None = None, debug: bool = False, report: bool = True,
) -> int:
    families = list(contracts.families())
    if only:
        unknown = sorted(set(only) - set(families))
        if unknown:
            print(f"error: unknown family {unknown}; known: {families}", file=sys.stderr)
            return 2
        families = [name for name in families if name in only]
    _, failed = _build_selected(families, dist, png_dir, write_png=write_png, debug=debug, report=report)
    return 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--dist", type=Path, default=DEFAULT_DIST)
    parser.add_argument("--png-dir", type=Path, default=DEFAULT_PNG)
    parser.add_argument(
        "--no-png", action="store_true", help="skip PNG previews (SVG is canonical)"
    )
    parser.add_argument(
        "--family", action="append", choices=list(contracts.families()),
        help="build one family only (repeatable); default is every family",
    )
    parser.add_argument('--debug', action=argparse.BooleanOptionalAction, default=False,
                        help='save per-icon spacing and hole debug images (default: false)')
    parser.add_argument('--report', action=argparse.BooleanOptionalAction, default=True,
                        help='save library-wide HTML and JSON QA report (default: true)')
    args = parser.parse_args(argv)
    return build(args.dist, args.png_dir, write_png=not args.no_png, only=args.family,
                 debug=args.debug, report=args.report)


if __name__ == "__main__":
    raise SystemExit(main())
