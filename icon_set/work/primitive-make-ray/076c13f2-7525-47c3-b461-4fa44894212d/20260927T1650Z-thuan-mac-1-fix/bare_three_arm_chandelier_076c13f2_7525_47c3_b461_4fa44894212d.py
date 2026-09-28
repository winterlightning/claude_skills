"""Bare three-arm chandelier.

Plan: shared axis x=24. Ceiling cap and stem on the axis; two mirrored U bowls
(half circles r 8) hang from outer candle posts at x=8/40 and
meet the stem in a cusp at (24,22). Three equal drip collars (half width 2) sit
on one row y=16, crossing the two posts and the stem. Outer candles rise to y=9.
A short finial hangs below the cusp. Keyshape SQUARE: collars reach x 6/42,
cap y 6, finial y 42. Lucide lamp-ceiling informed the cap + stem construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "076c13f2-7525-47c3-b461-4fa44894212d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bare-three-arm-chandelier/20260927T164350Z-thuan-mac-1/reference/chandelier_076c13f2-7525-47c3-b461-4fa44894212d.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
POST = 16          # outer post offset from axis -> x 8 / 40
COLLAR_Y = 16
COLLAR_HALF = 2
CANDLE_TOP = 9
BOWL_Y = 22
BOWL_RY = 8
FINIAL = (37, 42)


class BareThreeArmChandelier(Solo48):
    icon_id = "bare-three-arm-chandelier"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("chandelier", "candelabra")
    keywords = ("chandelier", "candles", "ceiling", "light", "lamp", "hanging")

    def build(self) -> None:
        left, right = AXIS - POST, AXIS + POST
        rx = POST // 2
        self.add_line("cap", (18, 6), (30, 6))
        self.add_line("stem-top", (AXIS, 6), (AXIS, COLLAR_Y))
        self.add_line("stem-low", (AXIS, COLLAR_Y), (AXIS, BOWL_Y))
        self.relate("connect", "cap", "stem-top")
        self.relate("connect", "stem-top", "stem-low")

        self.add_line("candle-l", (left, CANDLE_TOP), (left, COLLAR_Y))
        self.add_line("post-l", (left, COLLAR_Y), (left, BOWL_Y))
        self.add_arc("bowl-l", (left, BOWL_Y), (AXIS, BOWL_Y), radius_x=rx, radius_y=BOWL_RY, sweep=False)
        self.add_arc("bowl-r", (AXIS, BOWL_Y), (right, BOWL_Y), radius_x=rx, radius_y=BOWL_RY, sweep=False)
        self.add_line("post-r", (right, BOWL_Y), (right, COLLAR_Y))
        self.add_line("candle-r", (right, COLLAR_Y), (right, CANDLE_TOP))
        self.add_contour("arms", "candle-l", "post-l", "bowl-l", "bowl-r", "post-r", "candle-r")
        self.relate("connect", "stem-low", "arms")

        for name, x in (("l", left), ("c", AXIS), ("r", right)):
            self.add_line(f"collar-{name}-a", (x - COLLAR_HALF, COLLAR_Y), (x, COLLAR_Y))
            self.add_line(f"collar-{name}-b", (x, COLLAR_Y), (x + COLLAR_HALF, COLLAR_Y))
            self.add_contour(f"collar-{name}", f"collar-{name}-a", f"collar-{name}-b")
        self.relate("connect", "collar-l", "arms")
        self.relate("connect", "collar-r", "arms")
        self.relate("connect", "collar-c", "stem-top")
        self.relate("connect", "collar-c", "stem-low")

        self.add_line("finial", (AXIS, FINIAL[0]), (AXIS, FINIAL[1]))
