"""hand-holding-wrench (redraw of the new-pipeline traced SVG).

Subject: an upright open-end wrench gripped by a fist whose forearm enters
from the lower left; only the jaw head and a short neck show above the fist.

Plan: VRECT_M (centerline box (10,4)-(38,44)), wrench axis x=24.
- wrench: one open contour, mirrored about x=24. Jaw tips on y=4, short
  straight jaw walls x=19/x=29 into a r=5 round slot bottom (slot 10 wide,
  6 ink); each cheek is a two-cubic curve bulging to the box sides x=10/x=38
  and turning steeply into the neck at y=18; the neck walls continue the
  jaw-wall columns (as in the image) down to the fist top y=26, where they
  end on shared knots (T-junctions, declared connect).
- hand: one open contour. Forearm top (10,35)-(15,34), a corner at the
  wrist (kept from the image), the back of the hand rising to the fist top
  y=26, two finger bars 8 tall with r=4 round ends on x=38, the palm on
  y=42 and the forearm bottom out to (10,44).
- crease: one line on y=34 from the finger ends to a free end at x=25.
References: the generated PNG (upright wrench, U jaw, neck columns matching
the jaw walls, stacked finger ends on the right, forearm lower left). Lucide
`wrench` is diagonal and single-ended; only its open-jaw idea was used.
Dropped: the four traced finger lozenges and the separate thumb (three
bars plus a thumb cannot fit 8-apart in 16 units), reduced to two fingers.

Metric issues (svg_metrics) and what happened to them:
- stroke-width (info): fixed, redrawn at stroke 4 with every gap budgeted
  for it (slot 10, neck 10, finger bars 8, cheek-to-fist 8+).
- keyshape-short-axis (SQUARE x filled 60%): fixed by switching to VRECT_M
  (equal score 0.85, smaller stretch 1.18 vs 1.68); every extreme is on the
  box: jaw tips y=4, forearm bottom y=44, forearm and left cheek x=10,
  finger ends and right cheek x=38.
- clearance e0/e2, e1/e4, e1/e5, e2/e4, e3/e5, e4/e5 (3.8-7.6 on
  centerlines): all came from the tiny traced finger lozenges, thumb and
  palm fragments crowding the grip; the fist is rebuilt as two 8-tall bars
  and every unconnected pair is >= 8 apart on centerlines.
- hole 2.6 at (28.2,16.2) (the traced jaw slot / neck gap): fixed, the
  wrench interior is 10 wide between the neck walls and the slot is 10
  wide (6 ink).
Validation: validate_icon() valid, build_gate PASS (0 errors, 0 warnings).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "80b7765d-72c2-4b01-b0bf-6a084aa9bc97"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1314-hand-holding-wrench/hand-holding-wrench_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24                  # wrench axis
SLOT_HALF = 5              # jaw walls x=19 / x=29 (10 apart), also the neck walls
TIP_Y = 4                  # jaw tips on the box top
SLOT_WALL = 2              # straight jaw walls y=4..7, then a r=5 round bottom (y=12)
HEAD_X = 10                # cheek extremes on the box sides x=10 / x=38
HEAD_MID = 12              # cheek extreme height (vertical tangent)
SHOULDER_Y = 18            # cheeks meet the neck here, steeply
FIST_TOP = 26
FINGER_R = 4               # two finger bars, 8 tall, round ends on x=38
FINGER_X = 34              # finger-end arc centres
CREASE_X = 25              # free left end of the finger crease
WRIST = (15, 34)           # forearm top meets the back of the hand
ARM_TOP_END = (10, 35)     # forearm ends on the box left
PALM_END = (22, 42)
ARM_BOTTOM_END = (10, 44)


class HandHoldingWrenchRedraw(Solo48):
    icon_id = "hand-holding-wrench-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/tools"
    aliases = ("hand with wrench", "holding wrench", "wrench in hand", "hand holding spanner")
    keywords = ("wrench", "spanner", "hand", "holding", "grip", "tool", "repair",
                "maintenance", "mechanic", "fix", "service")

    def build(self) -> None:
        tl, tr = AXIS - SLOT_HALF, AXIS + SLOT_HALF    # 19, 29
        wall_bot = TIP_Y + SLOT_WALL                   # 7

        # Wrench (one open contour ending on the fist): left neck, left cheek,
        # jaw, right cheek, right neck. Right side mirrors the left about x=24.
        ext = (HEAD_X, HEAD_MID)
        sh = (tl, SHOULDER_Y)
        tip = (tl, TIP_Y)
        cheek_lo = ((tl - 4, SHOULDER_Y - 1), (HEAD_X, HEAD_MID + 4), ext)   # shoulder -> extreme
        cheek_hi = ((HEAD_X, HEAD_MID - 5), (tl - 4, TIP_Y), tip)          # extreme -> tip
        mx = lambda q: (2 * AXIS - q[0], q[1])
        self.add_line("neck-l", (tl, FIST_TOP), sh)
        self.add_bezier("cheek-l", sh, cheek_lo, cheek_hi)
        self.add_line("jaw-wall-l", tip, (tl, wall_bot))
        self.add_arc("jaw-l", (tl, wall_bot), (AXIS, wall_bot + SLOT_HALF), radius_x=SLOT_HALF, sweep=False)
        self.add_arc("jaw-r", (AXIS, wall_bot + SLOT_HALF), (tr, wall_bot), radius_x=SLOT_HALF, sweep=False)
        self.add_line("jaw-wall-r", (tr, wall_bot), mx(tip))
        self.add_bezier("cheek-r", mx(tip),
                        (mx(cheek_hi[1]), mx(cheek_hi[0]), mx(ext)),
                        (mx(cheek_lo[1]), mx(cheek_lo[0]), mx(sh)))
        self.add_line("neck-r", mx(sh), (tr, FIST_TOP))
        self.add_contour("wrench", "neck-l", "cheek-l", "jaw-wall-l", "jaw-l", "jaw-r",
                         "jaw-wall-r", "cheek-r", "neck-r")

        # Hand: forearm top, back of hand, fist top, two finger ends, palm, forearm bottom.
        mid = FIST_TOP + 2 * FINGER_R
        bot = mid + 2 * FINGER_R
        wx, wy = WRIST
        self.add_line("arm-top", ARM_TOP_END, WRIST)
        self.add_bezier("hand-back", WRIST, ((wx + 1, wy - 4), (wx + 1.5, FIST_TOP), (tl, FIST_TOP)))
        self.add_line("fist-top-1", (tl, FIST_TOP), (tr, FIST_TOP))
        self.add_line("fist-top-2", (tr, FIST_TOP), (FINGER_X, FIST_TOP))
        self.add_arc("finger-1a", (FINGER_X, FIST_TOP), (FINGER_X + FINGER_R, FIST_TOP + FINGER_R), radius_x=FINGER_R)
        self.add_arc("finger-1b", (FINGER_X + FINGER_R, FIST_TOP + FINGER_R), (FINGER_X, mid), radius_x=FINGER_R)
        self.add_arc("finger-2a", (FINGER_X, mid), (FINGER_X + FINGER_R, mid + FINGER_R), radius_x=FINGER_R)
        self.add_arc("finger-2b", (FINGER_X + FINGER_R, mid + FINGER_R), (FINGER_X, bot), radius_x=FINGER_R)
        self.add_line("palm", (FINGER_X, bot), PALM_END)
        self.add_line("arm-bottom", PALM_END, ARM_BOTTOM_END)
        self.add_contour("hand", "arm-top", "hand-back", "fist-top-1", "fist-top-2",
                         "finger-1a", "finger-1b", "finger-2a", "finger-2b", "palm", "arm-bottom")

        # Crease between the two fingers.
        self.add_line("crease", (FINGER_X, mid), (CREASE_X, mid))

        self.relate("connect", "wrench", "hand")
        self.relate("connect", "crease", "hand")
