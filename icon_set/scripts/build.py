#!/usr/bin/env python3
"""Validate every registered icon, then export SVG, PNG and a manifest per family.

Validate-then-export: nothing reaches a release folder that has not passed the
full chain, unless --artwork-dir explicitly opts into saved human choices.
Default builds read Python originals only and write to icon_set/.local/dist;
PNG previews go to icon_set/.local/previews-png. Both are ignored by Git.
The dist/ paths below describe the layout inside the chosen output directory.
Manual SVG uploads and accepted gallery edits retain their provenance and raw
validation findings. A failing icon still renders -- its SVG and its findings go to
``dist/failed/<family><canvas>/`` and the gallery's Failed build tab, grouped
by the rule it breaks -- while every passing icon is published to its family
folder. The exit code is 1 when anything failed. A family where no icon
exported keeps its previous release. Output is byte-stable, so a clean rebuild
produces an identical tree.

Builds are incremental by default: an icon is validated and exported only when
it is new or its source file (or an icon class it inherits) changed since its
last output; unchanged icons, passing or failing, reuse that last result. Use
``--all`` after changing validators, contracts, renderers or rules.

Each family ships to its own folder, named by the contract -- ``dist/sub32/``,
``dist/solo48/``, ``dist/container64/`` -- with its own ``manifest.json``. The
folders never mix: a family's manifest lists one profile, and an icon whose
profile is not its family's is sent to the failed build.

Results saved by ``qa_overlays.py`` into ``icon_set/work/qa_overlays/<folder>/``
also gate publication: an icon whose saved distance or hole check failed on the
exact SVG it would publish goes to the failed build. Run qa_overlays.py first,
then build; ``--qa-overlays DIR`` reads another folder.

    python3 icon_set/scripts/build.py                # all families, changed icons only
    python3 icon_set/scripts/build.py --all          # re-check every icon
    python3 icon_set/scripts/build.py --family solo  # one family only
    python3 icon_set/scripts/build.py --icon icon_set/model/icons/solo/anteater.py  # one icon only
"""

from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import os
import re
import shutil
import time
from contextlib import ExitStack
from tempfile import TemporaryDirectory
import sys
from pathlib import Path

if __package__:
    from .workspace import DEFAULT_DIST, DEFAULT_PNG, output_lock
else:
    from workspace import DEFAULT_DIST, DEFAULT_PNG, output_lock

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from icon_set.scripts.icon_artwork import ArtworkStore, resolve_artwork, icon_from_graph, sha
from icon_set.scripts.gallery import stage_gallery  # noqa: E402
from icon_set.model import contracts  # noqa: E402
from icon_set.model.metadata import publish_metadata
from icon_set.model.icons.registry import factories, icons_in, families as registry_families  # noqa: E402
from icon_set.model.profiles import Profile  # noqa: E402
from icon_set.renderers.png import render_png  # noqa: E402
from icon_set.validation.library_qa import inspect_icon, artifact_key, save_evidence  # noqa: E402

PACKAGE_ROOT = REPO_ROOT / "icon_set"


MANIFEST_VERSION = 2
ICONS_ROOT = PACKAGE_ROOT / "model" / "icons"
DEFAULT_QA_OVERLAYS = PACKAGE_ROOT / "work" / "qa_overlays"
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
    """Newest input to publication, including geometry and validation code.

    An unchanged drawing must be rechecked when the rules or their implementation
    change. Targeted builds still carry unselected icons over explicitly.
    """
    inputs = [* (PACKAGE_ROOT / 'validation').rglob('*.py'),
              * (PACKAGE_ROOT / 'renderers').rglob('*.py'),
              * (PACKAGE_ROOT / 'model').glob('*.py'),
              * (PACKAGE_ROOT / 'model' / 'contracts').glob('*.json')]
    newest = max((path.stat().st_mtime for path in inputs), default=None)
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
        self.debug = debug
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
            if self.debug:
                shutil.copytree(folder, self.qa_dir / key, dirs_exist_ok=True)
            else:
                # Without --debug the new snapshot must not inherit old debug images.
                row['artifacts'] = {name: path for name, path in (row.get('artifacts') or {}).items()
                                    if name in ('svg', 'metrics')}
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


def _source_path(icon) -> str | None:
    try:
        path = Path(inspect.getsourcefile(type(icon)) or '').resolve()
    except TypeError:
        return None
    return path.relative_to(REPO_ROOT).as_posix() if path.is_file() and path.is_relative_to(REPO_ROOT) else None


