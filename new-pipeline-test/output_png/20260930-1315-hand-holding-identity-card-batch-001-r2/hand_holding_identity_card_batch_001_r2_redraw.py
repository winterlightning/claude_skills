"""hand-holding-identity-card (redraw of the new-pipeline traced SVG).

Plan: an identity badge with a user portrait, held up on an open palm.
VRECT_L, centerline box (8,4)-(40,44).
- card: open rounded-rectangle contour (x 8..36, top y 4, corner r 4) whose
  walls end on the hand's top edge at y 32; the hand sits in front of the
  card's lower edge, so the card needs no bottom of its own.
- portrait on the card axis x=22: a dot head at (22,13), 9 below the card
  top, and a Lucide square-user bust standing on the palm edge (sides at
  x 17 / 27, r 4 shoulders, flat top y 21). Head-to-bust gap is exactly 8 on
  centerlines (4 ink), flagged with mark_human_figure (torso = the half of the
  flat top that starts at the neck point).
- hand: one open contour -- palm top edge y 32 (split where card walls and
  bust sides stand on it), a fingertip semicircle r 4 curling round to
  (36,40), and a palm underside easing down to the wrist at y 44.
Extremes: x=8 card/palm left, y=4 card top, x=40 fingertip, y=44 wrist.

Keyshape: the metrics suggest SQUARE (36 tall). Card + head + 8 gap + bust +
hand needs about 40 vertically, so VRECT_L is used; its 32 width still holds
the card and the fingertip. The landscape card of the image becomes an
upright badge (only way the portrait fits above the palm at stroke 4).

Metric issues (hand-holding-identity-card-batch-001-r2_metrics.json):
- stroke-width (info, trace 2.76): fixed, redrawn at stroke 4; every gap was
  re-budgeted at 9 (exact-8 pairs on curved walls come back as review).
- stroke-count (8, budget 6): fixed, 4 strokes -- card, head, bust, hand. The
  sleeve cuff and the thumb crease line are dropped (no room for 8 gaps
  inside a 12-tall palm band).
- keyshape-short-axis (SQUARE y 100%): fixed, VRECT_L extremes are hit
  exactly by card top, card/palm left, fingertip and wrist.
- clearance e0/e1, e1/e2 (card top vs head, head vs shoulders, 2.3-3.3):
  fixed, head dot is 9 below the card top and 8 above the bust.
- clearance e0/e2, e0/e5, e0/e6, e2/e5 (card bottom vs shoulders / palm,
  3.5-7.2): fixed, the separate card bottom is gone; card walls and bust
  sides meet the palm edge at shared nodes (relate connect), and the bust
  sides stay 9 from the card walls.
- clearance e0/e3, e3/e5, e3/e7, e5/e7 (fingers, thumb line and palm
  underside, 2.1-7.2): fixed, one hand contour with the fingertip r 4 and a
  palm band 8-12 tall; the thumb line is removed.
- hole [25,12.5] 2.1 wide (head ring): fixed, the head is a solid dot.
- hole [25,21.7] 3.3 wide and [32,28.7] 2.7 wide (gap between head and
  shoulders / finger slivers): fixed, the bust opening is 6 wide and 7 tall,
  the card openings beside it are >= 5 ink; build gate passes.
- no-head (warn): fixed, the head is explicit and flagged as a human figure.
Not kept: a ring head (needs r 5 for a 6-wide hole, which pushes the bust
below the palm) and the landscape card proportion.
Reference: Lucide `square-user` (bust standing on the frame edge, dot/circle
head) and `hand-heart` / `hand-coins` (open palm curling into a fingertip).
The hand is deliberately asymmetric (fingers to the right).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "cb16642c-e584-52b6-ae9d-bff1579af112"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1315-hand-holding-identity-card-batch-001-r2/hand-holding-identity-card-batch-001-r2_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 22                          # card and portrait mirror axis
CARD_L, CARD_R, CARD_T, CARD_RAD = 8, 36, 4, 4
HEAD = (AXIS, 13)                  # dot head, 9 below the card top
BUST_TOP, BUST_HALF, BUST_RAD = 21, 5, 4   # bust: flat top y=21, sides at AXIS -/+ 5, corner r4
PALM_TOP, PALM_LOW = 32, 44        # hand top edge (in front of the card) / wrist underside
TIP_R = 4                          # fingertip semicircle, rightmost x = CARD_R + 4


class HandHoldingIdentityCardBatch001R2Redraw(Solo48):
    icon_id = "hand-holding-identity-card-batch-001-r2-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "identity"
    aliases = ("hand-holding-id-card", "id-card-in-hand", "identity-verification")
    keywords = ("hand", "holding", "id", "identity", "card", "badge", "profile", "user", "verification", "kyc")

    def build(self) -> None:
        r = CARD_RAD
        # Card: open contour, both walls end on the hand's top edge.
        self.add_line("card-left", (CARD_L, PALM_TOP), (CARD_L, CARD_T + r))
        self.add_arc("card-tl", (CARD_L, CARD_T + r), (CARD_L + r, CARD_T), radius_x=r)
        self.add_line("card-top", (CARD_L + r, CARD_T), (CARD_R - r, CARD_T))
        self.add_arc("card-tr", (CARD_R - r, CARD_T), (CARD_R, CARD_T + r), radius_x=r)
        self.add_line("card-right", (CARD_R, CARD_T + r), (CARD_R, PALM_TOP))
        self.add_contour("card", "card-left", "card-tl", "card-top", "card-tr", "card-right")

        # Portrait: dot head; square-user bust standing on the palm edge.
        self.add_dot("head", HEAD)
        bl, br, sr = AXIS - BUST_HALF, AXIS + BUST_HALF, BUST_RAD
        neck = (AXIS, BUST_TOP)
        self.add_line("bust-l", (bl, PALM_TOP), (bl, BUST_TOP + sr))
        self.add_arc("shoulder-l", (bl, BUST_TOP + sr), (bl + sr, BUST_TOP), radius_x=sr)
        self.add_line("neck-l", (bl + sr, BUST_TOP), neck)
        self.add_line("torso", neck, (br - sr, BUST_TOP))
        self.add_arc("shoulder-r", (br - sr, BUST_TOP), (br, BUST_TOP + sr), radius_x=sr)
        self.add_line("bust-r", (br, BUST_TOP + sr), (br, PALM_TOP))
        self.add_contour("bust", "bust-l", "shoulder-l", "neck-l", "torso", "shoulder-r", "bust-r")
        self.mark_human_figure("portrait", head="head", torso="torso", torso_junction="start")

        # Hand: palm top edge (split where the card and bust stand on it) ->
        # fingertip -> palm underside sweeping down to the wrist.
        tip_low = (CARD_R, PALM_TOP + 2 * TIP_R)
        self.add_line("palm-top-l", (CARD_L, PALM_TOP), (bl, PALM_TOP))
        self.add_line("palm-top-m", (bl, PALM_TOP), (br, PALM_TOP))
        self.add_line("palm-top-r", (br, PALM_TOP), (CARD_R, PALM_TOP))
        self.add_arc("fingertip", (CARD_R, PALM_TOP), tip_low, radius_x=TIP_R)
        self.add_bezier("palm-under", tip_low, ((CARD_R - 8, tip_low[1]), (24, PALM_LOW), (18, PALM_LOW)))
        self.add_line("wrist-low", (18, PALM_LOW), (CARD_L, PALM_LOW))
        self.add_contour("hand", "palm-top-l", "palm-top-m", "palm-top-r", "fingertip", "palm-under", "wrist-low")

        self.relate("connect", "card", "hand")
        self.relate("connect", "bust", "hand")
