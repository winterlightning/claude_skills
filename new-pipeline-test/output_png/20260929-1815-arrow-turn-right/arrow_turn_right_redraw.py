"""arrow-turn-right (redraw of the new-pipeline traced SVG).

Plan: a turn arrow on SQUARE (centerline box (6,6)-(42,42)).
- shaft: one open contour -- a vertical rising on the x=6 extreme from the
  y=42 extreme, a tangent quarter arc of radius R into a horizontal that
  runs right to the arrow tip on the x=42 extreme.
- head: an open two-arm chevron at 45 degrees, mirrored about the shaft
  line y=HEAD_Y; its top arm end sits on the y=6 extreme, and its tip is the
  shaft's end node (shared endpoint, declared connect).
The trace was re-authored, not copied: integer arc centre (6+R, HEAD_Y+R),
arms of equal length HEAD, the elbow radius rounded from the trace's ~9.9.
Lucide `corner-up-right` construction (path M4 20v-7a4 4 0 0 1 4-4h12 plus
polyline 15 14/20 9/15 4): tangent elbow and a 45-degree open chevron.

Metric issues:
- stroke-width (info): redrawn at stroke 4; all gaps checked at stroke 4.
- clearance e0/e2 and e1/e2 (6.25 / 6.15 < 8): these are the two chevron
  arms against the shaft they meet at the tip. A 45-degree arm is always
  closer than 8 to its own shaft within ~11 units of the tip; this is the
  shared-endpoint arrowhead junction, which the Solo48 validator exempts
  (validate_icon() is valid with no warnings). Kept the Lucide 45-degree head
  rather than splaying it, since a wider head reads as a "T" at 48 px.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "90bda1dc-4ea8-4d9e-aace-a5784e398b7c"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1815-arrow-turn-right/arrow-turn-right_raw.svg"
AUTHOR = "claude-opus-5-5"

LEFT, RIGHT, TOP, BOTTOM = 6, 42, 6, 42
HEAD = 9                      # chevron arm run/rise (45 degrees)
HEAD_Y = TOP + HEAD           # shaft line; top arm end lands on y=6
R = 10                        # elbow radius
TIP = (RIGHT, HEAD_Y)


class ArrowTurnRightRedraw(Solo48):
    icon_id = "arrow-turn-right-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "arrows"
    aliases = ("turn right", "corner up right")
    keywords = ("arrow", "turn", "right", "corner", "direction", "navigation")

    def build(self) -> None:
        self.add_line("shaft-up", (LEFT, BOTTOM), (LEFT, HEAD_Y + R))
        self.add_arc("shaft-bend", (LEFT, HEAD_Y + R), (LEFT + R, HEAD_Y),
                     radius_x=R, radius_y=R, sweep=True)
        self.add_line("shaft-right", (LEFT + R, HEAD_Y), TIP)
        self.add_contour("shaft", "shaft-up", "shaft-bend", "shaft-right")

        self.add_line("head-top", (RIGHT - HEAD, HEAD_Y - HEAD), TIP)
        self.add_line("head-bottom", TIP, (RIGHT - HEAD, HEAD_Y + HEAD))
        self.add_contour("head", "head-top", "head-bottom")
        self.relate("connect", "shaft", "head")
