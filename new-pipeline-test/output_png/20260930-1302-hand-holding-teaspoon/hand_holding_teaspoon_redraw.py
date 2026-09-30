"""hand-holding-teaspoon (redraw of the new-pipeline traced SVG).

Subject: a hand gripping a teaspoon; the spoon rises diagonally to the
upper right.

Plan: SQUARE (centerline box (6,6)-(42,42)), everything on the 45 degree
arm axis.
- bowl: closed tilted oval, mirror-symmetric about the 45 degree axis
  through NECK; top knot on y=6, right knot on x=42 (level/plumb tangents
  so the extremes sit exactly on the box), neck knot on the axis.
- handle: 45 degree line from NECK down-left to the top of the fist (T-joint).
- hand: one open contour -- upper wrist line from x=6 (x + y = 44), back
  of the hand rising to the grip, index (r4) and second finger (r3) as
  stacked semicircles on one column, palm curving back into the lower
  wrist line (x + y = 57) that ends on y=42.
- dropped: the thumb stroke. The fist interior is 11 between the back and
  the palm, short of the 16-17 a mark needs between two curved walls.

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap was budgeted at 8
  on centerlines.
- keyshape-short-axis (warn): fixed -- bowl top on y=6, bowl right on
  x=42, upper wrist on x=6, lower wrist on y=42, all with exact extremes.
- clearance e1/e3 (7.62) and e1/e4 (6.46) (error): fixed -- the wrist
  lines are 9.19 apart and the fist and palm were re-laid out; no loose
  parts remain, and the build gate's internal spacing passes.
- loose-join e4/e0 (info): fixed -- the handle shares the bowl's neck
  knot and the index top, declared with relate("connect").
- hole 2.97 (error): fixed -- the bowl was rebuilt as a wider oval
  (neck to far tip about 13, across about 9 on centerlines); the build gate's hole check passes.
Validation: validate_icon() valid; build_gate PASS, 0 warnings.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d2d4de96-ee6e-420e-9d3b-ad79631d2a67"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1302-hand-holding-teaspoon/hand-holding-teaspoon_raw.svg"
AUTHOR = "claude-opus-5-5"

# Bowl: mirror-symmetric about the 45 degree axis through NECK.
TOP = (38, 6)          # level tangent on the box top
RIGHT = (42, 10)       # plumb tangent on the box right (mirror of TOP)
NECK = (32, 16)        # bowl neck on the axis, handle joint
NECK_H = 3.5           # neck handle length (each axis component)
TIP_H = 2.6            # handle length at TOP/RIGHT toward the far tip
SIDE_H = 4.5           # handle length at TOP/RIGHT toward the neck

# Hand.
WRIST_UP = ((6, 38), (12, 32))    # on x + y = 44
WRIST_LO = ((15, 42), (19, 38))   # on x + y = 57: 9.19 from the upper line: 8.49 from the upper line
GRIP = (25, 23)        # handle enters the fist here (top of the index)
FINGER_X = 25          # finger semicircles are centred on this column
FINGER_R = (4, 3)      # index, second finger


class HandHoldingTeaspoonRedraw(Solo48):
    icon_id = "hand-holding-teaspoon-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/kitchen"
    aliases = ("hand with spoon", "holding spoon", "teaspoon in hand")
    keywords = ("hand", "spoon", "teaspoon", "eat", "eating", "feeding", "cutlery", "kitchen", "grip")

    def build(self) -> None:
        nx, ny = NECK
        # Bowl: neck -> top (upper-left flank), top -> right (far tip),
        # right -> neck (lower-right flank, mirror of the first run).
        self.add_bezier(
            "bowl", NECK,
            ((nx - NECK_H, ny - NECK_H), (TOP[0] - SIDE_H, TOP[1]), TOP),
            ((TOP[0] + TIP_H, TOP[1]), (RIGHT[0], RIGHT[1] - TIP_H), RIGHT),
            ((RIGHT[0], RIGHT[1] + SIDE_H), (nx + NECK_H, ny + NECK_H), NECK),
        )
        self.add_contour("bowl-outline", "bowl", closed=True)

        self.add_line("handle", NECK, GRIP)
        self.relate("connect", "handle", "bowl-outline")

        (ax, ay), (bx, by) = WRIST_UP
        (ex, ey), (fx, fy) = WRIST_LO
        gx, gy = GRIP
        r1, r2 = FINGER_R
        f1 = (FINGER_X, gy + 2 * r1)          # index bottom / second top
        f2 = (FINGER_X, f1[1] + 2 * r2)       # second finger bottom
        self.add_line("wrist-up", WRIST_UP[0], WRIST_UP[1])
        self.add_bezier("back", (bx, by), ((bx + 2, by - 2), (gx - 5, gy), GRIP))
        self.add_arc("index", GRIP, f1, radius_x=r1, sweep=True)
        self.add_arc("finger", f1, f2, radius_x=r2, sweep=True)
        self.add_bezier("palm", f2, ((f2[0] - 2.5, f2[1]), (fx + 1.5, fy - 1.5), (fx, fy)))
        self.add_line("wrist-lo", (fx, fy), (ex, ey))
        self.add_contour("hand", "wrist-up", "back", "index", "finger", "palm", "wrist-lo")
        self.relate("connect", "handle", "hand")
