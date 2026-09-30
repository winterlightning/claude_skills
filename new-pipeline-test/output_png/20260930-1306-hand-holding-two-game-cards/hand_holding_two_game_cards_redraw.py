"""hand-holding-two-game-cards (redraw of the new-pipeline traced SVG).

Subject: two fanned game cards held up by a hand rising from the bottom;
the thumb presses across the front card's lower-left corner.

Plan: VRECT_L (centerline box (8,4)-(40,44)).
- cards: two equal 15.8 x 19 rectangles on 1:3 tilts, back card leaning
  left (width (15,-5), height (6,18)), front card leaning right (width
  (15,5), height (-6,18)). Extremes: back top-left x=8, back top-right y=4,
  front top-right x=40.
- overlap: the front card's top-left corner sits on the back card's right
  edge (B_TR + 2*(1,3)), so that edge ends in a Y node (53/127 deg) instead
  of the trace's crossing wedge.
- hand: one open contour -- left wrist (16,44) up, palm edge to P on the
  back card's left edge, thumb top P->Q (Q on the front card's left edge),
  a semicircular pad on the diameter Q->R (R on the front card's bottom
  edge, apex 9.5 from the card's right edge), and a short underside
  continuing the pad tangent into the palm. The right wrist is a vertical
  line from the front card's bottom edge to y=44 (extreme y=44), leaving
  the card's bottom-right corner visible as in the source.
- hidden parts (back card's lower half, front card's lower-left corner)
  are simply not drawn; every visible end sits on an integer node on the
  part it disappears behind and is declared connect.

Metric issues:
- keyshape-short-axis (SQUARE x fill 86%): fixed -- the subject is taller
  than wide, and SQUARE's 36-wide box cannot host two overlapping cards of
  equal size; VRECT_L's 32x40 box is filled exactly on all four sides.
- clearance e0/e3, e0/e4 (thumb free end against the hand side and back
  card corner, 4.2): fixed -- the thumb starts at the shared node P instead
  of floating next to it; its underside ends 10 from both hand sides.
- clearance e0/e5 (thumb against the right hand side, 5.19): fixed -- the
  right side starts on the card bottom at (31,32), 6 right of the pad end,
  and the thumb underside runs away from it.
- clearance e2/e3, e2/e4 (front card's left corner against the hand side
  and back card, 5.7): fixed -- that corner is hidden behind the thumb.
- narrow-join e1/e0 (26.67 deg): fixed -- joins are now 57.5 deg (thumb
  top / front card left edge), 85.6 deg (thumb top / back card left edge),
  45 deg (pad end / front card bottom), 71.6 deg (right wrist / card bottom)
  and 53 deg (back card edge / front card corner).
- loose-join e2 (0.8 short): fixed -- all contacts share exact integer
  endpoints and are declared with relate("connect").
- stroke-width (trace 2.38 vs 4): addressed by rebuilding every gap at
  stroke 4 on the 48 grid; validate_icon() valid, build gate pass, no
  warnings.
Not kept: the rounded card corners of the PNG (round joins give the only
rounding, so every extreme stays on an integer node) and the thumb's long
crease into the palm (it failed the 4-unit internal spacing against both
hand sides).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "9e452a20-d223-431c-a550-2caad608f489"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1306-hand-holding-two-game-cards/hand-holding-two-game-cards_raw.svg"
AUTHOR = "claude-opus-5-5"

K = 0.5523  # cubic quarter-circle constant

# Back card (left, tilted CCW 1:3): width (15,-5), height (6,18).
B_TL, B_TR = (8, 9), (23, 4)
# Front card (right, tilted CW 1:3): its top-left corner sits on the back
# card's right edge (B_TR + 2*(1,3)), so that edge ends in a clean Y node.
F_TL, F_TR, F_BR = (25, 10), (40, 15), (34, 33)
# Hand: thumb crosses the front card's lower-left corner; its pad is a
# semicircle on the diameter Q-R (Q on the left edge, R on the bottom edge).
P = (13, 24)          # back card's left edge meets the hand
Q, R = (21, 22), (25, 30)
WRIST_L, WRIST_R, WRIST_Y = 16, 31, 44
THUMB_END = (21, 32)   # pad tangent (-2,1) continued into the palm
HAND_R_TOP = (31, 32)  # on the front card's bottom edge


def _pad():
    mx, my = (Q[0] + R[0]) / 2, (Q[1] + R[1]) / 2
    ux, uy = (Q[0] - mx), (Q[1] - my)          # radius vector to Q
    ax, ay = -uy, ux                           # radius vector to the apex
    if ax * 3 + ay < 0:                        # apex points into the card
        ax, ay = -ax, -ay
    apex = (mx + ax, my + ay)
    # Leave Q along the thumb's top edge (P->Q) so the pad has no kink.
    tx, ty = Q[0] - P[0], Q[1] - P[1]
    t = K * (ax * ax + ay * ay) ** 0.5 / (tx * tx + ty * ty) ** 0.5
    return (
        ((Q[0] + t * tx, Q[1] + t * ty), (apex[0] - K * (-ux), apex[1] - K * (-uy)), apex),
        ((apex[0] + K * (-ux), apex[1] + K * (-uy)), (R[0] + K * ax, R[1] + K * ay), R),
    )


class HandHoldingTwoGameCardsRedraw(Solo48):
    icon_id = "hand-holding-two-game-cards-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "games"
    aliases = ("hand of cards", "holding playing cards", "card hand")
    keywords = ("cards", "playing cards", "game", "poker", "hand", "holding", "deal", "draw")

    def build(self) -> None:
        self.add_polyline("back-card", P, B_TL, B_TR, F_TL)
        self.add_polyline("front-card", Q, F_TL, F_TR, F_BR, R)
        self.relate("connect", "back-card", "front-card")

        self.add_line("wrist-left", (WRIST_L, WRIST_Y), (WRIST_L, 37))
        self.add_bezier("palm-left", (WRIST_L, 37), ((WRIST_L, 32), (12, 29), P))
        self.add_line("thumb-top", P, Q)
        self.add_bezier("thumb-pad", Q, *_pad())
        self.add_line("thumb-under", R, THUMB_END)
        self.add_contour("hand", "wrist-left", "palm-left", "thumb-top", "thumb-pad", "thumb-under")
        self.relate("connect", "hand", "back-card")
        self.relate("connect", "hand", "front-card")

        self.add_line("wrist-right", HAND_R_TOP, (WRIST_R, WRIST_Y))
        self.relate("connect", "wrist-right", "front-card")
