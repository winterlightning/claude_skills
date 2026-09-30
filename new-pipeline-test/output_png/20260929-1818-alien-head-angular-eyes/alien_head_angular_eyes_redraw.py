"""alien head with angular eyes (redraw of the new-pipeline traced SVG).

Plan: CIRCLE (centerline radius 20 about (24,24)); one head contour mirrored
on the axis x=AXIS plus two mirrored, hollow, angular almond eyes.
- head: closed contour. Crown = half circle radius CROWN_R about
  (AXIS, CROWN_Y); its apex (24,4) is the top extreme. Each cheek is one cubic
  leaving the crown vertically and easing into the chin; chin = arc radius
  CHIN_R about (AXIS, 44 - CHIN_R), apex (24,44) is the bottom extreme,
  entered along the (4,3) radius so cheek and chin share the tangent (3,4).
- eyes: each a closed pair of cubics from the outer-top corner O to the
  inner-low tip I, so the eye angles up toward the outer corner as in the
  image. The upper edge leaves O heading inward and drops onto I vertically,
  and the lower edge leaves I heading outward and rises into O. So O is an
  angular corner, and no control passes x=20: the two inner tips stay exactly
  8 apart. The interiors stay open (build-gate hole check passes).
No useful Lucide match (no alien head in the local Lucide set); construction
follows the generated image's broad cranium, tapered chin and slanted eyes.
Review feedback on this source (hina): taller head with a broad rounded
forehead tapering to the chin; large closed almond eyes angled up toward the
outer corners, symmetrical, interiors empty. The earlier redraws used solid
eyes; these are hollow.
Metric issues:
- stroke-width (trace 2.47): redrawn at stroke 4 on the integer grid.
- keyshape-short-axis (VRECT_L y fill 92%): keyshape changed to CIRCLE. Two
  hollow eyes need 8 + eye + 8 + eye + 8 across the face, and the 32-wide
  VRECT_L head leaves no room for any hole. The CIRCLE head is 38 wide x 40
  tall on centerlines (aspect 0.95; the trace is 0.87) and touches the
  circle at the crown apex and chin.
- clearance e0-e1 / e0-e2 (3.0 / 3.1 < 8): fixed; every eye point is 8+
  from the head.
- clearance e1-e2 (5.2 < 8): fixed; the inner tips are exactly 8 apart.
- holes (1.34 / 1.41): enlarged to the build gate's floor (validate_icon
  valid, build_gate PASS; svg_metrics now measures 2.24). The metrics floor
  of a 6-unit ink hole (10 on centerlines per eye) is not reachable: with 8
  to the head and 8 between the eyes it needs 44 of face width at eye level,
  and the CIRCLE head is at most 40. The cheek therefore keeps a slight
  inward S above the chin, which gives the eye bottoms their 8-unit clearance.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "194e70a7-f921-4957-b6e3-e9ba0cf49902"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1818-alien-head-angular-eyes/alien-head-angular-eyes_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
CROWN_R = 19
CROWN_Y = 4 + CROWN_R
CHIN_R = 5
CHIN_BOTTOM = 44
CHEEK_DROP = 16
CHEEK_TAPER = 2.5
EYE_OUTER = (14, 20)          # left eye outer-top corner
EYE_INNER = (20, 28)          # left eye inner-low tip
EYE_UPPER = ((18, 18), (20, 21.5))  # upper edge controls, O -> I
EYE_LOWER = ((16.5, 30.5), (11.5, 26.5))  # lower edge controls, I -> O


class AlienHeadAngularEyesRedraw(Solo48):
    icon_id = "alien-head-angular-eyes-redraw"
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

        mirror = lambda side, pt: (AXIS + side * (AXIS - pt[0]), pt[1])
        for side, name in ((-1, "eye-left"), (1, "eye-right")):
            o, i = mirror(side, EYE_OUTER), mirror(side, EYE_INNER)
            up = [mirror(side, c) for c in EYE_UPPER]
            lo = [mirror(side, c) for c in EYE_LOWER]
            self.add_bezier(f"{name}-upper", o, (up[0], up[1], i))
            self.add_bezier(f"{name}-lower", i, (lo[0], lo[1], o))
            self.add_contour(name, f"{name}-upper", f"{name}-lower", closed=True)
