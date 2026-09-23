"""Preview-only SUB32 redraws for the seven unresolved side subs.

These classes are deliberately outside the icon registry. Every drawing uses
the real Sub32 authoring API, a 32x32 SVG root, and a 4px stroke. The gallery
records validation findings without claiming that a failed drawing passed.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

import cairosvg
from PIL import Image, ImageDraw, ImageFont

from icon_set.model.icons.sub._base import Sub32
from icon_set.model.icons.sub._compact_reference_helpers import circle, rounded_rect
from icon_set.model.keyshapes import Keyshape
from icon_set.validation.library_qa import inspect_icon


OUT = Path(__file__).resolve().parent
PRIOR = OUT.parent / "strict32-evidence"


class Bluetooth(Sub32):
    icon_id = "bluetooth-wireless-connectivity-symbol-v3-preview"
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_polyline("bluetooth", (10, 11), (23, 21), (16, 25),
                          (16, 7), (23, 11), (10, 21))


class Bitcoin(Sub32):
    icon_id = "bitcoin-cryptocurrency-symbol-sub32-v3-preview"
    keyshape = Keyshape.CIRCLE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "objects/finance"

    def build(self):
        circle(self, "frame", 16, 16, 14)
        self.add_line("stem", (12, 8), (12, 24))
        self.add_polyline("upper-bowl", (12, 8), (19, 8), (23, 12),
                          (19, 16), (12, 16))
        self.add_polyline("lower-bowl", (12, 16), (19, 16), (23, 20),
                          (19, 24), (12, 24))
        for name, x in (("left", 13), ("right", 19)):
            self.add_line(name + "-top", (x, 8), (x, 7))
            self.add_line(name + "-bottom", (x, 24), (x, 25))


class Battery(Sub32):
    icon_id = "charging-battery-symbol-v3-preview"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"

    def build(self):
        rounded_rect(self, "case", 2, 4, 24, 28, 4)
        self.add_line("terminal", (30, 12), (30, 20))
        self.add_polyline("bolt", (17, 9), (11, 17), (17, 17), (13, 24))


class ChatClock(Sub32):
    icon_id = "chat-bubble-with-clock-v3-preview"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"

    def build(self):
        self.add_line("top", (7, 2), (25, 2))
        self.add_arc("top-right", (25, 2), (30, 7), radius_x=5)
        self.add_line("right", (30, 7), (30, 21))
        self.add_arc("bottom-right", (30, 21), (25, 26), radius_x=5)
        self.add_line("bottom", (25, 26), (10, 26))
        self.add_line("tail-top", (10, 26), (3, 30))
        self.add_line("tail-bottom", (3, 30), (5, 23))
        self.add_arc("bottom-left", (5, 23), (2, 20), radius_x=3)
        self.add_line("left", (2, 20), (2, 7))
        self.add_arc("top-left", (2, 7), (7, 2), radius_x=5)
        self.add_contour("bubble", "top", "top-right", "right", "bottom-right",
                         "bottom", "tail-top", "tail-bottom", "bottom-left",
                         "left", "top-left", closed=True)
        circle(self, "clock", 16, 14, 6)
        self.add_polyline("hands", (16, 11), (16, 14), (19, 16))


class CheckCross(Sub32):
    icon_id = "check-and-cross-square-v3-preview"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "primitives/symbol"

    def build(self):
        rounded_rect(self, "frame", 2, 2, 30, 30, 4)
        self.add_polyline("check", (8, 15), (10, 18), (12, 12))
        self.add_line("divider", (18, 7), (15, 25))
        self.add_line("cross-a", (21, 17), (25, 22))
        self.add_line("cross-b", (25, 17), (21, 22))


class HeartGift(Sub32):
    icon_id = "heart-gift-box-v3-preview"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives/symbol"

    def build(self):
        rounded_rect(self, "box", 2, 12, 30, 30, 3)
        self.add_bezier("left-bow", (16, 12), ((11, 12), (8, 9), (8, 6)),
                        ((8, 2), (13, 2), (16, 12)))
        self.add_bezier("right-bow", (16, 12), ((19, 2), (24, 2), (24, 6)),
                        ((24, 9), (21, 12), (16, 12)))
        self.add_bezier("heart", (16, 25), ((10, 21), (7, 18), (10, 16)),
                        ((12, 14), (15, 16), (16, 18)),
                        ((17, 16), (20, 14), (22, 16)),
                        ((25, 18), (22, 21), (16, 25)))
        self.add_contour("heart-shape", "heart", closed=True)


class Won(Sub32):
    icon_id = "won-sub32-v3-preview"
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "objects/finance"

    def build(self):
        self.add_polyline("w", (4, 5), (10, 27), (16, 8), (22, 27), (28, 5))
        self.add_line("bar", (2, 17), (30, 17))


ITEMS = [
    ("Bluetooth", Bluetooth, "809bf53d-f979-4aa8-bf75-748eb9b9dacd", "pictographic-primitives/other/circle bluetooth_809bf53d-f979-4aa8-bf75-748eb9b9dacd.svg", "bluetooth-wireless-connectivity-symbol-v2.svg"),
    ("Bitcoin", Bitcoin, "056563c8-a6c4-4201-b355-6ff5f08795ea", "pictographic-primitives/other/circle bitcoin_056563c8-a6c4-4201-b355-6ff5f08795ea.svg", "bitcoin-cryptocurrency-symbol-sub32-v2.svg"),
    ("Charging battery", Battery, "638f0a9f-914c-4078-b32c-13c8ec4aacf6", "pictographic-primitives/other/battery 1_638f0a9f-914c-4078-b32c-13c8ec4aacf6.svg", "charging-battery-symbol-v2.svg"),
    ("Chat with clock", ChatClock, "18f6d5a3-0426-4e7b-b6b1-88cb5fcf97ed", "pictographic-primitives/symbol/chat time clock_18f6d5a3-0426-4e7b-b6b1-88cb5fcf97ed.svg", "chat-bubble-with-clock-v2.svg"),
    ("Check and cross", CheckCross, "7dbf66c8-b270-487e-b0d5-155420bf9983", "pictographic-primitives/other/rectangle remove and check_7dbf66c8-b270-487e-b0d5-155420bf9983.svg", "check-and-cross-square-v2.svg"),
    ("Heart gift box", HeartGift, "15e4830e-dce1-452c-9f05-87646ea11df9", "pictographic-primitives/romance/love gift box heart_15e4830e-dce1-452c-9f05-87646ea11df9.svg", "heart-gift-box-v2.svg"),
    ("Korean won", Won, "18f047b9-f81e-571a-a3ea-2c4af962bcb7", "pictographic-primitives/money/won_18f047b9-f81e-571a-a3ea-2c4af962bcb7.svg", "won-sub32-v2.svg"),
]


def png(svg: bytes, size: int) -> Image.Image:
    return Image.open(__import__("io").BytesIO(cairosvg.svg2png(
        bytestring=svg, output_width=size, output_height=size))).convert("RGBA")


def on_white(image: Image.Image) -> Image.Image:
    result = Image.new("RGB", image.size, "white")
    result.paste(image, mask=image.getchannel("A"))
    return result


def main() -> None:
    font = ImageFont.load_default()
    sheet = Image.new("RGB", (800, 7 * 165 + 42), "white")
    draw = ImageDraw.Draw(sheet)
    draw.text((16, 12), "Original              Previous 32px          New 32px (enlarged)         New actual size", fill="#111", font=font)
    rows = []
    for index, (label, cls, uuid, source, prior_name) in enumerate(ITEMS):
        icon = cls()
        svg = icon.to_svg().encode()
        row = inspect_icon(icon)
        name = cls.icon_id
        (OUT / (name + ".svg")).write_bytes(svg)
        on_white(png(svg, 32)).save(OUT / (name + "-32.png"))
        on_white(png(svg, 256)).save(OUT / (name + "-256.png"))
        original = png((ROOT / source).read_bytes(), 128)
        previous = png((PRIOR / prior_name).read_bytes(), 128)
        new = png(svg, 128)
        y = 42 + index * 165
        draw.text((16, y + 5), f"{index + 1}. {label}", fill="#111", font=font)
        for image, x in ((original, 16), (previous, 198), (new, 380)):
            sheet.paste(image, (x, y + 25), image)
        native = png(svg, 32)
        sheet.paste(native, (585, y + 60), native)
        draw.text((635, y + 60), row["status"], fill="#b42318" if row["status"] != "pass" else "#008040", font=font)
        draw.line((0, y + 162, 800, y + 162), fill="#ddd", width=1)
        rows.append({"name": label, "source_uuid": uuid, "candidate": name,
                     "svg": name + ".svg", "status": row["status"],
                     "errors": row["errors"], "warnings": row["warnings"]})
    sheet.save(OUT / "comparison.png")
    (OUT / "review.json").write_text(json.dumps(rows, indent=2) + "\n")
    cards = []
    for row in rows:
        messages = "".join(f"<li>{__import__('html').escape(s)}</li>" for s in row["errors"] + row["warnings"])
        cards.append(f'''<section><h2>{row['name']}</h2><div class="views"><div><p>Original</p><img src="../../../../{next(x[3] for x in ITEMS if x[2] == row['source_uuid'])}"></div><div><p>Previous</p><img src="../strict32-evidence/{next(x[4] for x in ITEMS if x[2] == row['source_uuid'])}"></div><div><p>New at 32px</p><img class="native" src="{row['svg']}"></div><div><p>New enlarged</p><img src="{row['svg']}"></div></div><p><b>Validation: {row['status']}</b></p><details><summary>Findings</summary><ul>{messages or '<li>None</li>'}</ul></details></section>''')
    html = '<!doctype html><html><head><meta charset="utf-8"><title>Seven SUB32 redraws</title><style>body{font:16px system-ui;max-width:1100px;margin:30px auto;padding:0 20px}section{border-bottom:1px solid #ccc;padding:16px 0}.views{display:flex;gap:30px;align-items:start}.views>div{width:180px}.views img{width:128px;height:128px;object-fit:contain}.views img.native{width:32px;height:32px}details{font-size:13px;color:#555}p{margin:8px 0}</style></head><body><h1>Seven new 32×32 sub icon previews</h1><p>Every new SVG uses a 32×32 viewBox and 4px strokes. Validation findings are shown for review.</p>' + ''.join(cards) + '</body></html>'
    (OUT / "review.html").write_text(html)
    print(f"Wrote {len(rows)} previews to {OUT}")
    for row in rows:
        print(row["name"], row["status"], len(row["errors"]), len(row["warnings"]))


if __name__ == "__main__":
    main()
