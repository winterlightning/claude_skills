"""A plain desktop monitor with a blank rounded display and centered stand.

HRECT_L extrema (4,8)-(44,40). The screen is one rounded enclosure;
the support stem and foot share x=24. Lucide monitor supplies the stand.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "7970e882-268e-4442-bf17-d8c99a844271"
SOURCE_PATH = "pictographic-primitives/_uncategorized_14/desktop monitor_7970e882-268e-4442-bf17-d8c99a844271.svg"
AUTHOR = "gpt-6"


class ComputerMonitorDisplayScreen(Solo48):
    icon_id = "computer-monitor-display-screen"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/displays"
    aliases = ("desktop monitor", "computer screen")
    keywords = ("desktop", "display", "screen", "computer")

    def build(self) -> None:
        self.add_line("screen-top", (8, 8), (40, 8))
        self.add_arc("screen-ne", (40, 8), (44, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line("screen-right", (44, 12), (44, 28))
        self.add_arc("screen-se", (44, 28), (40, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_line("screen-bottom", (40, 32), (8, 32))
        self.add_arc("screen-sw", (8, 32), (4, 28), radius_x=4, radius_y=4, sweep=True)
        self.add_line("screen-left", (4, 28), (4, 12))
        self.add_arc("screen-nw", (4, 12), (8, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_contour("screen", "screen-top", "screen-ne", "screen-right", "screen-se", "screen-bottom", "screen-sw", "screen-left", "screen-nw", closed=True)
        self.add_line("stand", (24, 32), (24, 40))
        self.add_line("foot", (16, 40), (32, 40))
        self.relate("connect", "stand", "screen")
        self.relate("connect", "stand", "foot")
