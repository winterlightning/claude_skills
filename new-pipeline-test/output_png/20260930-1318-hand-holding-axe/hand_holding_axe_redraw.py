"""hand-holding-axe (redraw of the new-pipeline traced SVG).

Subject: a stick-figure forearm whose round fist grips an upright axe
low on the handle; the wedge head flares to a curved cutting edge on the
upper right.

Plan: VRECT_M (centerline box (10,4)-(38,44)), handle on the axis x=22.
- head: one closed contour -- the handle side x=22 from y=18 up to y=8,
  a sagging top edge (cubic, level at the handle) out to the upper tip
  (36,5), the cutting edge as two r=26 arcs about (12,15) whose shared
  knot (38,15) is the apex on the box right, and a sagging bottom edge
  back from the lower tip (36,25) to the handle.
- handle: a single stroke on x=22 split by the head and the fist: top
  stub from y=4 to the head, middle run from the head to the fist top,
  lower stub from the fist bottom to y=44.
- fist: circle r=5 about (22,32), three arcs so the handle runs and the
  forearm each end on a shared knot; the wrist knot (18,35) is a 3-4-5
  point so the forearm leaves the ring radially.
- forearm: one straight stroke continuing that radius (slope 3:4) to
  (10,41); the elbow bend in the image is dropped.

Metric issues:
- stroke-width (trace 2.55): redrawn at stroke 4 on the 48 grid.
- keyshape-short-axis (VRECT_M y fill 97%): handle top y=4, handle bottom
  y=44, arm end x=10, cutting-edge apex x=38 -- every extreme on the box.
- clearance e2/e3 (3.21): the traced forearm (e2) met the hollow fist
  outline (e3) beside the handle; the fist is now one ring the forearm
  connects to radially, and every unconnected pair is >= 8 apart.
- hole (5.13 inscribed in the head): the head is 10 tall at the handle
  and 20 at the cutting edge, well over 6 inscribed.
- no-head: not a defect -- the subject is a hand only; there is no head
  or torso, so no human figure is marked.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "47659966-6bcc-4338-8851-46f26e9cca27"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1318-hand-holding-axe/hand-holding-axe_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 22                  # axe handle column
HANDLE_TOP, HANDLE_END = 4, 44
HEAD_TOP, HEAD_BOT = 8, 18  # head edges at the handle
TIP_TOP, TIP_BOT = (36, 5), (36, 25)
EDGE_C, EDGE_R = (12, 15), 26
APEX = (EDGE_C[0] + EDGE_R, EDGE_C[1])  # (38,15) on the box right
FIST_C = (22, 32)
FIST_R = 5
WRIST = (18, 35)           # 3-4-5 knot on the fist: the arm leaves radially
ARM_END = (10, 41)


class HandHoldingAxeRedraw(Solo48):
    icon_id = "hand-holding-axe-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("hand with axe", "holding axe", "axe in hand", "hatchet in hand")
    keywords = ("axe", "hatchet", "hand", "holding", "grip", "tool", "chop", "wood", "lumberjack")

    def build(self) -> None:
        a = AXIS
        self.add_line("head-side", (a, HEAD_BOT), (a, HEAD_TOP))
        self.add_bezier("head-top", (a, HEAD_TOP), ((a + 7, HEAD_TOP), (TIP_TOP[0] - 3, TIP_TOP[1] + 2), TIP_TOP))
        self.add_arc("edge-a", TIP_TOP, APEX, radius_x=EDGE_R, sweep=True)
        self.add_arc("edge-b", APEX, TIP_BOT, radius_x=EDGE_R, sweep=True)
        self.add_bezier("head-bot", TIP_BOT, ((TIP_BOT[0] - 4, TIP_BOT[1] - 4), (a + 6, HEAD_BOT), (a, HEAD_BOT)))
        self.add_contour("head", "head-side", "head-top", "edge-a", "edge-b", "head-bot", closed=True)

        cx, cy = FIST_C
        r = FIST_R
        f_top, f_bot = (cx, cy - r), (cx, cy + r)
        self.add_arc("fist-a", f_top, WRIST, radius_x=r, sweep=False)
        self.add_arc("fist-b", WRIST, f_bot, radius_x=r, sweep=False)
        self.add_arc("fist-c", f_bot, f_top, radius_x=r, sweep=False)
        self.add_contour("fist", "fist-a", "fist-b", "fist-c", closed=True)

        self.add_line("handle-top", (a, HANDLE_TOP), (a, HEAD_TOP))
        self.add_line("handle", (a, HEAD_BOT), f_top)
        self.add_line("handle-end", f_bot, (a, HANDLE_END))
        self.add_line("forearm", WRIST, ARM_END)

        self.relate("connect", "handle-top", "head")
        self.relate("connect", "handle", "head")
        self.relate("connect", "handle", "fist")
        self.relate("connect", "handle-end", "fist")
        self.relate("connect", "forearm", "fist")
