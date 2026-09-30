"""hand-passing-capsule (redraw of the new-pipeline traced SVG).

Plan: SQUARE, centerline box (6,6)-(42,42); a seamed capsule floats over the
palm of a hand reaching in from the lower left.
- capsule: one closed stadium, r6 ends about (22,12) and (34,12), 24 x 12.
  Its top (y 6) is the keyshape top. The seam is a
  vertical line at x=28 sharing both wall midpoints (declared connect), so
  each half keeps an 8-wide opening.
- hand: one open contour. The forearm is two parallel 1:2 edges
  (x+2y=76 and x+2y=96, 8.9 apart) entering from the lower left; the upper
  edge rises into a rounded thumb heel (top (17,26)), dips into the level
  palm at y=28 and lifts into an r4 fingertip about (38,30) (right x=42).
  The lower edge eases from the fingertip through a level palm base (y=36)
  into the forearm. Extremes: left 6 and bottom 42 from the forearm ends,
  right 42 from the fingertip, top 6 from the capsule.
Metric issues fixed:
- clearance e0/e2 (capsule 4.1 from the hand): the capsule bottom (y 18) is
  10 above the palm and every hand point is at least 8 from the capsule.
- holes at (34.7,12.0) and (28.3,17.9) (4.0 / 4.1 wide): each capsule half
  now has a 7.9 inscribed opening (r6 ends, cap centres 12 apart).
- stroke-width: authored at stroke 4 with every gap budgeted on centerlines.
- keyshape-short-axis: resolved by moving to SQUARE (below); all four extremes
  sit on the box exactly. svg_metrics on the redraw suggests SQUARE and lists
  no issues.
Not fixable as traced:
- HRECT_L (suggested): 32 tall cannot stack a hole-safe capsule, an 8 gap and
  an 8-thick palm while the forearm still drops to the lower left; SQUARE's
  36 does.
- the 45-degree capsule tilt: a tilted capsule with 6-wide halves is ~20
  tall, which leaves the palm on the canvas floor and forces a level forearm
  (tried; it read as a shoe). The capsule is drawn level so the forearm keeps
  its diagonal reach.
- no-head: not applicable; the subject is an isolated arm and hand, not a
  figure, so no head, torso or mark_human_figure.
Lucide: `pill` for the seamed stadium, `hand-coins` / `hand-heart` for the
open palm-up hand read (upper palm edge + fingertip curl + forearm pair).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "37a4523d-3384-4c79-9494-a5cfb681f4f0"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1328-hand-passing-capsule/"
    "hand-passing-capsule_raw.svg"
)
AUTHOR = "claude-opus-5-5"

# Capsule: level stadium, r6 ends, centres 12 apart; its top is the
# keyshape top.
R = 6
C_LEFT, C_RIGHT = (22, 12), (34, 12)
# Hand: forearm on the 1:2 diagonal (edges x+2y=76 and x+2y=96, 8.9 apart),
# palm band 28..36, thumb heel rising to 26, r4 fingertip about (38,30).
ARM_TOP_END, HEEL = (6, 35), (10, 33)
THUMB = (17, 26)
PALM_L, PALM_R = (24, 28), (29, 28)
TIP, TIP_R = (38, 30), 4
BASE_R, WRIST_LOW, ARM_LOW_END = (29, 36), (20, 38), (12, 42)


class HandPassingCapsuleRedraw(Solo48):
    icon_id = "hand-passing-capsule-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "medical/medicine"
    aliases = ("hand with pill", "give medicine", "drug dealer", "pill in hand")
    keywords = ("hand", "capsule", "pill", "medicine", "drug", "dose", "pharmacy", "give")

    def build(self) -> None:
        # -- capsule: level stadium, seam at mid-length ------------------------
        (lx, cy), (rx, _) = C_LEFT, C_RIGHT
        top_y, bot_y = cy - R, cy + R
        mid = (lx + rx) // 2
        self.add_line("cap-top-l", (lx, top_y), (mid, top_y))
        self.add_line("cap-top-r", (mid, top_y), (rx, top_y))
        self.add_arc("cap-end-r", (rx, top_y), (rx, bot_y), radius_x=R)
        self.add_line("cap-bot-r", (rx, bot_y), (mid, bot_y))
        self.add_line("cap-bot-l", (mid, bot_y), (lx, bot_y))
        self.add_arc("cap-end-l", (lx, bot_y), (lx, top_y), radius_x=R)
        self.add_contour(
            "capsule", "cap-top-l", "cap-top-r", "cap-end-r", "cap-bot-r",
            "cap-bot-l", "cap-end-l", closed=True,
        )
        self.add_line("seam", (mid, top_y), (mid, bot_y))
        self.relate("connect", "seam", "capsule")

        # -- hand ---------------------------------------------------------
        tx, ty = TIP
        tip_top, tip_bot = (tx, ty - TIP_R), (tx, ty + TIP_R)
        self.add_line("arm-top", ARM_TOP_END, HEEL)
        self.add_bezier(
            "thumb", HEEL,
            ((HEEL[0] + 4, HEEL[1] - 2), (THUMB[0] - 3, THUMB[1]), THUMB),
            ((THUMB[0] + 3, THUMB[1]), (PALM_L[0] - 3, PALM_L[1]), PALM_L),
        )
        self.add_line("palm-top", PALM_L, PALM_R)
        self.add_bezier(
            "fingers-top", PALM_R,
            ((PALM_R[0] + 3, PALM_R[1]), (tx - 3, tip_top[1]), tip_top),
        )
        self.add_arc("fingertip", tip_top, tip_bot, radius_x=TIP_R)
        self.add_bezier(
            "fingers-low", tip_bot,
            ((tx - 3, tip_bot[1]), (BASE_R[0] + 3, BASE_R[1]), BASE_R),
        )
        # Palm base eases from level into the forearm's 1:2 slope.
        self.add_bezier(
            "palm-base", BASE_R,
            ((BASE_R[0] - 3, BASE_R[1]), (WRIST_LOW[0] + 2, WRIST_LOW[1] - 1), WRIST_LOW),
        )
        self.add_line("arm-low", WRIST_LOW, ARM_LOW_END)
        self.add_contour(
            "hand", "arm-top", "thumb", "palm-top", "fingers-top", "fingertip",
            "fingers-low", "palm-base", "arm-low",
        )
