"""hand-holding-fountain-pen (redraw of the new-pipeline traced SVG).

Subject: a fountain pen held diagonally, nib down-left, by a stylised hand
whose forearm enters from the lower right and whose curled finger presses
the barrel.

Plan: SQUARE (centerline box (6,6)-(42,42)).
- pen axis: the diagonal x+y=AXIS; positions along it are steps s from the
  nib tip, widths are perpendicular steps v (both in (1,-1)/(1,1) units, so
  every node stays on the integer grid).
- barrel: closed rectangle v=+-BARREL_V from s=NECK to s=TOP; its upper
  corner reaches y=6, its lower long side is split where the finger lands.
- nib: open polyline from the barrel's lower corners out to the flared
  shoulders (v=+-NIB_V) and in to the tip at x=6; it shares the barrel's
  bottom edge as its top.
- hand: forearm line from (42,42) to the wrist, then one cubic run that
  rises and curls over so the fingertip meets the barrel side (declared
  connect), i.e. the hand holds the pen.
Extremes: barrel cap corner y=6, nib tip x=6, forearm end (42,42).

Metric issues:
- stroke-width (info): redrawn at stroke 4; every gap is budgeted at 8 on
  centerlines.
- keyshape-short-axis: fixed; all four extremes sit on the SQUARE box.
- clearance e0/e1 (barrel vs hand): fixed; the fingertip now lands on the
  split barrel side as a declared contact and the rest of the hand keeps
  8+ from the barrel.
- clearance e0/e2 (barrel vs nib) and hole 1.0 at (13.4,25.5): fixed; the
  nib hangs off the barrel's bottom edge (shared nodes), so there is no
  collar sliver.
- hole 2.95 at (23.3,17.6): fixed; barrel is 8 steps (11.3) wide on
  centerlines, the nib interior is larger still.
- clearance e0/e3, e2/e3 and narrow-join e3/e2 (nib slit): resolved by
  dropping the slit. A slit from the tip fuses into a wedge, and one hung
  from the barrel edge measures 1.9 ink clearance to the nib shoulders
  (4 required) at this nib size; the flared diamond carries the nib.
- no-head: not applicable; the subject is a hand only (no head or torso),
  so no human figure is marked.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "83ff3171-53c2-4300-a683-6306ba8fe250"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1301-hand-holding-fountain-pen/hand-holding-fountain-pen_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 40                  # pen axis x+y=AXIS; nib tip at (6, AXIS-6)
TIP_X = 6
NECK, TOP = 11, 24         # barrel from s=NECK to s=TOP
BARREL_V = 4
NIB_S, NIB_V = 7, 6        # flared nib shoulders
FINGER_S = 17              # where the fingertip lands on the barrel's lower side
WRIST = (33, 36)
ARM_END = (42, 42)


def at(s: int, v: int = 0) -> tuple[int, int]:
    return (TIP_X + s + v, AXIS - TIP_X - s + v)


class HandHoldingFountainPenRedraw(Solo48):
    icon_id = "hand-holding-fountain-pen-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/stationery"
    aliases = ("holding pen", "fountain pen in hand", "writing hand")
    keywords = ("pen", "fountain pen", "nib", "hand", "write", "writing", "sign", "signature", "author")

    def build(self) -> None:
        # Barrel: bottom edge, upper side, cap, lower side split at the finger.
        self.add_line("barrel-bottom", at(NECK, BARREL_V), at(NECK, -BARREL_V))
        self.add_line("barrel-upper", at(NECK, -BARREL_V), at(TOP, -BARREL_V))
        self.add_line("barrel-cap", at(TOP, -BARREL_V), at(TOP, BARREL_V))
        self.add_line("barrel-lower-a", at(TOP, BARREL_V), at(FINGER_S, BARREL_V))
        self.add_line("barrel-lower-b", at(FINGER_S, BARREL_V), at(NECK, BARREL_V))
        self.add_contour("barrel", "barrel-bottom", "barrel-upper", "barrel-cap",
                         "barrel-lower-a", "barrel-lower-b", closed=True)

        # Nib: flared diamond hanging off the barrel's bottom edge.
        self.add_polyline("nib", at(NECK, -BARREL_V), at(NIB_S, -NIB_V), at(0),
                          at(NIB_S, NIB_V), at(NECK, BARREL_V))
        self.relate("connect", "nib", "barrel")

        # Hand: forearm, then a curled finger pressing the barrel.
        tip = at(FINGER_S, BARREL_V)
        self.add_line("forearm", ARM_END, WRIST)
        self.add_bezier(
            "finger", WRIST,
            ((31, 34.7), (33, 31.5), (33, 29)),
            ((33, 26), (29.5, 23.5), tip),
        )
        self.add_contour("hand", "forearm", "finger")
        self.relate("connect", "hand", "barrel")
