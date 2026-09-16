"""Publish read-only experiment collections without touching review data."""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def stage_experiments(target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    counts = {}
    for kind in ('color', 'fill'):
        output = target / f'experiment-{kind}.json'
        source = ROOT / 'work' / f'{kind}-review-500'
        rows = None
        if kind == 'color' and (source / 'data.json').is_file():
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
    (target / 'experiments.json').write_text(json.dumps(counts) + '\n')
    # Keep the existing fill review route and its browser feedback key intact.
    fill = ROOT / 'work/fill-review-500'
    for src, dest in [('index.html', 'fill-review-500.html'),
                      ('fill-review-500-data.js', 'fill-review-500-data.js')]:
        if (fill / src).is_file():
            shutil.copyfile(fill / src, target / dest)


if __name__ == '__main__':
    stage_experiments(ROOT / 'icon_set/dist/gallery')
