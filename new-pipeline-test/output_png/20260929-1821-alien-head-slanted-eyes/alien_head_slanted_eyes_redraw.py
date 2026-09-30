"""Alien head with slanted eyes (redraw of the new-pipeline traced SVG).

Subject: front view of a grey-alien head -- broad rounded cranium tapering on
straight-ish cheeks to a small rounded chin, two almond eyes slanting down
toward the centre (outer tip high, inner tip low).

Plan: CIRCLE (centerline radius 20 about (24,24)); everything mirrored on the
axis x=AXIS.
- head: one closed contour.
  crown  = upper half-ellipse rx 18 / ry CROWN_RY about (AXIS, CROWN_Y); apex
           (24,4) touches the circle and the ellipse stays inside radius 20
           (r^2 = 333 + 102 s - 35 s^2 <= 400, max at the apex).
  cheeks = one cubic each, leaving the crown's widest point vertically
           (CHEEK_DROP) and entering the chin along (3,-4), so both joins are
           tangent-continuous.
  chin   = arc radius CHIN_R about (AXIS, 44 - CHIN_R); apex (24,44) touches
           the circle; entered at the (4,3) radius point, tangent (3,-4).
- eyes: each a closed almond of two arcs between an outer-top tip EYE_OUTER
  and an inner-low tip EYE_INNER. The inner-upper lid (EYE_TOP_R) bulges more
  than the outer-lower lid (EYE_BOTTOM_R), echoing the trace's lopsided
  almond; the lens is ~3.5 across on centerlines so the stroke paints it
  solid with no pinhole. Inner tips sit 10 apart.
No useful Lucide match (no alien head in the local Lucide set); construction
follows the generated PNG's cranium / tapered chin silhouette.

Metric issues:
- stroke-width (trace 2.55 after fitting): fixed, redrawn at stroke 4 on the
  integer grid.
- keyshape-short-axis (VRECT_M, y fill 96%): fixed by using CIRCLE instead.
  VRECT_M caps the head at 28 wide on centerlines; with 8 to each wall and 8
  between the eyes that leaves 2 per eye. CIRCLE allows a 36 x 40 head whose
  top (24,4) and chin (24,44) sit exactly on radius 20. Cost: the head is a
  little rounder than the trace (0.9 vs 0.73 aspect).
- clearance e0-e1 / e0-e2 (2.48 / 2.46 < 8): fixed, eyes >= 8 from the head.
- clearance e1-e2 (4.65 < 8): fixed, eyes >= 8 apart (inner tips 10 apart).
- holes in both eyes (1.17 / 1.13 < 6 inscribed): fixed by drawing the eyes
  solid, so no hole remains. Not repairable as hollow eyes: an open almond
  needs >= 10 across on centerlines (6 hole + stroke), and inside a 36-wide
  head only 6 units per eye remain after the 8-unit wall and 8-unit centre
  clearances. The trace's large hollow eyes are therefore not kept, and the
  eyes are steeper than the trace's ~45 deg slant for the same width reason.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "3111e4ee-f8d7-5adc-8f71-0cc4e4063457"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1821-alien-head-slanted-eyes/alien-head-slanted-eyes_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
CROWN_RX = 18
CROWN_RY = 17
CROWN_Y = 4 + CROWN_RY     # widest line of the cranium
CHIN_R = 5
CHIN_BOTTOM = 44
CHEEK_DROP = 10            # vertical control run leaving the crown
CHEEK_TAPER = 3            # control run along (3,-4) leaving the chin
EYE_OUTER = (15, 18)       # left eye outer-top tip
EYE_INNER = (19, 27)       # left eye inner-low tip
EYE_TOP_R = 6
EYE_BOTTOM_R = 14


class AlienHeadSlantedEyesRedraw(Solo48):
    icon_id = "alien-head-slanted-eyes-redraw"
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ("alien face", "extraterrestrial head", "grey alien")
    keywords = ("alien", "head", "face", "eyes", "extraterrestrial", "ufo", "space", "fiction")

    def build(self) -> None:
        left, right = AXIS - CROWN_RX, AXIS + CROWN_RX
        chin_c = CHIN_BOTTOM - CHIN_R
        chin_r = (AXIS + 4, chin_c + 3)
        chin_l = (AXIS - 4, chin_c + 3)
        t = CHEEK_TAPER

        self.add_arc("crown", (left, CROWN_Y), (right, CROWN_Y), radius_x=CROWN_RX, radius_y=CROWN_RY)
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
            self.add_arc(f"{name}-top", outer, inner, radius_x=EYE_TOP_R, sweep=sweep)
            self.add_arc(f"{name}-bottom", inner, outer, radius_x=EYE_BOTTOM_R, sweep=sweep)
            self.add_contour(name, f"{name}-top", f"{name}-bottom", closed=True)
