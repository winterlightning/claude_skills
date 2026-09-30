"""boar head (redraw of the new-pipeline traced SVG).

Plan: SQUARE (centerline box (6,6)-(42,42), ink (4,4)-(44,44)), mirrored
about x=24. One closed silhouette contour carries the head and the snout;
the tusks hang off the snout's sides.
- ears: pointed tips at (6,6) / (42,6). Inner edge runs down to the brow
  notch (16,12); outer edge drops to the cheek notch (8,17).
- brow: an r17 arc about (24,27) from (16,12) to (32,12), apex (24,10).
- cheeks: one cubic per side bulging out to x~7 below the cheek notch (8,17)
  and sweeping in to the snout's top corner (20,30).
- snout: a stadium, r6 ends about (20,36) and (28,36), so x 14..34 and
  y 30..42; its top line (20,30)-(28,30) separates it from the face and its
  lower half is the chin. Each end arc is split at its outer extreme
  (14,36) / (34,36) where a tusk attaches.
- tusks: one cubic per side leaving the snout horizontally and curling up to
  a tip at (6,32) / (42,32); the ear and tusk tips set the side extremes.
Keyshape: SQUARE, as suggested (fit 1.0 x 1.0, matches the square hint).
Traced shape: boar-head_raw.svg and boar-head.png (read for the subject only;
nothing copied from its coordinates).
Lucide: no boar/pig icon; the construction (one silhouette contour with
integrated pointed ears, a stadium snout) follows Lucide's animal-head style
(cat, rabbit, piggy-bank snout), redrawn on this grid.

Metric issues:
- clearance e0/e1, e0/e2, e1/e3, e2/e3 (tusks 2-3 from the head outline and
  the snout): fixed. The tusks now attach to the snout (declared connect) and
  sit outside the face under the rounded cheeks, clear of them by 8+.
- clearance e0/e3 (snout 2.8 above the chin): fixed, the snout's lower half
  is the chin, so there is no chin line to crowd.
- clearance e0/e4, e0/e5, e1/e4, e2/e5, e3/e4, e3/e5, e4/e5 (nostrils 3-7
  from the snout, tusks, chin and each other): fixed by removing the
  nostrils. Two nostrils need 8 between them and 8 to each snout wall, i.e.
  a snout 18 tall and 26 wide (r9 ends); with tusks and cheeks around it
  that does not fit a 36-unit box, and the tusks are what make it a boar.
- hole x3 (1.0-1.5 slivers between snout, chin and tusks): fixed; the only
  enclosed openings are the face (large) and the snout (8 tall).
- stroke-width (info): drawn at stroke 4; every gap budgeted for 4.
Not kept: the nostril strokes (see above) and the detached tusk placement
beside the snout (detached tusks need 8 to both snout and cheek, 16 per side
that the box does not have).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "dc49666c-c237-4598-af85-2ca17697cbe2"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1807-boar-head/boar-head_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                 # mirror axis
EAR_TIP = (6, 6)
BROW_NOTCH = (16, 12)
CHEEK_NOTCH = (8, 17)
BROW_R = 17             # centre (24,27): apex (24,10)
SNOUT_Y = 36            # snout end-arc centre y
SNOUT_CX = 20           # left end-arc centre x
SNOUT_R = 6
SNOUT_TOP = (SNOUT_CX, SNOUT_Y - SNOUT_R)       # (20,30)
SNOUT_BOTTOM = (SNOUT_CX, SNOUT_Y + SNOUT_R)    # (20,42)
SNOUT_SIDE = (SNOUT_CX - SNOUT_R, SNOUT_Y)      # (14,36)
TUSK_TIP = (6, 32)


def m(p):
    return (2 * AX - p[0], p[1])


class BoarHeadRedraw(Solo48):
    icon_id = "boar-head-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/mammals"
    aliases = ("boar", "wild-boar", "warthog", "hog-head")
    keywords = ("boar", "wild boar", "hog", "pig", "tusks", "snout", "animal",
                "hunting", "face")

    def build(self) -> None:
        ear_in = ((10, 7), (13, 9), BROW_NOTCH)
        ear_out = ((6, 10), (6, 14), CHEEK_NOTCH)
        cheek = ((7, 21), (12, 29), SNOUT_TOP)
        tusk = ((10, SNOUT_Y), (6, 36), TUSK_TIP)

        self.add_bezier("ear-in-l", EAR_TIP, ear_in)
        self.add_arc("brow", BROW_NOTCH, m(BROW_NOTCH), radius_x=BROW_R, sweep=True)
        self.add_bezier("ear-in-r", m(BROW_NOTCH),
                        (m(ear_in[1]), m(ear_in[0]), m(EAR_TIP)))
        self.add_bezier("ear-out-r", m(EAR_TIP),
                        (m(ear_out[0]), m(ear_out[1]), m(CHEEK_NOTCH)))
        self.add_bezier("cheek-r", m(CHEEK_NOTCH),
                        (m(cheek[0]), m(cheek[1]), m(SNOUT_TOP)))
        self.add_arc("snout-r-top", m(SNOUT_TOP), m(SNOUT_SIDE), radius_x=SNOUT_R, sweep=True)
        self.add_arc("snout-r-low", m(SNOUT_SIDE), m(SNOUT_BOTTOM), radius_x=SNOUT_R, sweep=True)
        self.add_line("snout-bottom", m(SNOUT_BOTTOM), SNOUT_BOTTOM)
        self.add_arc("snout-l-low", SNOUT_BOTTOM, SNOUT_SIDE, radius_x=SNOUT_R, sweep=True)
        self.add_arc("snout-l-top", SNOUT_SIDE, SNOUT_TOP, radius_x=SNOUT_R, sweep=True)
        self.add_bezier("cheek-l", SNOUT_TOP, (cheek[1], cheek[0], CHEEK_NOTCH))
        self.add_bezier("ear-out-l", CHEEK_NOTCH, (ear_out[1], ear_out[0], EAR_TIP))
        self.add_contour(
            "head", "ear-in-l", "brow", "ear-in-r", "ear-out-r", "cheek-r",
            "snout-r-top", "snout-r-low", "snout-bottom", "snout-l-low",
            "snout-l-top", "cheek-l", "ear-out-l", closed=True,
        )

        self.add_line("snout-top", SNOUT_TOP, m(SNOUT_TOP))
        self.add_bezier("tusk-l", SNOUT_SIDE, tusk)
        self.add_bezier("tusk-r", m(SNOUT_SIDE),
                        (m(tusk[0]), m(tusk[1]), m(TUSK_TIP)))

        self.relate("connect", "snout-top", "cheek-l")
        self.relate("connect", "snout-top", "snout-l-top")
        self.relate("connect", "snout-top", "cheek-r")
        self.relate("connect", "snout-top", "snout-r-top")
        self.relate("connect", "tusk-l", "snout-l-low")
        self.relate("connect", "tusk-l", "snout-l-top")
        self.relate("connect", "tusk-r", "snout-r-top")
        self.relate("connect", "tusk-r", "snout-r-low")
