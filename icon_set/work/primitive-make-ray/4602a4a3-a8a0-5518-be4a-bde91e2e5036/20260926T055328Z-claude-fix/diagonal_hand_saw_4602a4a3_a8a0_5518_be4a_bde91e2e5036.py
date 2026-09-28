"""A hand saw lying diagonally: a long toothed blade reaching up-left from a diamond grip loop.

Symbol plan: the grip is a closed 45-degree diamond loop about (34, 34), half-diagonal 8
(its stroke is the handle, its inside the finger hole, 7 ink wide). The blade is one open
outline whose two ends are the diamond's top and left vertices, so the diamond's upper-left
side is the blade heel. Its straight back runs at 45 degrees (y = x - 8) to the tip at
(14, 6); a square tip edge drops to (6, 14), and the cutting edge returns to the heel as a
5-unit 45-degree staircase (the reference's stepped teeth): tooth points on y = x + 13,
roots on y = x + 8, 11.3 below the back.
Lucide construction: no Lucide saw exists; closed diamond loop and straight 45-degree runs
follow Lucide's plain-polygon construction. The earlier square-handle attempt (attempts/)
read as a key, so the grip became a stroked loop and the blade grew.
Keyshape SQUARE: centerline 6..42 (tip y 6, teeth x 6, grip right/bottom 42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4602a4a3-a8a0-5518-be4a-bde91e2e5036"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__diagonal-hand-saw/20260926T055140Z-thuan-mac/reference/tools saw_4602a4a3-a8a0-5518-be4a-bde91e2e5036.svg"
AUTHOR = "claude-opus-5-5"


class DiagonalHandSaw(Solo48):
    icon_id = "diagonal-hand-saw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tool"
    aliases = ("tools saw", "saw", "handsaw")
    keywords = ("saw", "tool", "carpentry", "woodwork", "cut", "diy", "construction", "hardware")

    def build(self) -> None:
        c, h = 34, 8
        top, right, bottom, left = (c, c - h), (c + h, c), (c, c + h), (c - h, c)
        self.add_polyline("grip", top, right, bottom, left, closed=True)
        step = 5
        pts = [top, (14, 6), (6, 14)]
        # staircase from the tip back to the heel: down then right
        x, y = 6, 14
        while (x, y) != left:
            y += step
            pts.append((x, y))
            x += step
            pts.append((x, y))
        self.add_polyline("blade", *pts)
        self.relate("connect", "grip", "blade")
