"""finger-tapping-projected-panel (redraw of the new-pipeline traced SVG).

Plan: a floating projected panel tapped by a single-line arm, on SQUARE
(centerline box (6,6)-(42,42)). Three parts, as in the generated image:
- panel: one open contour, a rounded rectangle x 6..35, y 6..34 (corner
  radius R=4) whose lower-right corner is left open; the right wall stops at
  y=25 and the bottom edge at x=21 so the arm can pass through the gap.
- arm: fingertip ring (radius 5, centre (21,20); inscribed hole 6) plus a
  three-segment arm polyline leaving the ring radially at (24,24) on a 3:4
  direction: forearm (24,24)->(30,32), wrist/elbow run (30,32)->(38,36) on
  2:1, upper arm (38,36)->(42,42) on 2:3, ending on the box corner.
- projector base: one horizontal stroke y=42, x 6..20, 8 below the panel.
Extremes: left x=6 (panel, base), top y=6 (panel), right x=42 and bottom
y=42 (arm end, base), so the SQUARE fit is exact.
Clearances (centerlines): ring to top wall / bottom wall / right wall 9 (the
engine cannot certify a curve sitting exactly on 8); right-wall end (35,25)
to forearm 8.2; bottom-wall end (21,34) to forearm 8.4 and to ring 9; panel
bottom to base 8.

Metric issues:
- stroke-width (info): redrawn at stroke 4, every gap re-budgeted at 8.
- keyshape-short-axis (warn, y filled 87%): fixed. The panel is taller and
  the arm and base reach y=42, so all four SQUARE extremes are on the box.
- clearance e0/e1 (panel vs ring, 4.54): fixed, 9.
- clearance e0/e3 and e0/e4 (panel vs arm, 6.98 / 4.44): fixed. The opening
  was widened and the arm re-routed: >= 8.2 to both wall ends.
- clearance e0/e5 (panel vs base, 6.26): fixed, 8.
- clearance e2/e4 (6.27): not a real clearance. e2/e3/e4 are consecutive
  segments of the one arm; they are rebuilt as a single polyline contour.
- head-gap e1/e4: not applicable. The ring is the tapping fingertip, not a
  head (the brief forbids a head or person), so it attaches to the arm by
  design at a shared endpoint declared with relate("connect"); no
  mark_human_figure is made.
Lucide construction: `presentation` / `monitor` style rounded panel with an
open corner and `pointer`-free single-stroke gesture; no closer match.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6d77d3d0-6bee-4348-b189-fc45ae2e6768"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1157-finger-tapping-projected-panel/"
    "finger-tapping-projected-panel_raw.svg"
)
AUTHOR = "claude-opus-5-5"

LO, HI = 6, 42                  # SQUARE centerline box
R = 4                           # panel corner radius
PX0, PY0, PX1, PY1 = LO, LO, 35, 34   # panel centerline rectangle
WALL_END = 25                   # right wall stops here (opening)
BOTTOM_END = 21                 # bottom edge stops here (opening)
TIP = (21, 20)                  # fingertip ring centre
TIP_R = 5
JOIN = (TIP[0] + 3, TIP[1] + 4)             # (24,24): radial 3:4 exit
FAR = (TIP[0] - 3, TIP[1] - 4)              # antipode, closes the ring
BASE_Y, BASE_END = HI, 20


class FingerTappingProjectedPanelRedraw(Solo48):
    icon_id = "finger-tapping-projected-panel-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology"
    aliases = ("touch projection", "tap projected screen", "virtual touch panel")
    keywords = ("finger", "tap", "touch", "projected", "panel", "projector",
                "hologram", "interactive", "screen", "gesture")

    def build(self) -> None:
        # panel: open rounded rectangle, gap at the lower-right corner
        self.add_line("panel-bottom", (BOTTOM_END, PY1), (PX0 + R, PY1))
        self.add_arc("panel-bl", (PX0 + R, PY1), (PX0, PY1 - R), radius_x=R)
        self.add_line("panel-left", (PX0, PY1 - R), (PX0, PY0 + R))
        self.add_arc("panel-tl", (PX0, PY0 + R), (PX0 + R, PY0), radius_x=R)
        self.add_line("panel-top", (PX0 + R, PY0), (PX1 - R, PY0))
        self.add_arc("panel-tr", (PX1 - R, PY0), (PX1, PY0 + R), radius_x=R)
        self.add_line("panel-right", (PX1, PY0 + R), (PX1, WALL_END))
        self.add_contour("panel", "panel-bottom", "panel-bl", "panel-left",
                         "panel-tl", "panel-top", "panel-tr", "panel-right")

        # fingertip ring, split where the arm attaches
        self.add_arc("tip-a", JOIN, FAR, radius_x=TIP_R)
        self.add_arc("tip-b", FAR, JOIN, radius_x=TIP_R)
        self.add_contour("tip", "tip-a", "tip-b", closed=True)

        # arm: forearm, elbow run, upper arm
        self.add_polyline("arm", JOIN, (30, 32), (38, 36), (HI, HI))
        self.relate("connect", "tip", "arm")

        # projector base
        self.add_line("base", (LO, BASE_Y), (BASE_END, BASE_Y))
