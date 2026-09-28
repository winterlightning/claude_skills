"""Publish read-only experiment collections without touching review data."""
import json
import base64
import io
import sys
import shutil
from pathlib import Path
from xml.sax.saxutils import quoteattr

if __package__:
    from .workspace import build_dist
else:
    from workspace import build_dist


ROOT = Path(__file__).resolve().parents[2]
# Tracked snapshots of experiments whose generating workspace was never versioned
# and no longer exists. They are source data now.
def preserved_copy(name: str) -> Path:
    return ROOT / 'icon_set/assets/experiments' / name


def restore_preserved(output: Path) -> None:
    """Fill an experiment collection from the tracked snapshot, else leave it empty."""
    saved = preserved_copy(output.name)
    if saved.is_file() and saved.resolve() != output.resolve():
        shutil.copyfile(saved, output)
    elif not output.is_file():
        output.write_text('{"icons":[]}\n')


def stage_container_experiment(target: Path) -> str:
    """Package the saved layouts and their actual components for offline browsing."""
    manifest = ROOT / 'icon_set/data/container-solo-trials.json'
    rows, seen, unavailable = [], set(), 0
    records = json.loads(manifest.read_text())['results'] if manifest.is_file() else {}
    for record in records.values():
        filename = record['svg_file']
        if filename in seen:
            continue
        seen.add(filename)
        host = record['main_key'].split('/', 1)[1]
        content = record['sub_key'].split('/', 1)[1]
        outline = target.parent / f'container64/{host}.svg'
        component = target.parent / f'solo48/{content}.svg'
        result = ROOT/'icon_set/assets/container-solo-trials'/filename
        if not all(path.is_file() for path in (outline, component, result)):
            unavailable += 1
            continue  # Optional historical experiments must not block a fresh build.
        rows.append(dict(number=len(rows)+1, name=host+' + '+content,
                         icon_id=filename.removesuffix('.svg'), canvas_size=64,
                         outline=outline.read_text(), content=component.read_text(),
                         result=result.read_text(),
                         status_label='Trial preview · '+('clearance estimate clear' if record['status']=='clearance-estimate-pass' else 'placement review required')))
    output = target / 'experiment-container.json'
    if not rows and preserved_copy(output.name).is_file():
        restore_preserved(output)
        payload = output.read_text().rstrip('\n')
    else:
        payload = json.dumps({'icons': rows, 'unavailable': unavailable}, ensure_ascii=True).replace('<', '\\u003c')
        output.write_text(payload+'\n')
    for source, dest in [('placement-rules.md', 'container-placement-rules.md'),
                         ('report.md', 'container-trials-report.md')]:
        document = ROOT/'icon_set/work/container-pair-trials'/source
        if document.is_file():
            shutil.copyfile(document, target/dest)
    return payload


def stage_animation_experiment(target: Path) -> int:
    """Publish the animated SVG samples built by work/animation-samples/build.py."""
    source = ROOT / 'work/animation-samples'
    output = target / 'experiment-animation.json'
    if (source / 'data.json').is_file():
        rows = [dict(key=r['key'], number=r['number'], name=r['name'], icon_id=r['icon_id'],
                     source=r['source'], canvas_size=r['canvas_size'], motion=r['motion'],
                     outline=(source / r['outline_url']).read_text(),
                     result=(source / r['result_url']).read_text())
                for r in json.loads((source / 'data.json').read_text())['icons']]
        output.write_text(json.dumps({'icons': rows}, separators=(',', ':')) + '\n')
    else:
        restore_preserved(output)
    return len(json.loads(output.read_text())['icons'])


def fitted_preview(document: str) -> str:
    """Trim only preview whitespace, preserving original aspect ratio and artwork."""
    import cairosvg
    from PIL import Image, ImageChops
    image = Image.open(io.BytesIO(cairosvg.svg2png(
        bytestring=document.encode(), output_width=384))).convert('RGBA')
    white = Image.new('RGBA', image.size, 'white')
    white.alpha_composite(image)
    rgb = white.convert('RGB')
    mask = ImageChops.difference(rgb, Image.new('RGB', rgb.size, 'white')).convert('L')
    bounds = mask.point(lambda value: 255 if value > 32 else 0).getbbox()
    if bounds:
        rgb = rgb.crop(bounds)
    result = io.BytesIO()
    rgb.save(result, format='PNG')
    return 'data:image/png;base64,'+base64.b64encode(result.getvalue()).decode('ascii')


