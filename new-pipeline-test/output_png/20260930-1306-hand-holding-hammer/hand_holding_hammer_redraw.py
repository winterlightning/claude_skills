"""hand-holding-hammer (redraw of the new-pipeline traced SVG).

Subject: a stick-figure forearm whose round fist grips an upright claw
hammer part-way down the handle.

Plan: VRECT_M (centerline box (10,4)-(38,44)), handle on the axis x=26 (under
the head body, the claw reaches out to the right).
- head: one closed contour -- flat striking face at x=14, level top on
  y=4, the claw as one cubic that leaves the top level and falls plumb to
  its tip on x=38, a concave return curve to the head bottom on y=14; the
  bottom edge is split at the handle column so the handle shares a knot.
- handle: a single stroke on x=26, interrupted by the fist: upper run
  from the head to the fist top, lower stub from the fist bottom to y=44.
- fist: circle r=5 about (26,30), built from three arcs so the handle
  runs and the forearm each end on a shared knot; the wrist knot (22,33)
  is a 3-4-5 point, so the forearm leaves the ring radially (a knot at
  the ring's side pinched the ring in the first draft).
- forearm: one straight stroke continuing that radius (slope 3:4) down to
  x=10; the elbow jog in the image is dropped (too short to read at 48).

Metric issues:
- stroke-width / stroke-count: redrawn at stroke 4 with 5 parts instead of
  the 16 traced fragments (hollow handle, face block, neck and elbow
  jog merged or dropped).
- keyshape-short-axis (VRECT_M y fill 97%): head top on y=4, handle
  bottom on y=44, arm end x=10, claw tip x=38 -- every extreme on the box.
- clearance errors (e0/e11-e13, e1/e5-e15, e2/e3-e15 ...): came from the
  thin hollow handle, the face-block neck and the fist overlapping the
  handle walls; the handle is now one stroke, the neck is gone and every
  unconnected pair is >= 8 apart on centerlines.
- holes (2.8 and 2.5 inscribed): the head interior is 10 tall (6 inscribed
  ink hole) and the fist ring is 10 across (6 inscribed).
- human head gap (e0 read as a head): false positive -- e0 is the fist,
  not a head; there is no human head or torso, so no human figure is marked.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9c2e6a00-c352-4f4c-97df-5e296d00637d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1306-hand-holding-hammer/hand-holding-hammer_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 26                  # hammer handle column
HEAD = (14, 4, 14)         # face x, top y, bottom y
CLAW_ROOT = 28             # top edge ends here, claw starts
CLAW_TIP = (38, 18)        # plumb tangent on the box right
CLAW_BACK = 30             # claw return meets the head bottom here
FIST_C = (26, 30)
FIST_R = 5
WRIST = (22, 33)           # 3-4-5 knot on the fist: the arm leaves radially
HANDLE_END = 44
ARM_END = (10, 42)


class HandHoldingHammerRedraw(Solo48):
    icon_id = "hand-holding-hammer-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("hand with hammer", "holding hammer", "hammer in hand")
    keywords = ("hammer", "hand", "holding", "grip", "tool", "carpentry", "construction", "build", "repair")

    def build(self) -> None:
        fx, top, bot = HEAD
        tx, ty = CLAW_TIP
        self.add_line("head-top", (fx, top), (CLAW_ROOT, top))
        self.add_bezier("claw", (CLAW_ROOT, top), ((CLAW_ROOT + 6, top), (tx, ty - 8), CLAW_TIP))
        self.add_bezier("claw-back", CLAW_TIP, ((tx - 1, ty - 3), (CLAW_BACK + 3, bot), (CLAW_BACK, bot)))
        self.add_line("head-bot-r", (CLAW_BACK, bot), (AXIS, bot))
        self.add_line("head-bot-l", (AXIS, bot), (fx, bot))
        self.add_line("face", (fx, bot), (fx, top))
        self.add_contour("head", "head-top", "claw", "claw-back", "head-bot-r", "head-bot-l", "face", closed=True)

        cx, cy = FIST_C
        r = FIST_R
        f_top, f_bot = (cx, cy - r), (cx, cy + r)
        self.add_arc("fist-a", f_top, WRIST, radius_x=r, sweep=False)
        self.add_arc("fist-b", WRIST, f_bot, radius_x=r, sweep=False)
        self.add_arc("fist-c", f_bot, f_top, radius_x=r, sweep=False)
        self.add_contour("fist", "fist-a", "fist-b", "fist-c", closed=True)

        self.add_line("handle", (AXIS, bot), f_top)
        self.add_line("handle-end", f_bot, (AXIS, HANDLE_END))
        self.add_line("forearm", WRIST, ARM_END)

        self.relate("connect", "handle", "head")
        self.relate("connect", "handle", "fist")
        self.relate("connect", "handle-end", "fist")
        self.relate("connect", "forearm", "fist")
