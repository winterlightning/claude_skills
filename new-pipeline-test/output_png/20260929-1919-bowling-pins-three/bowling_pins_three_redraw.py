"""bowling-pins-three (redraw of the new-pipeline traced SVG).

Plan: three bowling-pin outlines on HRECT_L (centerline box (4,8)-(44,40)),
mirrored about x=24. The middle pin stands in front and is drawn whole; the
two side pins stand behind it and are drawn only where they show, so each
side outline starts and ends on knots of the middle outline (declared
connect). The middle pin is the tallest, matching the generated image.
- middle pin: semicircle head r5 on (24,13) (top = y 8 extreme), neck 6 wide
  at y 20, belly 12 wide at y 30, base (20,40)-(28,40) (bottom extreme).
- side pins: semicircle head r4 on (8,20) / (40,20), neck at y 26, belly apex
  on x 4 / 44 (the side extremes); their inner side turns into the middle
  pin's belly apex (18,30) / (30,30) and their base runs to its base corner.
One pin definition per role, built by a shared helper and mirrored.
No useful Lucide match (Lucide has no bowling pin); construction follows
Lucide's rule of smooth cubic runs with vertical tangents at head joins.

Metric issues (bowling-pins-three_metrics.json) and how they were handled:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted for it.
- keyshape-short-axis (SQUARE fills 86% of y): HRECT_L is used instead. It
  matches the trace aspect (1.16) and fills y exactly; its 40-unit width is
  what lets the side heads clear the middle pin by 8.
- clearance e0/e1 and e0/e2 (pins 2.8 apart): three free-standing pins cannot
  fit at stroke 4 (each body needs >= 10 on centerlines for a 6 hole, plus
  two 8 gaps, > 40). The pins now overlap: the side pins meet the middle pin
  at shared knots instead of running beside it, and every free part (heads,
  necks) keeps 8 on centerlines.
- hole at (10.9,14.6) and (37.0,14.5) (side heads pinched shut): the heads
  are no longer closed holes; each pin interior is one opening through a
  neck at least 6 wide on centerlines.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "012843f4-1e2d-4bd4-8797-27a0f5f0fd46"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1919-bowling-pins-three/bowling-pins-three_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                                   # mirror axis
TOP, BASE = 8, 40                         # keyshape y extremes
MID_HEAD_R, MID_HEAD_Y = 5, 13            # middle head semicircle centre y
MID_NECK_HALF, MID_NECK_Y = 3, 21         # brief 6-wide pinch
MID_BELLY_HALF, MID_BELLY_Y = 7, 32
MID_BASE_HALF = 4
MID_LOW_C1 = (15.5, 36)                   # belly apex -> base corner pull
TUCK_C1_DY, TUCK_C2_DX = 3, 3
MID_BELLY_C = (4, 5)                      # belly handle lengths (apex, neck)
SIDE_HEAD_R, SIDE_HEAD_X, SIDE_HEAD_Y = 4, 8, 21
SIDE_NECK_OUT, SIDE_NECK_IN, SIDE_NECK_Y = 5, 11, 25   # brief 6-wide pinch
SIDE_BELLY_X, SIDE_BELLY_Y = 4, 32
SIDE_BASE_X = 7

def MID_LOW_C1_AT(b, by):
    return (AX - b, by + MID_LOW_C1[1] - MID_BELLY_Y + 0) if False else (AX - b, by + 4)


def mx(x):
    return 2 * AX - x


class BowlingPinsThreeRedraw(Solo48):
    icon_id = "bowling-pins-three-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "sports/bowling"
    aliases = ("bowling pins", "skittles", "tenpins")
    keywords = ("bowling", "pins", "skittles", "tenpin", "alley", "strike", "sport", "game")

    def build(self) -> None:
        # Middle pin (front, whole), clockwise from the base-left corner;
        # each side is split at the hip knot where a side pin's base lands.
        hr, hy = MID_HEAD_R, MID_HEAD_Y
        n, ny = MID_NECK_HALF, MID_NECK_Y
        b, by = MID_BELLY_HALF, MID_BELLY_Y
        f = MID_BASE_HALF
        left = [  # (id, start, c1, c2, end), base corner up to the head
            ("low", (AX - f, BASE), (AX - f - 1.5, BASE - 2.5), MID_LOW_C1_AT(b, by), (AX - b, by)),
            ("belly", (AX - b, by), (AX - b, by - MID_BELLY_C[0]), (AX - n, ny + MID_BELLY_C[1]), (AX - n, ny)),
            ("neck", (AX - n, ny), (AX - n, ny - 2), (AX - hr, hy + 4), (AX - hr, hy)),
        ]
        for name, p0, c1, c2, p3 in left:
            self.add_bezier(f"mid-l-{name}", p0, (c1, c2, p3))
        self.add_arc("mid-head", (AX - hr, hy), (AX + hr, hy), radius_x=hr, sweep=True)
        for name, p0, c1, c2, p3 in reversed(left):  # mirrored, head down
            m = lambda q: (mx(q[0]), q[1])
            self.add_bezier(f"mid-r-{name}", m(p3), (m(c2), m(c1), m(p0)))
        self.add_line("mid-base", (AX + f, BASE), (AX - f, BASE))
        self.add_contour(
            "mid", "mid-l-low", "mid-l-belly", "mid-l-neck", "mid-head",
            "mid-r-neck", "mid-r-belly", "mid-r-low", "mid-base", closed=True,
        )

        # Side pins (behind): the visible part, from the middle hip knot
        # round the outer side and head into the middle belly apex.
        for side, x in (("left", lambda v: v), ("right", mx)):
            self.add_contour(side, *self._side_pin(side + "-", x))
            self.relate("connect", side, "mid")

    def _side_pin(self, p, x):
        r, hx, sy = SIDE_HEAD_R, SIDE_HEAD_X, SIDE_HEAD_Y
        no, ni, ny = SIDE_NECK_OUT, SIDE_NECK_IN, SIDE_NECK_Y
        bx, by = SIDE_BELLY_X, SIDE_BELLY_Y
        jx, jy = AX - MID_BELLY_HALF, MID_BELLY_Y   # middle belly apex
        self.add_line(p + "base", (x(AX - MID_BASE_HALF), BASE), (x(SIDE_BASE_X), BASE))
        self.add_bezier(p + "low", (x(SIDE_BASE_X), BASE),
                        ((x(5.3), BASE - 2), (x(bx), by + 2.5), (x(bx), by)))
        self.add_bezier(p + "belly", (x(bx), by), ((x(bx), by - 3.5), (x(no), ny + 2.5), (x(no), ny)))
        self.add_bezier(p + "neck-out", (x(no), ny), ((x(no), ny - 1.5), (x(hx - r), sy + 1.5), (x(hx - r), sy)))
        self.add_arc(p + "head", (x(hx - r), sy), (x(hx + r), sy), radius_x=r, sweep=x(0) == 0)
        self.add_bezier(p + "neck-in", (x(hx + r), sy), ((x(hx + r), sy + 1.5), (x(ni), ny - 1.5), (x(ni), ny)))
        self.add_bezier(p + "tuck", (x(ni), ny), ((x(ni), ny + TUCK_C1_DY), (x(jx - TUCK_C2_DX), jy), (x(jx), jy)))
        return tuple(p + k for k in ("base", "low", "belly", "neck-out", "head", "neck-in", "tuck"))
