#!/usr/bin/env python3
"""Validate every registered icon, then export SVG, PNG and a manifest per family.

Validate-then-export: nothing reaches ``dist/`` that has not passed the full
chain. A failing icon is skipped -- listed with the element id and coordinates
that caused it -- while every passing icon is still published to its family
folder and the gallery. The exit code is 1 when anything was skipped. A family
where no icon exported keeps its previous release. Output is byte-stable, so a
clean rebuild produces an identical tree.

Builds are incremental by default: an icon is validated and exported only when
it is new or its source file (or an icon class it inherits) changed since its
last output; unchanged icons, passing or failing, reuse that last result. Use
``--all`` after changing validators, contracts, renderers or rules.

Each family ships to its own folder, named by the contract -- ``dist/sub32/``,
``dist/solo48/``, ``dist/container64/`` -- with its own ``manifest.json``. The
folders never mix: a family's manifest lists one profile, and the build skips
an icon whose profile is not its family's before it writes anything.

    python3 icon_set/scripts/build.py                # all families, changed icons only
    python3 icon_set/scripts/build.py --all          # re-check every icon
    python3 icon_set/scripts/build.py --family solo  # one family only
"""

from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import os
import shutil
import time
from contextlib import ExitStack
from tempfile import TemporaryDirectory
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.gallery import stage_gallery  # noqa: E402
from icon_set.model import contracts  # noqa: E402
from icon_set.model.icons.registry import icons_in  # noqa: E402
from icon_set.model.profiles import Profile  # noqa: E402
from icon_set.renderers.png import render_png  # noqa: E402
from icon_set.validation.library_qa import inspect_icon, artifact_key, save_evidence  # noqa: E402

PACKAGE_ROOT = REPO_ROOT / "icon_set"
DEFAULT_DIST = PACKAGE_ROOT / "dist"
DEFAULT_PNG = PACKAGE_ROOT / "assets" / "previews-png"
MANIFEST_VERSION = 2
ICONS_ROOT = PACKAGE_ROOT / "model" / "icons"
STALE_STAGE_SECONDS = 24 * 60 * 60


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


def _source_mtime(icon) -> float | None:
    """Newest authoring file behind an icon: its module and every icon class it inherits.

    Only files under ``model/icons`` count; a change to validators, contracts or
    renderers is not seen here -- rebuild with ``--all`` after one of those.
    """
    newest = None
    for cls in type(icon).__mro__:
        try:
            filename = inspect.getsourcefile(cls)
        except TypeError:
            continue
        if not filename:
            continue
        path = Path(filename).resolve()
        if path.is_relative_to(ICONS_ROOT) and path.is_file():
            newest = max(newest or 0.0, path.stat().st_mtime)
    return newest


class _Previous:
    """The last published build, consulted so unchanged icons are not re-checked."""

    def __init__(self, dist: Path, qa_dir: Path | None, *, debug: bool):
        self.qa_source = None
        self.qa_dir = qa_dir
        results = dist / 'qa' / 'results.json'
        if qa_dir is not None and results.is_file():
            try:
                aggregate = json.loads(results.read_text(encoding='utf-8'))
            except (OSError, ValueError):
                aggregate = None
            # Debug evidence is only reusable when the last run saved it too.
            if isinstance(aggregate, dict) and (aggregate.get('debug') or not debug):
                self.qa_source = dist / 'qa'

    def qa_row(self, key: str, mtime: float | None, *, selected: bool = True) -> dict | None:
        """The previous QA row for an icon unchanged since it, copied into the new evidence."""
        if self.qa_source is None or mtime is None or key.startswith('invalid/'):
            return None
        folder = self.qa_source / key
        metrics = folder / 'metrics.json'
        try:
            if metrics.stat().st_mtime < mtime:
                return None
            row = json.loads(metrics.read_text(encoding='utf-8'))
            shutil.copytree(folder, self.qa_dir / key, dirs_exist_ok=True)
            svg = folder / 'icon.svg'
            if svg.is_file():
                row['_svg'] = svg.read_text(encoding='utf-8')
        except (OSError, ValueError):
            return None
        if not isinstance(row, dict) or 'status' not in row:
            return None
        row['_key'] = key
        row['selected_for_build'] = selected
        return row


def _reusable_record(record: dict | None, svg: Path, png: Path | None, mtime: float | None) -> bool:
    """A manifest record still describes the files on disk, and both postdate the source."""
    if record is None or mtime is None:
        return False
    try:
        if svg.stat().st_mtime < mtime or (png is not None and png.stat().st_mtime < mtime):
            return False
        return hashlib.sha256(svg.read_bytes()).hexdigest() == record.get('svg_sha256')
    except OSError:
        return False


