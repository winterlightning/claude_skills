"""A computer monitor displaying code brackets and a slash."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "146cf53e-79f5-4e4e-b1a7-9dd29ba2bf90"
SOURCE_PATH = "pictographic-primitives/other/monitor code 1_146cf53e-79f5-4e4e-b1a7-9dd29ba2bf90.svg"
AUTHOR = "gpt-6"


class ComputerMonitorCode(Solo48):
    icon_id = "computer-monitor-code"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("code monitor", "developer screen")
    keywords = ("computer", "coding", "programming", "display")

    def build(self) -> None:
        # A rounded monitor face with one centerline stand and split foot.
        self.add_line("screen-top", (7, 8), (41, 8))
        self.add_arc("screen-ne", (41, 8), (44, 11), radius_x=3)
        self.add_line("screen-right", (44, 11), (44, 27))
        self.add_arc("screen-se", (44, 27), (41, 30), radius_x=3)
        self.add_line("screen-bottom-right", (41, 30), (24, 30))
        self.add_line("screen-bottom-left", (24, 30), (7, 30))
        self.add_arc("screen-sw", (7, 30), (4, 27), radius_x=3)
        self.add_line("screen-left", (4, 27), (4, 11))
        self.add_arc("screen-nw", (4, 11), (7, 8), radius_x=3)
        self.add_contour("monitor-frame", "screen-top", "screen-ne", "screen-right",
                         "screen-se", "screen-bottom-right", "screen-bottom-left",
                         "screen-sw", "screen-left", "screen-nw", closed=True)
        self.add_line("stand", (24, 30), (24, 40))
        self.add_line("foot-left", (16, 40), (24, 40))
        self.add_line("foot-right", (24, 40), (32, 40))
        self.relate("connect", "stand", "screen-bottom-right")
        self.relate("connect", "stand", "screen-bottom-left")
        self.relate("connect", "stand", "foot-left")
        self.relate("connect", "stand", "foot-right")

        # The three source marks stay distinct across the short screen band.
        self.add_polyline("angle-left", (15, 17), (13, 19), (15, 21))
        self.add_line("slash", (25, 17), (23, 21))
        self.add_polyline("angle-right", (33, 17), (35, 19), (33, 21))
