#!/usr/bin/env python3
"""Build a portable original / Python model / exported SVG review report.

python3 icon_set/scripts/category_report.py computers
python3 icon_set/scripts/category_report.py computers culture --full-qa
python3 icon_set/scripts/category_report.py --all

Read-only with respect to icons, sources and dist. Reports are snapshots, never
builds. Exact source identity takes precedence over manifest names; no fuzzy
matching. See category_report.md for details.
"""
from __future__ import annotations

import argparse
import base64
import collections
import csv
import hashlib
import inspect
import json
from pathlib import Path
import re
import sys
from datetime import datetime, timezone

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

UUID = re.compile(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}', re.I)


def source_id(path: Path) -> str | None:
    match = UUID.search(path.stem)
    return match[0].lower() if match else None


def path_label(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def data_url(data: bytes, mime: str) -> str:
    return f'data:{mime};base64,' + base64.b64encode(data).decode()


def preview(svg: str, size: int = 192) -> str:
    # Render the complete SVG document: extracting inner markup loses inherited
    # fill/stroke rules and makes some original screens appear solid black.
    import cairosvg
    return data_url(cairosvg.svg2png(bytestring=svg.encode(), output_width=size,
                                   output_height=size, background_color='white'), 'image/png')


def discover_sources(folder: Path, global_metadata: dict | None = None) -> list[dict]:
    metadata = dict(global_metadata or {})
    for manifest in sorted(folder.rglob('manifest.json'), key=lambda p: len(p.parts)):
        try:
            contents = json.loads(manifest.read_text())
            entries = contents if isinstance(contents, list) else contents.get('icons', [])
            for item in entries:
                key = source_id(Path(item.get('file', ''))) or item.get('file')
                if key:
                    metadata[key] = {**metadata.get(key, {}), **item}
        except (ValueError, AttributeError, TypeError) as error:
            raise ValueError(f'{manifest}: invalid manifest: {error}') from error
    grouped = collections.defaultdict(list)
    for path in sorted(folder.rglob('*.svg')):
        # Files without IDs are distinct, even if their basenames are equal.
        grouped[source_id(path) or path.relative_to(folder).as_posix()].append(path)
    rows = []
    for key, paths in grouped.items():
        paths.sort(key=lambda p: (len(p.parts), p.as_posix()))
        info = metadata.get(key, {})
        path = paths[0]
        title = info.get('concept') or UUID.sub('', path.stem).strip(' _-').replace('_', ' ').title()
        batch = info.get('batch') or next((part for p in paths for part in p.parts if part.startswith('batch-')), 'Unbatched')
        rows.append(dict(source_id=source_id(path), identity=key, paths=paths,
                         title=title, batch=batch, category=folder.name,
                         description=info.get('description', ''), tags=info.get('tags', []),
                         proposed_icon_id=info.get('icon_id'), proposed_family=info.get('family')))
    return sorted(rows, key=lambda r: (r['batch'], r['title'], r['identity']))


def model_catalog() -> list[dict]:
    from icon_set.model.icons.registry import factories
    records = []
    for icon_id, factory in factories().items():
        module = sys.modules[factory.__module__]
        source = getattr(module, 'SOURCE_PATH', None)
        references = getattr(module, 'SOURCE_REFERENCES', ())
        records.append(dict(icon_id=icon_id, factory=factory,
                            source_id=getattr(module, 'SOURCE_ICON_ID', None),
                            source_path=(REPO_ROOT / source).resolve() if source else None,
                            source_references=[
                                (uid.lower() if uid else None,
                                 (REPO_ROOT / path).resolve() if path else None)
                                for uid, path in references
                            ],
                            module_path=Path(inspect.getfile(factory)).resolve(),
                            family=factory.family))
    return records


def match_models(source: dict, models: list[dict]) -> tuple[list[dict], str]:
    uid = source['source_id']
    if uid:
        matches = [m for m in models if (m['source_id'] or '').lower() == uid]
        if matches:
            return matches, 'source ID'
        matches = [m for m in models if any(
            reference_id == uid for reference_id, _ in m.get('source_references', ())
        )]
        if matches:
            return matches, 'declared source reuse'
    paths = {p.resolve() for p in source['paths']}
    matches = [m for m in models if m['source_path'] in paths and
               (not uid or not m['source_id'] or m['source_id'].lower() == uid)]
    if matches:
        return matches, 'source path'
    matches = [m for m in models if any(
        path in paths and (not uid or not reference_id or reference_id == uid)
        for reference_id, path in m.get('source_references', ())
    )]
    if matches:
        return matches, 'declared source reuse'
    # Support older modules without identity metadata, but never override a
    # conflicting explicit identity just because an icon has a similar name.
    matches = [m for m in models if source['proposed_icon_id'] == m['icon_id'] and
               not m['source_id'] and not m['source_path'] and not m.get('source_references')]
    return matches, 'manifest name' if matches else 'unmatched'


def export_state(current: str, exported: str | None, record: dict | None) -> str:
    if exported is None:
        return 'missing'
    if exported != current:
        return 'stale'
    if record is None or record.get('svg_sha256') != digest(exported):
        return 'manifest mismatch'
    return 'current'


def load_export_manifests(dist: Path) -> dict:
    result = {}
    for path in dist.glob('*/manifest.json'):
        for row in json.loads(path.read_text()).get('icons', []):
            result[(path.parent.name, row['icon_id'])] = row
    return result


def build_rows(sources: list[dict], models: list[dict], dist: Path,
               manifests: dict, full_qa: bool = False) -> list[dict]:
    from icon_set.model import contracts
    from icon_set.validation.library_qa import inspect_icon
    rows = []
    for source in sources:
        matches, method = match_models(source, models)
        for model in matches or [None]:
            linked_paths = ({model['source_path']} | {p for _, p in model.get('source_references', ())}) if model else set()
            selected = next((p for p in source['paths'] if p.resolve() in linked_paths), source['paths'][0])
            row = {k: v for k, v in source.items() if k != 'paths'}
            row.update(source_path=path_label(selected), source_copies=[path_label(p) for p in source['paths']],
                       match_method=method, icon_id=model['icon_id'] if model else None,
                       family=model['family'] if model else None, status='pending',
                       reused=method == 'declared source reuse',
                       model_source_id=model['source_id'] if model else None,
                       export_state='not checked', findings=[], qa_level='model validation',
                       key=source['category'] + ':' + source['identity'] + ':' + (model['icon_id'] if model else 'pending'))
            try:
                original = selected.read_text()
                row.update(original_svg=data_url(original.encode(), 'image/svg+xml'), original_preview=preview(original), source_sha256=digest(original))
                if len({digest(p.read_text()) for p in source['paths']}) > 1:
                    row['findings'].append('Multiple source files carry this ID but have different contents; showing the model-linked path when available.')
            except Exception as error:
                row['findings'].append(f'Original could not be rendered: {error}')
                row['status'] = 'error'
            if model:
                row.update(module_path=path_label(model['module_path']), python_code=model['module_path'].read_text())
                try:
                    icon = model['factory']()
                    current = icon.to_svg()
                    validation = icon.validate_icon()
                    row.update(profile=icon.profile.name, canvas=icon.profile.spec.canvas_size,
                               keyshape=icon.keyshape.name, validation=validation.status,
                               model_preview=preview(current), model_svg=data_url(current.encode(), 'image/svg+xml'),
                               model_sha256=digest(current), author_notes=inspect.getmodule(model['factory']).__doc__ or '')
                    if validation.status != 'valid':
                        row['findings'].append(validation.describe())
                    if full_qa:
                        qa = inspect_icon(icon)
                        row['qa_level'] = 'model validation + holes/pinches'
                        row['qa_status'] = qa['status']
                        row['findings'].extend(qa['errors'] + qa['warnings'])
                    folder = Path(contracts.families()[icon.family]['dist']).name
                    path = dist / folder / f'{icon.icon_id}.svg'
                    exported = path.read_text() if path.is_file() else None
                    record = manifests.get((folder, icon.icon_id))
                    row.update(export_path=path_label(path), export_state=export_state(current, exported, record))
                    if exported is not None:
                        row.update(export_preview=preview(exported), export_svg=data_url(exported.encode(), 'image/svg+xml'), export_sha256=digest(exported))
                    if row['export_state'] != 'current':
                        row['findings'].append('Export: ' + row['export_state'] + '. Run the family build to refresh published artifacts.')
                    row['status'] = 'attention' if row['findings'] else 'ready'
                except Exception as error:
                    row['status'] = 'error'
                    row['findings'].append(f'Model/export inspection failed: {type(error).__name__}: {error}')
            rows.append(row)
    return rows


def render_html(report: dict) -> str:
    template = (Path(__file__).parent / 'templates/category_report.html').read_text()
    # Do not let source descriptions or Python strings terminate the JSON tag.
    payload = json.dumps(report, ensure_ascii=False).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')
    return template.replace('__REPORT_DATA__', payload)


def generate(categories: list[Path], out: Path, source_root: Path, dist: Path,
             full_qa: bool = False) -> dict:
    global_metadata = {}
    master = source_root / '_manifest.csv'
    if master.exists():
        with master.open(newline='') as handle:
            for row in csv.DictReader(handle):
                global_metadata[row['id']] = row
    models = model_catalog()
    manifests = load_export_manifests(dist)
    rows = []
    for category in categories:
        sources = discover_sources(category, global_metadata)
        print(f'Inspecting {category.name}: {len(sources)} originals', flush=True)
        rows.extend(build_rows(sources, models, dist, manifests, full_qa))
    counts = dict(collections.Counter(r['status'] for r in rows))
    groups = collections.defaultdict(list)
    for row in rows:
        if row['icon_id']:
            groups[row['icon_id']].append(row['source_id'] or row['identity'])
    for row in rows:
        row['shared_source_ids'] = groups.get(row['icon_id'], [])
    report = dict(version=1, generated_at=datetime.now(timezone.utc).isoformat(),
                  title=categories[0].name.replace('-', ' ').title() if len(categories) == 1 else 'All selected categories',
                  categories=[p.name for p in categories], counts=counts, rows=rows,
                  model_count=len(groups), reused_count=sum(r['reused'] for r in rows),
                  source_count=len({(r['category'], r['identity']) for r in rows}),
                  full_qa=full_qa)
    out.mkdir(parents=True, exist_ok=True)
    (out / 'index.html').write_text(render_html(report))
    # Compact, machine-readable inventory; previews and full code live in HTML.
    inventory = {**report, 'rows': [{k: v for k, v in r.items() if not k.endswith(('_preview', '_svg')) and k != 'python_code'} for r in rows]}
    (out / 'report.json').write_text(json.dumps(inventory, indent=2) + '\n')
    print(f'Report: {out / "index.html"}\n{counts}', flush=True)
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('categories', nargs='*', help='Category names or category directory paths')
    parser.add_argument('--all', action='store_true', help='Include every source category, including pending icons')
    parser.add_argument('--source-root', type=Path, default=REPO_ROOT / 'pictographic-primitives')
    parser.add_argument('--dist', type=Path, default=REPO_ROOT / 'icon_set/dist')
    parser.add_argument('--out', type=Path, help='Output folder; default work/reports/<category or all>')
    parser.add_argument('--full-qa', action='store_true', help='Also run hole/pinch checks (slower)')
    args = parser.parse_args(argv)
    if args.all == bool(args.categories):
        parser.error('Choose category names/paths or --all.')
    categories = sorted(p for p in args.source_root.iterdir() if p.is_dir()) if args.all else [Path(c) if Path(c).is_dir() else args.source_root / c for c in args.categories]
    categories = list(dict.fromkeys(p.resolve() for p in categories))
    for category in categories:
        if not category.is_dir():
            parser.error(f'Category does not exist: {category}')
    if not categories:
        parser.error('No categories found.')
    out = args.out or REPO_ROOT / 'work/reports' / (categories[0].name if len(categories) == 1 else 'all')
    generate(categories, out, args.source_root, args.dist, args.full_qa)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
