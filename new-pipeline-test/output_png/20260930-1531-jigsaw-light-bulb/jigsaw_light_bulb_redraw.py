"""jigsaw-light-bulb (redraw of the new-pipeline traced SVG).

Plan: a light bulb whose globe is split into two jigsaw pieces by a vertical
seam with one round tab, and a separate rounded base cap below, as in the
generated image. Authored on VRECT_M (the suggested keyshape), centerline box
(10,4)-(38,44), mirrored on x=24 except the tab.
- globe: dome r14 about (24,18) reaching x 10/38 and y 4, tangent-continuous
  S-shoulders (vertical tangents at both ends) narrowing from (38,18) to the
  neck walls x 16/32 at y 29, r2 bottom corners and a flat neck bottom y=31.
  One closed contour, walked clockwise, left half the mirror of the right.
- seam: x=24 from the dome apex to the neck bottom (split walls share both
  endpoints); the tab is a semicircle r4 about (24,17) bulging right, 9 from
  the dome and at least 8.6 from the shoulder, so the pieces interlock.
- base: an open U cap x 18..30 with r3 corners and a flat bottom y=44 (the
  box edge); its ends at y=40 sit 9 below the neck bottom, because the neck
  corner arcs cannot be certified at exactly 8.

Metric issues fixed:
- clearance e0/e1 (seam/tab 6.43 from the globe): the tab is r4 on (24,17),
  9 from the dome and 8.6 from the shoulder, and the neck is widened to
  x 16..32 so the seam stays 8 from both neck walls.
- clearance e0/e4 and e1/e4 (base 2.72 below the neck): the base now starts
  9 below the neck bottom line.
- hole at (28.2,9.5), 4.43 wide: the right piece is at least 8 wide on
  centerlines everywhere (10 beside the tab).
- hole at (23.2,40.4), 3.2 wide: the base is an open U, so it encloses no
  hole (a closed cap would need 10 centerline height, which the 40 unit
  budget cannot give after the globe and the 8 gap).
- keyshape-short-axis: the dome reaches x 10 and 38 exactly; y 4 at the apex
  and y 44 at the U.
- stroke-width (info): redrawn at stroke 4 with every gap budgeted at 8.
Deliberate asymmetry: the jigsaw tab only.
Construction reference: Lucide `lightbulb` (circular dome, smooth narrowing
shoulders, base drawn as a separate part below the neck).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "8013a3c2-dcf3-475e-98f6-cb6db629e137"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1531-jigsaw-light-bulb/jigsaw-light-bulb_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS, DOME_Y, DOME_R = 24, 18, 14       # dome centre and radius (x 10..38, top y 4)
NECK_HALF, NECK_Y, CORNER_R = 8, 31, 2       # neck walls x 16/32, flat bottom y 31
TAB_Y, TAB_R = 17, 4                    # jigsaw tab centre y and radius
BASE_HALF, BASE_TOP, BASE_Y, BASE_R = 6, 40, 44, 3   # open U cap x 18..30, ends y 40, flat bottom y 44


class JigsawLightBulbRedraw(Solo48):
    icon_id = "jigsaw-light-bulb-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ("puzzle light bulb", "puzzle idea", "jigsaw idea")
    keywords = ("light bulb", "jigsaw", "puzzle", "idea", "solution", "problem solving", "creativity", "insight")

    def build(self) -> None:
        a, top = AXIS, DOME_Y - DOME_R
        # One clockwise walk: right half top-down, left half bottom-up (mirror of x).
        wide = (a + DOME_R, DOME_Y)
        neck = (a + NECK_HALF, NECK_Y - CORNER_R)
        pts = [(a, top), wide, neck, (neck[0] - CORNER_R, NECK_Y), (a, NECK_Y)]
        ctrl = ((wide[0], DOME_Y + 6), (neck[0], NECK_Y - 7))
        m = lambda p: (2 * a - p[0], p[1])
        self.add_arc("dome-r", pts[0], pts[1], radius_x=DOME_R, sweep=True)
        self.add_bezier("shoulder-r", pts[1], (ctrl[0], ctrl[1], pts[2]))
        self.add_arc("corner-r", pts[2], pts[3], radius_x=CORNER_R, sweep=True)
        self.add_line("bottom-r", pts[3], pts[4])
        self.add_line("bottom-l", pts[4], m(pts[3]))
        self.add_arc("corner-l", m(pts[3]), m(pts[2]), radius_x=CORNER_R, sweep=True)
        self.add_bezier("shoulder-l", m(pts[2]), (m(ctrl[1]), m(ctrl[0]), m(pts[1])))
        self.add_arc("dome-l", m(pts[1]), pts[0], radius_x=DOME_R, sweep=True)
        self.add_contour(
            "globe",
            "dome-r", "shoulder-r", "corner-r", "bottom-r",
            "bottom-l", "corner-l", "shoulder-l", "dome-l",
            closed=True,
        )

        self.add_line("seam-top", (a, top), (a, TAB_Y - TAB_R))
        self.add_arc("tab", (a, TAB_Y - TAB_R), (a, TAB_Y + TAB_R), radius_x=TAB_R, sweep=True)
        self.add_line("seam-bottom", (a, TAB_Y + TAB_R), (a, NECK_Y))
        self.add_contour("seam", "seam-top", "tab", "seam-bottom")
        for wall in ("dome-l", "dome-r"):
            self.relate("connect", "seam-top", wall)
        for wall in ("bottom-l", "bottom-r"):
            self.relate("connect", "seam-bottom", wall)

        l, r, turn = a - BASE_HALF, a + BASE_HALF, BASE_Y - BASE_R
        self.add_line("base-l", (l, BASE_TOP), (l, turn))
        self.add_arc("base-corner-l", (l, turn), (l + BASE_R, BASE_Y), radius_x=BASE_R, sweep=False)
        self.add_line("base-bottom", (l + BASE_R, BASE_Y), (r - BASE_R, BASE_Y))
        self.add_arc("base-corner-r", (r - BASE_R, BASE_Y), (r, turn), radius_x=BASE_R, sweep=False)
        self.add_line("base-r", (r, turn), (r, BASE_TOP))
        self.add_contour("base", "base-l", "base-corner-l", "base-bottom", "base-corner-r", "base-r")
