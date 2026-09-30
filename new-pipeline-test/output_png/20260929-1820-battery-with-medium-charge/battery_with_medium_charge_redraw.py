"""battery-with-medium-charge (redraw of the new-pipeline traced SVG).

Plan: a wide battery on HRECT_M (centerline box (4,10)-(44,38)), mirrored
across y=24.
- case: rounded rectangle (4,10)-(36,38), corner radius 4, one closed contour
  of four lines and four quarter arcs (tangent joins).
- terminal: Lucide battery construction, a detached vertical stroke at x=44
  (y 20..28), 8 right of the case wall; it sets the right extreme.
- charge: a three-slot series inside the case at x = 13, 21, (29); medium
  charge fills the first two, so bars at x=13 and x=21 (y 19..29), 8 apart and
  9 from the case walls (the case contour has arcs, so an exact 8 against it
  cannot be certified), and the right half of the cell stays empty.
Extremes: x 4 (case) / 44 (terminal), y 10 / 38 (case).

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4; every gap re-budgeted for it.
- keyshape-short-axis: the case now spans the full 28 on y (10..38) instead of
  the trace's 67%, so every HRECT_M extreme lies on its box.
- clearance e1/e2 and e1/e3 (bars 4 from the top wall): bars now end 9 from
  the top and bottom walls (y 19..29).
- clearance e2/e3 (bars 6.3 apart): bars now 8 apart (x 13 and 21).
Deliberate change: the trace's hollow rounded terminal nub would enclose a
4-unit hole at stroke 4 (below the 6 minimum), so it becomes Lucide's single
detached terminal stroke.
Lucide: battery / battery-medium informed the rounded case, detached
terminal and evenly spaced charge bars.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "e4492a9c-8c97-4b9a-9c29-d08262d7e796"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1820-battery-with-medium-charge/battery-with-medium-charge_raw.svg"
AUTHOR = "claude-opus-5-5"

X0, X1, Y0, Y1 = 4, 36, 10, 38   # case centerline box
R = 4                            # case corner radius
TERM_X, TERM_H = 44, 4           # terminal x, half height about y=24
CY = (Y0 + Y1) // 2              # 24, mirror axis
BAR_X = (13, 21)                 # two of three slots (13, 21, 29)
BAR_Y0, BAR_Y1 = Y0 + 9, Y1 - 9  # 19..29


class BatteryWithMediumChargeRedraw(Solo48):
    icon_id = "battery-with-medium-charge-redraw"
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "devices"
    aliases = ("battery-medium", "half-battery")
    keywords = ("battery", "medium", "charge", "power", "energy", "level")

    def build(self) -> None:
        corners = [
            ((X0 + R, Y0), (X1 - R, Y0), (X1, Y0 + R)),
            ((X1, Y0 + R), (X1, Y1 - R), (X1 - R, Y1)),
            ((X1 - R, Y1), (X0 + R, Y1), (X0, Y1 - R)),
            ((X0, Y1 - R), (X0, Y0 + R), (X0 + R, Y0)),
        ]
        members = []
        for i, (a, b, c) in enumerate(corners):
            self.add_line(f"case-side-{i}", a, b)
            self.add_arc(f"case-corner-{i}", b, c, radius_x=R, radius_y=R, sweep=True)
            members += [f"case-side-{i}", f"case-corner-{i}"]
        self.add_contour("case", *members, closed=True)

        self.add_line("terminal", (TERM_X, CY - TERM_H), (TERM_X, CY + TERM_H))

        for x in BAR_X:
            self.add_line(f"charge-{x}", (x, BAR_Y0), (x, BAR_Y1))
