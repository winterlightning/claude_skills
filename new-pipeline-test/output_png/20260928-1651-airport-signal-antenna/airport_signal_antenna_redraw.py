"""airport-signal-antenna (redraw of the new-pipeline traced SVG).

Subject: an airport signal antenna -- a tall mast on a short ground bar,
topped by a small ring, with one radio-wave arc on each side of the ring.

Plan (mirrored about x=24): VRECT_M, centerline box (10,4)-(38,44), as the
metrics suggest (best score, matches the "tall" hint).
Extremes: x=10 / x=38 wave apexes, y=4 wave tops, y=44 ground bar.
- ring: circle r=5 about (24,13) -> 6 inscribed hole. Built as two
  semicircles split at the bottom point (24,18), where the mast attaches.
- mast: (24,18)-(24,44), shares the ring's bottom point and the bar's centre.
- ground bar: (17,44)-(31,44), split at the mast foot (T-junction).
- waves: one repeat definition, r=15 about a centre 1 inside the ring centre
  ((25,13) left / (23,13) right). Endpoints on the 9-12-15 triple so the
  apex lands on x=10 / 38 and the tips on y=4 / 22. The ring is 9 away
  (a curved pair exactly on 8 cannot be certified); the wave tips are 11
  from the mast.
Reference: generated PNG read for the subject only; Lucide `radio-tower`
/ `radio` style for the signal arcs (integer-centred arcs, round caps).
No coordinates copied from the trace.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4, every gap budgeted at 8.
- keyshape-short-axis (x fills 86%): waves widened to reach x=10 and 38
  exactly; y runs exactly 4 (wave tops) to 44 (bar). No stretch.
- clearance e0/e2 and e1/e2 (waves vs ring, 7.3): waves now clear the ring
  by 9 on centerlines.
- hole [24.0,11.3] (4.24 wide): ring radius 5 -> 6 inscribed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "58573359-f61e-52a8-b710-7818357fd8e0"
SOURCE_PATH = "new-pipeline-test/output_png/20260928-1651-airport-signal-antenna/airport-signal-antenna_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24             # mirror axis / mast
CY = 13             # ring and wave centre line
RING_R = 5          # 6 inscribed hole at stroke 4
GROUND_Y = 44
BAR_HALF = 7
WAVE_R = 15
WAVE_IN = 1         # wave centre sits this far inside the ring centre
WAVE_LEG = (12, 9)  # (x, y) legs of the 9-12-15 endpoint triple


class AirportSignalAntennaRedraw(Solo48):
    icon_id = "airport-signal-antenna-redraw"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "travel"
    aliases = ("airport signal", "antenna", "signal antenna", "radio mast")
    keywords = ("airport", "signal", "antenna", "radio", "broadcast", "wireless", "tower", "travel")

    def build(self) -> None:
        top, bottom = (AX, CY - RING_R), (AX, CY + RING_R)

        # Ring: two semicircles split where the mast attaches.
        self.add_arc("ring-l", bottom, top, radius_x=RING_R, sweep=True)
        self.add_arc("ring-r", top, bottom, radius_x=RING_R, sweep=True)
        self.add_contour("ring", "ring-l", "ring-r", closed=True)

        # Mast and ground bar (T-junction at the foot).
        foot = (AX, GROUND_Y)
        self.add_line("mast", bottom, foot)
        self.add_line("bar-l", (AX - BAR_HALF, GROUND_Y), foot)
        self.add_line("bar-r", foot, (AX + BAR_HALF, GROUND_Y))
        self.add_contour("bar", "bar-l", "bar-r")
        self.relate("connect", "mast", "ring")
        self.relate("connect", "mast", "bar")

        # Waves: one mirrored definition about centres just inside the ring.
        leg_x, leg_y = WAVE_LEG
        left_c, right_c = AX + WAVE_IN, AX - WAVE_IN
        self.add_arc(
            "wave-l", (left_c - leg_x, CY - leg_y), (left_c - leg_x, CY + leg_y),
            radius_x=WAVE_R, sweep=False,
        )
        self.add_arc(
            "wave-r", (right_c + leg_x, CY - leg_y), (right_c + leg_x, CY + leg_y),
            radius_x=WAVE_R, sweep=True,
        )
