"""A Chinese decorative knot: a woven diamond lattice with side loops, hanging from a cord
that ends in a tassel.

Symbol plan: a diamond (half-diagonal 12) about (24,18) woven as a 2x2 lattice -- two
45-degree cords cross at the centre and meet each side at its midpoint, so every cell is
the same diamond (8.5 across). Round ear loops (r3) sit on the left and right corners, and
the bottom corner drops a cord into a small arched tassel. Everything mirrors about x=24.
Lucide construction: no knot glyph; the lattice follows Lucide 'grid' construction turned
45 degrees, the tassel arch the round-cap arch of 'bell'.
Keyshape SQUARE: centerline x 6..42 (ear loops), y 6..42 (top corner, tassel hem).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "66f50153-1867-5790-86d6-291d9de28b8f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__chinese-endless-knot/20260925T093141Z-thuan-mac/reference/chinese ornament_66f50153-1867-5790-86d6-291d9de28b8f.svg"
AUTHOR = "claude-opus-5-5"


class ChineseEndlessKnot(Solo48):
    icon_id = "chinese-endless-knot"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/ornament"
    aliases = ("chinese-ornament", "chinese-knot", "endless-knot", "pan-chang")
    keywords = ("chinese", "knot", "ornament", "decoration", "new-year", "lunar", "luck", "tassel")

    def build(self) -> None:
        cx, cy, h = 24, 18, 12
        top, right, bottom, left = (cx, cy - h), (cx + h, cy), (cx, cy + h), (cx - h, cy)
        ul, ur, lr, ll = (cx - 6, cy - 6), (cx + 6, cy - 6), (cx + 6, cy + 6), (cx - 6, cy + 6)
        # diamond outline, split where the lattice cords meet each side
        self.add_polyline("diamond", top, ur, right, lr, bottom, ll, left, ul, closed=True)
        # lattice: two cords crossing at the centre, side midpoint to opposite side midpoint
        self.add_line("cord-a1", ul, (cx, cy))
        self.add_line("cord-a2", (cx, cy), lr)
        self.add_line("cord-b1", ur, (cx, cy))
        self.add_line("cord-b2", (cx, cy), ll)
        self.add_contour("cord-a", "cord-a1", "cord-a2")
        self.add_contour("cord-b", "cord-b1", "cord-b2")
        self.relate("connect", "diamond", "cord-a")
        self.relate("connect", "diamond", "cord-b")
        self.relate("connect", "cord-a", "cord-b")
        # ear loops on the side corners
        for side, corner, s in (("left", left, -1), ("right", right, 1)):
            far = (corner[0] + s * 6, corner[1])
            self.add_arc(f"ear-{side}-top", corner, far, radius_x=3, sweep=(s == 1))
            self.add_arc(f"ear-{side}-bottom", far, corner, radius_x=3, sweep=(s == 1))
            self.add_contour(f"ear-{side}", f"ear-{side}-top", f"ear-{side}-bottom", closed=True)
            self.relate("connect", "diamond", f"ear-{side}")
        # hanging cord and tassel arch
        self.add_line("hang-cord", bottom, (cx, 38))
        self.add_arc("tassel-left", (cx, 38), (cx - 4, 42), radius_x=4, sweep=False)
        self.add_arc("tassel-right", (cx, 38), (cx + 4, 42), radius_x=4, sweep=True)
        self.relate("connect", "diamond", "hang-cord")
        self.relate("connect", "hang-cord", "tassel-left")
        self.relate("connect", "hang-cord", "tassel-right")
