"""Create isolated before/after SOLO48 candidates; never publish to the library.

Run: python3 -m icon_set.scripts.preview_keyshape_fit
"""
from __future__ import annotations

import argparse
import html
import io
import json
from pathlib import Path

from icon_set.model.icons.registry import create
from icon_set.model.keyshapes import Keyshape
from icon_set.renderers.png import render_png


DEFAULT_ICONS = ["compact-disc", "baby-bib", "a-frame-church",
                 "analogue-wristwatch", "necktie", "round-eyeglasses"]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--icons", nargs="+", default=DEFAULT_ICONS)
    parser.add_argument("--output", type=Path, default=Path("icon_set/work/keyshape-fit-preview"))
    args = parser.parse_args(argv)
    from PIL import Image, ImageDraw

    args.output.mkdir(parents=True, exist_ok=True)
    sheet = Image.new("RGB", (1000, 240 * len(args.icons)), "white")
    pen = ImageDraw.Draw(sheet)
    reports, cards = [], []
    for index, icon_id in enumerate(args.icons):
        original = create(icon_id)
        keyshape = original.keyshape
        if keyshape.orientation == "landscape":
            keyshape = Keyshape.HRECT_L
        elif keyshape.orientation == "portrait":
            keyshape = Keyshape.VRECT_L
        result = original.fit_to_keyshape(keyshape)
        folder = args.output / icon_id
        folder.mkdir(parents=True, exist_ok=True)
        original.export_icon_to(folder / "before.svg")
        result.icon.export_icon_to(folder / "after.svg")
        original.export_json_graph(folder / "before.json")
        result.icon.export_json_graph(folder / "after.json")
        (folder / "report.json").write_text(json.dumps(result.report, indent=2) + "\n", encoding="utf-8")
        reports.append(result.report)
        qa = result.report["validation"]
        y = index * 240
        pen.text((16, y + 8), f"{icon_id}  ->  {keyshape.name}   scale {result.report['scale']:.3f}   QA: {qa['status']}", fill="black")
        for theme, background, ink, offset in [("Light", "#ffffff", "#111111", 0),
                                               ("Dark", "#171b24", "#f4f6fa", 500)]:
            pen.rectangle((offset, y + 30, offset + 499, y + 239), fill=background)
            for col, (label, icon) in enumerate([("Before", original), ("Candidate", result.icon)]):
                x = offset + col * 250
                pen.text((x + 12, y + 38), f"{theme} / {label}", fill=ink)
                for scale, dx in [(3, 10), (1, 182)]:
                    png = render_png(icon, ink=ink, scale=scale)
                    picture = Image.open(io.BytesIO(png)).convert("RGBA")
                    sheet.paste(picture, (x + dx, y + 72), picture)
        errors = "".join(f"<li>{html.escape(e)}</li>" for e in qa["errors"] + qa["warnings"] + result.report["notes"])
        cards.append(f'<article><h2>{html.escape(icon_id)} → {keyshape.name}</h2>'
                     f'<p>QA: {qa["status"]}. Visual review required.</p>'
                     f'<a href="{icon_id}/before.json">Before graph</a> · '
                     f'<a href="{icon_id}/after.json">Candidate graph</a> · '
                     f'<a href="{icon_id}/report.json">Full report</a><ul>{errors}</ul></article>')
        print(f"{icon_id}: {qa['status']}")
    sheet.save(args.output / "comparison.png")
    (args.output / "results.json").write_text(json.dumps(reports, indent=2) + "\n", encoding="utf-8")
    (args.output / "index.html").write_text(
        '<!doctype html><meta charset="utf-8"><title>Solo keyshape fitting review</title>'
        '<style>body{font:16px system-ui;max-width:1050px;margin:32px auto;padding:16px}'
        'img{max-width:100%}article{border-top:1px solid #bbb;padding:12px 0}</style>'
        '<h1>Solo keyshape fitting review</h1><p>Uniform scaling with fixed 4-unit stroke and '
        'integer snapping. Originals are preserved. Candidates require visual review; '
        'failed candidates need geometry adjustments before release. Each pair is shown '
        'at 3× and native 48 px.</p><img src="comparison.png" alt="Before and candidate icons '
        'in light and dark themes">' + ''.join(cards), encoding="utf-8")


if __name__ == "__main__":
    main()
