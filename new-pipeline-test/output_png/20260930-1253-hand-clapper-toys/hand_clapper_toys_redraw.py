"""hand-clapper-toys (redraw of the new-pipeline traced SVG).

Plan: a toy hand paddle on a short hollow stick, VRECT_L (centerline box
(8,4)-(40,44)).
- paddle: one closed contour. Three fingers on Lucide's `hand` construction,
  radius-4 tip arcs on a pitch of 8 (walls x = 16/24/32/40), with the middle
  finger highest (tip y=4) and the ring finger lowest. Two open notch lines
  (x=24, x=32) come down from the shared walls and stop free inside the
  palm, so the fingers stay open-bottomed and no slivers close off.
- thumb: a radius-5 tip on a (-4,-3) axis centred (13,20), so both tangent
  points are integers ((16,16) crotch, (10,24)); the straight lower wall
  runs to (14,27), then a smooth Bezier sweeps into the cuff.
- palm heel: radius-7 quarter arc from the right wall to the cuff, tangent
  at both ends.
- handle: walls x=23/33 below the cuff line y=30, closed by a radius-5 end
  arc (bottom y=44); centred under the middle finger (x=28).
Extremes: x 8 (thumb tip) / 40 (ring wall), y 4 (middle tip) / 44 (handle).

Keyshape: VRECT_L instead of the suggested VRECT_M. The metrics score them
1.16 against 1.21, and VRECT_L fills the height exactly (the M fit needed a
1.04 y stretch). At stroke 4 each finger costs 8, so three fingers use 24.
VRECT_M's 28 width would leave the thumb only 4 units, which is not enough
to show it.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap budgeted for it.
- keyshape-short-axis: all four extremes sit on the VRECT_L box.
- clearance e0/e3, e1/e3, e2/e3 (2.1-4.8 apart): e3 was the traced rear
  paddle layer squeezed against the front hand. It is dropped (see below),
  and every remaining parallel pair (notches, finger walls) is exactly 8.
- loose-join e1/e2 and narrow-join e2/e1 (9 deg), e3/e1 (24 deg): the paddle
  is now a single closed contour with shared endpoints; the notches and
  handle share exact endpoints with it and are declared with connect.
- holes at (23,7.2), (28.5,8.1) 1.0/0.8 wide: these were the traced finger
  slivers. The fingers are now open-bottomed tubes, so they enclose no holes.
- hole at (23.5,33.3) 0.2 wide (collar sliver): the collar is now a single
  cuff line. The only enclosed spaces are the palm and the handle interior
  (10 on centerlines = 6 inscribed).
- no-head (warn): false positive; this is a toy, not a person, and no human
  figure is marked.
Not kept: the offset rear paddle edge and the fourth finger. Either would
need 8 more units of width beside the thumb and three fingers, and VRECT_L
has none left. At 48 px, the hand on a stick carries the clapper reading.
Lucide: `hand` informed the shared-wall finger tubes and the angled thumb.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "d14f767a-d27e-45c9-837c-e0c5f4d0ad51"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1253-hand-clapper-toys/hand-clapper-toys_raw.svg"
AUTHOR = "claude-opus-5-5"

R = 4                       # finger radius: pitch 8 = SOLO48 centerline minimum
WALLS = (16, 24, 32, 40)    # finger walls; fingers centred at 20, 28, 36
TIPS = (10, 8, 12)          # finger arc centre y (middle finger highest, top y=4)
NOTCH_END = (20, 22)        # free ends of the two finger notches
CUFF_Y = 30                 # palm / handle seam
HX0, HX1 = 23, 33           # handle walls (10 apart -> 6 inscribed hole)
PR = WALLS[-1] - HX1        # palm heel radius 7: quarter arc tangent to wall and cuff
HR = (HX1 - HX0) // 2       # handle end radius 5
HB = 44 - HR                # handle end arc centre y (bottom ink at 46)
TC, TR = (13, 20), 5        # thumb tip centre / radius; axis (-4,-3)
TU = (TC[0] + 3, TC[1] - 4) # (16,16) crotch, upper tangent point
TL = (TC[0] - 3, TC[1] + 4) # (10,24) lower tangent point
TB = (TL[0] + 4, TL[1] + 3) # (14,27) end of the straight lower thumb wall


class HandClapperToysRedraw(Solo48):
    icon_id = "hand-clapper-toys-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "rewards"
    aliases = ("hand-clapper", "clapper-toy", "hand-on-stick")
    keywords = ("clapper", "toy", "hand", "applause", "clap", "cheer", "reward", "celebration")

    def build(self) -> None:
        w0, w1, w2, w3 = WALLS
        t1, t2, t3 = TIPS
        self.add_line("index-wall", TU, (w0, t1))
        self.add_arc("index", (w0, t1), (w1, t1), radius_x=R, sweep=True)
        self.add_line("notch-a-top", (w1, t1), (w1, t2))
        self.add_arc("middle", (w1, t2), (w2, t2), radius_x=R, sweep=True)
        self.add_line("notch-b-top", (w2, t2), (w2, t3))
        self.add_arc("ring", (w2, t3), (w3, t3), radius_x=R, sweep=True)
        self.add_line("palm-right", (w3, t3), (w3, CUFF_Y - PR))
        self.add_arc("palm-bottom-right", (w3, CUFF_Y - PR), (HX1, CUFF_Y), radius_x=PR, sweep=True)
        self.add_line("cuff", (HX1, CUFF_Y), (HX0, CUFF_Y))
        self.add_bezier("palm-bottom-left", (HX0, CUFF_Y), ((19.5, CUFF_Y), (17.2, 29.4), TB))
        self.add_line("thumb-lower", TB, TL)
        self.add_arc("thumb-tip", TL, TU, radius_x=TR, sweep=True)
        self.add_contour("paddle", "index-wall", "index", "notch-a-top", "middle", "notch-b-top",
                         "ring", "palm-right", "palm-bottom-right", "cuff", "palm-bottom-left",
                         "thumb-lower", "thumb-tip", closed=True)
        self.add_line("notch-a", (w1, t1), (w1, NOTCH_END[0]))
        self.add_line("notch-b", (w2, t3), (w2, NOTCH_END[1]))
        self.relate("connect", "notch-a", "paddle")
        self.relate("connect", "notch-b", "paddle")
        self.add_line("handle-right", (HX1, CUFF_Y), (HX1, HB))
        self.add_arc("handle-end", (HX1, HB), (HX0, HB), radius_x=HR, sweep=True)
        self.add_line("handle-left", (HX0, HB), (HX0, CUFF_Y))
        self.add_contour("handle", "handle-right", "handle-end", "handle-left")
        self.relate("connect", "handle", "paddle")
