"""arrow down rounded outline (redraw of the new-pipeline traced SVG).

Plan: VRECT_M (centerline box (10,4)-(38,44)), after Lucide `arrow-big-down`
(hollow shaft with a rounded top on a 90-degree arrowhead with 45-degree
sides), which is the generated image's construction. One closed contour,
mirrored about the axis x=AXIS:
- shaft: walls x=AXIS -/+ SHAFT_R from the shoulder line y=SHOULDER_Y up to
  y=TOP_Y + SHAFT_R, capped by a semicircle of radius SHAFT_R about
  (AXIS, TOP_Y + SHAFT_R), split at its apex (AXIS, TOP_Y) so the y=4
  extreme is an arc endpoint.
- head: shoulder lines out to the corners (10, SHOULDER_Y) and
  (38, SHOULDER_Y) (the x extremes), 45-degree sides to the tip
  (AXIS, TIP_Y) (the y=44 extreme). HEAD_HALF = 14 makes the sides exactly
  45 degrees. The soft corners of the image come from the round joins;
  Lucide's tiny corner arcs have no integer tangent points on 45-degree
  sides, so they are not drawn as arcs.
Metric issues:
- stroke-width (trace 2.67 fitted): redrawn at stroke 4 on the integer grid;
  the shaft is widened to 10 between centerlines (trace ~8) so its white
  channel stays 6 wide at stroke 4.
- keyshape-short-axis (x filled 86%): fixed; the head corners sit on x=10
  and x=38, the shaft apex on y=4 and the tip on y=44, so all four VRECT_M
  extremes are exact without stretching the shaft.
- the trace's lopsided tip (two unequal arcs plus a stray 1-unit segment)
  and elliptical corner arcs are gone: the drawing is mirror-symmetric.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6747c5ea-98ee-4045-b34c-2a968c515c7a"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1813-arrow-down-rounded-outline/arrow-down-rounded-outline_raw.svg"
AUTHOR = "claude-opus-5-5"

AXIS = 24
TOP_Y = 4
TIP_Y = 44
SHAFT_R = 5
HEAD_HALF = 14
SHOULDER_Y = TIP_Y - HEAD_HALF


class ArrowDownRoundedOutlineRedraw(Solo48):
    icon_id = "arrow-down-rounded-outline-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/arrows"
    aliases = ("big arrow down", "outlined down arrow")
    keywords = ("arrow", "down", "download", "direction", "downward", "descend")

    def build(self) -> None:
        left = AXIS - SHAFT_R
        right = AXIS + SHAFT_R
        cap_y = TOP_Y + SHAFT_R

        self.add_line("shaft_left", (left, SHOULDER_Y), (left, cap_y))
        self.add_arc("cap_left", (left, cap_y), (AXIS, TOP_Y), radius_x=SHAFT_R, sweep=True)
        self.add_arc("cap_right", (AXIS, TOP_Y), (right, cap_y), radius_x=SHAFT_R, sweep=True)
        self.add_line("shaft_right", (right, cap_y), (right, SHOULDER_Y))
        self.add_line("shoulder_right", (right, SHOULDER_Y), (AXIS + HEAD_HALF, SHOULDER_Y))
        self.add_line("side_right", (AXIS + HEAD_HALF, SHOULDER_Y), (AXIS, TIP_Y))
        self.add_line("side_left", (AXIS, TIP_Y), (AXIS - HEAD_HALF, SHOULDER_Y))
        self.add_line("shoulder_left", (AXIS - HEAD_HALF, SHOULDER_Y), (left, SHOULDER_Y))
        self.add_contour(
            "arrow", "shaft_left", "cap_left", "cap_right", "shaft_right",
            "shoulder_right", "side_right", "side_left", "shoulder_left",
            closed=True,
        )
