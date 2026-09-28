"""alien head with slanted eyes (redraw of the new-pipeline traced SVG).

Plan: CIRCLE (centerline radius 20 about (24,24)), one head contour mirrored
on the axis x=AXIS plus two mirrored slanted almond eyes.
- head: closed contour. Crown = half circle radius CROWN_R about
  (AXIS, CROWN_Y); its apex (24,4) touches the circle. Each cheek is one cubic
  leaving the crown vertically and tapering straight into the chin; chin = arc
  radius CHIN_R about (AXIS, 44 - CHIN_R), apex (24,44) touches the circle,
  entered on the (4,3) radius so cheek and chin share the tangent (3,-4).
- eyes: each a lens of two equal arcs from an outer-top tip O to an inner-low
  tip I, so the eye slants up toward the outer side. The lens is 3.1 across on
  centerlines, so the stroke paints it as a solid almond (the classic grey
  alien eye). Inner tips sit 10 apart; every eye point is 8+ from the head.
No useful Lucide match (no alien head in the local Lucide set); construction
follows the generated image's broad cranium and tapered chin.
Metric issues:
- stroke-width (trace 2.4): redrawn at stroke 4 on the integer grid.
- keyshape-short-axis (VRECT_L y fill 93%): keyshape changed to CIRCLE. The
  head is 36 wide x 40 tall on centerlines (aspect 0.9, the trace is 0.86),
  which fits inside radius 20 and touches it at top and chin; VRECT_L would
  cap the width at 32 and leave no room for two eyes plus 8-unit clearances.
- clearance e0-e1 / e0-e2 (2.7 / 2.8 < 8): fixed; eyes are 8+ from the head.
- clearance e1-e2 (5.9 < 8): fixed; inner eye tips are 10 apart.
- holes in the eyes (1.84 < 6 inscribed): fixed by filling. A hollow almond
  needs 10+ across on centerlines; two of them cannot fit in the band left
  inside the 8-unit head clearance, so each eye is drawn solid and no hole
  remains. The trace's hollow eye outlines are therefore not kept.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3111e4ee-f8d7-5adc-8f71-0cc4e4063457"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1659-alien-head-slanted-eyes/alien-head-slanted-eyes_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
CROWN_R = 18
CROWN_Y = 4 + CROWN_R
CHIN_R = 5
CHIN_BOTTOM = 44
CHEEK_DROP = 12          # vertical control run leaving the crown
CHEEK_TAPER = 4         # control run along (3,-4) leaving the chin
EYE_OUTER = (15, 21)    # left eye outer-top tip
EYE_INNER = (19, 28)    # left eye inner-low tip
EYE_R = 6


class AlienHeadSlantedEyesRedraw(Solo48):
    icon_id = "alien-head-slanted-eyes-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ("alien face", "extraterrestrial head", "grey alien")
    keywords = ("alien", "head", "face", "eyes", "extraterrestrial", "ufo", "space", "fiction")

    def build(self) -> None:
        left, right = AXIS - CROWN_R, AXIS + CROWN_R
        chin_c = CHIN_BOTTOM - CHIN_R
        chin_r = (AXIS + 4, chin_c + 3)
        chin_l = (AXIS - 4, chin_c + 3)
        t = CHEEK_TAPER

        self.add_arc("crown", (left, CROWN_Y), (right, CROWN_Y), radius_x=CROWN_R)
        self.add_bezier("cheek-right", (right, CROWN_Y),
                        ((right, CROWN_Y + CHEEK_DROP), (chin_r[0] + 3 * t, chin_r[1] - 4 * t), chin_r))
        self.add_arc("chin", chin_r, chin_l, radius_x=CHIN_R)
        self.add_bezier("cheek-left", chin_l,
                        ((chin_l[0] - 3 * t, chin_l[1] - 4 * t), (left, CROWN_Y + CHEEK_DROP), (left, CROWN_Y)))
        self.add_contour("head", "crown", "cheek-right", "chin", "cheek-left", closed=True)

        for side, name in ((-1, "eye-left"), (1, "eye-right")):
            outer = (AXIS + side * (AXIS - EYE_OUTER[0]), EYE_OUTER[1])
            inner = (AXIS + side * (AXIS - EYE_INNER[0]), EYE_INNER[1])
            sweep = side < 0
            self.add_arc(f"{name}-top", outer, inner, radius_x=EYE_R, sweep=sweep)
            self.add_arc(f"{name}-bottom", inner, outer, radius_x=EYE_R, sweep=sweep)
            self.add_contour(name, f"{name}-top", f"{name}-bottom", closed=True)