def typeface_samples(glyphs: list[dict]) -> list[dict]:
    """Render the exact published paths, with a thin overlay on their centerlines."""
    from icon_set.model.icons.registry import factories
    registered = factories()
    rows = []
    order = {'uppercase': 0, 'lowercase': 1, 'digit': 2}
    for number, glyph in enumerate(sorted(glyphs, key=lambda g: (
            order.get(g['kind'], 3), g['character'], not g['preferred'])), 1):
        paths = ''.join('<path d='+quoteattr(d)+'/>' for d in glyph['paths'])
        view_box = ' '.join(str(v) for v in glyph.get('preview_box', [0,0,48,48]))
        start = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox='+quoteattr(view_box)+' '
                 'width="48" height="48" fill="none" stroke-linecap="round" stroke-linejoin="round">')
        outline = start+'<g stroke="#202820" stroke-width="4">'+paths+'</g></svg>'
        result = (start+'<g stroke="#dce3dc" stroke-width="4">'+paths+'</g>'
                  '<g stroke="#ce4937" stroke-width="0.65">'+paths+'</g></svg>')
        label = glyph['character']+' · '+glyph['kind']
        if not glyph['preferred']:
            label += ' · large source'
        factory = registered.get(glyph['icon_id'])
        source = glyph.get('source_path') if 'source_path' in glyph else (getattr(sys.modules[factory.__module__], 'SOURCE_PATH', None) if factory else None)
        source_path = Path(source) if source else None
        if source_path and not source_path.is_absolute():
            source_path = ROOT / source_path
        original = source_path.read_text() if source_path and source_path.is_file() else None
        rows.append(dict(original=original,
                         original_name=source_path.name if original else None,
                         original_preview=fitted_preview(original) if original else None,
                         outline_preview=fitted_preview(outline),
                         key='solo/'+glyph['icon_id'], number=number,
                         name=label, icon_id=glyph['icon_id'], canvas_size=48,
                         outline=outline, result=result))
    return rows


POSITION_LABELS = {'br': 'Bottom-right', 'tr': 'Top-right', 'bo': 'Bottom', 'to': 'Top',
                   'bl': 'Bottom-left', 'tl': 'Top-left', 'ri': 'Right', 'le': 'Left'}


def stage_preview_combinations(target: Path) -> int:
    """The side-combination library for the Preview page's usage examples.

    Built from the gallery's own side-pair data (experiment-combination.json and
    experiment-combination-results.json), so the Preview picker offers exactly
    the combined 64 icons the Progression "Side pairs" view shows. Every script
    that rewrites those results calls this again, or the picker goes stale.
    preview-library.js appends these to the approved icons, and preview-scene.js
    resolves every template placement to one of these ids, so without this file
    all ten examples silently fall back to solo icons.
    """
    pairs, previews = target / 'experiment-combination.json', target / 'experiment-combination-results.json'
    rows = json.loads(pairs.read_text())['rows'] if pairs.is_file() else []
    results = json.loads(previews.read_text())['results'] if previews.is_file() else {}
    icons = [{'icon_id': row['id'], 'name': row['concept'], 'family': 'combination',
              'category': POSITION_LABELS.get(row['position'], row['position']),
              'preview_url': results[row['id']].get('url') or 'combination-previews/' + row['id'] + '.svg'}
             for row in rows if row['id'] in results]
    (target / 'preview-combination-icons.json').write_text(
        json.dumps({'icons': icons}, ensure_ascii=False) + '\n', encoding='utf-8')
    stage_side_combination64(target)
    return len(icons)


SIDE_COMBINATION_FAMILY = 'side_combination64'


