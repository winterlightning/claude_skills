"""computer-typing-keyboard (redraw of the new-pipeline traced SVG).

Plan: a wide keyboard on HRECT_M (centerline box (4,10)-(44,38)).
- body: one closed rounded rectangle on the box, corner radius R, drawn as
  four walls and four quarter arcs in one contour; its walls are the four
  keyshape extremes.
- keys: a repeat of three short vertical strokes on a shared pitch of 10,
  centred on the x=24 axis (x = 14, 24, 34), from KEY_TOP to KEY_BOTTOM.
- spacebar: one horizontal stroke centred on x=24, spanning from the left
  key's column to the right key's column plus a small overhang.
Vertical budget (28 between the walls): wall -> keys 9, keys 2 long,
keys -> spacebar 8, spacebar -> wall 9. Every gap to the arc-cornered body
is 9, not 8: an exact 8 against a contour that contains arcs cannot be
certified and comes back `review` (tested: 4 warnings at 8). A square-cornered
body passed at 8 with 4-long keys, but lost the trace's rounded corners;
the rounded body reads closer to the reference at 48 px.
Mirror-symmetric about x=24.
Lucide `keyboard` informed the construction (rounded body with key marks
and a spacebar), reduced to the trace's three keys + spacebar.

Metric issues repaired:
- stroke-width: redrawn at stroke 4; every gap budgeted for 4.
- keyshape-short-axis: the body's top and bottom walls sit on y=10/y=38 and
  its sides on x=4/x=44, so all four HRECT_M extremes are exact (the y axis
  was stretched from 67% to 100%).
- clearance e0/e1, e0/e2, e0/e3 (keys on the top wall): keys start 9 below it.
- clearance e0/e4 (spacebar on the bottom wall and corners): spacebar sits 9
  above the bottom wall and its ends 9 from the side walls.
- clearance e1/e4, e2/e4, e3/e4 (keys on the spacebar): 8 between them.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "6da646a1-34eb-51f2-af2d-b08aed786a57"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1050-computer-typing-keyboard/"
    "computer-typing-keyboard_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
LEFT, RIGHT, TOP, BOTTOM = 4, 44, 10, 38
R = 4                          # body corner radius
KEY_PITCH = 10
KEYS = tuple(AXIS + KEY_PITCH * k for k in (-1, 0, 1))
KEY_TOP = TOP + 9
KEY_BOTTOM = KEY_TOP + 2
SPACE_Y = KEY_BOTTOM + 8       # also BOTTOM - 9
SPACE_HALF = 11                # ends 9 from the side walls


class ComputerTypingKeyboardRedraw(Solo48):
    icon_id = "computer-typing-keyboard-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("keyboard", "computer keyboard", "typing")
    keywords = ("keyboard", "typing", "computer", "keys", "spacebar", "input", "type")

    def build(self) -> None:
        self.add_line("body-top", (LEFT + R, TOP), (RIGHT - R, TOP))
        self.add_arc("body-tr", (RIGHT - R, TOP), (RIGHT, TOP + R), radius_x=R, sweep=True)
        self.add_line("body-right", (RIGHT, TOP + R), (RIGHT, BOTTOM - R))
        self.add_arc("body-br", (RIGHT, BOTTOM - R), (RIGHT - R, BOTTOM), radius_x=R, sweep=True)
        self.add_line("body-bottom", (RIGHT - R, BOTTOM), (LEFT + R, BOTTOM))
        self.add_arc("body-bl", (LEFT + R, BOTTOM), (LEFT, BOTTOM - R), radius_x=R, sweep=True)
        self.add_line("body-left", (LEFT, BOTTOM - R), (LEFT, TOP + R))
        self.add_arc("body-tl", (LEFT, TOP + R), (LEFT + R, TOP), radius_x=R, sweep=True)
        self.add_contour("body", "body-top", "body-tr", "body-right", "body-br",
                         "body-bottom", "body-bl", "body-left", "body-tl", closed=True)

        for index, x in enumerate(KEYS, start=1):
            self.add_line(f"key-{index}", (x, KEY_TOP), (x, KEY_BOTTOM))

        self.add_line("spacebar", (AXIS - SPACE_HALF, SPACE_Y), (AXIS + SPACE_HALF, SPACE_Y))
