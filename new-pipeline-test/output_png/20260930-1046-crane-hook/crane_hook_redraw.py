"""crane-hook (redraw of the new-pipeline traced SVG).

Plan: VRECT_M keyshape (centerline box (10,4)-(38,44)), everything hung from
one vertical axis x=24.
- cable: a short vertical line from the top edge (24,4) down to the block.
- block: a rounded rectangle (16,8)-(32,18), corner radius 3, mirrored about
  x=24. Its top and bottom walls are split at x=24 so the cable and the hook
  share real endpoints with it (declared connect).
- hook: one open contour. An S-shaped neck cubic leaves the block bottom
  (24,18) heading straight down (it doubles as the shank) and swings down-left
  to the hook's back at (10,33), vertical there too; a half-ellipse bowl
  (rx 14, ry 11, centre (24,33)) runs round the bottom to (38,33), and a short
  vertical tip rises to (38,27). All joins are tangent-continuous; the throat
  between tip and neck stays open.
Extremes: cable top y=4, bowl bottom y=44, hook back x=10, hook tip x=38.

Metric issues:
- hole at [23.2, 17.3] (4.4 wide): fixed -- the block is 16x10 on
  centerlines, 12x6 clear, so its inscribed hole is 6.
- hole at [21.0, 40.4] (0.85 wide): fixed -- the trace's pinched double-line
  hook body is redrawn as a single stroke, so the hook encloses nothing.
- keyshape-short-axis (x fills 47%): fixed -- the hook bowl is widened to the
  full 28-unit short axis (x=10 and x=38) instead of stretching the block.
- stroke-width (2.67 vs 4): redrawn at stroke 4 with every gap between
  distinct parts budgeted at 8 on centerlines (tip to block corner 12).
Lucide fishing-hook informed the single-stroke J with an open throat and
round tip; the crane block and cable follow the generated image. The hook is
deliberately asymmetric (it opens to the right); block and cable are mirrored.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "40e56b92-93e6-4122-b70a-f6f602cc3011"
SOURCE_PATH = "new-pipeline-test/output_png/20260930-1046-crane-hook/crane-hook_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                      # shared vertical axis
TOP = 4                      # cable top
BX0, BX1, BY0, BY1, BR = 16, 32, 8, 18, 3   # block box and corner radius
NECK_PULL = 6                # vertical handle length at both ends of the neck
BOWL_CY, BOWL_RX, BOWL_RY = 33, 14, 11       # bowl half-ellipse
TIP = 27                     # hook tip end


class CraneHookRedraw(Solo48):
    icon_id = "crane-hook-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shipping"
    aliases = ("crane hook", "lifting hook", "hoist hook")
    keywords = ("crane", "hook", "hoist", "lift", "cargo", "construction", "rigging", "block")

    def build(self) -> None:
        self.add_line("cable", (AX, TOP), (AX, BY0))

        self.add_line("block-top-r", (AX, BY0), (BX1 - BR, BY0))
        self.add_arc("block-tr", (BX1 - BR, BY0), (BX1, BY0 + BR), radius_x=BR)
        self.add_line("block-right", (BX1, BY0 + BR), (BX1, BY1 - BR))
        self.add_arc("block-br", (BX1, BY1 - BR), (BX1 - BR, BY1), radius_x=BR)
        self.add_line("block-bottom-r", (BX1 - BR, BY1), (AX, BY1))
        self.add_line("block-bottom-l", (AX, BY1), (BX0 + BR, BY1))
        self.add_arc("block-bl", (BX0 + BR, BY1), (BX0, BY1 - BR), radius_x=BR)
        self.add_line("block-left", (BX0, BY1 - BR), (BX0, BY0 + BR))
        self.add_arc("block-tl", (BX0, BY0 + BR), (BX0 + BR, BY0), radius_x=BR)
        self.add_line("block-top-l", (BX0 + BR, BY0), (AX, BY0))
        self.add_contour(
            "block", "block-top-r", "block-tr", "block-right", "block-br",
            "block-bottom-r", "block-bottom-l", "block-bl", "block-left",
            "block-tl", "block-top-l", closed=True,
        )

        back = (AX - BOWL_RX, BOWL_CY)
        front = (AX + BOWL_RX, BOWL_CY)
        self.add_bezier(
            "hook-neck", (AX, BY1),
            ((AX, BY1 + NECK_PULL), (back[0], back[1] - NECK_PULL), back),
        )
        self.add_arc("hook-bowl", back, front, radius_x=BOWL_RX, radius_y=BOWL_RY, sweep=False)
        self.add_line("hook-tip", front, (front[0], TIP))
        self.add_contour("hook", "hook-neck", "hook-bowl", "hook-tip")

        self.relate("connect", "cable", "block")
        self.relate("connect", "hook", "block")
