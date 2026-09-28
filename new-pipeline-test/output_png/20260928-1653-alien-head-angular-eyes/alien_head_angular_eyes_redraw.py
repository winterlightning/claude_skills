"""alien head with angular eyes (redraw of the new-pipeline traced SVG).

Plan: VRECT_L (centerline box (8,4)-(40,44)), one mirrored head contour on
the axis x=AXIS plus two mirrored angular eyes.
- head: closed contour. Crown = half circle radius CROWN_R about
  (AXIS, CROWN_Y), so its apex is the y=4 extreme and its ends (8, CROWN_Y) /
  (40, CROWN_Y) are the x extremes; each cheek is one cubic leaving the crown
  tangent (vertical) and tapering into the chin; chin = arc radius CHIN_R
  about (AXIS, 44 - CHIN_R) whose apex is the y=44 extreme, entered along the
  (3,4) radius so cheek and chin share the tangent (-3,4).
- eyes: each a small closed slanted triangle, outer tip high, inner edge
  vertical, so the stroke fills it into a solid angular almond. Inner edges
  sit on x = AXIS -/+ EYE_GAP / 2 (8 apart), outer tips 8+ from the crown.
No useful Lucide match (no alien head in the local Lucide set); construction
follows the generated image's egg-and-taper silhouette.
Metric issues:
- stroke-width (trace 2.4): redrawn at stroke 4 on the integer grid.
- keyshape: moved from the suggested VRECT_M to VRECT_L (score 1.15 vs
  1.22). On VRECT_M the head is 28 wide on centerlines, which leaves a band
  of 12 inside the 8-unit wall clearance: two eyes 8 apart cannot fit. The
  L box gives 32 / 16. All four VRECT_L extremes are exact (y fill fixed).
- clearance e0-e1 / e0-e2 (2.6 / 2.5 < 8): fixed; eyes are 8+ from the head.
- clearance e1-e2 (4.1 < 8): fixed; inner eye edges are 8 apart.
- holes at the eyes (1.1 / 1.3 < 6 inscribed): fixed by design. A hollow eye
  needs 10+ across on centerlines and two of them cannot fit in the 16 band,
  so each eye is a triangle small enough for the stroke to fill solid: no
  hole remains. The trace's hollow eye outlines are therefore not kept.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "194e70a7-f921-4957-b6e3-e9ba0cf49902"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1653-alien-head-angular-eyes/alien-head-angular-eyes_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
CROWN_R = 16
CROWN_Y = 4 + CROWN_R
CHIN_R = 5
CHIN_BOTTOM = 44
EYE_GAP = 8
EYE_TOP = 21
EYE_OUTER = 3
EYE_MID = 23
EYE_BOTTOM = 29


class AlienHeadAngularEyesRedraw(Solo48):
    icon_id = "alien-head-angular-eyes-redraw"
    keyshape = Keyshape.VRECT_L
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

        self.add_arc("crown", (left, CROWN_Y), (right, CROWN_Y), radius_x=CROWN_R)
        self.add_bezier("cheek-right", (right, CROWN_Y),
                        ((right, CROWN_Y + 10), (chin_r[0] + 6, chin_r[1] - 8), chin_r))
        self.add_arc("chin", chin_r, chin_l, radius_x=CHIN_R)
        self.add_bezier("cheek-left", chin_l,
                        ((chin_l[0] - 6, chin_l[1] - 8), (left, CROWN_Y + 10), (left, CROWN_Y)))
        self.add_contour("head", "crown", "cheek-right", "chin", "cheek-left", closed=True)

        for side, name in ((-1, "eye-left"), (1, "eye-right")):
            inner = AXIS + side * EYE_GAP // 2
            self.add_polyline(name, (inner + side * EYE_OUTER, EYE_TOP), (inner, EYE_MID),
                              (inner, EYE_BOTTOM), closed=True)
