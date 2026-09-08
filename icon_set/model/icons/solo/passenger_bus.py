"""Side-profile passenger bus reconstructed on SOLO48.

The reference contributes the long body, raked nose, window band and two
wheels.  Small vehicle furniture is deliberately omitted so those four reads
remain open under the SOLO48 stroke and clearance rules.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'astra-chatgpt'


class PassengerBus(Solo48):
    icon_id = "passenger-bus"
    keyshape = Keyshape.HRECT_M
    category = "objects/transport"
    aliases = ("bus", "public-transport-passenger-bus", "transit-bus")
    keywords = (
        "bus", "transport", "transit", "vehicle", "travel", "coach",
        "passenger", "public transport",
    )

    def build(self) -> None:
        # HRECT_M's centreline envelope is (2,11)-(46,37).  The upper body
        # supplies the first three extremes and the wheel bottoms supply the
        # fourth.  The upper wheel semicircles are part of the body contour,
        # cutting clean wheel openings in its lower rail; the lower halves
        # then complete the two wheels without drawing a rail through them.
        self.add_line("roof-left", (6, 11), (16, 11))
        self.add_line("roof-middle", (16, 11), (30, 11))
        self.add_line("roof-right", (30, 11), (40, 11))
        self.add_line("nose-shoulder", (40, 11), (43, 12))
        self.add_line("windscreen-upper", (43, 12), (45, 22))
        self.add_line("windscreen-lower", (45, 22), (46, 27))
        self.add_line("nose-side", (46, 27), (46, 29))
        self.add_arc("corner-front-lower", (46, 29), (42, 33), radius_x=4)
        self.add_line("rail-rear-wheel", (42, 33), (39, 33))
        self.add_arc(
            "wheel-rear-upper", (39, 33), (31, 33), radius_x=4, sweep=False
        )
        self.add_line("rail-between-wheels", (31, 33), (17, 33))
        self.add_arc(
            "wheel-front-upper", (17, 33), (9, 33), radius_x=4, sweep=False
        )
        self.add_line("rail-front-wheel", (9, 33), (6, 33))
        self.add_arc("corner-rear-lower", (6, 33), (2, 29), radius_x=4)
        self.add_line("rear-side", (2, 29), (2, 15))
        self.add_arc("corner-rear-upper", (2, 15), (6, 11), radius_x=4)
        self.add_contour(
            "body",
            "roof-left", "roof-middle", "roof-right", "nose-shoulder",
            "windscreen-upper", "windscreen-lower", "nose-side",
            "corner-front-lower", "rail-rear-wheel", "wheel-rear-upper",
            "rail-between-wheels", "wheel-front-upper", "rail-front-wheel",
            "corner-rear-lower", "rear-side", "corner-rear-upper",
            closed=True,
        )

        self.add_arc(
            "wheel-front-lower", (9, 33), (17, 33), radius_x=4, sweep=False
        )
        self.add_arc(
            "wheel-rear-lower", (31, 33), (39, 33), radius_x=4, sweep=False
        )
        self.relate("connect", "body", "wheel-front-lower")
        self.relate("connect", "body", "wheel-rear-lower")

        # A single waist rail separates body and glazing.  Two dividers make
        # three broad panes; their endpoints coincide with split roof members
        # and the waist rail so every attachment is explicit and provable.
        self.add_line("window-waist", (2, 22), (45, 22))
        self.add_line("window-divider-left", (16, 11), (16, 22))
        self.add_line("window-divider-right", (30, 11), (30, 22))
        self.relate("connect", "body", "window-waist")
        self.relate("connect", "body", "window-divider-left")
        self.relate("connect", "body", "window-divider-right")
        self.relate("connect", "window-waist", "window-divider-left")
        self.relate("connect", "window-waist", "window-divider-right")
