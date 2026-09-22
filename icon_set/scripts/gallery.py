"""Generate a deterministic gallery from the manifests that will be published."""
import json
import hashlib
import inspect
import re
import sys
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote


REPO_ROOT = Path(__file__).resolve().parents[2]


def stage_review_facets(records: list[dict], staged: Path, published: Path, target: Path) -> None:
    """Expose small, revision-checked symmetry measurements for gallery filtering."""
    facets = {}
    for record in records:
        relative = Path('qa') / record['family'] / record['icon_id'] / 'metrics.json'
        for root in (staged, published):
            try:
                metrics = json.loads((root / relative).read_text(encoding='utf-8'))
            except (OSError, ValueError):
                continue
            if metrics.get('svg_sha256') != record.get('svg_sha256'):
                continue
            axes = metrics.get('symmetry', {}).get('axes', [])
            if not {'vertical', 'horizontal'} <= {axis.get('axis') for axis in axes}:
                continue
            facets[record['key']] = {
                'svg_sha256': record['svg_sha256'],
                'axes': [axis['axis'] for axis in axes
                         if axis.get('ink_symmetric') and axis.get('status') == 'pass'],
            }
            break
    (target / 'review-facets.json').write_text(
        json.dumps(facets, ensure_ascii=False, sort_keys=True) + '\n', encoding='utf-8')


def add_creation_times(records: list[dict], published: Path) -> None:
    """Persist first-known source dates so rebuilding/deploying does not reorder icons."""
    previous = published / 'gallery' / 'icons.json'
    saved = json.loads(previous.read_text()) if previous.is_file() else {}
    known = {row['key']: row for row in saved.get('icons', []) + saved.get('failed_icons', [])}
    dates = {}
    try:
        history = subprocess.run(
            ['git', 'log', '--format=@%ct', '--name-only', '--diff-filter=A', '--', 'icon_set/model/icons'],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True, timeout=30).stdout
        timestamp = None
        for line in history.splitlines():
            if line.startswith('@'):
                timestamp = datetime.fromtimestamp(int(line[1:]), timezone.utc).isoformat()
            elif line and timestamp:
                dates[line] = timestamp
    except (OSError, subprocess.SubprocessError, ValueError):
        pass  # Existing published dates remain usable without Git on production.
    for row in records:
        old = known.get(row['key'], {})
        if old.get('created_at'):
            row['created_at'] = old['created_at']
            row['created_at_source'] = old.get('created_at_source', 'recorded')
            continue
        source = (row.get('python_source') or {}).get('path')
        if source in dates:
            row['created_at'] = dates[source]
            row['created_at_source'] = 'source-first-commit'
        elif source and (REPO_ROOT / source).is_file():
            stat = (REPO_ROOT / source).stat()
            birth = getattr(stat, 'st_birthtime', None)
            row['created_at'] = datetime.fromtimestamp(birth or stat.st_mtime, timezone.utc).isoformat()
            row['created_at_source'] = 'source-created' if birth else 'source-modified-fallback'


def add_modification_times(records: list[dict], published: Path) -> None:
    """Keep modification dates for identical content, including after a fresh checkout."""
    previous = published / 'gallery' / 'icons.json'
    saved = json.loads(previous.read_text()) if previous.is_file() else {}
    known = {row['key']: row for row in saved.get('icons', []) + saved.get('failed_icons', [])}
    dates, dirty = {}, set()
    try:
        history = subprocess.run(
            ['git', 'log', '--format=@%ct', '--name-only', '--', 'icon_set/model/icons'],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True, timeout=30).stdout
        timestamp = None
        for line in history.splitlines():
            if line.startswith('@'):
                timestamp = datetime.fromtimestamp(int(line[1:]), timezone.utc).isoformat()
            elif line and timestamp:
                dates.setdefault(line, timestamp)
        dirty = set(subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD', '--', 'icon_set/model/icons'],
            cwd=REPO_ROOT, capture_output=True, text=True, check=True, timeout=30).stdout.splitlines())
    except (OSError, subprocess.SubprocessError, ValueError):
        dates = {}
    for row in records:
        old = known.get(row['key'], {})
        source = (row.get('python_source') or {}).get('path')
        path = REPO_ROOT / source if source else None
        digest = hashlib.sha256(path.read_bytes()).hexdigest() if path and path.is_file() else None
        if (old.get('modified_at') and old.get('modified_source_sha256') == digest
                and old.get('svg_sha256') == row.get('svg_sha256')):
            row['modified_at'] = old['modified_at']
            row['modified_at_source'] = old.get('modified_at_source', 'recorded')
        elif (old.get('modified_at') and old.get('modified_source_sha256') == digest
                and old.get('svg_sha256') != row.get('svg_sha256')):
            row['modified_at'] = datetime.now(timezone.utc).isoformat()
            row['modified_at_source'] = 'changed-svg-build'
        elif source in dates and source not in dirty:
            row['modified_at'] = dates[source]
            row['modified_at_source'] = 'source-last-commit'
        elif digest:
            row['modified_at'] = datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat()
            row['modified_at_source'] = 'source-modified'
        if digest:
            row['modified_source_sha256'] = digest