def _stage_family(
    family: str, dist: Path, png_dir: Path | None, *, write_png: bool, published_dist: Path,
    qa_rows: list, qa_dir: Path | None, debug: bool, previous: _Previous | None = None,
) -> tuple[int, int]:
    """Write one family into staging. Returns (prepared, failed).

    With ``previous`` (an incremental build), an icon whose source is older than
    its last output reuses that output -- and its last QA row -- instead of being
    validated and rendered again.
    """
    profile = Profile.for_family(family)
    folder = family_dist_name(family)
    target_dir = dist / folder
    preview_dir = png_dir / folder if (write_png and png_dir is not None) else None

    icons = list(icons_in(family))
    failures: list[tuple[str, list[str]]] = []
    records: list[dict] = []
    old_records = {}
    if previous is not None and (target_dir / 'manifest.json').is_file():
        try:
            old_records = {record['icon_id']: record for record in
                           json.loads((target_dir / 'manifest.json').read_text(encoding='utf-8'))['icons']}
        except (OSError, ValueError, KeyError, TypeError):
            old_records = {}
    reused = 0

    for icon in icons:
        key = artifact_key(icon)
        if icon.profile is not profile or icon.family != family:
            qa = inspect_icon(icon, debug_dir=qa_dir / key if debug and qa_dir else None)
            qa['_key'] = key
            qa_rows.append(qa)
            failures.append((icon.icon_id, [
                f"family {family!r} ships {profile.name} only; this icon is "
                f"{icon.family!r} on {getattr(icon.profile, 'name', icon.profile)!r}"
            ]))
            continue
        if previous is not None:
            mtime = _source_mtime(icon)
            record = old_records.get(icon.icon_id)
            old_qa = previous.qa_row(key, mtime) if qa_dir is not None else None
            png = preview_dir / f"{icon.icon_id}.png" if preview_dir is not None else None
            if _reusable_record(record, target_dir / f"{icon.icon_id}.svg", png, mtime) and \
                    (qa_dir is None or (old_qa is not None and old_qa['status'] == 'pass')):
                records.append(record)
                if old_qa is not None:
                    qa_rows.append(old_qa)
                reused += 1
                continue
            if record is None and old_qa is not None and old_qa['status'] != 'pass':
                # Unchanged since it last failed: the result would be the same.
                qa_rows.append(old_qa)
                failures.append((icon.icon_id, old_qa.get('errors') or old_qa.get('warnings') or []))
                reused += 1
                continue
        qa = inspect_icon(icon, debug_dir=qa_dir / key if debug and qa_dir else None)
        qa['_key'] = key
        qa_rows.append(qa)
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

            if preview_dir is not None:
                preview = preview_dir / f"{icon.icon_id}.png"
                preview.parent.mkdir(parents=True, exist_ok=True)
                preview.write_bytes(render_png(icon))
            # Recorded only once every output exists, so a half-exported icon is
            # left out of the manifest and its files are pruned below.
            records.append(record)
        except (OSError, ValueError, TypeError, RuntimeError) as error:
            qa['status'] = 'error'
            qa['errors'].append(f'export: {type(error).__name__}: {error}')
            failures.append((icon.icon_id, qa['errors']))

    if previous is not None:
        print(f"[{family}] {len(icons) - reused} of {len(icons)} icons checked; "
              f"{reused} unchanged since the last build reused")
    if failures:
        print(f"SKIPPED [{family}]: {len(failures)} of {len(icons)} icons did not validate\n")
        for icon_id, messages in failures:
            print(f"  {icon_id}")
            for message in messages:
                print(f"    {message}")
        print()
        if not records:
            # Nothing usable (e.g. the renderer is down): keep the previous release.
            return 0, len(failures)

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
    return len(records), len(failures)


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


def _sweep_stale_stages(root: Path) -> None:
    """Remove staging folders left by interrupted builds (or kept alive by Finder's .DS_Store)."""
    cutoff = time.time() - STALE_STAGE_SECONDS
    for stage in root.glob('.icon-build-*'):
        try:
            if stage.is_dir() and not stage.is_symlink() and stage.stat().st_mtime < cutoff:
                shutil.rmtree(stage, ignore_errors=True)
        except OSError:
            pass


