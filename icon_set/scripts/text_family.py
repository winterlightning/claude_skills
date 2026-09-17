"""Gallery integration for natural-proportion TEXT28 lettering exports.

Text is a layout family, not a geometric icon profile. Build it with
`node icon_set/scripts/build_text_icons.cjs` before staging a fresh gallery.
"""
import json
from pathlib import Path
from urllib.parse import quote


def gallery_records(staged: Path, published: Path, target: Path) -> list[dict]:
    from icon_set.scripts.gallery import copy_originals
    folder = staged / 'text28'
    if not (folder / 'manifest.json').exists():
        folder = published / 'text28'
    if not (folder / 'manifest.json').exists():
        return []
    data = json.loads((folder / 'manifest.json').read_text())
    if data.get('family') != 'text' or data.get('canvas_height') != 28:
        raise ValueError('Invalid text family manifest')
    records = []
    for item in data['icons']:
        if item.get('family') != 'text' or item.get('canvas_height') != 28:
            raise ValueError('Text export must have a 28-unit canvas height')
        if not (folder / (item['icon_id'] + '.svg')).is_file():
            raise ValueError('Missing text export: ' + item['icon_id'])
        row = dict(item, key='text/' + item['icon_id'],
                   preview_url='../text28/' + quote(item['icon_id'], safe='') + '.svg',
                   python_source=None)
        paths = [Path(r['source_path']) for r in item.get('original_sources', [])
                 if r.get('source_path') and Path(r['source_path']).is_file()]
        row['original_sources'] = copy_originals(paths, target)
        records.append(row)
    return records
