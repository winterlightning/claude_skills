"""curved war horn (redraw of the new-pipeline traced SVG).

Plan: a hollow horn tube curving from a flared bell rim at the upper right down
and left to a small ring mouthpiece, HRECT_M (centerline box (4,10)-(44,38)).
- bell rim: ellipse rx 10 / ry 5 about (34,15), a closed contour of two arcs
  split at the wall joints (26,18) and (42,18), integer points of the ellipse.
  Its top apex is the y=10 extreme and its right apex the x=44 extreme; the rim
  flares 2 wider than the tube on each side, as in the generated image.
- inner wall: one cubic leaving the rim along its normal (square to the rim),
  bending into a J and arriving level at the mouthpiece top joint (12,26).
- outer wall: two tangent cubics leaving the rim along its normal, swinging
  through the y=38 extreme at (24,38) with a level tangent, and rising into the
  mouthpiece bottom joint (12,34).
- mouthpiece: ring r 5 about (9,30), split at the two wall joints (3-4-5
  points), its left apex on the x=4 extreme.
Metric issues fixed:
- clearance e2/e3 (walls 2.93 apart where they met the mouthpiece): each wall
  ends on its own mouthpiece joint 8 apart, and the inner wall arrives level so
  it never dips toward the outer one.
- hole (0.6-wide sliver at the rim's left join, where the traced inner wall
  overshot the rim): the walls end exactly on the rim, so no sliver remains.
  Holes now: rim 6, tube 13, mouthpiece 5.88 (the 6 floor at raster sampling).
- keyshape-short-axis (x filled 95%): extremes rebuilt on x 4 and 44, y 10 and 38.
- stroke-width (2.55 fitted): drawn at the profile stroke 4. The walls meet the
  rim at about 90 degrees so no wedge forms at stroke 4.
No issues left unfixed; svg_metrics.py on the redraw reports none.
No useful Lucide match (no horn icon); construction follows Lucide's
ellipse-and-curve tube style.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f57ae871-f8c2-531a-86e3-1e726b05c69e"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1117-curved-war-horn/curved-war-horn_raw.svg"
AUTHOR = "claude-opus-5-5"

RIM_C, RIM_RX, RIM_RY = (34, 15), 10, 5       # x 24..44, y 10..20
# Wall joints on the rim's lower half: (x/10)^2 + (y/5)^2 = 1 at (+-8, 3).
RIM_IN = (RIM_C[0] - 8, RIM_C[1] + 3)          # (26,18)
RIM_OUT = (RIM_C[0] + 8, RIM_C[1] + 3)         # (42,18)
MOUTH_C, MOUTH_R = (9, 30), 5                  # x 4..14
MOUTH_TOP = (MOUTH_C[0] + 3, MOUTH_C[1] - 4)   # (12,26)
MOUTH_BOT = (MOUTH_C[0] + 3, MOUTH_C[1] + 4)   # (12,34)
BOTTOM = (24, 38)                              # y=38 extreme of the outer wall


class CurvedWarHornRedraw(Solo48):
    icon_id = "curved-war-horn-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/music"
    aliases = ("war horn", "horn", "drinking horn", "hunting horn")
    keywords = ("horn", "war", "battle", "viking", "call", "signal", "blow", "instrument")

    def build(self) -> None:
        self.add_arc("rim-top", RIM_IN, RIM_OUT, radius_x=RIM_RX, radius_y=RIM_RY, large_arc=True)
        self.add_arc("rim-bottom", RIM_OUT, RIM_IN, radius_x=RIM_RX, radius_y=RIM_RY)
        self.add_contour("rim", "rim-top", "rim-bottom", closed=True)

        self.add_arc("mouth-inner", MOUTH_TOP, MOUTH_BOT, radius_x=MOUTH_R)
        self.add_arc("mouth-outer", MOUTH_BOT, MOUTH_TOP, radius_x=MOUTH_R, large_arc=True)
        self.add_contour("mouth", "mouth-inner", "mouth-outer", closed=True)

        # Both walls leave the rim along its normal (-2,3) / (2,3), square to the
        # rim. The inner wall bends into a J and meets the mouthpiece level; the
        # outer wall swings through the bottom apex (level tangent) and rises
        # into the mouthpiece.
        self.add_bezier("wall-inner", RIM_IN, ((24, 21), (19, 26), MOUTH_TOP))
        self.add_bezier("wall-outer", RIM_OUT,
                        ((44, 21), (38, 38), BOTTOM),
                        ((18, 38), (14, 37), MOUTH_BOT))

        for wall in ("wall-inner", "wall-outer"):
            self.relate("connect", wall, "rim")
            self.relate("connect", wall, "mouth")