def _build_selected(families, dist, png_dir, *, write_png, debug=False, report=True, rebuild_all=False):
    dist = dist.resolve()
    png_dir = png_dir.resolve() if write_png and png_dir is not None else None
    counts = []
    with ExitStack() as stack:
        stages = {}
        for root in dict.fromkeys([dist] + ([png_dir] if png_dir is not None else [])):
            root.mkdir(parents=True, exist_ok=True)
            _sweep_stale_stages(root)
            # Finder can drop a .DS_Store into the stage mid-build; that must not
            # turn a published build into a traceback.
            stage = Path(stack.enter_context(TemporaryDirectory(
                prefix='.icon-build-', dir=root, ignore_cleanup_errors=True)))
            stages[root] = stage
            for family in families:
                folder = family_dist_name(family)
                target = root / folder
                if target.exists():
                    shutil.copytree(target, stage / folder)
                else:
                    (stage / folder).mkdir()
        qa_rows = []
        qa_dir = stages[dist] / 'qa' if debug or report else None
        if qa_dir is not None:
            qa_dir.mkdir()
        previous = None if rebuild_all else _Previous(dist, qa_dir, debug=debug)
        for family in families:
            counts.append(_stage_family(
                family, stages[dist], stages.get(png_dir),
                write_png=write_png, published_dist=dist,
                qa_rows=qa_rows, qa_dir=qa_dir, debug=debug, previous=previous,
            ))
        if qa_dir is not None:
            # A filtered build still shows the complete current library. Only
            # selected families determine whether this release can be published.
            from icon_set.model.icons.registry import all_icons
            for icon in all_icons():
                if icon.family in families:
                    continue
                key = artifact_key(icon)
                row = previous.qa_row(key, _source_mtime(icon), selected=False) if previous else None
                if row is None:
                    row = inspect_icon(icon, debug_dir=qa_dir / key if debug else None, selected=False)
                    row['_key'] = key
                qa_rows.append(row)
            save_evidence(qa_rows, qa_dir, debug=debug, report=report)
            _publish([(qa_dir, dist / 'qa')])
            print(f"QA evidence -> {dist / 'qa' / ('index.html' if report else 'results.json')}")
        # Publish every family that exported something; failing icons are simply
        # left out. A family where nothing exported keeps its previous release.
        published = [family for family, (count, bad) in zip(families, counts) if count or not bad]
        replacements = [(stage / family_dist_name(family), root / family_dist_name(family))
                        for root, stage in stages.items() for family in published]
        gallery = stage_gallery(stages[dist], dist, [family_dist_name(name) for name in contracts.families()])
        replacements.append((gallery, dist / 'gallery'))
        _publish(replacements)
        print(f"Icon gallery -> {dist / 'gallery' / 'index.html'}")
    for family, (count, bad) in zip(families, counts):
        name = Profile.for_family(family).name
        if family not in published:
            print(f"[{family}] no icon exported; previous release kept -> {dist / family_dist_name(family)}")
            continue
        skipped = f", skipped {bad} failing" if bad else ""
        print(f"[{family}] validated and exported {count} {name} icons{skipped} "
              f"-> {dist / family_dist_name(family)}")
    failed = sum(bad for _, bad in counts)
    if failed:
        print(f"\n{failed} icon(s) skipped; see the SKIPPED lists above.")
    return sum(count for count, _ in counts), failed


def build_family(
    family: str, dist: Path, png_dir: Path | None, *, write_png: bool,
    debug: bool = False, report: bool = True, rebuild_all: bool = False,
) -> tuple[int, int]:
    """Publish one family's passing icons; failing icons are skipped and counted."""
    return _build_selected([family], dist, png_dir, write_png=write_png, debug=debug, report=report,
                           rebuild_all=rebuild_all)


def build(
    dist: Path = DEFAULT_DIST, png_dir: Path | None = DEFAULT_PNG, *, write_png: bool = True,
    only: list[str] | None = None, debug: bool = False, report: bool = True,
    rebuild_all: bool = False,
) -> int:
    families = list(contracts.families())
    if only:
        unknown = sorted(set(only) - set(families))
        if unknown:
            print(f"error: unknown family {unknown}; known: {families}", file=sys.stderr)
            return 2
        families = [name for name in families if name in only]
    _, failed = _build_selected(families, dist, png_dir, write_png=write_png, debug=debug, report=report,
                                rebuild_all=rebuild_all)
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
    parser.add_argument('--all', dest='rebuild_all', action='store_true',
                        help='re-validate and re-export every icon; by default only icons that are new '
                             'or whose source changed since the last build are checked')
    args = parser.parse_args(argv)
    return build(args.dist, args.png_dir, write_png=not args.no_png, only=args.family,
                 debug=args.debug, report=args.report, rebuild_all=args.rebuild_all)


if __name__ == "__main__":
    raise SystemExit(main())
