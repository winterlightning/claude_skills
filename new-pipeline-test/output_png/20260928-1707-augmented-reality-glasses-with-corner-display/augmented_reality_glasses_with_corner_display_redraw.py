"""augmented-reality-glasses-with-corner-display (redraw of the new-pipeline traced PNG).

Plan: front view of smart glasses on HRECT_M (centerline box (4,10)-(44,38)).
- lenses: two mirrored rounded rectangles, 16 wide x 16 tall, corner radius
  4, about the axis x=24: left x 4..20, right x 28..44, y 22..38.
- bridge: a level line at y=28 joining the inner lens walls (gap 8).
- display: the corner display is a rounded housing standing on the upper
  outer corner of the right lens (x 32..44, y 10..22), Google-Glass style.
  Its right wall continues the lens's outer wall, so the right lens keeps a
  square top-right corner under it; the housing shares the lens top wall
  as its bottom edge, and its left wall rises from the tangent point where
  the lens's top-left corner arc ends.
Temples are dropped: at 48 the short side stubs of the trace cannot fit
beside 16-wide lenses in a 40-unit width.

Metric issues:
- clearance e0/e1 (lenses 5.23 apart): fixed, lens walls now 8 apart.
- clearance e1/e5 and e3/e5 (L mark 2.04 from the lens wall and temple):
  fixed by redrawing the display. A free L mark inside a 16-wide lens has
  no room (it needs 8 from both side walls, leaving a single column), so
  the display became a housing connected to the lens, whose window
  (12 x 12 on centerlines) clears the 6 inscribed-hole floor.
- keyshape-short-axis (y filled 47%): fixed, the housing top reaches y=10
  and the lens bottoms y=38.
- loose-join e4/e0, e4/e1: fixed, the bridge shares split endpoints on the
  lens walls with relate('connect').
- stroke-width: redrawn natively at stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f3f157a4-4ba4-56cb-af69-39f5c5fe3376"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1707-augmented-reality-glasses-with-corner-display/"
    "augmented-reality-glasses-with-corner-display_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
LENS_W = 16
GAP = 8                        # bridge span between the inner lens walls
TOP, BOTTOM = 22, 38           # lens top and bottom walls
R = 4                          # lens and housing corner radius
BRIDGE_Y = 28

L_OUT, L_IN = AXIS - GAP // 2 - LENS_W, AXIS - GAP // 2      # 4, 20
R_IN, R_OUT = AXIS + GAP // 2, AXIS + GAP // 2 + LENS_W      # 28, 44
DISPLAY_L, DISPLAY_TOP = R_IN + R, 10    # housing starts where the lens corner arc ends


class AugmentedRealityGlassesWithCornerDisplayRedraw(Solo48):
    icon_id = "augmented-reality-glasses-with-corner-display-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "devices"
    aliases = ("ar glasses", "smart glasses", "google glass", "heads-up display glasses")
    keywords = ("augmented", "reality", "ar", "glasses", "smart", "display", "wearable", "device")

    def build(self) -> None:
        # Left lens, clockwise from the top wall; inner wall split at the bridge.
        self.add_line("l-top", (L_OUT + R, TOP), (L_IN - R, TOP))
        self.add_arc("l-tr", (L_IN - R, TOP), (L_IN, TOP + R), radius_x=R)
        self.add_line("l-in-1", (L_IN, TOP + R), (L_IN, BRIDGE_Y))
        self.add_line("l-in-2", (L_IN, BRIDGE_Y), (L_IN, BOTTOM - R))
        self.add_arc("l-br", (L_IN, BOTTOM - R), (L_IN - R, BOTTOM), radius_x=R)
        self.add_line("l-bottom", (L_IN - R, BOTTOM), (L_OUT + R, BOTTOM))
        self.add_arc("l-bl", (L_OUT + R, BOTTOM), (L_OUT, BOTTOM - R), radius_x=R)
        self.add_line("l-out", (L_OUT, BOTTOM - R), (L_OUT, TOP + R))
        self.add_arc("l-tl", (L_OUT, TOP + R), (L_OUT + R, TOP), radius_x=R)
        self.add_contour(
            "lens-left", "l-top", "l-tr", "l-in-1", "l-in-2", "l-br",
            "l-bottom", "l-bl", "l-out", "l-tl", closed=True,
        )

        # Right lens, mirrored, except its top-right corner is square: the
        # display housing sits there and continues the outer wall upward.
        self.add_arc("r-tl", (R_IN, TOP + R), (R_IN + R, TOP), radius_x=R)
        self.add_line("r-top", (DISPLAY_L, TOP), (R_OUT, TOP))
        self.add_line("r-out", (R_OUT, TOP), (R_OUT, BOTTOM - R))
        self.add_arc("r-br", (R_OUT, BOTTOM - R), (R_OUT - R, BOTTOM), radius_x=R)
        self.add_line("r-bottom", (R_OUT - R, BOTTOM), (R_IN + R, BOTTOM))
        self.add_arc("r-bl", (R_IN + R, BOTTOM), (R_IN, BOTTOM - R), radius_x=R)
        self.add_line("r-in-2", (R_IN, BOTTOM - R), (R_IN, BRIDGE_Y))
        self.add_line("r-in-1", (R_IN, BRIDGE_Y), (R_IN, TOP + R))
        self.add_contour(
            "lens-right", "r-tl", "r-top", "r-out", "r-br",
            "r-bottom", "r-bl", "r-in-2", "r-in-1", closed=True,
        )

        # Bridge between the split inner walls.
        self.add_line("bridge", (L_IN, BRIDGE_Y), (R_IN, BRIDGE_Y))
        self.relate("connect", "bridge", "lens-left")
        self.relate("connect", "bridge", "lens-right")

        # Display housing: up from the lens top wall, over, and down onto the
        # lens's square corner.
        self.add_line("d-left", (DISPLAY_L, TOP), (DISPLAY_L, DISPLAY_TOP + R))
        self.add_arc("d-tl", (DISPLAY_L, DISPLAY_TOP + R), (DISPLAY_L + R, DISPLAY_TOP), radius_x=R)
        self.add_line("d-top", (DISPLAY_L + R, DISPLAY_TOP), (R_OUT - R, DISPLAY_TOP))
        self.add_arc("d-tr", (R_OUT - R, DISPLAY_TOP), (R_OUT, DISPLAY_TOP + R), radius_x=R)
        self.add_line("d-right", (R_OUT, DISPLAY_TOP + R), (R_OUT, TOP))
        self.add_contour("display", "d-left", "d-tl", "d-top", "d-tr", "d-right")
        self.relate("connect", "display", "lens-right")
