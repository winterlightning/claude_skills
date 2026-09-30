"""car-intersection-sensor-waves (redraw of the new-pipeline trace).

Plan: a front-facing car with two concentric sensor waves above the roof
(Lucide `car-front` body with the `wifi` arc construction).
- waves: two concentric arcs about W = (24,24), radius 10 and 20, both
  ending on the 3:4 direction, so the ends are integer nodes (18,16)/(30,16)
  and (12,8)/(36,8). The outer apex (24,4) is the keyshape top.
- car outline, one closed contour mirrored about x=24: a trapezoid cabin
  (roof y=25 from x=16 to 32, windshield sides with slope 1:2 down to the
  belt nodes (12,33)/(36,33)), r4 fender corners out to the walls x=8/40,
  the walls down to square wheel tabs (x 8-16 and 32-40, bottom y=44,
  r2 bottom corners) and the body bottom y=41 between the tabs.
- belt: one line (12,33)-(36,33) sharing the cabin/fender nodes; it closes
  the windshield and the body panel.
The roof sits 1 below the wave centre line, so its centre is 11 from the
inner wave and the roof point under each inner wave end is 9 below it. With
the roof on the centre line that pair was exactly 8 (curved pair on the
minimum), which validate_icon returns as review, so the car moved down 1
and the wheel tabs are 3 deep instead of 4.
Vertical budget: wave apexes 4 / 14, inner ends 16, roof 25, belt 33,
bottom 41, tabs 44; roof/belt and belt/bottom are 8 apart, tab walls 8.

Keyshape: VRECT_L instead of the suggested SQUARE (score 1.12 vs 0.92).
The source is taller than wide (aspect 0.87, SQUARE only fills 87% on x),
and the SQUARE height (36) cannot hold waves 8 apart, 8 of clearance to the
roof, a windshield and body panel of 8 each and visible wheel tabs. VRECT_L
gives the 40 units needed; x now fills the full 32 width.

Metric issues fixed:
- stroke-width (info): redrawn at stroke 4, every gap budgeted at 8.
- keyshape-short-axis (x 87%): the car walls sit on x=8/40, the outer wave
  apex on y=4 and the tabs on y=44, exactly the VRECT_L box.
- clearance e0/e1 (5.4) and e1/e3 (3.46): the waves are concentric, 10
  apart, and the inner wave is 9-11 from the roof.
- clearance e0/e3 (7.5): the outer wave ends are 16+ from the cabin.
- holes at (24,15) (3.2 wide, between the waves and the roof) and
  (17.6,23) (5.2 wide, windshield): the waves no longer enclose a pocket
  with the roof, and the windshield is 8 tall (roof to belt) and 16-24 wide.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "ab4d1610-e735-4977-967a-897386cdcc6d"
SOURCE_PATH = "new-pipeline-test/output_png/20260929-1935-car-intersection-sensor-waves/car-intersection-sensor-waves_raw.svg"
AUTHOR = "claude-opus-5-5"

AX = 24                     # mirror axis
WY = 24                     # wave centre y (= roof line)
WAVES = (10, 20)            # concentric radii; ends on the 3:4 direction
L, R = 8, 40                # body walls (VRECT_L x extremes)
ROOF, BELT, BOTTOM, TAB = 25, 33, 41, 44
ROOF_HW = 8                 # roof half-width -> x 16..32
BELT_HW = 12                # windshield foot / fender node -> x 12..36
FENDER = 4                  # fender corner radius (belt node to wall)
TAB_W, TAB_R = 8, 2         # wheel tab width and bottom corner radius


def _mx(x: int) -> int:
    return 2 * AX - x


class CarIntersectionSensorWavesRedraw(Solo48):
    icon_id = "car-intersection-sensor-waves-redraw"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicle"
    aliases = ("connected car", "car sensor", "smart car")
    keywords = ("car", "sensor", "signal", "waves", "intersection", "vehicle", "connected", "wireless")

    def build(self) -> None:
        for i, r in enumerate(WAVES):
            dx, dy = r * 3 // 5, r * 4 // 5
            self.add_arc(f"wave-{i + 1}", (AX - dx, WY - dy), (AX + dx, WY - dy), radius_x=r, sweep=True)

        tab_in = L + TAB_W   # x = 16 (left tab inner wall)
        steps = []           # (id, kind, start, end)
        pts = [
            ("windshield-l", "line", (AX - BELT_HW, BELT), (AX - ROOF_HW, ROOF)),
            ("roof", "line", (AX - ROOF_HW, ROOF), (AX + ROOF_HW, ROOF)),
            ("windshield-r", "line", (AX + ROOF_HW, ROOF), (AX + BELT_HW, BELT)),
            ("fender-r", "arc", (AX + BELT_HW, BELT), (R, BELT + FENDER), FENDER),
            ("wall-r", "line", (R, BELT + FENDER), (R, TAB - TAB_R)),
            ("tab-r-out", "arc", (R, TAB - TAB_R), (R - TAB_R, TAB), TAB_R),
            ("tab-r-bottom", "line", (R - TAB_R, TAB), (_mx(tab_in) + TAB_R, TAB)),
            ("tab-r-in", "arc", (_mx(tab_in) + TAB_R, TAB), (_mx(tab_in), TAB - TAB_R), TAB_R),
            ("tab-r-wall", "line", (_mx(tab_in), TAB - TAB_R), (_mx(tab_in), BOTTOM)),
            ("bottom", "line", (_mx(tab_in), BOTTOM), (tab_in, BOTTOM)),
            ("tab-l-wall", "line", (tab_in, BOTTOM), (tab_in, TAB - TAB_R)),
            ("tab-l-in", "arc", (tab_in, TAB - TAB_R), (tab_in - TAB_R, TAB), TAB_R),
            ("tab-l-bottom", "line", (tab_in - TAB_R, TAB), (L + TAB_R, TAB)),
            ("tab-l-out", "arc", (L + TAB_R, TAB), (L, TAB - TAB_R), TAB_R),
            ("wall-l", "line", (L, TAB - TAB_R), (L, BELT + FENDER)),
            ("fender-l", "arc", (L, BELT + FENDER), (AX - BELT_HW, BELT), FENDER),
        ]
        for ident, kind, start, end, *radius in pts:
            if kind == "line":
                self.add_line(ident, start, end)
            else:
                self.add_arc(ident, start, end, radius_x=radius[0], sweep=True)
            steps.append(ident)
        self.add_contour("car", *steps, closed=True)

        self.add_line("belt", (AX - BELT_HW, BELT), (AX + BELT_HW, BELT))
        self.relate("connect", "belt", "car")