def _failed_record(icon, family: str, qa: dict, messages: list[str], mtime: float | None) -> dict:
    """What the Failed build tab needs to show an icon and mark what it violates."""
    pairs = [{"a": pair["nearestPoints"][0], "b": pair["nearestPoints"][1],
              "distance": round(pair["centerlineDistance"], 3)}
             for pair in qa.get('spacing', {}).get('pairs', [])
             if pair.get('status') == 'fail' and pair.get('nearestPoints') and pair.get('centerlineDistance', 0) > 0]
    pairs.extend({"a": finding['nearest_points'][0], "b": finding['nearest_points'][1],
                  "distance": finding['centerline_distance'], "status": "review"}
                 for finding in qa.get('internal_spacing', {}).get('findings', []))
    holes = [hole["bbox_viewbox"] for hole in qa.get('negative_space', {}).get('holes', [])
             if hole.get('status') == 'fail' and hole.get('bbox_viewbox')]
    return {
        "icon_id": str(icon.icon_id), "family": family,
        "profile": getattr(icon.profile, 'name', str(icon.profile)),
        "canvas_size": (qa.get('rules') or {}).get('profile', {}).get('canvas_size')
                       or Profile.for_family(family).spec.canvas_size,
        "status": qa.get('status', 'error'), "errors": list(messages), "warnings": list(qa.get('warnings') or []),
        "svg": None, "svg_sha256": None, "source_path": _source_path(icon), "source_mtime": mtime,
        "spacing_pairs": pairs, "holes": holes,
    }


def _qa_overlay_failure(results: Path | None, folder: str, icon_id: str, svg_sha: str | None) -> dict | None:
    """qa_overlays.py's saved verdict for this exact SVG, when its distance or hole check failed.

    Returns the findings to fail the icon with, or None: no results, a result for
    another drawing, or a pass. An errored measurement is not a failure.
    """
    if results is None or svg_sha is None:
        return None
    try:
        metrics = json.loads((results / folder / f"{icon_id}.metrics.json").read_text(encoding='utf-8'))
    except (OSError, ValueError):
        return None
    if not isinstance(metrics, dict) or metrics.get('svg_sha256') != svg_sha:
        return None
    errors, holes = [], []
    if metrics.get('distance_passed') is False:
        errors.append(f"qa-overlays distance: lowest {metrics.get('min_gap_kind') or 'gap'} distance "
                      f"{metrics.get('lowest_distance')} on centerlines; requires at least {metrics.get('distance_gate')}")
    if metrics.get('negative_space_passed') is False:
        failed = [hole for hole in metrics.get('holes') or [] if hole.get('status') == 'fail']
        errors.append(f"qa-overlays holes/pinches: {len(failed)} undersized holes; "
                      f"{len(metrics.get('pinches') or [])} pinches")
        for hole in failed:
            (cx, cy), radius = hole['center'], hole['inscribed_radius_u']
            holes.append([cx - radius, cy - radius, cx + radius, cy + radius])
    return {'errors': errors, 'holes': holes} if errors else None


def _drawing_sha(icon) -> str | None:
    """Hash of the SVG the model draws now; cheap next to validation, and it sees edits
    made outside the icon's own file (a shared base, a keyshape) that mtimes miss."""
    try:
        return hashlib.sha256(icon.to_svg().encode('utf-8')).hexdigest()
    except Exception:  # a broken model is reported by validation, not here
        return None


def _reusable_record(record: dict | None, svg: Path, png: Path | None, mtime: float | None,
                     drawing: str | None) -> bool:
    """A manifest record still describes the files on disk and the current drawing."""
    if record is None or mtime is None or drawing is None or record.get('svg_sha256') != drawing:
        return False
    try:
        if svg.stat().st_mtime < mtime or (png is not None and png.stat().st_mtime < mtime):
            return False
        return hashlib.sha256(svg.read_bytes()).hexdigest() == drawing
    except OSError:
        return False


