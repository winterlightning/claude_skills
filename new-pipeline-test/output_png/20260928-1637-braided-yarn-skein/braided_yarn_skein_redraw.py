"""braided-yarn-skein (redraw of the new-pipeline traced SVG).

Plan: tall skein on VRECT_M (centerline box (10,4)-(38,44)).
- body: one closed capsule, walls x=10 / x=30, r=10 domes centred (20,14) and
  (20,30), so the top sits on y=4 and the left wall on x=10. The bottom dome is
  split at (28,36) (a 6-8-10 point) where the tail leaves it.
- strands: two mirrored curved wraps cross on the axis x=20 at the node N.
  Each wrap is tangent-continuous through N (collinear controls) and ends on
  the body: from the top dome (14,6)/(26,6) down to the opposite wall/dome
  junction (30,30)/(10,30). The four halves share N, so the crossing is a
  real junction rather than an overlap.
- tail: one S cubic from the dome split point that swings out and hooks down,
  owning the right extreme x=38 and the bottom extreme y=44.
Metric issues: every clearance error (e0..e8 strands 2-7 apart) is fixed by
dropping the trace's parallel winding arcs in both domes and the double-edged
band, so the front reads as two single crossing wraps; stroke-count 10 -> 7
strokes; keyshape-short-axis fixed by letting the tail own x=38 instead of
stretching the body; the five sub-6 holes disappear with the dropped windings;
stroke-width is rebuilt at 4. Mirrored about x=20 except the tail. No useful
Lucide match (no yarn skein; Lucide `pill` informed the capsule construction).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5ab9f3b5-03e7-4655-9d6a-e84a5583b790"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1637-braided-yarn-skein/"
    "braided-yarn-skein_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 20
L, R = 10, 30               # capsule walls
TOP_C, BOT_C = 14, 30       # dome centres on the axis
DOME_R = 10
TAIL_ROOT = (28, 36)        # (20+8, 30+6) on the bottom dome
NODE = (AXIS, 20)           # strand crossing
WRAP_TOP = (14, 6)          # (20-6, 14-8) on the top dome
WRAP_END = (R, BOT_C)       # right wall / bottom dome junction
TAN = (2.0, 3.0)            # wrap tangent through the node


def mx(p):
    return (2 * AXIS - p[0], p[1])


class BraidedYarnSkeinRedraw(Solo48):
    icon_id = "braided-yarn-skein-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/crafts"
    aliases = ("yarn skein", "skein of yarn", "wool skein", "hank of yarn")
    keywords = ("yarn", "skein", "wool", "knitting", "crochet", "craft", "thread")

    def build(self) -> None:
        top_l, top_r = (L, TOP_C), (R, TOP_C)
        bot_l, bot_r = (L, BOT_C), (R, BOT_C)
        wt_l, wt_r = WRAP_TOP, mx(WRAP_TOP)
        # Body clockwise from the left wall top; top dome split at the wrap roots.
        self.add_arc("dome-t1", top_l, wt_l, radius_x=DOME_R)
        self.add_arc("dome-t2", wt_l, wt_r, radius_x=DOME_R)
        self.add_arc("dome-t3", wt_r, top_r, radius_x=DOME_R)
        self.add_line("wall-r", top_r, bot_r)
        self.add_arc("dome-b1", bot_r, TAIL_ROOT, radius_x=DOME_R)
        self.add_arc("dome-b2", TAIL_ROOT, bot_l, radius_x=DOME_R)
        self.add_line("wall-l", bot_l, top_l)
        self.add_contour(
            "body", "dome-t1", "dome-t2", "dome-t3", "wall-r",
            "dome-b1", "dome-b2", "wall-l", closed=True,
        )

        nx, ny = NODE
        tx, ty = TAN
        # Wrap A: top-left dome -> node -> right junction; wrap B mirrors it.
        a_up = (wt_l, ((15.5, 11.0), (nx - tx * 1.6, ny - ty * 1.6), NODE))
        a_dn = (NODE, ((nx + tx * 1.6, ny + ty * 1.6), (27.0, 28.0), WRAP_END))
        self.add_bezier("wrap-a1", a_up[0], a_up[1])
        self.add_bezier("wrap-a2", a_dn[0], a_dn[1])
        self.add_bezier("wrap-b1", wt_r, tuple(mx(p) for p in a_up[1]))
        self.add_bezier("wrap-b2", NODE, tuple(mx(p) for p in a_dn[1][:2]) + (bot_l,))
        for w in ("wrap-a1", "wrap-a2", "wrap-b1", "wrap-b2"):
            self.relate("connect", w, "body")
        self.relate("connect", "wrap-a1", "wrap-a2", "wrap-b1", "wrap-b2")

        # Tail: out of the bottom dome, swing right, hook down to the corner.
        self.add_bezier(
            "tail", TAIL_ROOT,
            ((30.0, 40.0), (32.0, 41.0), (35.0, 40.0)),
            ((37.0, 39.4), (38.0, 41.0), (38, 44)),
        )
        self.relate("connect", "tail", "body")