def original_sources(only=None) -> dict[str, list[Path]]:
    """Use declared source paths/UUIDs only; never infer provenance from names."""
    from icon_set.model.icons.registry import factories
    primitives = (REPO_ROOT / 'pictographic-primitives').resolve()
    if not primitives.is_dir():
        return {}
    declared = {}
    missing_ids = set()
    for icon_id, factory in factories().items():
        if only is not None and icon_id not in only:
            continue
        module = sys.modules[factory.__module__]
        refs = [(getattr(module, 'SOURCE_ICON_ID', None), getattr(module, 'SOURCE_PATH', None))]
        for entry in getattr(module, 'SOURCE_REFERENCES', None) or ():
            # Entries are (uid, path) pairs or dicts keyed source_icon_id/source_path in any case.
            if isinstance(entry, dict):
                entry = {str(key).lower(): value for key, value in entry.items()}
                refs.append((entry.get('source_icon_id'), entry.get('source_path')))
            elif isinstance(entry, (tuple, list)) and len(entry) == 2:
                refs.append(tuple(entry))
        paths = []
        ids = set()
        for uid, source in refs:
            for value in (uid if isinstance(uid, (tuple, list)) else (uid,)):
                if value:
                    ids.add(value.lower())
            for source in (source if isinstance(source, (tuple, list)) else (source,)):
                if not source:
                    continue
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
        # Collapse batch copies of one reference, not distinct reference IDs
        # whose artwork happens to be identical. Every source identity must
        # remain visible on the linked icon's provenance list.
        seen = set()
        selected = []
        for path in sorted(set(paths), key=lambda p: (p.suffix.lower() != '.svg', str(p))):
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            match = uuid.search(path.stem)
            identity = (match[0].lower() if match else str(path), digest)
            if identity not in seen:
                seen.add(identity)
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


def python_sources(only=None) -> dict[str, dict]:
    """Include registered authoring file locations, without publishing source code."""
    from icon_set.model.icons.registry import factories
    result = {}
    for icon_id, factory in factories().items():
        if only is not None and icon_id not in only:
            continue
        filename = inspect.getsourcefile(factory)
        if not filename:
            continue
        path = Path(filename).resolve()
        if not path.is_relative_to(REPO_ROOT) or not path.is_file():
            continue
        result[icon_id] = {'path': path.relative_to(REPO_ROOT).as_posix(),
                           'family': factory.family, 'class_name': factory.__name__}
    return result


