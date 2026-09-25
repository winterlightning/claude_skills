"""An irregular mainland outline inside a rounded map tile.

Plan: one symmetric tile frames a deliberately asymmetric coastline.
The coastline keeps broad western and southeastern bulges from the reference.
No Lucide original provides this particular territory silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "9e40b751-30db-44ed-8d7f-6043962fb748"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/mainland_9e40b751-30db-44ed-8d7f-6043962fb748.svg"
AUTHOR = "gpt-6"


class MainlandTerritoryMapIcon(Solo48):
    icon_id = "mainland-territory-map-icon"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("territory-outline",)
    keywords = ("mainland", "map", "region", "geography")

    def build(self) -> None:
        self.add_line("frame-top", (10, 6), (38, 6))
        self.add_arc("frame-ne", (38, 6), (42, 10), radius_x=4, sweep=True)
        self.add_line("frame-right", (42, 10), (42, 38))
        self.add_arc("frame-se", (42, 38), (38, 42), radius_x=4, sweep=True)
        self.add_line("frame-bottom", (38, 42), (10, 42))
        self.add_arc("frame-sw", (10, 42), (6, 38), radius_x=4, sweep=True)
        self.add_line("frame-left", (6, 38), (6, 10))
        self.add_arc("frame-nw", (6, 10), (10, 6), radius_x=4, sweep=True)
        self.add_contour("frame", "frame-top", "frame-ne", "frame-right", "frame-se", "frame-bottom", "frame-sw", "frame-left", "frame-nw", closed=True)
        self.add_polyline("mainland", (22, 15), (26, 15), (29, 15),
                          (32, 16), (30, 20), (32, 23), (33, 25),
                          (31, 29), (33, 32), (29, 33), (25, 32),
                          (21, 33), (17, 30), (15, 30), (16, 25),
                          (15, 22), (17, 19), (19, 16), closed=True)
