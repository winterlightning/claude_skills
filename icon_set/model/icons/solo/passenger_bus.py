"""Side-profile passenger bus reconstructed on SOLO48.

The reference contributes the long body, raked nose, window band and two
wheels.  Small vehicle furniture is deliberately omitted so those four reads
remain open under the SOLO48 stroke and clearance rules.
"""

from __future__ import annotations

from ...keyshapes import Keyshape
from ._base import Solo48

AUTHOR = 'gpt-6'


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
        self.add_line("roof-left", (8, 8), (16, 8))
        self.add_line("roof-middle", (16, 8), (30, 8))
        self.add_line("roof-right", (30, 8), (40, 8))
        self.add_line("nose-shoulder", (40, 8), (41, 9))
        self.add_line("windscreen-upper", (41, 9), (43, 22))
        self.add_line("windscreen-lower", (43, 22), (44, 30))
        self.add_line("nose-side", (44, 30), (44, 32))
        self.add_arc("corner-front-lower", (44, 32), (40, 36), radius_x=4)
        self.add_line("rail-rear-wheel", (40, 36), (39, 36))
        self.add_arc(
            "wheel-rear-upper", (39, 36), (31, 36), radius_x=4, sweep=False
        )
        self.add_line("rail-between-wheels", (31, 36), (17, 36))
        self.add_arc(
            "wheel-front-upper", (17, 36), (9, 36), radius_x=4, sweep=False
        )
        self.add_line("rail-front-wheel", (9, 36), (8, 36))
        self.add_arc("corner-rear-lower", (8, 36), (4, 32), radius_x=4)
        self.add_line("rear-side", (4, 32), (4, 12))
        self.add_arc("corner-rear-upper", (4, 12), (8, 8), radius_x=4)
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
            "wheel-front-lower", (9, 36), (17, 36), radius_x=4, sweep=False
        )
        self.add_arc(
            "wheel-rear-lower", (31, 36), (39, 36), radius_x=4, sweep=False
        )
        self.relate("connect", "body", "wheel-front-lower")
        self.relate("connect", "body", "wheel-rear-lower")

        # A single waist rail separates body and glazing.  Two dividers make
        # three broad panes; their endpoints coincide with split roof members
        # and the waist rail so every attachment is explicit and provable.
        self.add_line("window-waist", (4, 22), (43, 22))
        self.add_line("window-divider-left", (16, 8), (16, 22))
        self.add_line("window-divider-right", (30, 8), (30, 22))
        self.relate("connect", "body", "window-waist")
        self.relate("connect", "body", "window-divider-left")
        self.relate("connect", "body", "window-divider-right")
        self.relate("connect", "window-waist", "window-divider-left")
        self.relate("connect", "window-waist", "window-divider-right")
