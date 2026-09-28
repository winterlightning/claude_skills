"""Colour picker: an eyedropper on the diagonal, tip at lower left and
rounded bulb at upper right with a collar between bulb and barrel, beside a
round colour sample at lower right.

Symbol plan: the dropper is built on the 45-degree axis x + y = 48 (see
``pipette``): one closed outline (tapered barrel, straight walls, bulb cap),
a nozzle stroke and a split collar. The sample is a radius-5 circle whose
centre lies 14 from the near wall, clearing it by 9. Mirror-symmetric about
the dropper axis except the sample.
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: pipette (diagonal dropper with collar and rounded bulb).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "23e4bb5e-d3ef-5855-950c-33bdbdf61648"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__eyedropper-beside-round-sample/20260925T092530Z-thuan-mac/reference/color picker 3_23e4bb5e-d3ef-5855-950c-33bdbdf61648.svg"
AUTHOR = "claude-opus-5-5"


class EyedropperBesideRoundSample(Solo48):
    icon_id = "eyedropper-beside-round-sample"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    aliases = ("color picker", "eyedropper", "pipette")
    keywords = ("color", "picker", "eyedropper", "pipette", "sample", "swatch")

    def build(self) -> None:
        self.pipette(tip=(6, 42), nozzle=(12, 36), shoulder=(18, 30), collar=(29, 19), cap=(38, 10))
        cx, cy, r = 37, 37, 5
        self.add_arc("sample-1", (cx, cy - r), (cx, cy + r), radius_x=r)
        self.add_arc("sample-2", (cx, cy + r), (cx, cy - r), radius_x=r)
        self.add_contour("sample", "sample-1", "sample-2", closed=True)

    def pipette(self, tip, nozzle, shoulder, collar, cap):
        """Eyedropper on the 45-degree axis x + y = const.

        Walls sit (3,3) either side of the axis (8.5 apart); the collar
        crosses both walls at split nodes and overhangs by (2,2). The bulb cap
        is two quarter runs through a rightmost and a topmost node, 4 from its
        centre, so its extremes are exact nodes.
        """
        def off(p, d):
            return (p[0] + d, p[1] + d)
        cx, cy = cap
        w1_top, w2_top = off(cap, 3), off(cap, -3)
        self.add_line("nozzle", tip, nozzle)
        self.add_line("body-1", nozzle, off(shoulder, 3))
        self.add_line("body-2", off(shoulder, 3), off(collar, 3))
        self.add_line("body-3", off(collar, 3), w1_top)
        self.add_bezier("body-4", w1_top, ((cx + 4, cy + 2), (cx + 4, cy + 1.5), (cx + 4, cy)),
                        ((cx + 4, cy - 2.2), (cx + 2.2, cy - 4), (cx, cy - 4)))
        self.add_bezier("body-5", (cx, cy - 4), ((cx - 1.5, cy - 4), (cx - 2, cy - 4), w2_top))
        self.add_line("body-6", w2_top, off(collar, -3))
        self.add_line("body-7", off(collar, -3), off(shoulder, -3))
        self.add_line("body-8", off(shoulder, -3), nozzle)
        self.add_contour("body", *[f"body-{i}" for i in range(1, 9)], closed=True)
        self.add_line("collar-1", off(collar, 5), off(collar, 3))
        self.add_line("collar-2", off(collar, 3), off(collar, -3))
        self.add_line("collar-3", off(collar, -3), off(collar, -5))
        for part in ("nozzle", "collar-1", "collar-2", "collar-3"):
            self.relate("connect", "body", part)
