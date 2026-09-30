"""desktop computer (redraw of the new-pipeline traced SVG).

Plan: HRECT_L (centerline box (4,8)-(44,40), ink (2,6)-(46,42)), mirrored
about x=24. Three parts, as in the generated image:
- screen: one closed rounded-rectangle contour, x 4..44, y 8..32, corner
  r4 (Lucide monitor's rx 2 at 24 -> 4 at 48). The bottom edge is split at
  (24,32) where the stand attaches. Empty screen, as in the image.
- stand: a vertical line (24,32)-(24,40), 8 long, so the foot sits exactly
  8 below the screen's bottom edge on centerlines.
- foot: (16,40)-(32,40), split at (24,40) where the stand ends (half the
  screen width, as Lucide's monitor foot).
Keyshape: HRECT_L instead of the suggested HRECT_M. The metrics scored them
1.20 vs 1.17, but the fix for the clearance error lengthens the stand from
5.3 to 8, which needs vertical room: on HRECT_M (28 tall) the screen would
shrink to 40x20 (aspect 2.0); on HRECT_L (32 tall) it is 40x24 (aspect
1.67), matching the traced screen (38.2 x 22.7 = 1.69).
Traced shape: batch-02-desktop-computer-computers_raw.svg and .png (read for
the subject only; nothing copied from its coordinates).
Lucide: `monitor` (rounded rect 20x14 rx2, stand 17->21, foot 8..16),
redrawn on this grid and keyshape.

Metric issues:
- clearance e1/e2 (foot 5.34 below the screen): fixed, the stand is 8 long,
  so the foot is 8 from the screen on centerlines (4 ink gap).
- keyshape-short-axis (x filled only 95% of HRECT_M): fixed, the screen now
  spans x 4..44 and every extreme is on the HRECT_L box (see keyshape note).
- stroke-width (info): drawn at stroke 4; every gap budgeted for 4.
Nothing dropped.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "94bf7c3e-3c0a-4019-a95a-f28f2638320e"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1809-batch-02-desktop-computer-computers/batch-02-desktop-computer-computers_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                  # mirror axis
LEFT, RIGHT = 4, 44      # screen sides
TOP, BOTTOM = 8, 32      # screen top / bottom edge
R = 4                    # screen corner radius
FOOT_Y = 40              # foot line; stand = BOTTOM..FOOT_Y = 8
FOOT_HALF = 8            # foot x 16..32


class Batch02DesktopComputerComputersRedraw(Solo48):
    icon_id = "batch-02-desktop-computer-computers-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "computers"
    aliases = ("desktop-computer", "monitor", "display", "screen")
    keywords = ("desktop", "computer", "monitor", "display", "screen", "pc")

    def build(self) -> None:
        self.add_line("top", (LEFT + R, TOP), (RIGHT - R, TOP))
        self.add_arc("corner-tr", (RIGHT - R, TOP), (RIGHT, TOP + R), radius_x=R, sweep=True)
        self.add_line("right", (RIGHT, TOP + R), (RIGHT, BOTTOM - R))
        self.add_arc("corner-br", (RIGHT, BOTTOM - R), (RIGHT - R, BOTTOM), radius_x=R, sweep=True)
        self.add_line("bottom-r", (RIGHT - R, BOTTOM), (AX, BOTTOM))
        self.add_line("bottom-l", (AX, BOTTOM), (LEFT + R, BOTTOM))
        self.add_arc("corner-bl", (LEFT + R, BOTTOM), (LEFT, BOTTOM - R), radius_x=R, sweep=True)
        self.add_line("left", (LEFT, BOTTOM - R), (LEFT, TOP + R))
        self.add_arc("corner-tl", (LEFT, TOP + R), (LEFT + R, TOP), radius_x=R, sweep=True)
        self.add_contour(
            "screen", "top", "corner-tr", "right", "corner-br", "bottom-r",
            "bottom-l", "corner-bl", "left", "corner-tl", closed=True,
        )

        self.add_line("stand", (AX, BOTTOM), (AX, FOOT_Y))
        self.add_line("foot-l", (AX - FOOT_HALF, FOOT_Y), (AX, FOOT_Y))
        self.add_line("foot-r", (AX, FOOT_Y), (AX + FOOT_HALF, FOOT_Y))
        self.add_contour("foot", "foot-l", "foot-r")

        self.relate("connect", "stand", "bottom-r")
        self.relate("connect", "stand", "bottom-l")
        self.relate("connect", "stand", "foot-l")
        self.relate("connect", "stand", "foot-r")
