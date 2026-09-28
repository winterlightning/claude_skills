"""burning-crashed-aircraft (redraw of the new-pipeline traced PNG).

Plan: a side-view airliner nose-down on the ground with fire on its tail,
on HRECT_L (centerline box (4,8)-(44,40); flame tip owns y=8, ground owns
x=4..44 and y=40).
- fuselage: one closed contour. Its bottom and top edges are parallel 1:3
  diagonals, OFFSET (3,-9) apart (9.5 on centerlines). The bottom edge lands
  on the ground at LAND, the ground under the nose (skid) closes the
  contour, and the nose is one cubic leaving the top edge tangent and
  dropping onto the ground. The tail is the flat cap TAIL_BOT-(7,21).
- wing: a tapered quadrilateral jutting up from the top edge, its trailing
  root on the nose node; the tip (33,12)-(41,14) stays over 8 from the
  leading edge.
- flame: one open cubic run with a tall left tongue and a small right
  tongue, rising from the tail corner and landing back on the top edge, so
  the fire sits on the rear fuselage and needs no detached clearance band.
- ground: a level line split where the fuselage and nose touch it.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap re-budgeted for it.
- stroke-count (warn, 10 strokes): now 4 subjects (fuselage, wing, flame,
  ground); the cockpit window is dropped and the two detached
  flame fragments are merged into one two-tongue flame.
- keyshape-short-axis (warn, x filled 93%): the ground spans the full
  x=4..44 and the flame tip reaches y=8, so HRECT_L fits exactly.
- clearance errors e0/e1/e2/e3/e4 vs e7 and each other (1.5-6.5 apart):
  the three flame fragments are one contour joined to the fuselage, and
  every remaining non-adjacent pair is at least 8 apart on centerlines.
- holes (inscribed 0.6-4.1, need 6): the cockpit pocket and the fin notch
  are gone; the fuselage tube is 9.5 wide, and the wing and flame openings
  pass the build gate's hole check.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "81f5c526-61a1-4426-afae-2fec80a31cb2"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1702-burning-crashed-aircraft/"
    "burning-crashed-aircraft_raw.svg"
)
AUTHOR = "claude-opus-5-5"

GROUND_Y = 40
LEFT, RIGHT = 4, 44
OFFSET = (3, -9)              # bottom edge -> top edge, perpendicular to (3,1)
TAIL_BOT = (4, 30)
LAND = (34, 40)               # bottom edge meets the ground
NOSE_TOP = (37, 31)           # top edge ends, nose begins
NOSE_DOWN = (42, 40)          # nose touches the ground
WING_ROOT_L = (28, 28)        # wing root on the top edge, leading side
WING_ROOT_T = NOSE_TOP        # wing root, trailing side
WING_TIP_L = (33, 12)         # tapered tip, narrower than the root
WING_TIP_T = (41, 14)
FLAME_END = (19, 25)          # flame lands back on the top edge


def add(p, q):
    return (p[0] + q[0], p[1] + q[1])


class BurningCrashedAircraftRedraw(Solo48):
    icon_id = "burning-crashed-aircraft-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "war"
    aliases = ("plane crash", "crashed plane", "burning plane", "air disaster")
    keywords = ("aircraft", "airplane", "crash", "fire", "accident", "disaster", "flight")

    def build(self) -> None:
        tail_top = add(TAIL_BOT, OFFSET)                      # (7,21)

        # Fuselage, clockwise from the tail cap.
        self.add_line("tail", tail_top, TAIL_BOT)
        self.add_line("belly", TAIL_BOT, LAND)
        self.add_line("skid", LAND, NOSE_DOWN)
        self.add_bezier("nose", NOSE_DOWN, ((42, 35.5), (40, 32), NOSE_TOP))
        self.add_line("top-wing", NOSE_TOP, WING_ROOT_L)
        self.add_line("top-mid", WING_ROOT_L, FLAME_END)
        self.add_line("top-rear", FLAME_END, tail_top)
        self.add_contour(
            "fuselage", "tail", "belly", "skid", "nose",
            "top-wing", "top-mid", "top-rear", closed=True,
        )

        # Wing: leading edge, tip, trailing edge, tapering toward the tip.
        self.add_line("wing-lead", WING_ROOT_L, WING_TIP_L)
        self.add_line("wing-tip", WING_TIP_L, WING_TIP_T)
        self.add_line("wing-trail", WING_TIP_T, WING_ROOT_T)
        self.add_contour("wing", "wing-lead", "wing-tip", "wing-trail")
        self.relate("connect", "wing", "fuselage")

        # Flame: tall tongue on the left, small tongue on the right.
        self.add_bezier(
            "flame",
            tail_top,
            ((4, 17), (5, 11), (11, 8)),          # left flank up to the tall tip
            ((11, 11), (13, 15), (16, 15)),       # down into the notch
            ((18, 15), (19, 13), (21, 11)),       # up to the small tip
            ((24, 15), (23, 21), FLAME_END),      # right flank down to the fuselage
        )
        self.relate("connect", "flame", "fuselage")

        # Ground: one level line split where the fuselage touches it.
        self.add_line("ground-l", (LEFT, GROUND_Y), LAND)
        self.add_line("ground-r", NOSE_DOWN, (RIGHT, GROUND_Y))
        self.relate("connect", "ground-l", "fuselage")
        self.relate("connect", "ground-r", "fuselage")
