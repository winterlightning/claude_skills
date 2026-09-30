"""hand-holding-bowl-beneath-round-object (redraw of the new-pipeline traced SVG).

Plan: a ring ball floats above a flat-rimmed bowl on a shared vertical axis
x=X, and the bowl rests on a flat hand whose forearm drops at 45 degrees to
the lower-left corner. SQUARE, centerline box (6,6)-(42,42).
- ball: 4-cardinal-arc circle r5 about (X,11); top y=6 is the keyshape top,
  and the 10-unit ring leaves a 6-unit hole.
- bowl: rim line (16,25)-(42,25) closed by two quarter-ellipse arcs
  (rx13, ry10) meeting at the apex (X,35). The right rim end x=42 is the
  keyshape right side. Depth 10 leaves a 6-unit hole.
- hand: one contour: forearm (6,42)->(13,35) at 45 degrees (the (6,42) end
  is the left/bottom extreme), then palm (13,35)->(X,35) and fingers
  (X,35)->(38,35). The hand touches the bowl at its apex, which is shared
  with both bowl arcs and declared with `connect`.

Metric issues:
- stroke-width (info): redrawn at stroke 4.
- keyshape-short-axis (warn): fixed. The bowl was widened to 26 and the
  forearm reaches x=6, so the x extremes sit on 6 and 42 without stretching.
- clearance e0/e1 (ball vs bowl, 3.69): fixed. The ball bottom (16) and the rim (25)
  are 9 apart on centerlines. At exactly 8 the curve-to-line pair came back
  `review`, so the gap is one unit wider.
- clearance e1/e2 (bowl vs hand, 2.75): resolved by contact, not by a gap.
  The 36-unit height cannot hold ball (10) + 8 + bowl (10) + 8 + a hand with
  a falling forearm, so the hand now holds the bowl: the palm passes through
  the bowl apex, and that shared endpoint is a declared connection.
- hole at (23.7,25.1), 2.8 wide: fixed. The traced bowl was a thin shape;
  the redraw uses a 10-deep rim + arc bowl, which leaves a 6-unit hole.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e92a7970-9b72-4523-8caa-4f5d34540b96"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1250-hand-holding-bowl-beneath-round-object/hand-holding-bowl-beneath-round-object_raw.svg"
AUTHOR = "claude-opus-5-5"

X = 29              # shared axis of ball and bowl
BR = 5              # ball radius
BY = 6 + BR         # ball centre y (top on the keyshape edge)
RIM = BY + BR + 9   # rim 9 below the ball bottom (curve vs line clearance)
RX, RY = 13, 10     # bowl half-width and depth
BOT = RIM + RY      # bowl apex = palm line
WRIST = (6 + 42 - BOT, BOT)  # 45 degrees up from (6,42)
TIP = 38            # fingertip x


class HandHoldingBowlBeneathRoundObjectRedraw(Solo48):
    icon_id = "hand-holding-bowl-beneath-round-object-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/food"
    aliases = ("hand-holding-bowl", "offering-bowl", "serving-bowl")
    keywords = ("hand", "bowl", "ball", "hold", "serve", "offer", "dish", "food", "give")

    def build(self) -> None:
        ring = [(X, BY - BR), (X + BR, BY), (X, BY + BR), (X - BR, BY)]
        for i in range(4):
            self.add_arc(f"ball-{i}", ring[i], ring[(i + 1) % 4], radius_x=BR)
        self.add_contour("ball", *(f"ball-{i}" for i in range(4)), closed=True)

        self.add_line("bowl-rim", (X - RX, RIM), (X + RX, RIM))
        self.add_arc("bowl-right", (X + RX, RIM), (X, BOT), radius_x=RX, radius_y=RY)
        self.add_arc("bowl-left", (X, BOT), (X - RX, RIM), radius_x=RX, radius_y=RY)
        self.add_contour("bowl", "bowl-rim", "bowl-right", "bowl-left", closed=True)

        self.add_line("forearm", (6, 42), WRIST)
        self.add_line("palm", WRIST, (X, BOT))
        self.add_line("fingers", (X, BOT), (TIP, BOT))
        self.add_contour("hand", "forearm", "palm", "fingers")
        self.relate("connect", "palm", "bowl-right")
        self.relate("connect", "palm", "bowl-left")
