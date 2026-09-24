#!/usr/bin/env python3
"""Register icons drawn by the folder-only skills so the gallery can count them.

side-main-make-thuan and side-sub-make-thuan save each drawing in
``icon_set/work/<skill>/<source-uuid>/<run>/`` and never touch the registry, so
the side-mains and side-subs pages keep showing those sources as missing until
the module is copied into ``icon_set/model/icons/<family>/`` and a build runs.
This script does that step: for every source it takes the newest run whose
result.json says ``valid``, rewrites the module's imports to the relative form
the model tree uses, and copies it in. A source with no valid run is left
alone. A source already promoted (a run carries promoted.json) is left alone
unless a valid run was created after that promotion (its result.json is newer
than promoted_at and its recorded build gate did not fail): that run is a
repair, so it replaces the module in the tree under the same icon_id and
takes over promoted.json.

An icon id already owned by another family gets the ``-<family>`` suffix, so a
solo main drawn for a source that also has a container icon becomes
``<id>-solo``. Pass --no-suffix to skip those instead.

Note the skills validate with ``validate_icon()`` only; the build also runs the
hole/pinch and internal-spacing gates, so some promoted icons land in the
Failing bucket rather than Done. --strict runs those gates first and skips
icons that would fail, reporting them. --include-invalid promotes the newest
run of a source that has no valid run, so it counts as a build failure (and can
be fixed in the model tree) instead of staying folder-only.

    python3 icon_set/scripts/promote_work_icons.py --dry-run      # what would be promoted
    python3 icon_set/scripts/promote_work_icons.py --build        # promote, then build --changed-only
    python3 icon_set/scripts/promote_work_icons.py --skill side-sub-make-thuan --build
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

WORK = REPO_ROOT / 'icon_set' / 'work'
MODELS = REPO_ROOT / 'icon_set' / 'model' / 'icons'
SKILLS = {  # work folder -> (family, base class)
    'side-main-make-thuan': ('solo', 'Solo48'),
    'side-sub-make-thuan': ('sub', 'Sub32'),
    'primitive-make-ray': ('solo', 'Solo48'),
}
ICON_ID = re.compile(r'''^(\s*)icon_id\s*=\s*(['"])([^'"]+)\2''', re.MULTILINE)


def _relative_imports(text: str, family: str, base: str) -> str:
    text = text.replace('from icon_set.model.keyshapes import Keyshape', 'from ...keyshapes import Keyshape')
    text = text.replace(f'from icon_set.model.icons.{family}._base import {base}', f'from ._base import {base}')
    return text


def _icon_module(run: Path, source_dir: Path) -> Path | None:
    """The run's icon module: the one result.json names, else the only .py, else the one named after the source uuid."""
    try:
        named = json.loads((run / 'result.json').read_text(encoding='utf-8')).get('module')
    except (OSError, ValueError, AttributeError):
        named = None
    if isinstance(named, str) and Path(named).name == named and (run / named).is_file():
        return run / named
    modules = [p for p in run.glob('*.py') if not p.name.startswith('.')]
    if len(modules) == 1:
        return modules[0]
    stem = source_dir.name.replace('-', '_').lower()
    named = [p for p in modules if stem in p.name.lower()]
    return named[0] if len(named) == 1 else None


def _latest_valid_run(source_dir: Path, include_invalid: bool = False) -> Path | None:
    """The newest valid run; with include_invalid, fall back to the newest run of any status."""
    runs, others = [], []
    for run in source_dir.iterdir():
        result = run / 'result.json'
        if not result.is_file():
            continue
        try:
            data = json.loads(result.read_text(encoding='utf-8'))
        except ValueError:
            continue
        if _icon_module(run, source_dir) is None:
            continue
        (runs if data.get('validation_status') == 'valid' else others).append(run)
    if not runs and include_invalid:
        runs = others
    return max(runs, key=lambda run: run.name) if runs else None


