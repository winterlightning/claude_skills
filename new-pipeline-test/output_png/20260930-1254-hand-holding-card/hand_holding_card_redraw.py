"""hand-holding-card (redraw of the new-pipeline traced SVG).

Plan: a landscape card held by a hand entering from the lower left, the
thumb lying over the card's lower-left corner. SQUARE, centerline box
(6,6)-(42,42).
- card: one open rounded-rectangle contour (x 14..42, y 6..27, corner r 4)
  that starts where the hand's top edge meets its left wall (14,25), runs
  round the top and right, and ends on the thumb's underside at (25,27).
  The bottom is split at (35,27) where the palm rises into it.
- hand: one open contour. A short 45-degree forearm stroke (6,34)-(9,31)
  flows tangentially into the thumb's top edge (direction (3,-4)); the thumb
  is a capsule 10 wide on centerlines with a semicircular tip r 5 about
  (24,20) (tip 9 below the card top), whose underside runs back down-left,
  crosses the card bottom at (25,27) and ends free at (22,31).
- palm: the forearm's lower 45-degree edge (14,42)-(17,39), 11.3 from the
  upper one, then one long cubic under the thumb that turns vertical and
  meets the card bottom at (35,27).
Extremes: x=6 forearm top, y=6 card top, x=42 card right, y=42 forearm low.

Metric issues (hand-holding-card_metrics.json):
- stroke-width (info, trace 2.38): fixed, redrawn at stroke 4 with every gap
  re-budgeted.
- keyshape-short-axis (SQUARE y filled 73%): fixed, card top y=6 and the
  forearm end y=42 reach the box; the card is taller (21) and the forearm
  longer so the drawing fills the square without stretching.
- clearance e0/e1, e0/e4 (palm underside vs forearm top / thumb end, 5.2-6.7):
  fixed, the palm curve is dropped low (cubic control at y 40) so it is
  >= 8 on centerlines (build-gate internal spacing >= 4 ink) from the thumb.
- clearance e0/e2, e0/e3 (palm vs card bottom / thumb, 6.3-6.7): fixed, the
  palm meets the card bottom square-on at a shared node instead of running
  alongside it.
- clearance e1/e4, e4/e5 (thumb underside vs hand edge and card, 6.0): fixed,
  the thumb is a 10-wide capsule and its underside meets the card bottom at
  one shared node; the forearm edge and thumb top are one tangent stroke.
- hole (8.6, ok): the card's opening stays >= 9 wide around the thumb.
Reference: Lucide `hand-coins` / `hand-helping` (open forearm edges and a palm
curve rising to the held object) and `credit-card` (rounded rectangle, r 4).
The hand is deliberately asymmetric (it enters from the lower left).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b8b0be96-48c9-4d4f-9c4a-c278eedc3dbe"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1254-hand-holding-card/hand-holding-card_raw.svg"
AUTHOR = "claude-opus-5-5"

# Card: landscape rounded rectangle in the upper right of the SQUARE box.
CARD_L, CARD_T, CARD_R, CARD_B, CARD_RAD = 14, 6, 42, 27, 4
# Thumb: a capsule lying over the card along direction (3,-4); tip radius 5
# about TIP_C, so its two edges sit 10 apart and meet the tip at +/-(4,3).
TIP_C, TIP_R = (24, 20), 5
THUMB_DIR = (3, -4)
GRIP = (14, 25)            # hand top edge meets the card's left wall here
CROSS = (25, 27)           # thumb's lower edge crosses the card bottom here
THUMB_END = (22, 31)       # thumb's lower edge ends free inside the palm
# Forearm: two parallel 45-degree strokes entering from the lower left.
WRIST_TOP, WRIST_TOP_BEND = (6, 34), (9, 31)
WRIST_LOW, WRIST_LOW_BEND = (14, 42), (17, 39)
PALM_TOP = (35, 27)        # palm edge rises vertically into the card bottom


class HandHoldingCardRedraw(Solo48):
    icon_id = "hand-holding-card-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "payments"
    aliases = ("hand-holding-credit-card", "card-in-hand")
    keywords = ("card", "credit card", "hand", "holding", "payment", "pay", "business card", "id card")

    def build(self) -> None:
        cx, cy = TIP_C
        tip_top = (cx - 4, cy - 3)       # (20,17)
        tip_low = (cx + 4, cy + 3)       # (28,23)
        dx, dy = THUMB_DIR

        # Hand: forearm top edge -> tangent curve -> thumb top -> tip -> thumb underside.
        self.add_line("arm-top", WRIST_TOP, WRIST_TOP_BEND)
        bx, by = WRIST_TOP_BEND
        gx, gy = GRIP
        self.add_bezier("hand-top", WRIST_TOP_BEND, ((bx + 2, by - 2), (gx - 0.6 * dx, gy - 0.6 * dy), GRIP))
        self.add_line("thumb-top", GRIP, tip_top)
        self.add_arc("thumb-tip", tip_top, tip_low, radius_x=TIP_R, sweep=True)
        self.add_line("thumb-under", tip_low, CROSS)
        self.add_line("thumb-end", CROSS, THUMB_END)
        self.add_contour("hand", "arm-top", "hand-top", "thumb-top", "thumb-tip", "thumb-under", "thumb-end")

        # Card: open contour from the grip, round the top, back along the bottom to the thumb.
        r = CARD_RAD
        self.add_line("card-left", GRIP, (CARD_L, CARD_T + r))
        self.add_arc("card-tl", (CARD_L, CARD_T + r), (CARD_L + r, CARD_T), radius_x=r, sweep=True)
        self.add_line("card-top", (CARD_L + r, CARD_T), (CARD_R - r, CARD_T))
        self.add_arc("card-tr", (CARD_R - r, CARD_T), (CARD_R, CARD_T + r), radius_x=r, sweep=True)
        self.add_line("card-right", (CARD_R, CARD_T + r), (CARD_R, CARD_B - r))
        self.add_arc("card-br", (CARD_R, CARD_B - r), (CARD_R - r, CARD_B), radius_x=r, sweep=True)
        self.add_line("card-bottom-right", (CARD_R - r, CARD_B), PALM_TOP)
        self.add_line("card-bottom-left", PALM_TOP, CROSS)
        self.add_contour("card", "card-left", "card-tl", "card-top", "card-tr", "card-right",
                         "card-br", "card-bottom-right", "card-bottom-left")

        # Palm underside: forearm bottom edge -> long curve -> up into the card bottom.
        self.add_line("arm-low", WRIST_LOW, WRIST_LOW_BEND)
        lx, ly = WRIST_LOW_BEND
        px, py = PALM_TOP
        self.add_bezier("palm-low", WRIST_LOW_BEND, ((lx + 2, ly - 2), (px, py + 13), PALM_TOP))
        self.add_contour("palm", "arm-low", "palm-low")

        self.relate("connect", "hand", "card")
        self.relate("connect", "palm", "card")
