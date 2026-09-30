"""v1 | v2 contact sheets (and v2 SVGs) for every staged module."""
import io, json, sys
from pathlib import Path
import cairosvg
from PIL import Image, ImageDraw
sys.path.insert(0, '.')
from icon_set.scripts.container_v2_fit import load_classes, WORK
from icon_set.model.icons.registry import create
out = WORK / 'svg'; out.mkdir(exist_ok=True)
report = json.loads((WORK / 'report.json').read_text())
rows = []
for path in sorted(WORK.glob('*.py')):
    if path.name in ('baseline.py', 'categorize.py', 'sheet.py'):
        continue
    for cls in load_classes(path):
        v2 = cls().to_svg()
        (out / f'{cls.icon_id}.svg').write_text(v2)
        rows.append((cls.icon_id, create(cls.icon_id).to_svg(), v2))
only = set(sys.argv[1:])
if only:
    rows = [r for r in rows if r[0] in only]
def png(svg, size=128):
    return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(), output_width=size, output_height=size, background_color='white')))
per = 30
for page in range(0, len(rows), per):
    chunk = rows[page:page + per]
    cols = 5
    sheet = Image.new('RGB', (cols * 290, ((len(chunk) + cols - 1) // cols) * 160), 'white')
    d = ImageDraw.Draw(sheet)
    for i, (iid, v1, v2) in enumerate(chunk):
        x, y = (i % cols) * 290, (i // cols) * 160
        sheet.paste(png(v1), (x + 8, y + 4)); sheet.paste(png(v2), (x + 146, y + 4))
        d.rectangle([x + 146 + 8, y + 4 + 8, x + 146 + 120, y + 4 + 120], outline=(120, 170, 220))
        st = report.get(iid, {}).get('status', '?')
        d.text((x + 8, y + 136), f'{iid[:40]} [{st}]', fill=(200, 0, 0) if st != 'pass' else (0, 0, 0))
    sheet.save(WORK / f'sheet-{page // per + 1:02d}.png')
print(len(rows), 'icons')