_SAFE_ID = re.compile(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*')


def _manifest_icons(path: Path) -> dict[str, dict]:
    try:
        return {record['icon_id']: record for record in json.loads(path.read_text(encoding='utf-8'))['icons']}
    except (OSError, ValueError, KeyError, TypeError):
        return {}


def _stage_family(
    family: str, dist: Path, png_dir: Path | None, *, write_png: bool, published_dist: Path,
    qa_rows: list, qa_dir: Path | None, debug: bool, previous: _Previous | None = None,
    only: set[str] | None = None, qa_overlays: Path | None = None, artwork_dir: Path | None = None,
) -> tuple[int, int]:
    """Write one family into staging. Returns (prepared, failed).

    With ``previous`` (an incremental build), an icon whose source is older than
    its last output reuses that output -- and its last QA row -- instead of being
    validated and rendered again. With ``only`` (icon ids), just those icons are
    validated; the failed count covers them alone.
    """
    profile = Profile.for_family(family)
    folder = family_dist_name(family)
    target_dir = dist / folder
    preview_dir = png_dir / folder if (write_png and png_dir is not None) else None

    failures: list[tuple[str, list[str]]] = []
    records: list[dict] = []
    failed_records: list[dict] = []
    # Failed icons still get an SVG, kept apart from the release folder so a
    # consumer of dist/<family> never ships one.
    failed_dir = dist / 'failed' / folder
    failed_dir.mkdir(parents=True, exist_ok=True)
    old_records = _manifest_icons(target_dir / 'manifest.json') if previous is not None or only else {}
    old_failed = _manifest_icons(published_dist / 'failed' / folder / 'manifest.json') if previous is not None or only else {}
    reused = 0

    if only is None:
        icons = list(icons_in(family))
    else:
        # A targeted build checks only the selected icons. Every other icon keeps
        # its last published result as-is -- not re-rendered, not re-checked --
        # and one that never built stays out.
        base = registry_families()[family]
        members = {icon_id: factory for icon_id, factory in factories().items() if issubclass(factory, base)}
        icons = [factory() for icon_id, factory in members.items() if icon_id in only]
        for icon_id, factory in members.items():
            if icon_id in only:
                continue
            key = f"{factory.family}/{icon_id}"
            old_qa = previous.qa_row(key, 0.0) if previous is not None and qa_dir is not None else None
            if icon_id in old_records:
                records.append(old_records[icon_id])
            elif icon_id in old_failed:
                stale = dict(old_failed[icon_id])
                try:
                    if stale.get('svg'):
                        (failed_dir / stale['svg']).write_bytes(
                            (published_dist / 'failed' / folder / stale['svg']).read_bytes())
                except OSError:
                    stale['svg'] = None
                failed_records.append(stale)
            else:
                continue
            if old_qa is not None:
                qa_rows.append(old_qa)
            reused += 1

    def fail(icon, qa, messages, mtime, document=None):
        failures.append((icon.icon_id, messages))
        entry = _failed_record(icon, family, qa, messages, mtime)
        document = document if document is not None else qa.get('_svg')
        if document and _SAFE_ID.fullmatch(str(icon.icon_id)):
            (failed_dir / f"{icon.icon_id}.svg").write_text(document, encoding='utf-8')
            entry["svg"] = f"{icon.icon_id}.svg"
            entry["svg_sha256"] = hashlib.sha256(document.encode('utf-8')).hexdigest()
        failed_records.append(entry)

    def overlay_failure(icon_id, svg_sha):
        return _qa_overlay_failure(qa_overlays, folder, icon_id, svg_sha)

    artwork_store = ArtworkStore(artwork_dir) if artwork_dir is not None else None
    for icon in icons:
        key = artifact_key(icon)
        choice = artwork_store.get(key) if artwork_store is not None else None
        manual = resolve_artwork(icon.to_record(), choice) if choice else None
        mtime = _source_mtime(icon) if previous is not None else None
        if icon.profile is not profile or icon.family != family:
            qa = inspect_icon(icon, debug_dir=qa_dir / key if debug and qa_dir else None)
            qa['_key'] = key
            qa_rows.append(qa)
            fail(icon, qa, [
                f"family {family!r} ships {profile.name} only; this icon is "
                f"{icon.family!r} on {getattr(icon.profile, 'name', icon.profile)!r}"
            ], mtime)
            continue
        if previous is not None and only is None and manual is None:
            drawing = _drawing_sha(icon)
            record = old_records.get(icon.icon_id)
            if record and record.get('artwork_source', 'use_org') != 'use_org':
                record = None
            old_qa = previous.qa_row(key, mtime) if qa_dir is not None else None
            png = preview_dir / f"{icon.icon_id}.png" if preview_dir is not None else None
            overlay = overlay_failure(icon.icon_id, drawing)
            if _reusable_record(record, target_dir / f"{icon.icon_id}.svg", png, mtime, drawing) and \
                    overlay is None and \
                    (qa_dir is None or (old_qa is not None and old_qa['status'] == 'pass')):
                records.append(record)
                if old_qa is not None:
                    qa_rows.append(old_qa)
                reused += 1
                continue
            stale = old_failed.get(icon.icon_id)
            if record is None and stale is not None and mtime is not None and \
                    (stale.get('source_mtime') or 0) >= mtime and stale.get('svg_sha256') == drawing and \
                    bool(stale.get('qa_overlays_failed')) == (overlay is not None) and \
                    (qa_dir is None or (old_qa is not None and old_qa['status'] != 'pass')):
                # Unchanged since it last failed: the result would be the same.
                document = None
                if stale.get('svg'):
                    try:
                        document = (published_dist / 'failed' / folder / stale['svg']).read_text(encoding='utf-8')
                    except OSError:
                        document = None
                if stale.get('svg') is None or document is not None:
                    if old_qa is not None:
                        qa_rows.append(old_qa)
                    failures.append((icon.icon_id, stale.get('errors') or stale.get('warnings') or []))
                    if document is not None:
                        (failed_dir / stale['svg']).write_text(document, encoding='utf-8')
                    failed_records.append(stale)
                    reused += 1
                    continue
        if manual and manual['source_mode'] == 'use_upload':
            # Uploaded outlines are an explicit human-selected source, not a
            # claim that the original Python primitive graph passed checks.
            qa = {'icon_id': icon.icon_id, 'family': family, 'profile': profile.name,
                  'selected_for_build': True, 'status': 'pass', 'automatic_status': 'not-run',
                  'errors': [], 'warnings': ['Manually selected SVG; Python primitive checks do not describe this artwork.'],
                  'checks_run': ['SVG import', 'human source selection'], 'artifacts': {},
                  'spacing': {'status': 'not_run'}, 'negative_space': {'status': 'not_run'},
                  'symmetry': {'status': 'not_run'}, 'rules_sha256': None,
                  '_svg': manual['svg'], 'svg_sha256': manual['svg_sha256']}
        else:
            qa = inspect_icon(icon_from_graph(manual['graph']) if manual else icon,
                              debug_dir=qa_dir / key if debug and qa_dir else None)
        if manual:
            qa['artwork_source'] = manual['source_mode']
            qa['human_selection'] = {'by': choice.get('selected_by', choice['updated_by']), 'at': choice.get('selected_at', choice['updated_at'])}
            if manual['validation_override']:
                qa['automatic_status'] = qa['status'] if manual['source_mode']=='use_edited' else 'not-run'
                qa['validation_override'] = manual['validation_override']
                qa['status'] = 'pass'
        qa['_key'] = key
        qa_rows.append(qa)
        document = qa.get('_svg')
        overlay = overlay_failure(icon.icon_id, hashlib.sha256(document.encode('utf-8')).hexdigest()
                                  if document else None)
        if overlay is not None:
            qa['errors'].extend(overlay['errors'])
            qa['qa_overlays'] = overlay
            if qa['status'] == 'pass' and not (manual and manual['validation_override']):
                qa['status'] = 'fail'
        if qa['status'] != 'pass':
            fail(icon, qa, qa['errors'] or qa['warnings'], mtime)
            if overlay is not None:
                failed_records[-1]['qa_overlays_failed'] = True
                failed_records[-1]['holes'].extend(overlay['holes'])
            continue
        try:
            document = qa['_svg']
            target = target_dir / f"{icon.icon_id}.svg"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(document, encoding="utf-8")

            record = icon.to_record()
            record['artwork_source'] = 'use_org'
            if manual:
                record['generated_graph'] = {k: v for k, v in record.items() if k != 'artwork_source'}
                record['generated_svg_sha256'] = sha(icon.to_svg())
                if manual['graph']:
                    record.update(manual['graph'])
                record['artwork_source'] = manual['source_mode']
                record['artwork_revision'] = choice['revision']
                record['artwork_review'] = qa.get('human_selection')
            record["svg_path"] = os.path.relpath(published_dist / folder / target.name, PACKAGE_ROOT)
            record["svg_sha256"] = hashlib.sha256(document.encode("utf-8")).hexdigest()
            record["validation"] = {
                "status": "human-selected" if manual and (manual['source_mode']=='use_upload' or manual['validation_override']) else "valid",
                "automatic_status": qa.get('automatic_status', qa['status']),
                "validation_override": qa.get('validation_override'),
                "errors": qa['errors'],
                "checks_run": qa['checks_run'] + ([] if manual and manual['source_mode']=='use_upload' else ['holes/pinches', 'internal-spacing-review']),
                "warnings": qa['warnings'],
                "negative_space": {key: value for key, value in qa['negative_space'].items()
                                   if key not in ('holes', 'pinches')},
                "rules_sha256": qa['rules_sha256'],
                "internal_spacing_advisory": qa.get("internal_spacing"),
            }

            if preview_dir is not None:
                preview = preview_dir / f"{icon.icon_id}.png"
                preview.parent.mkdir(parents=True, exist_ok=True)
                if manual:
                    import cairosvg
                    preview.write_bytes(cairosvg.svg2png(bytestring=document.encode('utf-8'),
                                                        output_width=profile.spec.canvas_size,
                                                        output_height=profile.spec.canvas_size))
                else:
                    preview.write_bytes(render_png(icon))
            # Recorded only once every output exists, so a half-exported icon is
            # left out of the manifest and its files are pruned below.
            records.append(record)
        except (OSError, ValueError, TypeError, RuntimeError) as error:
            qa['status'] = 'error'
            qa['errors'].append(f'export: {type(error).__name__}: {error}')
            fail(icon, qa, qa['errors'], mtime)

    if only is not None:
        # Carried-over records went in first; restore canonical order so output stays byte-stable.
        order = {icon_id: index for index, icon_id in enumerate(factories())}
        records.sort(key=lambda record: order.get(record["icon_id"], len(order)))
    publish_metadata(records, target_dir, factories())
    publish_metadata(failed_records, failed_dir, factories())
    failed_records.sort(key=lambda entry: entry["icon_id"])
    (failed_dir / 'manifest.json').write_text(json.dumps({
        "manifest_version": MANIFEST_VERSION, "family": family, "profile": profile.name,
        "canvas_size": profile.spec.canvas_size, "count": len(failed_records), "icons": failed_records,
    }, indent=2) + "\n", encoding="utf-8")

    checked = len(icons) if only is not None else len(icons) - reused
    if previous is not None or only is not None:
        print(f"[{family}] {checked} of {checked + reused} icons checked; "
              f"{reused} {'others' if only is not None else 'unchanged since the last build'} reused")
    if failures:
        print(f"FAILED BUILD [{family}]: {len(failures)} of {checked} checked icons did not validate "
              f"-> {published_dist / 'failed' / folder}\n")
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


def _build_selected(families, dist, png_dir, **options):
    with output_lock(dist):
        if (Path(dist) / 'release.json').exists():
            raise ValueError('Cannot build into a production release. Build locally, then export a new release.')
        return _build_selected_locked(families, dist, png_dir, **options)


def _build_selected_locked(families, dist, png_dir, *, write_png, debug=False, report=True, rebuild_all=False, only=None,
                    qa_overlays=None, artwork_dir=None):
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
                qa_rows=qa_rows, qa_dir=qa_dir, debug=debug, previous=previous, only=only,
                qa_overlays=qa_overlays, artwork_dir=artwork_dir,
            ))
        if qa_dir is not None:
            # A filtered build still shows the complete current library. Only
            # selected families determine whether this release can be published.
            from icon_set.model.icons.registry import all_icons
            for icon in all_icons():
                if icon.family in families:
                    continue
                key = artifact_key(icon)
                # A targeted build keeps other icons' last rows rather than re-checking them.
                mtime = 0.0 if only is not None else _source_mtime(icon)
                row = previous.qa_row(key, mtime, selected=False) if previous else None
                if row is None:
                    row = inspect_icon(icon, debug_dir=qa_dir / key if debug else None, selected=False)
                    row['_key'] = key
                qa_rows.append(row)
            save_evidence(qa_rows, qa_dir, debug=debug, report=report)
            # Publish QA with the gallery and manifests in the same transaction.
        # Publish every family that exported something; failing icons are simply
        # left out. A family where nothing exported keeps its previous release.
        published = [family for family, (count, bad) in zip(families, counts) if count or not bad]
        replacements = [(stage / family_dist_name(family), root / family_dist_name(family))
                        for root, stage in stages.items() for family in published]
        # The failed-build list always reflects this run, even when a family kept its release.
        (dist / 'failed').mkdir(exist_ok=True)
        replacements += [(stages[dist] / 'failed' / family_dist_name(family), dist / 'failed' / family_dist_name(family))
                         for family in families]
        if qa_dir is not None:
            replacements.append((qa_dir, dist / 'qa'))
        gallery = stage_gallery(stages[dist], dist, [family_dist_name(name) for name in contracts.families()])
        replacements.append((gallery, dist / 'gallery'))
        _publish(replacements)
        if qa_dir is not None:
            print(f"QA evidence -> {dist / 'qa' / ('index.html' if report else 'results.json')}")
        print(f"Icon gallery -> {dist / 'gallery' / 'index.html'}")
    for family, (count, bad) in zip(families, counts):
        name = Profile.for_family(family).name
        if family not in published:
            print(f"[{family}] no icon exported; previous release kept -> {dist / family_dist_name(family)}")
            continue
        failed_note = f"; {bad} failed -> {dist / 'failed' / family_dist_name(family)}" if bad else ""
        print(f"[{family}] validated and exported {count} {name} icons "
              f"-> {dist / family_dist_name(family)}{failed_note}")
    failed = sum(bad for _, bad in counts)
    if failed:
        print(f"\n{failed} icon(s) failed validation; their SVGs and errors are in {dist / 'failed'} "
              f"and the gallery's Failed build tab.")
    return sum(count for count, _ in counts), failed


