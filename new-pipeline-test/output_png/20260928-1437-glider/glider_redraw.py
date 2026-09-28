"""glider (redraw of the new-pipeline traced SVG).

Plan: front view of a sailplane on HRECT_M (centerline box (4,10)-(44,38)),
mirrored about x=24.
- fuselage: upright oval, four quarter arcs rx=R_X ry=R_Y about (24, FUS_CY);
  its bottom apex is the y=38 extreme, its side apexes are the wing roots.
- wings: one smooth cubic per side from the fuselage side apex, flat at the
  root and sweeping up to a round tip on the x=4 / x=44 extremes.
- T-tail: fin straight up from the fuselage top apex to the tailplane, which
  sits on the y=10 extreme; the fin splits the tailplane so they share a node.
Dropped from the trace: the canopy line through the fuselage and the four
wing-root fillet ticks, which at 48 px sat 0-5 units from the fuselage wall
(metrics clearance errors), and would close the 6-unit opening. The trace
fills only 46% of the short axis, so the tail is lifted and the fuselage
lengthened to reach the HRECT_M extremes. No useful Lucide match (Lucide
`plane` is a top-down airliner).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1437-glider/glider_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
R_X, R_Y = 5, 8
FUS_CY = 30                    # fuselage oval spans y 22..38
FUS_TOP = (AXIS, FUS_CY - R_Y)
FUS_BOTTOM = (AXIS, FUS_CY + R_Y)
ROOT_L = (AXIS - R_X, FUS_CY)  # wing roots on the oval's side apexes
TAIL_Y = 10
TAIL_HALF = 8
TIP_L = (4, 25)
# Left wing: level leaving the root, bending up into the tip.
WING_L = ((12, FUS_CY), (7, 29), TIP_L)


def mx(p):
    return (2 * AXIS - p[0], p[1])


class GliderRedraw(Solo48):
    icon_id = "glider-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/aircraft"
    aliases = ("sailplane", "glider plane")
    keywords = ("glider", "sailplane", "gliding", "soaring", "aircraft", "flight", "wings")

    def build(self) -> None:
        root_r = mx(ROOT_L)
        self.add_arc("fus-1", FUS_TOP, root_r, radius_x=R_X, radius_y=R_Y)
        self.add_arc("fus-2", root_r, FUS_BOTTOM, radius_x=R_X, radius_y=R_Y)
        self.add_arc("fus-3", FUS_BOTTOM, ROOT_L, radius_x=R_X, radius_y=R_Y)
        self.add_arc("fus-4", ROOT_L, FUS_TOP, radius_x=R_X, radius_y=R_Y)
        self.add_contour("fuselage", "fus-1", "fus-2", "fus-3", "fus-4", closed=True)

        self.add_bezier("wing-l", ROOT_L, WING_L)
        self.add_bezier("wing-r", root_r, tuple(mx(p) for p in WING_L))
        self.relate("connect", "wing-l", "fuselage")
        self.relate("connect", "wing-r", "fuselage")

        tail_mid = (AXIS, TAIL_Y)
        self.add_line("fin", FUS_TOP, tail_mid)
        self.relate("connect", "fin", "fuselage")
        self.add_line("tailplane-l", (AXIS - TAIL_HALF, TAIL_Y), tail_mid)
        self.add_line("tailplane-r", tail_mid, (AXIS + TAIL_HALF, TAIL_Y))
        self.add_contour("tailplane", "tailplane-l", "tailplane-r")
        self.relate("connect", "fin", "tailplane")
