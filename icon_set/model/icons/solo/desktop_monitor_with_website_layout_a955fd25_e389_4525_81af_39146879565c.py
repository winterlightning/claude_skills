"""A monitor showing a two-column page with text and a mountain image.

HRECT_L extrema (4,8)-(44,40). The screen is one rounded enclosure;
the webpage divides at x=24 and y=24. Lucide monitor supplies the stand.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "a955fd25-e389-4525-81af-39146879565c"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/coding apps website monitor image_a955fd25-e389-4525-81af-39146879565c.svg"
AUTHOR = "gpt-6"


class DesktopMonitorWithWebsiteLayout(Solo48):
    icon_id = "desktop-monitor-with-website-layout"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("website monitor", "webpage screen")
    keywords = ("desktop", "layout", "image", "text")

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
        self.add_line("column", (24, 8), (24, 24))
        self.add_line("text", (13, 20), (15, 20))
        self.add_polyline("image", (24, 24), (34, 14), (44, 24))
        self.add_line("stand", (24, 32), (24, 40))
        self.add_line("foot", (16, 40), (32, 40))
        for a, b in (("column", "screen"), ("image", "column"), ("image", "screen"), ("stand", "screen"), ("stand", "foot")):
            self.relate("connect", a, b)
