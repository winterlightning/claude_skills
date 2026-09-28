"""easter-egg-wrapped-with-ribbon-bow-middle (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42)), mirrored about x=24. The bow sits
in front of the egg and is wider than it, so the bow sets the x extremes and
the egg sets the y extremes.
- bow: an 8x8 square knot at the centre of the bow row, with one rounded loop
  per side. Each loop leaves a knot corner, runs out to a round outer end
  (a quarter-ellipse pair about (EGG_X, BOW_Y) with a vertical tangent at x=6/42)
  and returns to the other knot corner.
- egg: drawn behind the bow, so only a top dome and a bottom cap show. Both
  end on the loops' top/bottom nodes (x=12/36), where the loop runs level and
  the shell arrives steeply -- a clean T junction. The hidden widest band lies
  under the loops. Pointed dome, fuller bottom.
Dropped from the trace: the two vertical ribbon edges (removed on review).
Lucide `egg` informed the shell; Lucide `gift` the knot-and-loops bow.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1422-easter-egg-wrapped-with-ribbon-bow-middle/"
    "easter-egg-wrapped-with-ribbon-bow-middle_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP_Y, BOT_Y = 6, 42        # egg apex / base
EGG_X = 12                  # where the shell meets the loops (hidden widest band)
BOW_Y = 25                  # bow row centre
LOOP_RX, LOOP_RY = 6, 7     # outer loop end: x 6..12, y 18..32
KNOT = 4                    # knot half-size: x 20..28, y 21..29
K = 0.5523                  # quarter-ellipse handle ratio


def mx(p):
    return (2 * AXIS - p[0], p[1])


class EasterEggWrappedWithRibbonBowMiddleRedraw(Solo48):
    icon_id = "easter-egg-wrapped-with-ribbon-bow-middle-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ("easter egg with ribbon", "gift egg", "wrapped easter egg")
    keywords = ("easter", "egg", "ribbon", "bow", "gift", "present", "spring", "holiday")

    def build(self) -> None:
        kx0, kx1 = AXIS - KNOT, AXIS + KNOT
        ky0, ky1 = BOW_Y - KNOT, BOW_Y + KNOT
        self.add_polyline("knot", (kx0, ky0), (kx1, ky0), (kx1, ky1), (kx0, ky1), closed=True)

        # Left loop: knot top-left -> loop top -> outer end -> loop bottom -> knot bottom-left.
        top, out, bot = (EGG_X, BOW_Y - LOOP_RY), (EGG_X - LOOP_RX, BOW_Y), (EGG_X, BOW_Y + LOOP_RY)
        hx, hy = LOOP_RX * K, LOOP_RY * K
        segs = [
            ("in-top", (kx0, ky0), ((18, 19), (15, top[1]), top)),
            ("out-top", top, ((EGG_X - hx, top[1]), (out[0], BOW_Y - hy), out)),
            ("out-bot", out, ((out[0], BOW_Y + hy), (EGG_X - hx, bot[1]), bot)),
            ("in-bot", bot, ((15, bot[1]), (18, 31), (kx0, ky1))),
        ]
        for name, start, ctrl in segs:
            self.add_bezier(f"bow-l-{name}", start, ctrl)
            self.add_bezier(f"bow-r-{name}", mx(start), tuple(mx(p) for p in ctrl))
        for side in ("l", "r"):
            self.add_contour(f"bow-{side}", *(f"bow-{side}-{n}" for n, *_ in segs))
            self.relate("connect", f"bow-{side}", "knot")

        # Egg behind the bow: top dome and bottom cap, each ending on the loops.
        self.add_bezier("dome-l", top, ((13, 13), (17, TOP_Y), (AXIS, TOP_Y)))
        self.add_bezier("dome-r", (AXIS, TOP_Y), ((31, TOP_Y), (35, 13), mx(top)))
        self.add_contour("dome", "dome-l", "dome-r")
        self.add_bezier("base-l", bot, ((12.5, 37), (16, BOT_Y), (AXIS, BOT_Y)))
        self.add_bezier("base-r", (AXIS, BOT_Y), ((32, BOT_Y), (35.5, 37), mx(bot)))
        self.add_contour("base", "base-l", "base-r")
        for part in ("dome", "base"):
            self.relate("connect", part, "bow-l")
            self.relate("connect", part, "bow-r")