def stage_side_combination64(target: Path) -> int:
    """The combined side icons as review records: the "Side combination 64" family.

    Rewritten whole from the current side-pair results, so each combine run
    replaces the previous set and `count` is the number of combined icons that
    actually exist. deploy.py merges these records into the review catalog;
    reviews key on (key, svg_sha256), so a changed drawing is a new revision.
    """
    import hashlib
    from datetime import datetime, timezone
    pairs, previews = target / 'experiment-combination.json', target / 'experiment-combination-results.json'
    rows = json.loads(pairs.read_text())['rows'] if pairs.is_file() else []
    results = json.loads(previews.read_text())['results'] if previews.is_file() else {}
    output = target / 'side-combination64.json'
    previous = json.loads(output.read_text()) if output.is_file() else {}
    known = {r['key']: r for r in previous.get('icons', [])}
    catalog = target / 'combinations.json'
    references = json.loads(catalog.read_text()).get('references', {}) if catalog.is_file() else {}
    now = datetime.now(timezone.utc).isoformat()
    icons = []
    for row in rows:
        item = results.get(row['id'])
        if not item or 'error' in item:
            continue
        url = (item.get('url') or 'combination-previews/' + row['id'] + '.svg').split('?', 1)[0]
        svg = item.get('result', {}).get('svg')
        path = target / url
        if svg is None and path.is_file():
            svg = path.read_text()
        if not svg:
            continue
        sha = hashlib.sha256(svg.encode()).hexdigest()
        key = SIDE_COMBINATION_FAMILY + '/' + row['id']
        old = known.get(key, {})
        placed = {p.get('role'): p.get('icon') for p in item.get('result', {}).get('placements', [])}
        reference = references.get(row['id'], {}).get('reference_url')
        icons.append({
            'key': key, 'icon_id': row['id'], 'name': row['concept'], 'family': SIDE_COMBINATION_FAMILY,
            'profile': 'SIDE_COMBINATION64', 'canvas_size': int(item.get('result', {}).get('canvas') or 64),
            'category': POSITION_LABELS.get(row.get('position'), row.get('position') or 'Side'),
            'position': row.get('position'), 'native_text': bool(row.get('native_text') or item.get('native_text')),
            'main_icon': placed.get('main') or item.get('main') or (row.get('mains') or [{}])[0].get('icon'),
            'sub_icon': placed.get('sub') or item.get('sub') or (row.get('subs') or [{}])[0].get('icon'),
            'tags': [], 'keywords': [], 'aliases': [], 'description': '',
            'svg_sha256': sha, 'preview_url': url + '?v=' + sha[:12],
            'validation': {'status': 'valid', 'automatic_status': 'pass', 'errors': []},
            'original_sources': [{'url': reference, 'format': 'SVG', 'source_path': reference}] if reference else [],
            'python_source': None,
            'created_at': old['created_at'] if old.get('svg_sha256') == sha and old.get('created_at') else now,
            'created_at_source': 'side-combination-run',
        })
    output.write_text(json.dumps({'generated_at': now, 'count': len(icons), 'icons': icons},
                                 ensure_ascii=False, separators=(',', ':')) + '\n', encoding='utf-8')
    return len(icons)


