"""Stage the complete combination remake catalog and portable reference SVGs."""
from __future__ import annotations
import json
import hashlib
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# Some source IDs contain non-hex characters; preserve their exact identity.
ID = re.compile(r'([a-z0-9]{8}(?:-[a-z0-9]{4}){3}-[a-z0-9]{12})$', re.I)


def write_catalog(target: Path, primitives: dict, records: list[dict], root: Path = ROOT) -> dict:
    source = root / 'combination_data.json'
    data = json.loads(source.read_text()) if source.exists() else {}
    originals = {}
    for path in sorted((root / 'pictographic-combinations').rglob('*.svg')):
        match = ID.search(path.stem)
        if match:
            originals.setdefault(match[1].lower(), path)
    primitive_rows = {r['uuid']: r for r in primitives['rows']}
    generated = {}
    for uid, row in primitive_rows.items():
        generated[uid] = list(row.get('generated', []))
    for record in records:
        for ref in record.get('original_sources', []):
            match = ID.search(Path(ref.get('source_path', '')).stem)
            if match:
                items = generated.setdefault(match[1].lower(), [])
                if not any(x['icon_id'] == record['icon_id'] for x in items):
                    items.append({k: record[k] for k in ('icon_id', 'key', 'preview_url')})
    assets = target / 'combination-originals'
    assets.mkdir(parents=True, exist_ok=True)
    references = {}

    def reference(uid):
        if uid in references:
            return references[uid]
        row = primitive_rows.get(uid, {})
        path = originals.get(uid)
        if path is None and row.get('path'):
            path = root / 'pictographic-primitives' / row['path']
        url = None
        if path and path.is_file():
            destination = assets / (uid + '.svg')
            if not destination.exists() or destination.read_bytes() != path.read_bytes():
                shutil.copyfile(path, destination)
            url = 'combination-originals/' + destination.name
        result = {'id': uid, 'concept': row.get('concept') or (ID.sub('', path.stem).strip(' _-') if path else uid or 'Unspecified component'),
                  'reference_url': url, 'generated': generated.get(uid, [])}
        references[uid] = result
        return result

    compositions = {}
    for path in sorted((target.parent / 'compositions').glob('*.json')):
        svg = path.with_suffix('.svg')
        if not svg.is_file():
            continue
        record = json.loads(path.read_text())
        children = record.get('children', [])
        kind = {'CONTAINER_COMBINE': 'container', 'SIDE_COMBINE': 'side'}.get(record.get('composition_class'))
        if kind and len(children) == 2:
            key = (kind, children[0]['icon_id'], children[1]['icon_id'])
            compositions.setdefault(key, []).append({'icon_id': record['icon_id'], 'preview_url': '../compositions/' + svg.name})
    remap_path = root / 'icon_set/data/combination-remaps.json'
    remaps = json.loads(remap_path.read_text()).get('rules', []) if remap_path.exists() else []
    preview_cache = root / 'icon_set/data/combination-previews.json'
    previews = json.loads(preview_cache.read_text()) if preview_cache.exists() else {}
    main_map_path = root / 'icon_set/data/container-main-icons.json'
    main_map = json.loads(main_map_path.read_text()).get('mappings', {}) if main_map_path.exists() else {}
    containers = {r['icon_id']: r for r in records if r.get('family') == 'container'
                  and r.get('key', '').startswith('container/')}
    export_path = root / 'icon_set/data/combination-sub32.json'
    sub_exports = json.loads(export_path.read_text()) if export_path.exists() else {}
    trial_path = root / 'icon_set/data/container-solo-trials.json'
    trials = json.loads(trial_path.read_text()).get('results', {}) if trial_path.exists() else {}
    records_by_key = {r.get('key'): r for r in records}
    rows = []
    for kind in ('container', 'side'):
        for item in data.get(kind, []):
            row = dict(item, kind=kind)
            row['remappings'] = []
            for rule in remaps:
                field = rule['role'] + '_id'
                fragment = item['id'][:18] if rule['role'] == 'main' else item['id'][19:34]
                if not item.get(field) and fragment == rule['fragment'] and rule['reference_id'] in primitive_rows:
                    row[field] = rule['reference_id']
                    row['remappings'].append(dict(rule, original_id=item.get(field)))
            for field in ('id', 'main_id', 'sub_id'):
                reference(row[field])
            # Main/sub roles are contextual: the same reference can still use its
            # solo drawing in a side combination. Do not mutate shared references.
            main_artwork = references[row['main_id']]['generated']
            if kind == 'container':
                mapping = main_map.get(row['main_id'])
                if mapping:
                    row['main_icon_id'] = mapping['icon_id']
                    selected = containers.get(mapping['icon_id'])
                    main_artwork = [{k: selected[k] for k in ('icon_id', 'key', 'preview_url')}] if selected else []
                else:
                    main_artwork = [g for g in main_artwork if g.get('key', '').startswith('container/')]
                row['main_generated'] = main_artwork
            row['generated'] = []
            preview = previews.get(row['id'], {})
            if kind == 'side' and preview.get('result', {}).get('svg'):
                row['generated'].append({'icon_id': row['id'], 'preview_url': preview['url'], 'kind': 'side experiment'})
            seen = set()
            for main in main_artwork:
                for sub in references[row['sub_id']]['generated']:
                    for result in compositions.get((kind, main['icon_id'], sub['icon_id']), []):
                        if result['icon_id'] not in seen:
                            row['generated'].append(result)
                            seen.add(result['icon_id'])
            if kind == 'side':
                row['sub_exports'] = [sub_exports[g['icon_id']] for g in references[row['sub_id']]['generated'] if g['icon_id'] in sub_exports]
            trial = trials.get(row['id']) if kind == 'container' else None
            if trial:
                # Trials are separate from validated/generated compositions.
                # A source edit or remap invalidates the saved preview.
                current = (
                    trial.get('main_source_id') == row['main_id']
                    and trial.get('sub_source_id') == row['sub_id']
                    and any(g['key'] == trial.get('main_key') for g in main_artwork)
                    and any(g['key'] == trial.get('sub_key') for g in references[row['sub_id']]['generated'])
                    and all(records_by_key.get(trial.get(role + '_key'), {}).get('svg_sha256') == trial.get(role + '_sha256')
                            and trial.get(role + '_sha256') for role in ('main', 'sub'))
                )
                filename = trial.get('svg_file', '')
                source = root / 'icon_set/assets/container-solo-trials' / filename
                intact = (bool(filename) and Path(filename).name == filename and source.is_file()
                          and hashlib.sha256(source.read_bytes()).hexdigest() == trial.get('svg_sha256'))
                if current and intact:
                    destination = target / 'container-solo-trials' / filename
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(source, destination)
                    row['trial_preview'] = {
                        'preview_url': 'container-solo-trials/' + filename,
                        'status': trial['status'], 'native_sub32': False,
                        'main_key': trial['main_key'], 'sub_key': trial['sub_key'],
                        'placement': trial['placement'],
                    }
                else:
                    row['trial_status'] = 'stale'
            rows.append(row)
    result = {'rows': rows, 'references': references}
    if sub_exports:
        from .deduplicate_subs import canonical_map, update_catalog
        aliases, _ = canonical_map(sub_exports, root)
        update_catalog(result, sub_exports, aliases, root)
    (target / 'combinations.json').write_text(json.dumps(result, ensure_ascii=False, separators=(',', ':')) + '\n')
    return result


if __name__ == '__main__':
    gallery = ROOT / 'icon_set/dist/gallery'
    result = write_catalog(gallery, json.loads((gallery / 'primitives.json').read_text()),
                           json.loads((gallery / 'icons.json').read_text())['icons'])
    print(f"Staged {len(result['rows'])} combinations; {sum(not r['reference_url'] for r in result['references'].values())} missing references")
