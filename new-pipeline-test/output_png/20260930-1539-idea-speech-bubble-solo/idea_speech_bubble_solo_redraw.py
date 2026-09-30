"""idea-speech-bubble-solo (redraw of the new-pipeline traced SVG).

Plan: a rounded speech bubble with a short lower-left tail holding one
hollow lightbulb, on SQUARE (centerline box (6,6)-(42,42)), as suggested
by the metrics (fill 1.0 x 1.0).
- bubble: body (6,6)-(42,37) with r8 corners; the lower-left arc ends at
  (14,37), a vertical tail edge drops to the tip (14,42) and a 45 degree
  edge returns to the bottom wall at (19,37). The flat bottom wall is a
  standalone line joined to the rest of the outline (connect), because an
  exact 8 certifies only between plain lines.
- bulb: mirrored about x=24. An r7 semicircle dome (centre (24,22), apex
  y=15) flows tangent-continuous into two S-shaped cubic tapers that land
  vertically on the neck corners (20,29) and (28,29); a standalone flat
  base line closes it (connect). The neck is 8 wide, the MIC minimum for
  facing edges inside one shape.
Vertical budget: bubble top 6 + 9 (dome apex to a flat wall: an exact 8
against a curve cannot certify) + bulb 14 + 8 (flat base to flat bottom
wall) = 37, the bubble's bottom wall; the tail keeps the last 5 units.

Metric issues fixed:
- clearance (error, e0/e1 4.67 apart): the generated image's separate
  screw-cap band sat 4.67 from the bubble's bottom edge. The band is
  dropped; the bulb's flat base sits exactly 8 from the bottom wall, the
  tail's return point (19,37) is kept off the neck corner, and every other
  gap is >= 8.
- stroke-width (info): redrawn at stroke 4 with every gap sized for it.
- T-junctions (cap band meeting the neck): gone with the band; the base
  shares both endpoints with the bulb outline.
Not kept: the cap band. A band line across the neck needs a hole of 8 on
centerlines below it, and the bubble's 31-unit interior (after the 9 and 8
gaps) leaves only 14 for the whole bulb.

Lucide: lightbulb (round dome, S-taper into a narrow neck) and
message-square (tail dropping from the lower-left corner) informed the
construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "33b77e00-f537-4f70-8180-1310be0dbea9"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260930-1539-idea-speech-bubble-solo/"
    "idea-speech-bubble-solo_raw.svg"
)
AUTHOR = "claude-opus-5-5"

L, R, T, B = 6, 42, 6, 37   # bubble body walls
CR = 8                      # bubble corner radius
TAIL_X, TAIL_TIP_Y, TAIL_END_X = 14, 42, 19

AXIS = 24
DOME_R, DOME_CY = 7, 22     # apex y=15
NECK_HALF, BASE_Y = 4, 29    # neck walls 8 apart (MIC)


class IdeaSpeechBubbleSoloRedraw(Solo48):
    icon_id = "idea-speech-bubble-solo-redraw"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ("idea-message", "lightbulb-speech-bubble")
    keywords = ("idea", "lightbulb", "speech bubble", "message", "chat",
                "suggestion", "tip", "thought")

    def build(self) -> None:
        # Bubble, clockwise from the top-left corner.
        self.add_line("top", (L + CR, T), (R - CR, T))
        self.add_arc("tr", (R - CR, T), (R, T + CR), radius_x=CR, sweep=True)
        self.add_line("right", (R, T + CR), (R, B - CR))
        self.add_arc("br", (R, B - CR), (R - CR, B), radius_x=CR, sweep=True)
        self.add_line("bottom", (R - CR, B), (TAIL_END_X, B))
        self.add_line("tail-diag", (TAIL_END_X, B), (TAIL_X, TAIL_TIP_Y))
        self.add_line("tail-drop", (TAIL_X, TAIL_TIP_Y), (TAIL_X, B))
        self.add_arc("bl", (TAIL_X, B), (L, B - CR), radius_x=CR, sweep=True)
        self.add_line("left", (L, B - CR), (L, T + CR))
        self.add_arc("tl", (L, T + CR), (L + CR, T), radius_x=CR, sweep=True)
        # The flat bottom wall is its own line: an exact 8 to the bulb's flat
        # base certifies only between plain lines, not inside arc contours.
        self.add_contour("bubble", "tail-diag", "tail-drop", "bl", "left",
                         "tl", "top", "tr", "right", "br")
        self.relate("connect", "bottom", "bubble")

        # Bulb, mirrored about x=24: an r7 dome flowing through S-tapers
        # straight into the neck corners, closed by a flat base line.
        xl, xr = AXIS - DOME_R, AXIS + DOME_R
        nl, nr = AXIS - NECK_HALF, AXIS + NECK_HALF
        self.add_bezier("taper-l", (nl, BASE_Y),
                        ((nl, BASE_Y - 3), (xl, DOME_CY + 3), (xl, DOME_CY)))
        self.add_arc("dome", (xl, DOME_CY), (xr, DOME_CY),
                     radius_x=DOME_R, sweep=True)
        self.add_bezier("taper-r", (xr, DOME_CY),
                        ((xr, DOME_CY + 3), (nr, BASE_Y - 3), (nr, BASE_Y)))
        self.add_contour("bulb", "taper-l", "dome", "taper-r")
        self.add_line("base", (nr, BASE_Y), (nl, BASE_Y))
        self.relate("connect", "base", "bulb")
