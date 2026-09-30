"""fist-bump (redraw of the new-pipeline traced SVG).

Plan: two mirrored stick-figure busts about x=24 on HRECT_L (centerline box
(4,8)-(44,40)), each reaching one bent arm inward so the two fists meet at
chest height across a one-stroke gap.
- body (left, mirrored right): outer side x=4 from the bottom extreme up to an
  r6 shoulder arc about (10,32), level shoulder top on y=26, then the arm drops
  to an elbow and the forearm rises to the fist, all one round-joined contour.
- head: r5 circle about (10,13); top on the keyshape top, bottom exactly 8
  above the shoulder top on the same axis x=10 (4-unit ink gap).
- arm: shoulder top -> elbow (14,33) -> forearm rising to the fist (20,31);
  a rounded inner shoulder was tried and read as a U-turn arrow.
- fists: forearm ends at (20,31) and (28,31), 8 apart on centerlines.
Keyshape: HRECT_M (suggested) leaves 28 of height; head (10) + head gap (8)
+ a bust with a readable elbow dip (>=14) needs 32, so HRECT_L (the second
candidate, same x fit) is used.

Metric issues fixed:
- stroke-width: redrawn at stroke 4 with every gap budgeted at 8 centerlines.
- keyshape-short-axis: head tops and body feet sit on y=8 / y=40, sides on
  x=4 / x=44, so all four HRECT_L extremes are exact.
- clearance e0/e2, e1/e3 and head-gap: heads r5 sit exactly 8 above their own
  shoulder tops and >=8 from the arms.
- clearance e2/e3: the fists end 8 apart instead of touching.
- holes at the heads: r5 heads leave a 6-unit inscribed hole.
Reference: icon_set/references/human_ref/user.svg (circle head over a
shoulder arch); Lucide `users` for the bust construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "7eb37a5d-4cd8-4996-8500-94d9331cc88f"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1217-fist-bump/fist-bump_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
HEAD_R = 5
HEAD_C = (10, 13)          # left head; bottom (10,18)
SHOULDER_Y = 26            # 8 below the head bottom
SHOULDER_R = 6
SIDE_X = 4
FOOT_Y = 40
TOP_END = (12, SHOULDER_Y)   # end of the level shoulder top
ELBOW = (14, 33)
FIST = (20, 31)              # mirrored fist at (28,31): 8 apart


def _m(p):
    return (2 * AXIS - p[0], p[1])


class FistBumpRedraw(Solo48):
    icon_id = "fist-bump-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "people"
    aliases = ("fist bump", "dap", "knuckle bump")
    keywords = ("fist", "bump", "greeting", "friends", "people", "teamwork", "agreement")

    def _figure(self, side: str, mirror) -> None:
        cx, cy, r = mirror(HEAD_C)[0], HEAD_C[1], HEAD_R
        m = mirror
        right = side == "right"
        # Head: four cardinal arcs, clockwise on screen.
        pts = [(cx, cy - r), (cx + r, cy), (cx, cy + r), (cx - r, cy)]
        ids = []
        for i in range(4):
            eid = f"{side}-head-{i + 1}"
            self.add_arc(eid, pts[i], pts[(i + 1) % 4], radius_x=r, sweep=True)
            ids.append(eid)
        self.add_contour(f"{side}-head", *ids, closed=True)

        sx = SHOULDER_R + SIDE_X
        self.add_line(f"{side}-side", m((SIDE_X, FOOT_Y)), m((SIDE_X, SHOULDER_Y + SHOULDER_R)))
        self.add_arc(f"{side}-shoulder", m((SIDE_X, SHOULDER_Y + SHOULDER_R)), m((sx, SHOULDER_Y)),
                     radius_x=SHOULDER_R, sweep=not right)
        self.add_line(f"{side}-torso", m((sx, SHOULDER_Y)), m(TOP_END))
        self.add_line(f"{side}-upper-arm", m(TOP_END), m(ELBOW))
        self.add_line(f"{side}-forearm", m(ELBOW), m(FIST))
        self.add_contour(f"{side}-body", f"{side}-side", f"{side}-shoulder", f"{side}-torso",
                         f"{side}-upper-arm", f"{side}-forearm")
        self.mark_human_figure(side, head=f"{side}-head", torso=f"{side}-torso",
                               torso_junction="start")

    def build(self) -> None:
        self._figure("left", lambda p: p)
        self._figure("right", _m)
