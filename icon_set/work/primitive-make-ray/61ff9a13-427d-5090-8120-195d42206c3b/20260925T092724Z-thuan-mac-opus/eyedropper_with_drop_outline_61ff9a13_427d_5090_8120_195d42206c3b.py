"""Colour picker: an eyedropper on the diagonal, bulb at upper right, whose
nozzle points into an open teardrop outline at lower left - the picked drop.

Symbol plan: the dropper is built on the 45-degree axis x + y = 48 (see
``pipette``): one closed outline (tapered barrel, straight walls, bulb cap),
a nozzle stroke and a split collar. The drop is one open run - a round
upper-left side into a pointed bottom and a short straight return - opening
toward the nozzle tip, which sits 8+ from every part of it.
Keyshape SQUARE, centerline box (6,6)-(42,42).
Lucide construction: pipette (diagonal dropper with collar and rounded
bulb) and droplet (round top into a pointed end).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "61ff9a13-427d-5090-8120-195d42206c3b"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__eyedropper-with-open-pointed-outline/20260925T092530Z-thuan-mac/reference/color picker 1_61ff9a13-427d-5090-8120-195d42206c3b.svg"
AUTHOR = "claude-opus-5-5"


class EyedropperWithDropOutline(Solo48):
    icon_id = "eyedropper-with-open-pointed-outline"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    aliases = ("color picker", "eyedropper", "pipette")
    keywords = ("color", "picker", "eyedropper", "pipette", "drop")

    def build(self) -> None:
        self.pipette(tip=(16, 32), nozzle=(20, 28), shoulder=(23, 25), collar=(30, 18), cap=(38, 10))
        point = (14, 42)
        self.add_bezier("drop-1", (11, 22),
                        ((8, 23), (6, 27), (6, 31)),
                        ((6, 35), (10, 39), point))
        self.add_line("drop-2", point, (18, 40))
        self.add_contour("drop", "drop-1", "drop-2")

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
