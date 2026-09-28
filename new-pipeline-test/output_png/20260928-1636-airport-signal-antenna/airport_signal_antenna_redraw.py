"""airport-signal-antenna (redraw of the new-pipeline traced SVG).

Subject: an airport signal antenna -- a wide rounded antenna head split by
the mast, standing on a low trapezoid base, radiating one signal wave on
each side.

Plan (mirrored about x=24): HRECT_L, centerline box (4,8)-(44,40).
Extremes: x=4 / x=44 wave apexes, y=8 wave tops, y=40 base bottom.
- head: stadium, cap radius 5 about (18,17) and (30,17); centerline 22x10
  (outer 26x14, about 2:1 as in the brief). Top and bottom edges split at
  x=24 where the divider meets them; each half-cell is 6 inscribed.
- divider + mast: one axis x=24, divider (24,12)-(24,22) inside the head,
  mast (24,22)-(24,30) down to the base top (split there).
- base: closed trapezoid, top (17,30)-(31,30), bottom (11,40)-(37,40),
  10 tall so its hole is 6 inscribed; its top edge sits 8 below the head's
  straight bottom edge (straight parallel pair).
- waves: one repeat definition, radius 15 about a centre 1 inside the cap
  centre ((19,17) / (29,17)); endpoints on the 9-12-15 triple, so the tops
  land on y=8 and the wave clears the cap by 9 on the axis (a curved pair
  exactly on 8 cannot be certified) while sweeping +/-37 deg.
HRECT_L instead of the suggested SQUARE: with one wave per side the head can
grow to the brief's 2:1 on the 40-wide axis, and HRECT_L fills y exactly
(metrics: HRECT_L fill x 0.93 / y 1.0, the y-stretch warning disappears).
Reference: generated PNG + reference.svg read for the subject only; Lucide
`radio` style for the signal arcs (arcs on integer centres, round caps). No
coordinates copied from the trace.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4, every gap budgeted at 8.
- stroke-count (7 > 6): 6 strokes -- head, divider+mast, base, two waves.
- keyshape-short-axis (y fills 86%): HRECT_L, y runs exactly 8 (wave tops)
  to 40 (base bottom), x exactly 4 to 44 (wave apexes).
- clearance e5/e6 (head vs divider/mast, 6.75): divider and mast share the
  head's split points and are declared connected.
- clearance e0/e5, e1/e5 (outer wave vs head, 5.7): the kept wave clears the
  head cap by 9.
- holes [15.1,14.8] and [26.7,14.8] (1.4 wide): head is 10 tall, cells 6
  inscribed.
- hole [17.1,36.5] (1.8 wide): base is 10 tall, 6 inscribed.

Not fixed as drawn: clearance e0/e2, e1/e3 (3.1, outer vs inner wave) and
e2/e5, e3/e5 (2.7, inner wave vs head). Two waves per side need head
half-width + 8 + 8 on each side; any head with a 6-wide hole is at least 5
half-wide on centerlines, so 2 x (5 + 16 + 1 curve margin) = 44 > the widest
40 budget (HRECT_L). The inner wave on each side was removed (repair
ladder: remove the part, never squeeze).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "58573359-f61e-52a8-b710-7818357fd8e0"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1636-airport-signal-antenna/airport-signal-antenna_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24             # mirror axis / mast
CY = 17             # head centre line
CAP_R = 5           # head cap radius -> head 10 tall on centerlines
CAP_DX = 6          # cap centres at AX -/+ CAP_DX -> head 22 wide
BASE_TOP_Y = 30
BASE_TOP_HALF = 7
BASE_BOTTOM_Y = 40
BASE_BOTTOM_HALF = 13
WAVE_R = 15
WAVE_IN = 1         # wave centre sits this far inside the cap centre
WAVE_LEG = (12, 9)  # (x, y) legs of the 9-12-15 endpoint triple


class AirportSignalAntennaRedraw(Solo48):
    icon_id = "airport-signal-antenna-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    aliases = ("airport signal", "antenna", "signal antenna")
    keywords = ("airport", "signal", "antenna", "radio", "broadcast", "wireless", "travel")

    def build(self) -> None:
        top, bottom = CY - CAP_R, CY + CAP_R
        lx, rx = AX - CAP_DX, AX + CAP_DX

        # Head: stadium, edges split at the divider.
        self.add_line("head-top-l", (lx, top), (AX, top))
        self.add_line("head-top-r", (AX, top), (rx, top))
        self.add_arc("head-cap-r", (rx, top), (rx, bottom), radius_x=CAP_R, sweep=True)
        self.add_line("head-bottom-r", (rx, bottom), (AX, bottom))
        self.add_line("head-bottom-l", (AX, bottom), (lx, bottom))
        self.add_arc("head-cap-l", (lx, bottom), (lx, top), radius_x=CAP_R, sweep=True)
        self.add_contour(
            "head", "head-top-l", "head-top-r", "head-cap-r",
            "head-bottom-r", "head-bottom-l", "head-cap-l", closed=True,
        )

        # Divider continuing down as the mast.
        self.add_line("divider", (AX, top), (AX, bottom))
        self.add_line("mast", (AX, bottom), (AX, BASE_TOP_Y))
        self.relate("connect", "divider", "head")
        self.relate("connect", "mast", "head")
        self.relate("connect", "divider", "mast")

        # Base: trapezoid, top edge split at the mast foot.
        tl, tr = (AX - BASE_TOP_HALF, BASE_TOP_Y), (AX + BASE_TOP_HALF, BASE_TOP_Y)
        bl, br = (AX - BASE_BOTTOM_HALF, BASE_BOTTOM_Y), (AX + BASE_BOTTOM_HALF, BASE_BOTTOM_Y)
        self.add_line("base-top-l", tl, (AX, BASE_TOP_Y))
        self.add_line("base-top-r", (AX, BASE_TOP_Y), tr)
        self.add_line("base-side-r", tr, br)
        self.add_line("base-bottom", br, bl)
        self.add_line("base-side-l", bl, tl)
        self.add_contour(
            "base", "base-top-l", "base-top-r", "base-side-r", "base-bottom", "base-side-l",
            closed=True,
        )
        self.relate("connect", "mast", "base")

        # Waves: one mirrored definition about centres just inside the caps.
        leg_x, leg_y = WAVE_LEG
        left_c, right_c = lx + WAVE_IN, rx - WAVE_IN
        self.add_arc(
            "wave-l", (left_c - leg_x, CY - leg_y), (left_c - leg_x, CY + leg_y),
            radius_x=WAVE_R, sweep=False,
        )
        self.add_arc(
            "wave-r", (right_c + leg_x, CY - leg_y), (right_c + leg_x, CY + leg_y),
            radius_x=WAVE_R, sweep=True,
        )
