"""curving-snake (redraw of the new-pipeline traced SVG).

Plan: VRECT_L as suggested, centerline box (8,4)-(40,44).
Extremes: y=4 the head/neck top, x=8 the left of the upper loop, x=40 the
tongue tips, y=44 the tail tip.
- body: one closed hollow outline. Head = r5 half-round snout facing right
  (nose (31,9)); a neck 10 wide (walls y=4 / y=14) runs left into the upper
  loop, a semicircle pair about x=22 (outer r14, inner r4.5), which turns the
  body back to the right as a middle run 9 wide (walls y=23 / y=32). The two
  middle walls taper into one point P=(31,27), so the hollow body narrows
  toward the tail.
- tail: one stroke continuing from P, an r7 half-turn down the right side
  (rightmost x=38) and a tapering sweep back left to the tip at (10,44).
- tongue: a short stem from the nose and a forked V reaching x=40.
Stacked walls: 4 / 14 / 23 / 32 / 41, every gap 9 or 10 on centerlines.
References: the generated PNG for the subject only (head top right with a
forked tongue, S body, tapering tail bottom left). No trace coordinates
copied. No useful Lucide snake exists; construction follows Lucide's
round-cap single-line tails and half-round caps.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for 4.
- keyshape-short-axis (warn, y fill 93%): fixed; the neck top sits on y=4
  and the tail tip on y=44, left loop on x=8, tongue on x=40.
- clearance e0/e1 (tongue prong 1.99 from the head): fixed; the tongue is
  one stem leaving the nose plus a fork 4 beyond it, joined only at its
  declared junction, with no loose prong along the head.
- hole [29.6,8.6] (2.72, the pinch inside the head): fixed; the head is the
  open end of a 10-wide neck (inscribed 6 at stroke 4).
- hole [29.4,24.3] (1.17, the thin body tube): fixed; the hollow body is
  10 wide in the neck and loop and 9 in the middle run before it tapers.
Changed: a full hollow S (two loops plus a hollow tail) needs six stacked
walls, about 45 units at 9 spacing against the 40 available, so the lower
loop and tail are one tapering stroke instead of a hollow tube.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "2ec00ca4-5f8a-4ca6-b750-8ed6a3306564"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1037-curving-snake/curving-snake_raw.svg"
AUTHOR = "claude-opus-5-5"

LOOP_X = 22                 # upper loop axis
NECK_TOP, NECK_BOT = 4, 14  # neck walls (10 wide)
MID_TOP, MID_BOT = 23, 32   # middle run walls (9 wide)
HEAD_X = 26                 # neck meets the r5 snout
P = (31, 27)                # middle walls taper into the tail here
CURL_R = 7                  # tail half-turn, centre (31,34)
TIP = (10, 44)


class CurvingSnakeRedraw(Solo48):
    icon_id = "curving-snake-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ("serpent", "s-curved snake")
    keywords = ("snake", "serpent", "reptile", "curving", "slither", "tongue", "animal", "wild")

    def build(self) -> None:
        # Hollow body: neck, upper loop, middle run tapering into P.
        self.add_line("neck-top", (HEAD_X, NECK_TOP), (LOOP_X, NECK_TOP))
        self.add_arc("loop-out", (LOOP_X, NECK_TOP), (LOOP_X, MID_BOT),
                     radius_x=(MID_BOT - NECK_TOP) // 2, sweep=False)
        self.add_bezier("belly", (LOOP_X, MID_BOT), ((26, MID_BOT), (29, 30), P))
        self.add_bezier("back", P, ((29, 24.5), (26, MID_TOP), (LOOP_X, MID_TOP)))
        # Inner loop: cubic half-circle (r4.5 has no integer arc radius).
        k = 4 / 3 * (MID_TOP - NECK_BOT) / 2
        self.add_bezier("loop-in", (LOOP_X, MID_TOP),
                        ((LOOP_X - k, MID_TOP), (LOOP_X - k, NECK_BOT), (LOOP_X, NECK_BOT)))
        self.add_line("neck-bot", (LOOP_X, NECK_BOT), (HEAD_X, NECK_BOT))
        self.add_arc("head", (HEAD_X, NECK_BOT), (HEAD_X, NECK_TOP),
                     radius_x=(NECK_BOT - NECK_TOP) // 2, sweep=False)
        self.add_contour("body", "neck-top", "loop-out", "belly", "back",
                         "loop-in", "neck-bot", "head", closed=True)

        # Tail: half-turn down the right side, then a sweep back to the tip.
        bottom = (P[0], P[1] + 2 * CURL_R)
        self.add_arc("tail-curl", P, bottom, radius_x=CURL_R, sweep=True)
        self.add_bezier("tail-sweep", bottom, ((24, bottom[1]), (16, 42.5), TIP))
        self.add_contour("tail", "tail-curl", "tail-sweep")
        self.relate("connect", "tail", "body")

        # Forked tongue from the nose.
        nose = (HEAD_X + 5, (NECK_TOP + NECK_BOT) // 2)
        fork = (nose[0] + 4, nose[1])
        self.add_line("tongue", nose, fork)
        self.add_polyline("tongue-fork", (40, nose[1] - 4), fork, (40, nose[1] + 4))
        self.relate("connect", "tongue", "body")
        self.relate("connect", "tongue", "tongue-fork")
