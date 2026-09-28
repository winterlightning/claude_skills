"""autonomous-domed-car-with-signal (redraw of the new-pipeline traced SVG).

Plan: a long, low side-view car with rounded nose and tail, a dome cabin on
the roofline, two ring wheels hanging from the body, a short roof antenna
and one broad radio arc on each side of the roof. HRECT_L, centerline box
(4,8)-(44,40): nose/tail extremes on x=4 / x=44, antenna tip on y=8, wheel
bottoms on y=40. Everything is mirrored about x=24.
- wheels: circle r5 at (12,35) and (36,35) (6-unit hole), split where the
  body (a 3-4-5 point at (9,31)) and the axle (inner side) attach.
- body: one open contour. The nose is a half circle r5 about (9,26) from
  the wheel join (9,31) through the extreme (4,26) to the shoulder (9,21);
  the shoulder runs flat to the dome foot (17,21), the dome is a half
  circle r7 about (24,21) with its top at (24,14), and the tail mirrors the
  nose back down to the right wheel. Ending the body on the wheel (the
  toy-car construction) keeps the nose off the wheel ring, which a
  vertical end wall at stroke 4 cannot do inside 40 units.
- axle: straight line joining the inner wheel sides, (17,35)-(31,35).
- antenna: (24,14)-(24,8), joined to the dome top.
- signal: one arc per side on the circle of radius sqrt(250) about the dome
  centre (24,21), (11,12)-(15,8) and its mirror (9-13 integer points).
  Concentric with the r7 dome, so it stays ~8.8 clear of the dome, 9 clear
  of the antenna and 9 above the shoulder line.

Metric issues (autonomous-domed-car-with-signal_metrics.json):
- clearance e0/e2, e1/e2 (radio arcs 2.2 from the dome) and e0/e7, e1/e7
  (4.2 from the antenna): fixed, the arcs now sit on the roof's shoulders,
  concentric with the dome, >= 8.8 from dome and antenna.
- clearance e2/e3, e2/e4, e2/e5 and the other dome/body/wheel crowding:
  fixed, the dome sits on the roofline 9 above the wheel tops, there is no
  body line under the dome, and the body meets each wheel at one declared
  junction instead of running along it.
- wheel/hub clearances (e3/e8, e5/e9, e6 underside line): fixed, the hubs
  are dropped (a hub cannot sit 8 inside an r5 wheel and vanishes at 48 px)
  and the underside line became the axle between the wheels.
- holes 0.57 / 2.8 / 3.2 wide: fixed, the slivers between body, wheels and
  underside line are gone; each wheel keeps a 6-unit hole and the cabin and
  body share one large interior.
- stroke-count (10, budget 6): now 6 paths (body, 2 wheels, axle,
  antenna, 2 signal arcs).
- stroke-width (info): redrawn at stroke 4 with every gap budgeted for it.
- keyshape-short-axis (HRECT_M fills 85% of y): switched to HRECT_L. The
  stack wheel (10) + wheel-to-roofline (9) + dome (7) + antenna (6) needs
  32 units; HRECT_M's 28 cannot hold it, HRECT_L is filled exactly.
Not repairable as traced: the "( )" arcs hugging the antenna tip cannot sit
8 from both antenna and dome in 32 units of height, so they moved out onto
the roof shoulders (still one broad arc per side of the antenna). The dome is
smaller than the trace's (r7 vs ~11 wide half-span) for the same reason; a
tried SQUARE layout with a bigger dome read as a bell, not a car.
Lucide `car` informs the wheels hanging from the body with an axle line
between them; Lucide `radio` informs arcs concentric with their source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "148a6d3d-6e93-44b0-ad9c-3c3c30856f29"
SOURCE_PATH = (
    "new-pipeline-test/output_png/20260928-1713-autonomous-domed-car-with-signal/"
    "autonomous-domed-car-with-signal_raw.svg"
)
AUTHOR = "claude-opus-5-5"

AXIS = 24
WHEEL_X = 12             # left wheel centre x (right wheel mirrored)
WHEEL_Y = 35
WHEEL_R = 5
BODY_JOIN = (9, 31)      # (-3, -4) from the wheel centre
NOSE_Y = 26              # nose extreme height
NOSE_LOW_R = 5           # both nose arcs lie on one circle r5 about (9, 26)
NOSE_UP_R = 5
ROOF_Y = 21              # shoulder line = dome base
DOME_RX = 7
DOME_RY = 7
SIGNAL_R = 16            # about the dome centre (24, 21); ends at 250 = 13^2+9^2 = 9^2+13^2
SIGNAL_LOW = (11, 12)
SIGNAL_HIGH = (15, 8)
ANTENNA_TOP = 8


def mirror(p):
    return (2 * AXIS - p[0], p[1])


class AutonomousDomedCarWithSignalRedraw(Solo48):
    icon_id = "autonomous-domed-car-with-signal-redraw"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicles"
    aliases = ("self-driving car", "autonomous car", "connected car", "robotaxi")
    keywords = ("autonomous", "self-driving", "car", "dome", "signal", "antenna",
                "wireless", "vehicle", "connected")

    def wheel(self, name: str, cx: int, join: tuple, axle: tuple) -> None:
        r = WHEEL_R
        top, bottom = (cx, WHEEL_Y - r), (cx, WHEEL_Y + r)
        left, right = (cx - r, WHEEL_Y), (cx + r, WHEEL_Y)
        # Clockwise on screen from the left side, passing the two attachments.
        ring = [left, join, top, right, bottom] if join[0] < cx else [left, top, join, right, bottom]
        ids = []
        for i, a in enumerate(ring):
            b = ring[(i + 1) % len(ring)]
            self.add_arc(f"{name}-{i}", a, b, radius_x=r, sweep=True)
            ids.append(f"{name}-{i}")
        self.add_contour(name, *ids, closed=True)
        assert axle in ring

    def build(self) -> None:
        self.wheel("wheel-left", WHEEL_X, BODY_JOIN, (WHEEL_X + WHEEL_R, WHEEL_Y))
        self.wheel("wheel-right", 2 * AXIS - WHEEL_X, mirror(BODY_JOIN),
                   (2 * AXIS - WHEEL_X - WHEEL_R, WHEEL_Y))

        nose_x = BODY_JOIN[0] - NOSE_LOW_R
        nose = (nose_x, NOSE_Y)
        shoulder = (nose_x + NOSE_UP_R, ROOF_Y)
        foot_l = (AXIS - DOME_RX, ROOF_Y)
        roof = (AXIS, ROOF_Y - DOME_RY)

        # Left half of the body: wheel -> nose -> shoulder -> dome -> roof.
        self.add_arc("nose-low", BODY_JOIN, nose, radius_x=NOSE_LOW_R, sweep=True)
        self.add_arc("nose-up", nose, shoulder, radius_x=NOSE_UP_R, sweep=True)
        self.add_line("shoulder-left", shoulder, foot_l)
        self.add_arc("dome-left", foot_l, roof, radius_x=DOME_RX, radius_y=DOME_RY, sweep=True)
        # Right half mirrored: roof -> dome -> shoulder -> tail -> wheel.
        self.add_arc("dome-right", roof, mirror(foot_l), radius_x=DOME_RX, radius_y=DOME_RY, sweep=True)
        self.add_line("shoulder-right", mirror(foot_l), mirror(shoulder))
        self.add_arc("tail-up", mirror(shoulder), mirror(nose), radius_x=NOSE_UP_R, sweep=True)
        self.add_arc("tail-low", mirror(nose), mirror(BODY_JOIN), radius_x=NOSE_LOW_R, sweep=True)
        self.add_contour(
            "body", "nose-low", "nose-up", "shoulder-left", "dome-left",
            "dome-right", "shoulder-right", "tail-up", "tail-low",
        )
        self.relate("connect", "body", "wheel-left")
        self.relate("connect", "body", "wheel-right")

        self.add_line("axle", (WHEEL_X + WHEEL_R, WHEEL_Y), (2 * AXIS - WHEEL_X - WHEEL_R, WHEEL_Y))
        self.relate("connect", "axle", "wheel-left")
        self.relate("connect", "axle", "wheel-right")

        self.add_line("antenna", roof, (AXIS, ANTENNA_TOP))
        self.relate("connect", "antenna", "body")

        self.add_arc("signal-left", SIGNAL_LOW, SIGNAL_HIGH, radius_x=SIGNAL_R, sweep=True)
        self.add_arc("signal-right", mirror(SIGNAL_HIGH), mirror(SIGNAL_LOW), radius_x=SIGNAL_R, sweep=True)