def stage_experiments(target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    counts = {}
    for kind in ('color', 'fill', 'duotone'):
        output = target / f'experiment-{kind}.json'
        source = ROOT / 'work' / f'{kind}-review-500'
        rows = None
        if kind in ('color', 'duotone') and (source / 'data.json').is_file():
            data = json.loads((source / 'data.json').read_text())
            rows = [dict(key=r['key'], number=r['number'], name=r['name'],
                         canvas_size=r['canvas_size'],
                         outline=(source / r['outline_url']).read_text(),
                         result=(source / r['color_url']).read_text()) for r in data['icons']]
        elif kind == 'fill' and (source / 'fill-review-500-data.js').is_file():
            text = (source / 'fill-review-500-data.js').read_text()
            data = json.loads(text.split('=', 1)[1].strip().removesuffix(';'))
            rows = [dict(key=r['key'], number=r['sample_number'], name=r['icon_id'],
                         canvas_size=r['canvas_size'], fill_applicable=r['fill_applicable'],
                         outline=r['outline'], result=r['fill']) for r in data]
        if rows is not None:
            if len({r['key'] for r in rows}) != len(rows):
                raise ValueError(f'Duplicate {kind} experiment samples')
            output.write_text(json.dumps({'icons': rows}, separators=(',', ':')) + '\n')
        else:
            restore_preserved(output)
        counts[kind] = len(json.loads(output.read_text())['icons'])
    typeface_path = target / 'typeface.json'
    glyphs = json.loads(typeface_path.read_text())['glyphs'] if typeface_path.is_file() else []
    typeface = {'icons': typeface_samples(glyphs)}
    payload = json.dumps(typeface, ensure_ascii=True).replace('<', '\\u003c')
    (target / 'experiment-typeface.json').write_text(payload+'\n')
    counts['typeface'] = len(typeface['icons'])
    v2_path = target / 'typeface-v2.json'
    v2_glyphs = json.loads(v2_path.read_text())['glyphs'] if v2_path.is_file() else []
    v2_payload = json.dumps({'icons': typeface_samples(v2_glyphs)}, ensure_ascii=True).replace('<', '\\u003c')
    (target / 'experiment-typeface-v2.json').write_text(v2_payload+'\n')
    counts['typeface-v2'] = len(v2_glyphs)
    from .side_combination_progress import stage as stage_side_progress
    stage_side_progress(target)
    combination = ROOT / 'icon_set/data/combination-pairs.json'
    if combination.is_file():
        shutil.copyfile(combination, target / 'experiment-combination.json')
        counts['combination'] = len(json.loads(combination.read_text())['rows'])
    shutil.copyfile(Path(__file__).with_name('templates') / 'combination-experiment.js', target / 'combination-experiment.js')
    sub_exports = ROOT / 'icon_set/assets/combination-sub32'
    if sub_exports.exists():
        shutil.copytree(sub_exports, target / 'combination-sub32', dirs_exist_ok=True)
    state_exports = ROOT / 'icon_set/assets/combination-state32'
    if state_exports.is_dir():
        shutil.copytree(state_exports, target / 'combination-state32', dirs_exist_ok=True)
    preview_cache = ROOT / 'icon_set/data/combination-previews.json'
    if preview_cache.is_file():
        results = json.loads(preview_cache.read_text())
        preview_dir = target / 'combination-previews'
        preview_dir.mkdir(exist_ok=True)
        for key, item in results.items():
            (preview_dir / (key + '.svg')).write_text(item['result']['svg'])
        for stale in preview_dir.glob('*.svg'):
            if stale.stem not in results:
                stale.unlink()
        (target / 'experiment-combination-results.json').write_text(json.dumps({'results': results}))
        stage_preview_combinations(target)
    manifest = target / 'side-combination64.json'
    if manifest.is_file():
        # The tab counts combined icons, not candidate pairs.
        counts['combination'] = json.loads(manifest.read_text())['count']

    template = (Path(__file__).with_name('templates') / 'experiment.html').read_text()
    # Embed this small collection so the user's local-file experiment works offline.
    container_payload = stage_container_experiment(target)
    counts['container'] = len(json.loads(container_payload)['icons'])
    counts['animation'] = stage_animation_experiment(target)
    (target / 'experiment.html').write_text(template.replace('__TYPEFACE_EXPERIMENT_DATA__', payload).replace('__TYPEFACE_V2_EXPERIMENT_DATA__', v2_payload).replace('__CONTAINER_EXPERIMENT_DATA__', container_payload))
    (target / 'experiments.json').write_text(json.dumps(counts) + '\n')
    # Keep the existing fill review route and its browser feedback key intact.
    fill = ROOT / 'work/fill-review-500'
    for src, dest in [('index.html', 'fill-review-500.html'),
                      ('fill-review-500-data.js', 'fill-review-500-data.js')]:
        if (fill / src).is_file():
            shutil.copyfile(fill / src, target / dest)


if __name__ == '__main__':
    stage_experiments(build_dist(ROOT) / 'gallery')
