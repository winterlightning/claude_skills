"""cylindrical marshmallow on slanted stick (redraw of the new-pipeline traced SVG).

Subject: a plump cylindrical marshmallow at the upper right, seen slightly
from above (open elliptical top, straight sides, curved bottom), skewered on
a straight stick that slants down to the lower left.

Plan: SQUARE (centerline box (6,6)-(42,42)), the suggested keyshape.
- rim: one ellipse rx 10 / ry 5 about (32,11); back half is the top of the
  body contour (apex (32,6), the y 6 extreme), front half is a separate arc
  sharing both side nodes (22,11) / (42,11), declared connected.
- body: sides x 22 / 42 from y 11 to 24 (x 42 is the right extreme), bottom
  is the same ellipse shifted down 13 about (32,24), split at the integer
  ellipse point (24,27) (64/100 + 9/25 = 1) where the stick leaves.
- stick: one line (24,27) -> (6,42), the x 6 / y 42 extremes, about 40
  degrees like the image's diagonal; the shared node is declared connected.
Lucide `cylinder` informed the rim-plus-sides construction; no marshmallow
or skewer original exists, and the stick's slant is deliberately asymmetric.

Metric issues (cylindrical-marshmallow-on-slanted-stick_metrics.json):
- stroke-width (info, trace 2.39 fitted): redrawn at stroke 4 with every
  gap budgeted for stroke 4.
- keyshape-short-axis (warn, SQUARE x fill 86%): fixed; the stick end sits
  on (6,42) and the body side on x 42, the rim apex on y 6, so all four
  extremes are exactly on the box without stretching the marshmallow.
- clearance (error, rim back and front 5.78 apart): fixed; the rim ellipse
  is 10 deep on centerlines (ry 5), so the two halves are 10 apart.
- hole (error, top opening 1.8 inscribed): fixed; the rim opening is 6
  inscribed at stroke 4, and the body band between the rim front and the
  bottom arc is 13 on centerlines (9 of ink), a
  taller body than the first 11-unit try so it reads as a marshmallow.
The trace's small kink where its rim met the right side is replaced by
shared tangent-vertical ellipse nodes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "51eb3863-a02f-4624-ba65-ff48208cd5b7"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1059-cylindrical-marshmallow-on-slanted-stick/cylindrical-marshmallow-on-slanted-stick_raw.svg"
AUTHOR = "claude-opus-5-5"

CX = 32                   # cylinder axis
RX, RY = 10, 5            # rim / bottom ellipse radii
RIM_Y = 11                # rim ellipse centre (apex y 6)
BASE_Y = 24               # bottom ellipse centre (lowest point y 29)
STICK_NODE = (24, 27)     # integer point on the bottom ellipse (dx -8, dy 3)
STICK_END = (6, 42)


class CylindricalMarshmallowOnSlantedStickRedraw(Solo48):
    icon_id = "cylindrical-marshmallow-on-slanted-stick-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food/sweets"
    aliases = ("marshmallow on stick", "roasting marshmallow", "toasted marshmallow")
    keywords = ("marshmallow", "stick", "skewer", "campfire", "camping", "roast", "s'mores", "candy", "sweet", "food")

    def build(self) -> None:
        left, right = CX - RX, CX + RX
        rim_l, rim_r = (left, RIM_Y), (right, RIM_Y)
        base_l, base_r = (left, BASE_Y), (right, BASE_Y)

        self.add_arc("rim-back", rim_l, rim_r, radius_x=RX, radius_y=RY, sweep=True)
        self.add_line("side-r", rim_r, base_r)
        self.add_arc("bottom-r", base_r, STICK_NODE, radius_x=RX, radius_y=RY, sweep=True)
        self.add_arc("bottom-l", STICK_NODE, base_l, radius_x=RX, radius_y=RY, sweep=True)
        self.add_line("side-l", base_l, rim_l)
        self.add_contour("body", "rim-back", "side-r", "bottom-r", "bottom-l", "side-l", closed=True)

        self.add_arc("rim-front", rim_r, rim_l, radius_x=RX, radius_y=RY, sweep=True)
        self.relate("connect", "rim-front", "body")

        self.add_line("stick", STICK_NODE, STICK_END)
        self.relate("connect", "stick", "body")
