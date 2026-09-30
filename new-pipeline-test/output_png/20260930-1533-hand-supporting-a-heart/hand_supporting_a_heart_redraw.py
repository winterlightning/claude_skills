"""hand-supporting-a-heart (redraw of the new-pipeline traced SVG).

Plan: a palm-up hand enters from the left with a sleeve cuff, its thumb tip
curled over the palm, and the fingers rise to the right; a hollow heart hovers
above the fingers with a clear gap, as in the generated image. Authored on
SQUARE (the suggested keyshape), centerline box (6,6)-(42,42).
- heart (Lucide `heart` construction, mirrored on x=27): r4 lobes centred
  (22,10)/(32,10) reaching y 6 and x 18/36, a 3-deep notch at (27,9), sides
  that turn into straight 45-degree runs meeting at the tip (27,21).
- hand, one closed outline: cuff x=6 from y 42 up to 27, a tangent thumb-base
  mound into the thumb top y=26, an r4 thumb tip about (17,30), the finger top
  rising from the thumb tip to an r5 fingertip about (37,31) whose 3-4-5
  endpoints keep both finger edges tangent and put the extreme exactly on
  x=42, then the finger underside sweeping down to the flat base y=42.
- thumb crease: the lower half of the thumb tip plus a short crease y=34 that
  stops 9 from the cuff, so the palm stays one open hole.
Why the heart sits over the fingers, not over the thumb as in the image: at
stroke 4 the thumb needs 8 between its top, its crease and the palm base, which
pins the thumb top at y=26; a heart tip 9 above that would leave a heart only
11 tall. Over the fingers the tip can drop to y=21 (heart 18x15).

Metric issues fixed:
- clearance e0/e2 (heart 4.27 from the thumb): the heart tip is now 9.45 from
  the thumb tip and 8.8 from the finger top (centerlines; nearest pair).
- hole at (16.4,33.6), 5.6 wide: the palm opening between the thumb crease,
  the cuff and the base is now the only small opening and is 8 on centerlines
  (the crease ends 9 from the cuff and 8 above the base); the heart hole is
  wide open.
- keyshape-short-axis (y filled 87%): every extreme sits on the SQUARE box:
  y 6 at the heart lobes, y 42 at the palm base, x 6 at the cuff, x 42 at the
  fingertip.
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8 or more.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "353c0a3e-5be1-4b87-8e05-ba32a7f03da8"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1533-hand-supporting-a-heart/hand-supporting-a-heart_raw.svg"
AUTHOR = "claude-opus-5-5"

HEART_AXIS, HEART_TIP = 27, 21          # heart mirror axis and tip y
LOBE_R, LOBE_DX, NOTCH_Y = 4, 5, 9      # lobe radius, lobe centre offset, notch depth
THUMB = (17, 30)                        # thumb-tip arc centre, r4
CREASE_END = 15                         # thumb crease stops 9 from the cuff
CUFF_TOP = 27
TIP = (37, 31)                          # fingertip arc centre, r5 (3-4-5 ends)
BASE_START = 24                         # palm base y=42 from the cuff to here


class HandSupportingAHeartRedraw(Solo48):
    icon_id = "hand-supporting-a-heart-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ("hand holding heart", "heart in hand", "offer love", "care")
    keywords = ("hand", "heart", "palm", "support", "care", "charity", "love", "donate", "kindness")

    def build(self) -> None:
        a, t = HEART_AXIS, HEART_TIP
        r, d = LOBE_R, LOBE_DX
        s = t - 6                                   # start of the straight 45-degree runs
        self.add_bezier("heart-top-r", (a, NOTCH_Y), ((a + 1.5, 7.5), (a + 3, 6), (a + d, 6)))
        self.add_arc("heart-lobe-r", (a + d, 6), (a + d + r, 6 + r), radius_x=r, sweep=True)
        self.add_bezier("heart-side-r", (a + d + r, 6 + r), ((a + 9, 12.5), (a + 7.5, s - 1.5), (a + 6, s)))
        self.add_line("heart-v-r", (a + 6, s), (a, t))
        self.add_line("heart-v-l", (a, t), (a - 6, s))
        self.add_bezier("heart-side-l", (a - 6, s), ((a - 7.5, s - 1.5), (a - 9, 12.5), (a - d - r, 6 + r)))
        self.add_arc("heart-lobe-l", (a - d - r, 6 + r), (a - d, 6), radius_x=r, sweep=True)
        self.add_bezier("heart-top-l", (a - d, 6), ((a - 3, 6), (a - 1.5, 7.5), (a, NOTCH_Y)))
        self.add_contour(
            "heart", "heart-top-r", "heart-lobe-r", "heart-side-r", "heart-v-r",
            "heart-v-l", "heart-side-l", "heart-lobe-l", "heart-top-l", closed=True,
        )

        bx, by = THUMB
        cx, cy = TIP
        apex = (bx + 4, by)
        self.add_line("cuff", (6, 42), (6, CUFF_TOP))
        self.add_bezier("wrist-top", (6, CUFF_TOP), ((8, 20), (bx - 4, by - 4), (bx, by - 4)))
        self.add_arc("thumb-top", (bx, by - 4), apex, radius_x=4, sweep=True)
        self.add_bezier("finger-top", apex, ((apex[0] + 3, by), (cx - 9, cy + 0.5), (cx - 3, cy - 4)))
        self.add_arc("fingertip", (cx - 3, cy - 4), (cx + 3, cy + 4), radius_x=5, sweep=True)
        self.add_bezier("finger-under", (cx + 3, cy + 4), ((cx - 1, cy + 7), (BASE_START + 5, 42), (BASE_START, 42)))
        self.add_line("palm-base", (BASE_START, 42), (6, 42))
        hand = ["cuff", "wrist-top", "thumb-top", "finger-top", "fingertip", "finger-under", "palm-base"]
        self.add_contour("hand", *hand, closed=True)
        for x, y in zip(hand, hand[1:] + hand[:1]):
            self.relate("connect", x, y)

        self.add_arc("thumb-tip", apex, (bx, by + 4), radius_x=4, sweep=True)
        self.add_line("thumb-crease", (bx, by + 4), (CREASE_END, by + 4))
        self.add_contour("thumb", "thumb-tip", "thumb-crease")
        self.relate("connect", "thumb-tip", "thumb-crease")
        self.relate("connect", "thumb-tip", "thumb-top")
        self.relate("connect", "thumb-tip", "finger-top")
