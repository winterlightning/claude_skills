"""The mains and subs the fill side pairs use, from this workspace's build: each part's status (filled, outline only,
redrawn since its pairs were laid out, text sub, …), its variants and the pairs that use it.

d1_import writes them into fill_parts; fill_icons exports their fill variant icons.
"""
import json
import re
from pathlib import Path
from urllib.parse import unquote

from .paths import DATA, WORK

NUMBER = re.compile(r'-?\d+\.\d{3,}')


def compact(svg: str) -> str:
    """Drop the XML header and newlines and round long decimals: the same picture, a fraction of the size."""
    svg = re.sub(r'<\?xml[^>]*>\s*', '', svg)
    svg = NUMBER.sub(lambda m: f'{float(m.group()):.2f}'.rstrip('0').rstrip('.'), svg)
    return re.sub(r'>\s+<', '><', svg).strip()


def read_work(url: str | None) -> str | None:
    """The SVG behind a gallery row URL (relative to WORK, with a ?v= cache tag)."""
    if not url:
        return None
    path = (WORK / unquote(url.split('?', 1)[0])).resolve()
    if not path.is_file() or not (path.is_relative_to(WORK.resolve()) or path.is_relative_to(DATA.resolve())):
        return None
    return compact(path.read_text())


def source_svg(role: str, part: dict) -> str | None:
    """The outline (source drawing) a part's fills were made from, read from the imported sources."""
    name, revision = part.get('name'), part.get('revision')
    if not name:
        return None
    if role == 'main':
        candidates = [DATA / 'normal' / f'{name}.svg']
    else:
        candidates = [DATA / 'archive/side-sub-32' / f'{name}.svg', DATA / 'archive/sub-32-revisions' / name / f'{revision}.svg']
    path = next((p for p in candidates if p.is_file()), None)
    return compact(path.read_text()) if path else None


def fill_svg(role: str, part: dict) -> str | None:
    """The part's fill as the engine reads it (adaptive_overlap.fill_path: the reviewed stroke-fill, else the
    shared collection's fill), from the imported data."""
    from .adaptive_overlap import fill_path
    if not part.get('key'):
        return None
    path = fill_path({'icon': part['key'], 'current_sha': part.get('revision')}, role)
    return compact(path.read_text()) if path.is_file() else None


STATUS_NOTE = {
    'ready': 'Has a fill: combined in its pairs.',
    'outline': 'Only an outline: the fill region algorithm found nothing to fill.',
    'redrawn': 'Redrawn since its pairs were laid out: the saved layout points at another drawing, so its pairs are not combined.',
    'no-source': 'Its drawing is missing from the imported sources.',
    'no-fill': 'No fill made for this drawing yet.',
    'not-drawn': 'No drawing linked to this part yet.',
    'text': 'A text sub, set from the typeface: the fill combine does not place text subs yet.',
}


def side_texts():
    """{part reference id: text} of the text subs (icon_set/data side-text-v2.json and container-text-v2.json)."""
    texts = {}
    for name in ('container-text-v2.json', 'side-text-v2.json'):
        path = DATA.parents[1] / 'data' / name
        if path.is_file():
            for icon in json.loads(path.read_text()).get('icons', []):
                for sid in icon.get('source_ids') or [icon.get('source_id')]:
                    if sid and icon.get('text'):
                        texts[sid] = icon['text']
    return texts


def text_svg(text):
    """A text sub drawn as the site's typeface sets it (side_text.native_text)."""
    try:
        from ..side_text import glyph_map, native_text
        return compact(native_text(text, glyph_map())[0])
    except Exception:
        return None


def parts_listing(combined: set):
    """Every main and sub the side layouts use, combined or not: ([(entry, art)] mains, [(entry, art)] subs).
    A part that cannot be combined says why (STATUS_NOTE)."""
    from .adaptive_overlap import source_path
    from .build_gallery import component
    texts = side_texts()
    tables = {'main': {}, 'sub': {}}
    for item in json.loads((DATA / 'data/production-layouts.json').read_text())['items']:
        for part in item['parts']:
            role = part['role']
            if part.get('icon'):
                key = part['icon']
            elif role == 'sub':
                key = 'text/' + part['part_reference_id']
            else:
                key = 'undrawn/' + part['part_reference_id']
            entry = tables[role].get(key)
            if entry is None:
                entry = tables[role][key] = {'key': key, 'part': part, 'pairs': [], 'combined_pairs': []}
            entry['pairs'].append(item['reference_id'])
            if item['reference_id'] in combined:
                entry['combined_pairs'].append(item['reference_id'])
    out = {}
    for role, table in tables.items():
        rows = []
        for key, entry in table.items():
            part, art, variants = entry['part'], {}, []
            if key.startswith('text/'):
                text = texts.get(part['part_reference_id'])
                status, name = 'text', f'Text sub “{text}”' if text else 'Text sub'
                art['text'] = text
                art['source'] = text_svg(text) if text else None
            elif key.startswith('undrawn/'):
                status, name = 'not-drawn', part.get('draw_name') or 'Not drawn yet'
            else:
                name = key.split('/', 1)[1]
                source = source_path(part, role)
                want = part.get('current_sha') or part.get('built_sha')
                c = component(part, role)
                art = {'source': source_svg(role, {'name': name, 'revision': want}),
                       'fill': fill_svg(role, {'key': key, 'revision': want})}
                for variant in c.get('variants', []):
                    if variant.get('status') == 'rejected':
                        continue                         # rejected variants are not shown or combined
                    svg = read_work(variant.get('url'))
                    if svg:
                        art[variant['variant']] = svg
                        variants.append({'variant': variant['variant'], 'status': variant['status']})
                if not source.is_file():
                    status = 'no-source'
                elif sha_of(source) != want:
                    status = 'redrawn'
                elif art['fill'] is None:
                    status = 'no-fill'
                else:
                    status = 'ready' if c.get('has_fill') else 'outline'
            rows.append(({'key': key, 'name': name, 'status': status, 'note': STATUS_NOTE[status],
                          'revision': part.get('current_sha') or part.get('built_sha'), 'variants': variants,
                          'pairs': entry['pairs'], 'combined_pairs': entry['combined_pairs']}, art))
        out[role] = rows
    return out['main'], out['sub']


def sha_of(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()
