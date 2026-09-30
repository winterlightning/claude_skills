"""Big renders on a 1-unit grid with the 32x32 symbol slot and the centre lines.

    python3 closeup.py OUT.png ICON_ID [ICON_ID ...]   # v1 (git HEAD SVG) | v2 (current model)

``frame(paths)`` is importable for rendering candidate path data.
"""
import io
import re
import subprocess
import sys


def frame(paths, label=''):
    grid = ''.join(f'<path d="M{i} 0V64M0 {i}H64" stroke="#{"c9d3cc" if i % 8 == 0 else "eef1ee"}" stroke-width=".12"/>'
                   for i in range(1, 64))
    ink = ''.join(f'<path d="{d}"/>' for d in paths)
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1 -1 66 66">'
            f'<rect width="64" height="64" fill="white" stroke="#999" stroke-width=".2"/>{grid}'
            '<path d="M32 0V64M0 32H64" stroke="#e05555" stroke-width=".2"/>'
            '<rect x="16" y="16" width="32" height="32" fill="none" stroke="#3b82f6" stroke-width=".3" stroke-dasharray="1 .6"/>'
            f'<g fill="none" stroke="#111" stroke-opacity=".85" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{ink}</g>'
            f'<g fill="none" stroke="#f59e0b" stroke-width=".25">{ink}</g></svg>')


def main():
    import cairosvg
    from PIL import Image, ImageDraw
    sys.path.insert(0, '.')
    from icon_set.model.icons.registry import create
    out, ids = sys.argv[1], sys.argv[2:]
    tiles = []
    for iid in ids:
        v1 = subprocess.run(['git', 'show', f'HEAD:published/container64/{iid}.svg'], capture_output=True, text=True).stdout
        for svg in (v1, create(iid).to_svg()):
            d = re.findall(r' d="([^"]+)"', svg)
            tiles.append(Image.open(io.BytesIO(cairosvg.svg2png(bytestring=frame(d).encode(), output_width=520, output_height=520))))
    sheet = Image.new('RGB', (1060, 540 * len(ids)), 'white')
    draw = ImageDraw.Draw(sheet)
    for i, tile in enumerate(tiles):
        sheet.paste(tile, ((i % 2) * 530, (i // 2) * 540))
        draw.text(((i % 2) * 530 + 8, (i // 2) * 540 + 522), f"{ids[i // 2]} {'v1' if i % 2 == 0 else 'v2'}", fill='black')
    sheet.save(out)


if __name__ == '__main__':
    main()
