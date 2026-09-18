"""Publish read-only experiment collections without touching review data."""
import json
import base64
import io
import sys
import shutil
from pathlib import Path
from xml.sax.saxutils import quoteattr

ROOT = Path(__file__).resolve().parents[2]


def stage_container_experiment(target: Path) -> str:
    """Package the saved layouts and their actual components for offline browsing."""
    manifest = ROOT / 'icon_set/data/container-solo-trials.json'
    rows, seen = [], set()
    records = json.loads(manifest.read_text())['results'] if manifest.is_file() else {}
    for record in records.values():
        filename = record['svg_file']
        if filename in seen:
            continue
        seen.add(filename)
        host = record['main_key'].split('/', 1)[1]
        content = record['sub_key'].split('/', 1)[1]
        rows.append(dict(number=len(rows)+1, name=host+' + '+content,
                         icon_id=filename.removesuffix('.svg'), canvas_size=64,
                         outline=(ROOT/f'icon_set/dist/container64/{host}.svg').read_text(),
                         content=(ROOT/f'icon_set/dist/solo48/{content}.svg').read_text(),
                         result=(ROOT/'icon_set/assets/container-solo-trials'/filename).read_text(),
                         status_label='Trial preview · '+('clearance estimate clear' if record['status']=='clearance-estimate-pass' else 'placement review required')))
    payload = json.dumps({'icons': rows}, ensure_ascii=True).replace('<', '\\u003c')
    (target/'experiment-container.json').write_text(payload+'\n')
    for source, dest in [('placement-rules.md', 'container-placement-rules.md'),
                         ('report.md', 'container-trials-report.md')]:
        shutil.copyfile(ROOT/'icon_set/work/container-pair-trials'/source, target/dest)
    return payload


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
            published = ROOT / 'icon_set/dist/gallery' / output.name
            if published.is_file() and published.resolve() != output.resolve():
                shutil.copyfile(published, output)
            elif not output.is_file():
                output.write_text('{"icons":[]}\n')
        counts[kind] = len(json.loads(output.read_text())['icons'])
    typeface_path = target / 'typeface.json'
    glyphs = json.loads(typeface_path.read_text())['glyphs'] if typeface_path.is_file() else []
    typeface = {'icons': typeface_samples(glyphs)}
    payload = json.dumps(typeface, ensure_ascii=True).replace('<', '\\u003c')
    (target / 'experiment-typeface.json').write_text(payload+'\n')
    counts['typeface'] = len(typeface['icons'])
    combination = ROOT / 'icon_set/data/combination-pairs.json'
    if combination.is_file():
        shutil.copyfile(combination, target / 'experiment-combination.json')
        counts['combination'] = len(json.loads(combination.read_text())['rows'])
    shutil.copyfile(Path(__file__).with_name('templates') / 'combination-experiment.js', target / 'combination-experiment.js')
    from .sub_scaling_gallery import stage_sub_scaling
    stage_sub_scaling(target)
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
        (target / 'experiment-combination-results.json').write_text(json.dumps({'results': results}))

    template = (Path(__file__).with_name('templates') / 'experiment.html').read_text()
    # Embed this small collection so the user's local-file experiment works offline.
    container_payload = stage_container_experiment(target)
    counts['container'] = len(json.loads(container_payload)['icons'])
    (target / 'experiment.html').write_text(template.replace('__TYPEFACE_EXPERIMENT_DATA__', payload).replace('__CONTAINER_EXPERIMENT_DATA__', container_payload))
    (target / 'experiments.json').write_text(json.dumps(counts) + '\n')
    # Keep the existing fill review route and its browser feedback key intact.
    fill = ROOT / 'work/fill-review-500'
    for src, dest in [('index.html', 'fill-review-500.html'),
                      ('fill-review-500-data.js', 'fill-review-500-data.js')]:
        if (fill / src).is_file():
            shutil.copyfile(fill / src, target / dest)


if __name__ == '__main__':
    stage_experiments(ROOT / 'icon_set/dist/gallery')
