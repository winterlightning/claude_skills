"""Build one original, report compact findings, and render only its exported SVG."""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import inspect
import io
import json
from pathlib import Path
import tempfile

from .workspace import DEFAULT_DIST


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path, help='one registered Python original')
    parser.add_argument('--dist', type=Path, default=DEFAULT_DIST)
    parser.add_argument('--out', type=Path, help='preview/log directory; default: a new temporary directory')
    args = parser.parse_args(argv)
    from icon_set.model.icons.registry import factories
    matches = [(key, factory) for key, factory in factories().items()
               if inspect.getsourcefile(factory) and Path(inspect.getsourcefile(factory)).resolve() == args.source.resolve()]
    if len(matches) != 1:
        parser.error('source must define exactly one registered icon')
    icon_id, factory = matches[0]
    out = args.out or Path(tempfile.mkdtemp(prefix='icon-review-'))
    out.mkdir(parents=True, exist_ok=True)
    log = out / 'build.log'
    from .build import build, family_dist_name
    with log.open('w') as stream, contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
        code = build(args.dist, None, write_png=False, report=False, sources=[args.source])
    folder = family_dist_name(factory.family)
    root = args.dist / ('failed' if code else '') / folder
    manifest = root / 'manifest.json'
    rows = json.loads(manifest.read_text())['icons'] if manifest.exists() else []
    row = next((r for r in rows if r['icon_id'] == icon_id), None)
    if row is None:
        print(f'ERROR: no result for {icon_id}; log: {log}')
        return 2
    validation = row.get('validation', row)
    errors, warnings = validation.get('errors', []), validation.get('warnings', [])
    status = validation.get('status', 'failed' if code else 'unknown')
    print(f'{icon_id}: {status}; {len(errors)} errors; {len(warnings)} warnings')
    for message in errors + warnings:
        print(f'  {message}')
    svg = root / f'{icon_id}.svg'
    if svg.exists():
        document = svg.read_text()
        digest = hashlib.sha256(document.encode()).hexdigest()
        if row.get('svg_sha256') and row['svg_sha256'] != digest:
            raise ValueError('export does not match its manifest hash')
        import cairosvg
        from PIL import Image
        canvas = factory().profile.spec.canvas_size
        panels = []
        for name, ink, background in [('light', '#141413', '#ffffff'), ('dark', '#f5f4ef', '#1c1c19')]:
            themed = document.replace('currentColor', ink)
            path = out / f'{name}.png'
            cairosvg.svg2png(bytestring=themed.encode(), write_to=str(path),
                            output_width=canvas, output_height=canvas, background_color=background)
            with Image.open(path) as rendered:
                native = rendered.convert('RGB')
            panel = Image.new('RGB', (canvas * 4, canvas * 3), background)
            enlarged_bytes = cairosvg.svg2png(bytestring=themed.encode(),
                                              output_width=canvas * 3, output_height=canvas * 3,
                                              background_color=background)
            with Image.open(io.BytesIO(enlarged_bytes)) as enlarged:
                panel.paste(enlarged.convert('RGB'), (0, 0))
            panel.paste(native, (canvas * 3, canvas))
            panels.append(panel)
        sheet = Image.new('RGB', (canvas * 8, canvas * 3))
        for index, panel in enumerate(panels):
            sheet.paste(panel, (index * canvas * 4, 0))
        sheet.save(out / 'review.png')
        print(f'SVG: {svg}\nPreview (light/dark, enlarged/native): {out / "review.png"}')
    print(f'Manifest: {manifest}\nLog: {log}')
    print('Visual fidelity still requires inspection; numeric success is not visual approval.')
    return code or int(bool(errors or warnings) or status != 'valid')


if __name__ == '__main__':
    raise SystemExit(main())