def _repair_after_promotion(source_dir: Path) -> tuple[Path, Path, dict] | None:
    """A valid run created after the source's promotion: (repair run, old promoted.json, its data).

    A run counts as created when its result.json was written. A run whose recorded
    build gate failed is not a repair and is left alone.
    """
    marker = next(source_dir.glob('*/promoted.json'), None)
    if marker is None:
        return None
    try:
        promoted = json.loads(marker.read_text(encoding='utf-8'))
        promoted_at = datetime.fromisoformat(promoted['promoted_at']).timestamp()
    except (OSError, ValueError, KeyError, TypeError):
        return None
    repairs = []
    for run in source_dir.iterdir():
        result = run / 'result.json'
        if run == marker.parent or not result.is_file() or result.stat().st_mtime <= promoted_at:
            continue
        try:
            data = json.loads(result.read_text(encoding='utf-8'))
        except ValueError:
            continue
        gate = data.get('build_gate')
        gate = gate.get('status') if isinstance(gate, dict) else gate
        if data.get('validation_status') == 'valid' and gate != 'fail' and _icon_module(run, source_dir) is not None:
            repairs.append((result.stat().st_mtime, run))
    return (max(repairs)[1], marker, promoted) if repairs else None


def _promote_repair(source_dir: Path, family: str, base: str, *, dry_run: bool) -> tuple[str, str] | None:
    """Replace an already promoted module with its newer repair, keeping the published icon_id."""
    found = _repair_after_promotion(source_dir)
    if found is None:
        return None
    run, marker, promoted = found
    target = REPO_ROOT / promoted['module']
    if not target.is_file():
        return None
    current = ICON_ID.search(target.read_text(encoding='utf-8'))
    text = _icon_module(run, source_dir).read_text(encoding='utf-8')
    match = ICON_ID.search(text)
    if current is None or match is None:
        return None
    icon_id = current[3]
    text = _relative_imports(text[:match.start(3)] + icon_id + text[match.end(3):], family, base)
    if not dry_run:
        now = datetime.now(timezone.utc).isoformat()
        target.write_text(text, encoding='utf-8')
        (marker.parent / 'promoted.superseded.json').write_text(json.dumps(
            {**promoted, 'superseded_by': run.name, 'superseded_at': now}, indent=2) + '\n', encoding='utf-8')
        marker.unlink()
        (run / 'promoted.json').write_text(json.dumps({
            'icon_id': icon_id, 'module': promoted['module'], 'promoted_at': now, 'replaces_run': marker.parent.name,
        }, indent=2) + '\n', encoding='utf-8')
    return icon_id, promoted['module']


