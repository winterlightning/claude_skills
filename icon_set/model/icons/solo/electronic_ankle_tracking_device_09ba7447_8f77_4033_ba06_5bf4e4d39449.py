"""A foot and lower leg wearing a tracker with bilateral radio waves."""

from ...keyshapes import Keyshape
from ._base import Solo48


SOURCE_ICON_ID = "09ba7447-8f77-4033-ba06-5bf4e4d39449"
SOURCE_PATH = "pictographic-primitives/_uncategorized_03/ankle tracker_09ba7447-8f77-4033-ba06-5bf4e4d39449.svg"
AUTHOR = "gpt-5"


class ElectronicAnkleTrackingDevice(Solo48):
    icon_id = "electronic-ankle-tracking-device"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/wearables"
    aliases = ("ankle-tracker-with-radio-waves", "ankle-monitor")
    keywords = ("tracker", "ankle", "foot", "wearable", "signal", "monitor")

    def build(self) -> None:
        # Plan: a rounded tracker owns four exact attachment nodes for the two
        # upper-leg runs and the continuous lower foot contour. Mirrored radio
        # arcs remain detached with nine-unit endpoint clearance.
        self.add_line("leg-left", (20, 6), (20, 14))
        self.add_line("leg-right", (28, 6), (28, 14))

        self.add_line("tracker-top", (20, 14), (28, 14))
        self.add_arc("tracker-top-right", (28, 14), (31, 17), radius_x=3)
        self.add_line("tracker-right", (31, 17), (31, 25))
        self.add_arc("tracker-bottom-right", (31, 25), (28, 28), radius_x=3)
        self.add_line("tracker-bottom", (28, 28), (20, 28))
        self.add_arc("tracker-bottom-left", (20, 28), (17, 25), radius_x=3)
        self.add_line("tracker-left", (17, 25), (17, 17))
        self.add_arc("tracker-top-left", (17, 17), (20, 14), radius_x=3)
        self.add_contour(
            "tracker",
            "tracker-top",
            "tracker-top-right",
            "tracker-right",
            "tracker-bottom-right",
            "tracker-bottom",
            "tracker-bottom-left",
            "tracker-left",
            "tracker-top-left",
            closed=True,
        )
        self.relate("connect", "tracker-top", "leg-left")
        self.relate("connect", "tracker-top", "leg-right")

        self.add_polyline(
            "foot-outline",
            (20, 28),
            (20, 32),
            (18, 36),
            (8, 42),
            (16, 42),
            (24, 38),
            (34, 40),
            (38, 38),
            (36, 34),
            (28, 28),
        )
        self.relate("connect", "tracker-bottom", "foot-outline")

        self.add_arc("signal-left", (8, 20), (8, 24), radius_x=2, sweep=False)
        self.add_arc("signal-right", (40, 24), (40, 20), radius_x=2, sweep=False)