def build_family(
    family: str, dist: Path, png_dir: Path | None, *, write_png: bool,
    debug: bool = False, report: bool = True, rebuild_all: bool = False, qa_overlays: Path | None = None, artwork_dir: Path | None = None,
) -> tuple[int, int]:
    """Publish one family's passing icons; failing icons go to dist/failed and are counted."""
    return _build_selected([family], dist, png_dir, write_png=write_png, debug=debug, report=report,
                           rebuild_all=rebuild_all, qa_overlays=qa_overlays, artwork_dir=artwork_dir)


def build(
    dist: Path = DEFAULT_DIST, png_dir: Path | None = DEFAULT_PNG, *, write_png: bool = True,
    only: list[str] | None = None, debug: bool = False, report: bool = True,
    rebuild_all: bool = False, sources: list[Path] | None = None, qa_overlays: Path | None = None, artwork_dir: Path | None = None,
) -> int:
    families = list(contracts.families())
    if only:
        unknown = sorted(set(only) - set(families))
        if unknown:
            print(f"error: unknown family {unknown}; known: {families}", file=sys.stderr)
            return 2
        families = [name for name in families if name in only]
    selected = None
    if sources:
        wanted = {Path(source).resolve() for source in sources}
        by_path = {}
        for icon_id, factory in factories().items():
            filename = inspect.getsourcefile(factory)
            if filename and Path(filename).resolve() in wanted:
                by_path.setdefault(Path(filename).resolve(), []).append((icon_id, factory.family))
        missing = sorted(str(path) for path in wanted - set(by_path))
        if missing:
            print(f"error: no registered icon is defined in {missing}", file=sys.stderr)
            return 2
        selected = {icon_id for rows in by_path.values() for icon_id, _ in rows}
        icon_families = {family for rows in by_path.values() for _, family in rows}
        # Without --family, build just the families the selected icons belong to.
        families = [name for name in families if name in icon_families] if not only else families
    _, failed = _build_selected(families, dist, png_dir, write_png=write_png, debug=debug, report=report,
                                rebuild_all=rebuild_all, only=selected, qa_overlays=qa_overlays, artwork_dir=artwork_dir)
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
    parser.add_argument('--icon', dest='sources', action='append', type=Path, metavar='PYTHON_FILE',
                        help='check only the icons defined in this file (repeatable); every other icon '
                             'keeps its last built result unchecked, and the exit code covers these alone')
    parser.add_argument('--qa-overlays', type=Path, default=DEFAULT_QA_OVERLAYS, metavar='DIR',
                        help='qa_overlays.py results per family folder (DIR/solo48/...); icons whose saved '
                             'distance or hole check failed on the SVG being published go to the failed build '
                             f'(default: {DEFAULT_QA_OVERLAYS.relative_to(REPO_ROOT)})')
    parser.add_argument('--artwork-dir', type=Path, default=None,
                        help='Opt in to a manual-artwork export; default builds Python originals only')
    args = parser.parse_args(argv)
    try:
        return build(args.dist, args.png_dir, write_png=not args.no_png, only=args.family,
                     debug=args.debug, report=args.report, rebuild_all=args.rebuild_all, sources=args.sources,
                     qa_overlays=args.qa_overlays, artwork_dir=args.artwork_dir)
    except (OSError, ValueError) as error:
        parser.exit(2, f'error: {error}\n')


if __name__ == "__main__":
    raise SystemExit(main())
