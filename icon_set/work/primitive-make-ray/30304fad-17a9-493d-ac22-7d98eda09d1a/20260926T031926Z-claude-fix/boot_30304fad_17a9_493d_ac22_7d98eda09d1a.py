"""An ankle boot in side view, toe to the right, with a cuffed top and two lace marks.

Symbol plan: one closed outline. The cuff is a rounded band (r2 corners) 2 wider than the
shaft on both sides, stepping in at 45 degrees to the shaft walls. The front wall drops
straight, then a smooth cubic run turns it into the instep and a rounded toe; the sole is
flat with r3 corners at heel and toe. Two lace marks run inward, square to the outline:
one from the front wall, one from the instep curve.
Lucide construction: 'footprints'/'boot' style - one continuous closed silhouette,
straight shaft and a cubic instep into a round toe.
Keyshape SQUARE: centerline x 6..42 (cuff back, toe), y 6..42 (cuff top, sole).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "30304fad-17a9-493d-ac22-7d98eda09d1a"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__boot/20260926T030905Z-thuan-mac/reference/boot_30304fad-17a9-493d-ac22-7d98eda09d1a.svg"
AUTHOR = "claude-opus-5-5"


class Boot(Solo48):
    icon_id = "boot"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "clothing/footwear"
    aliases = ("ankle-boot", "work-boot")
    keywords = ("boot", "shoe", "footwear", "ankle", "hiking", "work", "winter", "laces", "clothing")

    def build(self) -> None:
        back, front, sole = 8, 22, 42
        self.add_line("lip-back", (back, 15), (6, 13))
        self.add_line("cuff-back", (6, 13), (6, 8))
        self.add_arc("cuff-corner-back", (6, 8), (8, 6), radius_x=2, sweep=True)
        self.add_line("cuff-top", (8, 6), (22, 6))
        self.add_arc("cuff-corner-front", (22, 6), (24, 8), radius_x=2, sweep=True)
        self.add_line("cuff-front", (24, 8), (24, 13))
        self.add_line("lip-front", (24, 13), (front, 15))
        self.add_line("front-wall", (front, 15), (front, 20))
        self.add_bezier("instep-upper", (front, 20), ((front, 24.5), (23, 26.5), (25, 28)))
        self.add_bezier("instep-lower", (25, 28), ((27, 29.5), (29.5, 30), (33, 30)))
        self.add_bezier("toe", (33, 30), ((39, 30), (42, 32), (42, 36)))
        self.add_line("toe-front", (42, 36), (42, 39))
        self.add_arc("toe-corner", (42, 39), (39, sole), radius_x=3, sweep=True)
        self.add_line("sole", (39, sole), (back + 3, sole))
        self.add_arc("heel-corner", (back + 3, sole), (back, 39), radius_x=3, sweep=True)
        self.add_line("back-wall", (back, 39), (back, 15))
        self.add_contour("outline", "lip-back", "cuff-back", "cuff-corner-back", "cuff-top",
                         "cuff-corner-front", "cuff-front", "lip-front", "front-wall",
                         "instep-upper", "instep-lower", "toe", "toe-front", "toe-corner",
                         "sole", "heel-corner", "back-wall", closed=True)
        self.add_line("lace-upper", (front, 20), (17, 20))
        self.add_line("lace-lower", (25, 28), (22, 32))
        self.relate("connect", "outline", "lace-upper")
        self.relate("connect", "outline", "lace-lower")
