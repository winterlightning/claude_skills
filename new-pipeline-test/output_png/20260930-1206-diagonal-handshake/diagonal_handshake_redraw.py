"""diagonal-handshake (redraw of the new-pipeline traced SVG).

Plan: two hands clasped on the lower-left -> upper-right diagonal, on SQUARE
(centerline box (6,6)-(42,42)), the keyshape the metrics suggest.
The arm axis is the diagonal x+y=48; every wrist runs at 45 degrees in one of
two bands, 12 apart in x+y (8.49 on centerlines):
- lower-left hand: wrist lines x+y=36 (top) and x+y=48 (bottom), from the
  square's left edge (6,30)/(6,42).
- upper-right hand: wrist lines x+y=48 (top) and x+y=60 (bottom), from the
  square's right edge (42,6)/(42,18). The two arms are offset by one arm
  width, which is what makes the hands overlap in the middle.
- top silhouette: lower-left wrist straight into the upper-right thumb, a
  horizontal back of the hand at y=14, then the upper-right wrist.
- thumb: a cardinal r4 hook leaves the top line at (16,20) and turns into the
  thumb underside at y=24 (10 below the back), then the palm edge drops at 45
  degrees onto the bottom line -- the "broad thumb overlap" of the grip.
- bottom silhouette: lower-left wrist, heel of the palm dropping to (20,40),
  then the lower-left fingers wrapped over the other palm as two r5
  knuckle bumps on x+y=60 (three r3 bumps were tried: too small at 48 px), which runs on as the upper-right wrist.
Lucide `handshake` informed the construction (one thumb hook over the grip,
fingertips wrapping the other hand, bare diagonal wrists); its 1-unit
fingertip loops do not survive stroke 4, so the fingers are knuckle bumps.

Metric issues:
- clearance e0/e1 (7.87), e0/e4 (4.2), e1/e5 (3.92), e2/e4 (4.38): the traced
  fingertip loop and the three short finger-crease strokes crowded the thumb
  underside and the wrist. The creases are dropped (between the thumb
  underside and the knuckle row there are 10 units, too few for a free
  stroke with 8 on each side); the fingers read from the knuckle bumps.
  Every remaining part is either joined (declared connect) or >= 8 apart.
- stroke-width (trace 2.77 after fitting): redrawn at stroke 4 with the
  8-unit centerline gaps budgeted before drawing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "135d01ca-c11c-4e70-a645-04b5dbcd9502"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1206-diagonal-handshake/diagonal-handshake_raw.svg"
AUTHOR = "claude-opus-5-5"

LO, HI = 6, 42          # SQUARE centerline box
BAND = 12               # wrist width in x+y (8.49 on centerlines)
AXIS = 48               # x+y of the arm axis
BACK_Y = 14             # upper-right hand's back
THUMB_R = 4             # thumb hook radius
UNDER_Y = BACK_Y + 10   # thumb underside
KNUCKLES = 2            # finger bumps on the bottom row
KNUCKLE_R = 5           # integer radius over an 8.49 chord: each bump bulges 2.35


class DiagonalHandshakeRedraw(Solo48):
    icon_id = "diagonal-handshake-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "work"
    aliases = ("handshake", "clasped hands", "shaking hands")
    keywords = ("hands", "handshake", "greeting", "agreement", "deal", "teamwork", "partnership", "grip")

    def build(self) -> None:
        top_c, bot_c = AXIS - BAND, AXIS + BAND          # 36 and 60
        # Top silhouette: lower-left wrist, thumb top, back of hand, upper-right wrist.
        hook_x = top_c - (UNDER_Y - THUMB_R)             # hook meets the top line at (16,20)
        hook = (hook_x, top_c - hook_x)
        back_l = (top_c - BACK_Y, BACK_Y)                # (22,14)
        back_r = (AXIS - BACK_Y, BACK_Y)                 # (34,14)
        self.add_line("wrist-ll-top", (LO, top_c - LO), hook)
        self.add_line("thumb-top", hook, back_l)
        self.add_line("back", back_l, back_r)
        self.add_line("wrist-ur-top", back_r, (HI, AXIS - HI))
        self.add_contour("top", "wrist-ll-top", "thumb-top", "back", "wrist-ur-top")

        # Thumb: hook down into the underside, then the palm edge onto the bottom row.
        under_l = (hook[0] + THUMB_R, UNDER_Y)           # (20,24)
        under_r = (bot_c - UNDER_Y - 8, UNDER_Y)         # (28,24)
        palm = (under_r[0] + 4, UNDER_Y + 4)             # (32,28) on x+y=60
        self.add_arc("thumb-tip", hook, under_l, radius_x=THUMB_R, sweep=False)
        self.add_line("thumb-under", under_l, under_r)
        self.add_line("palm-edge", under_r, palm)
        self.add_contour("thumb", "thumb-tip", "thumb-under", "palm-edge")

        # Bottom silhouette: lower-left wrist, heel, knuckle row, upper-right wrist.
        heel = (AXIS - 34, 34)                           # (14,34)
        row_start = (bot_c - 40, 40)                     # (20,40)
        self.add_line("wrist-ll-bottom", (LO, AXIS - LO), heel)
        self.add_line("heel", heel, row_start)
        members = ["wrist-ll-bottom", "heel"]
        step = (palm[0] - row_start[0]) // KNUCKLES
        for i in range(KNUCKLES):
            a = (row_start[0] + i * step, row_start[1] - i * step)
            b = (a[0] + step, a[1] - step)
            self.add_arc(f"knuckle-{i + 1}", a, b, radius_x=KNUCKLE_R, sweep=False)
            members.append(f"knuckle-{i + 1}")
        self.add_line("wrist-ur-bottom", palm, (HI, bot_c - HI))
        members.append("wrist-ur-bottom")
        self.add_contour("bottom", *members)

        self.relate("connect", "top", "thumb")
        self.relate("connect", "thumb", "bottom")
