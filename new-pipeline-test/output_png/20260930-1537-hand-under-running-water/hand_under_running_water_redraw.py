"""hand-under-running-water (redraw of the new-pipeline traced SVG).

Plan: a bent tap at the upper left, two water strokes falling from its
spout, and a cupped palm-up hand below them (fingertips curled up at the
left, thumb hook at the right, arm leaving at the right edge), on SQUARE
(centerline box (6,6)-(42,42)).
The vertical stack is exactly 36: pipe 8 wide (y 6/14) + spout 4 (bottom
y=18) + gap 9 + water 6 (y 27..33) + gap 9 + palm (y=42). Gaps next to a
curved contour are 9, not 8: the engine returns an exact-8 curved pair as
review. The hand is open where the water lands (only the palm line lies
under the streams); the horizontal run is lip x=6 -> water 15/23 -> thumb
hook 32..42, every gap 8 or 9.
- tap: one open contour, top line y=6, r8 bend about (15,14) down to the
  outer spout wall x=23, flat spout bottom y=18, inner wall x=15 back up
  to the lower pipe line y=14; both pipe lines end on the box edge x=6.
- water: two vertical strokes x=15 and x=23 (under the spout walls),
  y 27..33.
- palm: fingertip lip (6,30)->(6,34), r8 quarter turn about (14,34) into the
  palm line y=42 running out to the wrist at x=42.
- thumb: back-of-hand line y=25 from the wrist edge x=42 to x=36, r4 hook
  about (36,29) round to the thumb tip line y=33 ending free at x=38,
  9 above the palm line.
Lucide: hand-helping / hand-coins (thumb capsule "h2 a2 2 0 1 0 0-4 h-3"
and palm line with a curled fingertip) mirrored so the arm leaves right;
at 2x scale Lucide's 2-unit capsules are exactly this grid's 8-unit gap.
Lucide has no faucet, so the tap follows the generated image.

Metric issues:
- clearance e0/e1, e0/e2 (tap vs water, ~3.0): fixed; water starts 9
  below the spout bottom.
- clearance e1/e2 (water strokes 3.4 apart): fixed; strokes are 8 apart.
- clearance e1/e3, e1/e4, e2/e3 ... (water vs hand, 3.9-5.7): fixed; the
  hand is open under the streams, water ends 9 above the palm line, and
  the fingertip and thumb hook sit 9 to either side.
- clearances inside the hand (thumb curl, knuckle and palm edges under 8):
  fixed by redrawing the hand as two open paths (palm with lip, thumb
  hook) whose runs are 8 or 9 apart.
- keyshape-short-axis (SQUARE 87% on y): fixed; the stack now spans y
  6..42 so every extreme lands on the box.
- stroke-width (trace 2.4): redrawn at stroke 4 with all gaps re-measured.
Dropped: the knuckle hump, the upper finger edge and the lower edge's wavy
detail. The finger band became a single curled lip because a second finger
edge cannot sit 8 from the first water stream inside 36 (the brief asks
for an open palm outline with no finger lines anyway). Tried and rejected:
a wrist edge closing palm and thumb (reads as a box) and an upright thumb
capsule (reads as an "n").
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "a34cf5c7-6f9d-4929-bade-fa576555a44e"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1537-hand-under-running-water/"
    "hand-under-running-water_raw.svg"
)
AUTHOR = "claude-opus-5-5"

EDGE_L, EDGE_R = 6, 42
PIPE_TOP, PIPE_LOW = 6, 14          # pipe 8 wide
BEND_R = PIPE_LOW - PIPE_TOP        # outer bend concentric with the inner corner
SPOUT_IN, SPOUT_OUT = 15, 23        # spout walls = water columns
SPOUT_BOTTOM = 18
WATER_TOP, WATER_BOTTOM = 27, 33    # SPOUT_BOTTOM + 9, PALM - 9
PALM = 42
LIP_TOP = 30
CURL_C = (14, 34)                   # fingertip curl centre, r = PALM - 34
THUMB_C, THUMB_R = (36, 29), 4      # thumb hook, back y=25, tip y=33 (9 above PALM)
THUMB_TIP_X = 38


class HandUnderRunningWaterRedraw(Solo48):
    icon_id = "hand-under-running-water-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "hygiene/handwashing"
    aliases = ("wash hands", "hand washing", "tap water")
    keywords = ("hand", "wash", "water", "faucet", "tap", "hygiene", "clean", "sink")

    def build(self) -> None:
        self.add_line("tap-top", (EDGE_L, PIPE_TOP), (SPOUT_IN, PIPE_TOP))
        self.add_arc("tap-bend", (SPOUT_IN, PIPE_TOP), (SPOUT_OUT, PIPE_LOW),
                     radius_x=BEND_R, sweep=True)
        self.add_line("tap-wall-out", (SPOUT_OUT, PIPE_LOW), (SPOUT_OUT, SPOUT_BOTTOM))
        self.add_line("tap-mouth", (SPOUT_OUT, SPOUT_BOTTOM), (SPOUT_IN, SPOUT_BOTTOM))
        self.add_line("tap-wall-in", (SPOUT_IN, SPOUT_BOTTOM), (SPOUT_IN, PIPE_LOW))
        self.add_line("tap-low", (SPOUT_IN, PIPE_LOW), (EDGE_L, PIPE_LOW))
        self.add_contour("tap", "tap-top", "tap-bend", "tap-wall-out", "tap-mouth",
                         "tap-wall-in", "tap-low", closed=False)

        for index, x in enumerate((SPOUT_IN, SPOUT_OUT), start=1):
            self.add_line(f"water-{index}", (x, WATER_TOP), (x, WATER_BOTTOM))

        cx, cy = CURL_C
        r = PALM - cy
        self.add_line("palm-lip", (EDGE_L, LIP_TOP), (cx - r, cy))
        self.add_arc("palm-curl", (cx - r, cy), (cx, PALM), radius_x=r, sweep=False)
        self.add_line("palm-line", (cx, PALM), (EDGE_R, PALM))
        self.add_contour("palm", "palm-lip", "palm-curl", "palm-line", closed=False)

        tx, ty = THUMB_C
        tr = THUMB_R
        self.add_line("thumb-back", (EDGE_R, ty - tr), (tx, ty - tr))
        self.add_arc("thumb-hook-1", (tx, ty - tr), (tx - tr, ty), radius_x=tr, sweep=False)
        self.add_arc("thumb-hook-2", (tx - tr, ty), (tx, ty + tr), radius_x=tr, sweep=False)
        self.add_line("thumb-tip", (tx, ty + tr), (THUMB_TIP_X, ty + tr))
        self.add_contour("thumb", "thumb-back", "thumb-hook-1", "thumb-hook-2",
                         "thumb-tip", closed=False)
