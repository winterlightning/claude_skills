"""Three bowling pins: a large front pin with two smaller pins standing behind it.

Symbol plan: one pin profile (round head, narrow neck, full belly, flat foot) defined
as a right-side curve and mirrored about each pin axis. The front pin sits on x=24 and
reaches the floor; the two rear pins share a smaller copy of the profile, stand higher,
and only their outer half (head, outer flank, a stub of foot) is drawn -- their inner
flanks are hidden behind the front pin. Left and right rear pins mirror about x=24.
Lucide construction: no bowling-pin glyph; built on Lucide's rule of vertical-tangent
cubics flowing out of a round head (as in lucide 'flask-round' / 'bottle' shoulders).
Keyshape HRECT_L: centerline x 4..44 (rear bellies), y 8..40 (rear heads, front foot).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "012843f4-1e2d-4bd4-8797-27a0f5f0fd46"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__bowling-pins-three/20260925T093141Z-thuan-mac/reference/three bowlings_012843f4-1e2d-4bd4-8797-27a0f5f0fd46.svg"
AUTHOR = "claude-opus-5-5"


class BowlingPinsThree(Solo48):
    icon_id = "bowling-pins-three"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ("three-bowling-pins", "bowling")
    keywords = ("bowling", "pins", "skittles", "sport", "game", "strike")

    def curve(self, name, start, c1, c2, end):
        self.add_bezier(name, start, (c1, c2, end))
        return name

    def build(self) -> None:
        # front pin: axis 24, head r6 centred at y21, neck +-4 @28, belly +-8 @34, foot +-5 @40
        a, hc, r = 24, 21, 6
        m = []
        m.append(self.curve("front-l-foot", (a - 5, 40), (a - 7, 39), (a - 8, 37), (a - 8, 34)))
        m.append(self.curve("front-l-belly", (a - 8, 34), (a - 8, 31), (a - 4, 30), (a - 4, 28)))
        m.append(self.curve("front-l-neck", (a - 4, 28), (a - 4, 26), (a - 6, 24), (a - 6, hc)))
        self.add_arc("front-head", (a - r, hc), (a + r, hc), radius_x=r, sweep=True)
        m.append("front-head")
        m.append(self.curve("front-r-neck", (a + 6, hc), (a + 6, 24), (a + 4, 26), (a + 4, 28)))
        m.append(self.curve("front-r-belly", (a + 4, 28), (a + 4, 30), (a + 8, 31), (a + 8, 34)))
        m.append(self.curve("front-r-foot", (a + 8, 34), (a + 8, 37), (a + 7, 39), (a + 5, 40)))
        self.add_line("front-base", (a + 5, 40), (a - 5, 40))
        m.append("front-base")
        self.add_contour("front-pin", *m, closed=True)

        # rear pins stand behind and above: axis 12 / 36, head r5 centred at y13.
        # The outer flank and most of the head show; the inner flank is hidden.
        for side, s in (("left", 1), ("right", -1)):
            x = lambda d: 24 - s * (12 - d)  # d is the offset from the rear axis, outward negative
            p = f"rear-{side}"
            names = [
                self.curve(f"{p}-foot", (x(-5), 34), (x(-7), 33.5), (x(-8), 32), (x(-8), 28)),
                self.curve(f"{p}-belly", (x(-8), 28), (x(-8), 23), (x(-3), 22), (x(-3), 19)),
                self.curve(f"{p}-neck", (x(-3), 19), (x(-3), 17), (x(-5), 15), (x(-5), 13)),
            ]
            self.add_arc(f"{p}-head", (x(-5), 13), (x(3), 9), radius_x=5, sweep=(s == 1))
            names.append(f"{p}-head")
            self.add_contour(p, *names)