def _strict_ok(module_path: Path, icon_id: str) -> list[str]:
    """The build's own findings for a module, so a failing icon can be held back."""
    import importlib.util
    from icon_set.validation.library_qa import inspect_icon
    spec = importlib.util.spec_from_file_location(f'_promote_{module_path.stem}', module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    for value in vars(module).values():
        if isinstance(value, type) and getattr(value, 'icon_id', None) == icon_id:
            qa = inspect_icon(value())
            return [] if qa['status'] == 'pass' else (qa['errors'] or qa['warnings'] or ['failed'])
    return [f'no class with icon_id {icon_id!r}']


def promote(skills: list[str], *, dry_run: bool, suffix: bool, strict: bool, only: list[str] | None = None,
            include_invalid: bool = False) -> dict:
    from icon_set.model.icons.registry import factories
    registered = factories()
    report = {'promoted': [], 'replaced': [], 'skipped': [], 'held': [], 'families': set()}
    taken = set(registered)  # ids owned by the tree plus those promoted earlier in this run
    for skill in skills:
        family, base = SKILLS[skill]
        root = WORK / skill
        if not root.is_dir():
            continue
        target_dir = MODELS / family
        for source_dir in sorted(p for p in root.iterdir() if p.is_dir()):
            if only and not any(source_dir.name.lower().startswith(prefix) for prefix in only):
                continue
            if any(source_dir.glob('*/promoted.json')):
                # One promoted drawing per source; a valid run created after it is a repair and replaces it.
                replaced = _promote_repair(source_dir, family, base, dry_run=dry_run)
                if replaced is not None:
                    report['replaced'].append((source_dir.name, *replaced))
                    report['families'].add(family)
                continue
            run = _latest_valid_run(source_dir, include_invalid)
            if run is None:
                report['skipped'].append((source_dir.name, 'no valid run'))
                continue
            module = _icon_module(run, source_dir)
            target = target_dir / module.name
            if (run / 'promoted.json').is_file() or target.is_file():
                continue
            # Rename on the original text; the strict check imports it standalone, so the
            # package-relative rewrite happens only for the copy that lands in the tree.
            text = module.read_text(encoding='utf-8')
            match = ICON_ID.search(text)
            if match is None:
                report['skipped'].append((source_dir.name, f'{module.name}: no icon_id'))
                continue
            icon_id = match[3]
            if icon_id in taken:
                owner = registered.get(icon_id)
                where = f'registered in {owner.family}' if owner is not None else 'promoted from another run in this batch'
                # A clash inside this batch is two sources naming the same subject; the uuid tells them apart.
                new_id = f'{icon_id}-{family}' if owner is not None else f'{icon_id}-{source_dir.name[:8].lower()}'
                if new_id in taken:
                    new_id = f'{icon_id}-{source_dir.name[:8].lower()}'
                if not suffix or new_id in taken:
                    report['skipped'].append((source_dir.name, f'{icon_id} already {where}; rename the icon_id in {module.name}'))
                    continue
                text = text[:match.start(3)] + new_id + text[match.end(3):]
                icon_id = new_id
            if strict:
                # Check the copy as the build will see it, in a scratch location.
                scratch = run / f'.strict-{module.name}'
                scratch.write_text(text, encoding='utf-8')  # absolute imports, loadable from anywhere
                try:
                    findings = _strict_ok(scratch, icon_id)
                finally:
                    scratch.unlink(missing_ok=True)
                if findings:
                    report['held'].append((source_dir.name, icon_id, findings[0]))
                    continue
            taken.add(icon_id)
            text = _relative_imports(text, family, base)
            report['promoted'].append((source_dir.name, icon_id, str(target.relative_to(REPO_ROOT))))
            report['families'].add(family)
            if dry_run:
                continue
            target.write_text(text, encoding='utf-8')
            (run / 'promoted.json').write_text(json.dumps({
                'icon_id': icon_id, 'module': str(target.relative_to(REPO_ROOT)),
                'promoted_at': datetime.now(timezone.utc).isoformat(),
            }, indent=2) + '\n', encoding='utf-8')
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--skill', action='append', choices=sorted(SKILLS), metavar='WORK_FOLDER',
                        help='work folder to promote from (repeatable); default: side-main-make-thuan and side-sub-make-thuan')
    parser.add_argument('--dry-run', action='store_true', help='report only; copy nothing')
    parser.add_argument('--no-suffix', dest='suffix', action='store_false',
                        help='skip icons whose id another family already owns instead of adding -<family>')
    parser.add_argument('--strict', action='store_true',
                        help="run the build's hole/pinch and spacing gates first and hold back icons that fail them")
    parser.add_argument('--build', action='store_true', help='after promoting, run build.py --changed-only for the touched families')
    parser.add_argument('--include-invalid', action='store_true',
                        help='for a source with no valid run, promote its newest run anyway; it builds into the Failed bucket')
    parser.add_argument('--only', action='append', metavar='UUID_PREFIX',
                        help='promote only source folders whose uuid starts with this (repeatable)')
    args = parser.parse_args(argv)
    skills = args.skill or ['side-main-make-thuan', 'side-sub-make-thuan']

    report = promote(skills, dry_run=args.dry_run, suffix=args.suffix, strict=args.strict,
                     only=[p.lower() for p in args.only] if args.only else None,
                     include_invalid=args.include_invalid)
    verb = 'would promote' if args.dry_run else 'promoted'
    print(f"{verb} {len(report['promoted'])} icon(s)")
    for source, icon_id, path in report['promoted']:
        print(f"  {source[:8]}  {icon_id}  -> {path}")
    if report['replaced']:
        print(f"{'would replace' if args.dry_run else 'replaced'} {len(report['replaced'])} promoted icon(s) with a newer repair run")
        for source, icon_id, path in report['replaced']:
            print(f"  {source[:8]}  {icon_id}  -> {path}")
    for source, icon_id, finding in report['held']:
        print(f"  held {source[:8]}  {icon_id}: {finding}")
    for source, reason in report['skipped']:
        if reason != 'no valid run':
            print(f"  skipped {source[:8]}: {reason}")
    quiet = sum(reason == 'no valid run' for _, reason in report['skipped'])
    if quiet:
        print(f"  {quiet} source folder(s) have no valid run yet")

    changed = report['promoted'] or report['replaced']
    if args.build and changed and not args.dry_run:
        command = [sys.executable, str(REPO_ROOT / 'icon_set' / 'scripts' / 'build.py'), '--changed-only']
        for family in sorted(report['families']):
            command += ['--family', family]
        print('$', ' '.join(command[1:]), flush=True)
        return subprocess.call(command, cwd=REPO_ROOT)
    if changed and not args.dry_run:
        families = ' '.join(f'--family {f}' for f in sorted(report['families']))
        print(f"now run: python3 icon_set/scripts/build.py {families} --changed-only")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
