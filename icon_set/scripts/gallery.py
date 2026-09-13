"""Generate a deterministic gallery from the manifests that will be published."""
import json
import hashlib
import inspect
import re
import sys
import shutil
from pathlib import Path
from urllib.parse import quote


REPO_ROOT = Path(__file__).resolve().parents[2]


def original_sources() -> dict[str, list[Path]]:
    """Use declared source paths/UUIDs only; never infer provenance from names."""
    from icon_set.model.icons.registry import factories
    primitives = (REPO_ROOT / 'pictographic-primitives').resolve()
    if not primitives.is_dir():
        return {}
    declared = {}
    missing_ids = set()
    for icon_id, factory in factories().items():
        module = sys.modules[factory.__module__]
        refs = [(getattr(module, 'SOURCE_ICON_ID', None), getattr(module, 'SOURCE_PATH', None))]
        refs += list(getattr(module, 'SOURCE_REFERENCES', ()))
        paths = []
        ids = set()
        for uid, source in refs:
            if uid:
                ids.add(uid.lower())
            if source:
                path = (REPO_ROOT / source).resolve()
                for candidate in (path, path.with_suffix('.svg'), path.with_suffix('.png')):
                    if candidate.is_relative_to(primitives) and candidate.suffix.lower() in ('.svg', '.png') and candidate.is_file():
                        paths.append(candidate)
        declared[icon_id] = (paths, ids)
        missing_ids.update(ids)
    # Match UUIDs even when original folders have moved, and include PNG siblings.
    by_id = {}
    uuid = re.compile(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}', re.I)
    if missing_ids:
        for path in primitives.rglob('*'):
            if path.suffix.lower() not in ('.svg', '.png') or not path.is_file():
                continue
            match = uuid.search(path.stem)
            if match and match[0].lower() in missing_ids and path.resolve().is_relative_to(primitives):
                by_id.setdefault(match[0].lower(), []).append(path.resolve())
    result = {}
    for icon_id, (paths, ids) in declared.items():
        for uid in sorted(ids):
            paths.extend(by_id.get(uid, []))
        # Multiple batch folders can contain identical copies of the same original.
        seen = set()
        selected = []
        for path in sorted(set(paths), key=lambda p: (p.suffix.lower() != '.svg', str(p))):
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest not in seen:
                seen.add(digest)
                selected.append(path)
        result[icon_id] = selected
    return result


def copy_originals(paths: list[Path], target: Path) -> list[dict]:
    rows = []
    for source in paths:
        content = source.read_bytes()
        name = hashlib.sha256(content).hexdigest() + source.suffix.lower()
        destination = target / 'originals' / name
        destination.parent.mkdir(exist_ok=True)
        if not destination.exists():
            destination.write_bytes(content)
        rows.append({'url': 'originals/' + name, 'format': source.suffix[1:].upper(),
                     'source_path': source.relative_to(REPO_ROOT).as_posix()})
    return rows


def python_sources() -> dict[str, dict]:
    """Include registered authoring file locations, without publishing source code."""
    from icon_set.model.icons.registry import factories
    result = {}
    for icon_id, factory in factories().items():
        filename = inspect.getsourcefile(factory)
        if not filename:
            continue
        path = Path(filename).resolve()
        if not path.is_relative_to(REPO_ROOT) or not path.is_file():
            continue
        result[icon_id] = {'path': path.relative_to(REPO_ROOT).as_posix(),
                           'family': factory.family, 'class_name': factory.__name__}
    return result


def stage_laboratory(target: Path) -> None:
    """Publish the learning page with the same contracts used by the builder."""
    from icon_set.model import contracts
    templates = Path(__file__).with_name('templates')
    for name in ('icon-laboratory.html', 'icon-laboratory.css', 'icon-laboratory.js'):
        shutil.copyfile(templates / name, target / name)
    data = {'profile': contracts.icon_profile(), 'keyshapes': contracts.keyshapes()}
    (target / 'laboratory.json').write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def stage_gallery(staged: Path, published: Path, folders: list[str]) -> Path:
    target = staged / 'gallery'
    target.mkdir()
    records = []
    sources = original_sources()
    authoring = python_sources()
    from icon_set.model.icons.registry import factories
    registered = factories()
    for folder in folders:
        manifest = staged / folder / 'manifest.json'
        if not manifest.exists():
            manifest = published / folder / 'manifest.json'
        if not manifest.exists():
            continue
        for record in json.loads(manifest.read_text(encoding='utf-8'))['icons']:
            record = dict(record)
            record['key'] = record['family'] + '/' + record['icon_id']
            record['preview_url'] = '../' + quote(folder, safe='') + '/' + quote(record['icon_id'], safe='') + '.svg'
            record['original_sources'] = copy_originals(sources.get(record['icon_id'], []), target)
            record['python_source'] = authoring.get(record['icon_id'])
            factory = registered.get(record['icon_id'])
            if factory is not None:
                record['variant_of'] = getattr(factory, 'variant_of', None)
                record['variant_label'] = getattr(factory, 'variant_label', '')
                ancestor = factory
                while getattr(ancestor, 'variant_of', None):
                    ancestor = registered[ancestor.variant_of]
                record['variant_root'] = ancestor.icon_id
            records.append(record)
    records.sort(key=lambda item: (item['family'], item['icon_id']))
    (target / 'icons.json').write_text(json.dumps({'icons': records}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    shutil.copyfile(Path(__file__).with_name('templates') / 'gallery.html', target / 'index.html')
    shutil.copyfile(Path(__file__).with_name('templates') / 'generate.html', target / 'generate.html')
    shutil.copyfile(Path(__file__).with_name('templates') / 'icon-canvas.css', target / 'icon-canvas.css')
    stage_laboratory(target)
    return target