def stage_preview(target: Path, records: list[dict]) -> None:
    """Ship lightweight library metadata for the editable usage examples."""
    icons = [{key: row.get(key, '') for key in
              ('icon_id', 'name', 'family', 'preview_url', 'category')}
             for row in records]
    (target / 'preview-icons.json').write_text(
        json.dumps({'icons': icons}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    templates = Path(__file__).with_name('templates')
    for name in ('preview.html', 'preview.css', 'preview.js', 'preview-scene.html',
                 'preview-scene.css', 'preview-scene.js', 'preview-editor.js', 'preview-editor.css', 'preview-library.js', 'preview-more.js', 'preview-more.css'):
        shutil.copyfile(templates / name, target / name)


def stage_ai_quality_review(target: Path) -> None:
    """Keep the saved visual audit and its exact artwork evidence across builds."""
    templates = Path(__file__).with_name('templates')
    for name in ('ai-review.html', 'ai-review.css', 'ai-review.js'):
        shutil.copyfile(templates / name, target / name)
    source = REPO_ROOT / 'icon_set/reviews/approved-quality-50-20260917'
    if source.is_dir():
        shutil.copytree(source, target / 'ai-review-data', dirs_exist_ok=True)


def stage_laboratory(target: Path) -> None:
    """Publish the learning page with the same contracts used by the builder."""
    from icon_set.model import contracts
    templates = Path(__file__).with_name('templates')
    for name in ('icon-laboratory.html', 'icon-laboratory.css', 'icon-laboratory.js'):
        shutil.copyfile(templates / name, target / name)
    data = {'profile': contracts.icon_profile(), 'keyshapes': contracts.keyshapes()}
    (target / 'laboratory.json').write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def stage_failures(staged: Path, published: Path, folders: list[str], target: Path, *, passed: int) -> None:
    """The Failed build tab: failed icons of the focus families, rendered and grouped by rule."""
    from icon_set.scripts.failure_report import FOCUS_FAMILIES, collect, write_report
    manifests = []
    for folder in folders:
        manifest = staged / 'failed' / folder / 'manifest.json'
        if not manifest.exists():
            manifest = published / 'failed' / folder / 'manifest.json'
        if manifest.exists():
            manifests.append((manifest, '../failed/' + quote(folder, safe='') + '/'))
    data = collect(manifests, families=FOCUS_FAMILIES)
    data['total'] = passed + data['failed']
    write_report(data, target / 'failures.html')
    (target / 'failures.json').write_text(json.dumps({'failed': data['failed'], 'total': data['total']}) + '\n',
                                          encoding='utf-8')


def remap_categories(records: list[dict], catalog: dict) -> None:
    """Use the primitives page's identity links, not generated category guesses.

    Native containers and geometric primitives retain their own categories.
    The small alias list covers authored icons with no original primitive ID.
    Ambiguous source reuse is left alone instead of choosing an arbitrary row.
    """
    categories = {}
    for row in catalog['rows']:
        for icon_id in row.get('models', []):
            categories.setdefault(icon_id, set()).add(row['category'])
    aliases = {
        'objects/clothing': 'clothes', 'objects/drink': 'drinks',
        'nature/animals': 'animals', 'animals/mammals': 'animals',
        'objects/sports': 'sports', 'people/sports': 'sports',
        'objects/tool': 'tools', 'objects/organization': 'business',
        'objects/communication': 'messages', 'objects/transport': 'transportation',
        'objects/baby': 'babies', 'places/landmarks': 'landmarks',
        'objects/nature': 'nature', 'people/users': 'users',
        'people/occupations': 'avatars', 'objects/media': 'audio',
    }
    valid = set(catalog['categories'])
    for record in records:
        candidates = categories.get(record['icon_id'])
        if candidates is None:
            candidates = categories.get(record.get('variant_root'))
        if candidates:
            if len(candidates) == 1:
                record['category'] = next(iter(candidates))
        else:
            category = aliases.get(record.get('category'))
            if category in valid:
                record['category'] = category


def stage_primitives(target: Path, records: list[dict], failed_records: list[dict]) -> dict:
    """The Primitives tab: every original primitive and whether it has been remade."""
    from icon_set.scripts.primitives_catalog import write_catalog
    catalog = write_catalog(target / 'primitives.json',
                            {record['icon_id']: record for record in records},
                            {record['icon_id']: record for record in failed_records})
    from icon_set.scripts.combination_catalog import write_catalog as write_combinations
    write_combinations(target, catalog, records)
    if catalog['warning']:
        print('Primitives page: ' + catalog['warning'])
    return catalog


def stage_gallery(staged: Path, published: Path, folders: list[str], *, only=None) -> Path:
    if only is not None:
        from .targeted_gallery import stage_targeted_gallery
        return stage_targeted_gallery(staged, published, folders, only)
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
            current = registered.get(record['icon_id'])
            if current is not None and current.family != record['family']:
                continue
            record['key'] = record['family'] + '/' + record['icon_id']
            record['preview_url'] = '../' + quote(folder, safe='') + '/' + quote(record['icon_id'], safe='') + '.svg'
            record['original_sources'] = copy_originals(sources.get(record['icon_id'], []), target)
            record['python_source'] = authoring.get(record['icon_id'])
            factory = registered.get(record['icon_id'])
            if factory is not None:
                record['author'] = getattr(sys.modules[factory.__module__], 'AUTHOR', '')
                record['variant_of'] = getattr(factory, 'variant_of', None)
                record['variant_label'] = getattr(factory, 'variant_label', '')
                ancestor = factory
                while getattr(ancestor, 'variant_of', None):
                    ancestor = registered[ancestor.variant_of]
                record['variant_root'] = ancestor.icon_id
            records.append(record)
    from icon_set.scripts.text_family import gallery_records as text_records
    records.extend(text_records(staged, published, target))
    from .symbol_family import stage as stage_symbols
    stage_symbols(target, records)
    failed_records = []
    exported_keys = {record['key'] for record in records}
    for folder in folders:
        manifest = staged / 'failed' / folder / 'manifest.json'
        if not manifest.exists():
            manifest = published / 'failed' / folder / 'manifest.json'
        if not manifest.exists():
            continue
        for failure in json.loads(manifest.read_text(encoding='utf-8'))['icons']:
            icon_id = failure['icon_id']
            factory = registered.get(icon_id)
            if factory is None:
                continue
            key = factory.family + '/' + icon_id
            if key in exported_keys:
                continue
            failed_records.append({
                **failure, 'key': key, 'name': icon_id, 'build_failed': True,
                'author': getattr(sys.modules[factory.__module__], 'AUTHOR', ''),
                'category': getattr(factory, 'category', ''),
                'keywords': getattr(factory, 'keywords', ()),
                'preview_url': '../failed/' + quote(folder, safe='') + '/' + quote(failure.get('svg') or icon_id + '.svg', safe=''),
                'original_sources': copy_originals(sources.get(icon_id, []), target),
                'python_source': authoring.get(icon_id),
            })
    failed_records.sort(key=lambda item: (item['family'], item['icon_id']))
    records.sort(key=lambda item: (item['family'], item['icon_id']))
    author_counts = {}
    for factory in registered.values():
        author = getattr(sys.modules[factory.__module__], 'AUTHOR', '')
        if author:
            author_counts[author] = author_counts.get(author, 0) + 1
    (target / 'authors.json').write_text(json.dumps(author_counts, sort_keys=True) + '\n', encoding='utf-8')
    from icon_set.scripts.failure_report import FOCUS_FAMILIES
    stage_failures(staged, published, folders, target,
                   passed=sum(record['family'] in FOCUS_FAMILIES for record in records))
    catalog = stage_primitives(target, records, failed_records)
    remap_categories(records + failed_records, catalog)
    add_creation_times(records + failed_records, published)
    add_modification_times(records + failed_records, published)
    from icon_set.scripts.sub_reference_fidelity import annotate_sub_references, stage_sub_reference_review
    annotate_sub_references(records + failed_records)
    from .sub_usage_categories import annotate_records as annotate_sub_usage
    annotate_sub_usage(records + failed_records)
    stage_sub_reference_review(target)
    from .profile_links import annotate as annotate_profile_links
    annotate_profile_links(records + failed_records)
    from .sub_profile_report import stage as stage_sub_profiles
    stage_sub_profiles(target)
    role_assets = REPO_ROOT / 'icon_set/assets/sub-usage'
    if role_assets.is_dir():
        shutil.copytree(role_assets, target / 'sub-usage', dirs_exist_ok=True)
    stage_review_facets(records, staged, published, target)
    (target / 'icons.json').write_text(json.dumps({'icons': records, 'failed_icons': failed_records}, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    shutil.copyfile(Path(__file__).with_name('templates') / 'gallery.html', target / 'index.html')
    shutil.copyfile(Path(__file__).with_name('templates') / 'generate.html', target / 'generate.html')
    shutil.copyfile(Path(__file__).with_name('templates') / 'icon-canvas.css', target / 'icon-canvas.css')
    for asset in ("api.html", "api.css", "api.js", "upload.html", "upload.js", "home.html", "login.html", "site.css", "site.js", "reviewers.html", "reviewers.css", "reviewers.js", "experiment.html", "experiment.css", "experiment.js", "combination-experiment.js", "side-combination-popup.js", "side-repair-flags.js", "side-combination-progress.js", "icons.html", "approved-icons.js", "reference-picker.js",
                  "primitives.html", "progression-combinations.js", "symbols-needed.html", "review-workspace.css", "stroke-fit.js", "stroke-editor.js", "stroke-editor.css", "icon-guides.js", "icon-artwork.js", "icon-feedback.js"):
        shutil.copyfile(Path(__file__).with_name("templates") / asset, target / asset)
    side_review = REPO_ROOT / 'icon_set/work/side-combinations-passing-sub'
    if (side_review / 'index.html').is_file():
        shutil.copytree(side_review, target / 'side-combinations-passing-sub', dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns('pairs-before.json', 'previews-before.json', 'sample-review.png'))
        page = target / 'side-combinations-passing-sub/index.html'
        page.write_text(page.read_text().replace('../../dist/gallery/', '../').replace('../../.local/dist/gallery/', '../').replace('../../../published/gallery/', '../'))
    from .sub_repair_review import stage as stage_sub_repair_review
    stage_sub_repair_review(target / 'sub-repair-review')
    stage_ai_quality_review(target)
    stage_laboratory(target)
    stage_preview(target, records)
    from icon_set.scripts.typeface_gallery import stage_typeface
    stage_typeface(target, records, registered)
    from icon_set.scripts.experiment_gallery import stage_experiments
    stage_experiments(target)
    # Keep the saved container review available when a build replaces the gallery.
    container_review = REPO_ROOT / 'icon_set/work/container-skip-review-20260917'
    if (container_review / 'index.html').is_file():
        shutil.copytree(container_review, target / 'container-skip-review', dirs_exist_ok=True)
    return target
