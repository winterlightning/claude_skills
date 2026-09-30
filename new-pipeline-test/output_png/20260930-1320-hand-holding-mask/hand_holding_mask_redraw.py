"""hand-holding-mask (redraw of the new-pipeline traced SVG).

Subject: an open, upward-facing hand entering from the lower left, its
palm holding a medical face mask (body plus two ear loops) above it.

Plan: SQUARE (centerline box (6,6)-(42,42)), as suggested by the metrics
(score 1.11). Mirror axis x=24 for the mask; the hand is directional.
Vertical budget at the centre: mask top 6 / mask bottom 17 / thumb top 26
/ thumb bottom 34 / palm underside 42 -- 9, 8 and 8 between centerlines
(9 where the curved mask bottom faces the thumb).
- mask body: one closed lens contour -- symmetric cubic top bulging to
  its apex (24,6), short straight sides (pleat edges) x=16 / x=32 from
  y=9 to y=15, symmetric cubic bottom sagging to (24,17). (A flatter
  r=17-arc body with 8-tall sides was rendered and rejected: at 48 px it
  read as a chain link.)
- ear loops: mirrored two-cubic loops from the body corners out to a
  knot on x=6 / x=42 (y=12), kept >= 5 from the loop centre (11,12) /
  (37,12) so each loop holds a 6-wide opening.
- hand, after Lucide `hand-helping` (thumb pill + finger + underside), on
  this grid: upper contour = wrist top on 45 degrees from (6,34), knuckle
  cubic into the thumb top y=26, r=4 thumb end about (25,30), thumb
  underside back to a free end (20,34). Lower contour = palm underside on
  y=42 from a free end (14,42), a cubic rising into the finger's lower
  edge on 4:-3, an r=5 fingertip about (37,31) on 3-4-5 knots, and the
  finger's upper edge down to the thumb end's knot (29,30) (connect).
Extremes: x=6 wrist + left ear, x=42 right ear + fingertip, y=6 mask
apex, y=42 palm underside.

Metric issues:
- clearance e0/e4, e1/e4 (mask vs hand, 4.12 / 3.14): mask bottom at 17,
  thumb top at 26 -- 9 on centerlines.
- clearance e1/e5, e3/e5 (mask right side / ear vs finger, 4.78 / 5.96):
  right ear bottom ~17.3, fingertip top 26 -- >= 8.5.
- clearance e4/e5 (the two wrist ends, 7.49): wrist ends (6,34) and
  (14,42) are 11.3 apart; the thumb underside sits exactly 8 above the
  straight palm underside.
- holes at the ear loops (3.03 / 2.8 inscribed): ear loops redrawn 10 wide
  around a radius-5 clear zone, 6 inscribed.
- keyshape-short-axis (y filled 86%): the mask apex now sits on y=6 and
  the palm underside on y=42, so both SQUARE axes are exact.
- stroke-width (trace 2.39): redrawn at stroke 4 with every gap re-spaced
  for the heavier weight.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "5521723a-f61f-58b0-9d3b-7bb857fa845d"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1320-hand-holding-mask/hand-holding-mask_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24                  # mask mirror axis
SIDE = 8                   # mask body half-width: sides on x=16 / x=32
TOP, BOTTOM = 9, 15        # mask side ends
EAR_OUT = 6                # outer ear reach (x=6 / x=42)
THUMB_TOP, THUMB_BOTTOM, PALM = 26, 34, 42
THUMB_C = (25, 30)         # thumb end centre, r=4
TIP_C = (37, 31)           # fingertip centre, r=5 (3-4-5 knots)


def mx(p):
    return (2 * AXIS - p[0], p[1])


class HandHoldingMaskRedraw(Solo48):
    icon_id = "hand-holding-mask-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "medical"
    aliases = ("mask donation", "offer face mask", "hand with mask")
    keywords = ("hand", "mask", "face mask", "medical", "holding", "protection", "health", "donation", "covid")

    def build(self) -> None:
        left, right = AXIS - SIDE, AXIS + SIDE
        # mask body: a lens -- cubic top and bottom, short straight sides
        self.add_bezier("mask-top", (left, TOP), ((left + 5, 5), (right - 5, 5), (right, TOP)))
        self.add_line("mask-right", (right, TOP), (right, BOTTOM))
        self.add_bezier(
            "mask-bottom", (right, BOTTOM),
            ((right - 5, 53 / 3), (left + 5, 53 / 3), (left, BOTTOM)),
        )
        self.add_line("mask-left", (left, BOTTOM), (left, TOP))
        self.add_contour("mask", "mask-top", "mask-right", "mask-bottom", "mask-left", closed=True)

        # ear loops: top half then mirrored bottom half, left ear mirrored right
        ear_l = (
            ((13, 5), (EAR_OUT, 6), (EAR_OUT, 12)),
            ((EAR_OUT, 18), (13, 19), (left, BOTTOM)),
        )
        self.add_bezier("ear-left", (left, TOP), *ear_l)
        self.add_bezier(
            "ear-right", (right, TOP),
            *(tuple(mx(p) for p in seg) for seg in ear_l),
        )
        self.relate("connect", "ear-left", "mask")
        self.relate("connect", "ear-right", "mask")

        # hand, upper contour: wrist top, knuckle, thumb pill
        tx, ty = THUMB_C
        self.add_line("wrist-top", (6, 34), (11, 29))
        self.add_bezier("knuckle", (11, 29), ((13, 27), (14.5, THUMB_TOP), (17, THUMB_TOP)))
        self.add_line("thumb-top", (17, THUMB_TOP), (tx, THUMB_TOP))
        self.add_arc("thumb-end-a", (tx, THUMB_TOP), (tx + 4, ty), radius_x=4, sweep=True)
        self.add_arc("thumb-end-b", (tx + 4, ty), (tx, THUMB_BOTTOM), radius_x=4, sweep=True)
        self.add_line("thumb-under", (tx, THUMB_BOTTOM), (20, THUMB_BOTTOM))
        self.add_contour(
            "hand-upper", "wrist-top", "knuckle", "thumb-top",
            "thumb-end-a", "thumb-end-b", "thumb-under",
        )

        # hand, lower contour: palm underside, finger, fingertip
        cx, cy = TIP_C
        lo, hi = (cx + 3, cy + 4), (cx - 3, cy - 4)
        self.add_line("palm-under", (14, PALM), (26, PALM))
        self.add_bezier("palm-rise", (26, PALM), ((30, PALM), (lo[0] - 4, lo[1] + 3), lo))
        self.add_arc("fingertip", lo, hi, radius_x=5, sweep=False)
        self.add_line("finger-top", hi, (tx + 4, ty))
        self.add_contour("hand-lower", "palm-under", "palm-rise", "fingertip", "finger-top")
        self.relate("connect", "hand-lower", "hand-upper")
