"""airport-signal-antenna (redraw of the new-pipeline traced SVG).

Subject: an airport signal antenna -- a wide rounded radar panel on a
vertical mast with a short foot, and one signal arc on each side.

Plan (mirrored about x=24): HRECT_M, centerline box (4,10)-(44,38).
The metrics suggested SQUARE, but its y axis only fills 60% (stretch 1.68);
HRECT_M ties on score and needs only 1.17, so the wide subject keeps its
proportions instead of being inflated vertically.
Extremes: x=4 / x=44 wave apexes, y=10 wave tips, y=38 foot.
- panel: rounded rect (14,11)-(34,21), corner radius 2, one closed contour.
  The bottom edge is split at (24,21) where the mast attaches. Inner opening
  16x6 -> 6 inscribed.
- mast: (24,21)-(24,38), shares the panel's bottom midpoint and the foot's
  centre (T-junctions, both declared).
- foot: (19,38)-(29,38), split at the mast foot.
- waves: one repeat definition, r=10 about the panel's side centres
  (14,16) / (34,16), endpoints on the 6-8-10 triple so the apex lands on
  x=4 / 44 and the tips on y=10 / 22. Apex to panel side is 10 on
  centerlines; tip to panel corner ~8.4.
Reference: generated PNG read for the subject only; Lucide `radio` style for
the side arcs (integer-centred arcs, round caps). No trace coordinates copied.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4, every gap budgeted at 8.
- keyshape-short-axis (SQUARE y fills 60%): switched to HRECT_M; ink now
  reaches all four edges exactly (x 4/44 waves, y 10 tips, y 38 foot).
- clearance e0/e2 and e1/e2 (waves vs panel, 3.9): waves now clear the
  panel by >= 8 on centerlines.
- holes [8.4,17.7] and [39.5,17.2] (slivers between waves and panel): gone,
  the waves no longer touch the panel.
- hole [13.9,18.1] (panel interior 2.2 wide): panel is 10 tall on
  centerlines, giving a 6-inscribed opening.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "58573359-f61e-52a8-b710-7818357fd8e0"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1816-airport-signal-antenna/airport-signal-antenna_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24             # mirror axis / mast
CY = 16             # panel and wave centre line
PANEL_HALF_W = 10   # panel x 14..34
PANEL_HALF_H = 5    # panel y 11..21
CORNER_R = 2
FOOT_Y = 38
FOOT_HALF = 5
WAVE_R = 10
WAVE_LEG = (8, 6)   # (x, y) legs of the 6-8-10 endpoint triple


class AirportSignalAntennaRedraw(Solo48):
    icon_id = "airport-signal-antenna-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    aliases = ("airport signal", "antenna", "radar antenna", "signal antenna")
    keywords = ("airport", "signal", "antenna", "radar", "broadcast", "wireless", "travel")

    def build(self) -> None:
        left, right = AX - PANEL_HALF_W, AX + PANEL_HALF_W
        top, bottom = CY - PANEL_HALF_H, CY + PANEL_HALF_H
        r = CORNER_R
        joint = (AX, bottom)

        # Panel: clockwise rounded rect, bottom edge split at the mast joint.
        self.add_line("p-bottom-l", joint, (left + r, bottom))
        self.add_arc("p-bl", (left + r, bottom), (left, bottom - r), radius_x=r)
        self.add_line("p-left", (left, bottom - r), (left, top + r))
        self.add_arc("p-tl", (left, top + r), (left + r, top), radius_x=r)
        self.add_line("p-top", (left + r, top), (right - r, top))
        self.add_arc("p-tr", (right - r, top), (right, top + r), radius_x=r)
        self.add_line("p-right", (right, top + r), (right, bottom - r))
        self.add_arc("p-br", (right, bottom - r), (right - r, bottom), radius_x=r)
        self.add_line("p-bottom-r", (right - r, bottom), joint)
        self.add_contour(
            "panel", "p-bottom-l", "p-bl", "p-left", "p-tl", "p-top",
            "p-tr", "p-right", "p-br", "p-bottom-r", closed=True,
        )

        # Mast and foot (T-junctions at both ends).
        foot = (AX, FOOT_Y)
        self.add_line("mast", joint, foot)
        self.add_line("foot-l", (AX - FOOT_HALF, FOOT_Y), foot)
        self.add_line("foot-r", foot, (AX + FOOT_HALF, FOOT_Y))
        self.add_contour("foot", "foot-l", "foot-r")
        self.relate("connect", "mast", "panel")
        self.relate("connect", "mast", "foot")

        # Waves: one mirrored definition centred on the panel sides.
        leg_x, leg_y = WAVE_LEG
        self.add_arc(
            "wave-l", (left - leg_x, CY - leg_y), (left - leg_x, CY + leg_y),
            radius_x=WAVE_R, sweep=False,
        )
        self.add_arc(
            "wave-r", (right + leg_x, CY - leg_y), (right + leg_x, CY + leg_y),
            radius_x=WAVE_R, sweep=True,
        )
