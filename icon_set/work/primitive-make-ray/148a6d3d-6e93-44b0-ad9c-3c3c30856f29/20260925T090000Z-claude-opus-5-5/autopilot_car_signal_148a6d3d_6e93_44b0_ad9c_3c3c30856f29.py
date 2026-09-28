"""Autopilot car signal: a domed pod car with a roof beacon broadcasting signal arcs.

Symbol plan: mirrored about x=24. Two full-circle wheels (radius 4) at the
bottom corners, as in the reference. The body is one closed contour: two
quarter ellipses (rx 11, ry 14) rise from the wheel tops to an upright
half-ellipse beacon bump (rx 3, ry 5); a flat underside joins the wheels' inner points, and each wheel's
upper-inner quarter closes the body. The rest of each wheel is a separate arc
sharing both endpoints. One signal arc on each side is centred inside the
beacon (radius 13, 5-12-13 endpoints), flanking it above the narrowed dome.
Dropped: the reference's inner signal arcs and the round window with its sill
line -- no 8-unit clearance remains inside the dome or between arc pairs.
Lucide: `car` wheels-on-underside idea and `radio` arcs.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "148a6d3d-6e93-44b0-ad9c-3c3c30856f29"
SOURCE_PATH = "icon_set/work/todo-references/auto pilot car signal 1_148a6d3d-6e93-44b0-ad9c-3c3c30856f29.svg"
AUTHOR = "claude-opus-5-5"

CX = 24
WHEEL_R, WHEEL_Y, WHEEL_DX = 4, 38, 14          # wheel centres (24 +- 14, 38)
DOME_RX, DOME_RY = 11, 14
BEACON_RX, BEACON_RY = 3, 5                  # upright siren bump
SIG_Y = 18                                   # signal centre, just inside the beacon
SIG_R = 13
SIG_NEAR, SIG_FAR = (12, 5), (5, 12)             # 5-12-13 endpoints from the beacon centre


class AutopilotCarSignal(Solo48):
    icon_id = "autopilot-car-signal"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transport/vehicle"
    aliases = ("autonomous pod signal", "self-driving car beacon", "robot car signal")
    keywords = ("autopilot", "autonomous", "self-driving", "car", "signal", "beacon", "connected")

    def build(self) -> None:
        base = WHEEL_Y - WHEEL_R                   # dome feet sit on the wheel tops
        top = base - DOME_RY
        wl, wr = CX - WHEEL_DX, CX + WHEEL_DX
        bl, br = (CX - BEACON_RX, top), (CX + BEACON_RX, top)

        self.add_arc("dome-left", (wl, base), bl, radius_x=DOME_RX, radius_y=DOME_RY, sweep=True)
        self.add_arc("beacon", bl, br, radius_x=BEACON_RX, radius_y=BEACON_RY, sweep=True)
        self.add_arc("dome-right", br, (wr, base), radius_x=DOME_RX, radius_y=DOME_RY, sweep=True)
        self.add_arc("wheel-front-inner", (wr, base), (wr - WHEEL_R, WHEEL_Y), radius_x=WHEEL_R, radius_y=WHEEL_R, sweep=False)
        self.add_line("underside", (wr - WHEEL_R, WHEEL_Y), (wl + WHEEL_R, WHEEL_Y))
        self.add_arc("wheel-rear-inner", (wl + WHEEL_R, WHEEL_Y), (wl, base), radius_x=WHEEL_R, radius_y=WHEEL_R, sweep=False)
        self.add_contour(
            "body", "dome-left", "beacon", "dome-right", "wheel-front-inner",
            "underside", "wheel-rear-inner", closed=True,
        )
        self.add_arc("wheel-front", (wr, base), (wr - WHEEL_R, WHEEL_Y), radius_x=WHEEL_R, radius_y=WHEEL_R, large_arc=True, sweep=True)
        self.add_arc("wheel-rear", (wl + WHEEL_R, WHEEL_Y), (wl, base), radius_x=WHEEL_R, radius_y=WHEEL_R, large_arc=True, sweep=True)
        self.relate("connect", "wheel-front", "dome-right", "wheel-front-inner", "underside")
        self.relate("connect", "wheel-rear", "dome-left", "wheel-rear-inner", "underside")

        (nx, ny), (fx, fy) = SIG_NEAR, SIG_FAR
        self.add_arc("signal-left", (CX - nx, SIG_Y - ny), (CX - fx, SIG_Y - fy), radius_x=SIG_R, radius_y=SIG_R, sweep=True)
        self.add_arc("signal-right", (CX + fx, SIG_Y - fy), (CX + nx, SIG_Y - ny), radius_x=SIG_R, radius_y=SIG_R, sweep=True)
