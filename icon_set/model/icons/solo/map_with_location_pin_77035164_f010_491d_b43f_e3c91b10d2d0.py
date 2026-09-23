"""A central location pin above a divided road map.

Plan: the pin owns a broad arched outline and center mark; an open map
surround holds one crossbar and two repeated lower divisions. The broken top
edge leaves room for the pin. Lucide map-pin and map guided the construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "77035164-f010-491d-b43f-e3c91b10d2d0"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/maps pin_77035164-f010-491d-b43f-e3c91b10d2d0.svg"
AUTHOR = "gpt-6"


class MapWithLocationPin(Solo48):
    icon_id = "map-with-location-pin"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/maps"
    aliases = ("road-map-pin",)
    keywords = ("map", "pin", "road", "location", "navigation")

    def build(self) -> None:
        self.add_arc("pin-crown", (10, 14), (38, 14), radius_x=14, radius_y=10, sweep=True)
        self.add_line("pin-right", (38, 14), (24, 26))
        self.add_line("pin-left", (24, 26), (10, 14))
        self.add_contour("pin", "pin-crown", "pin-right", "pin-left", closed=True)
        self.add_dot("pin-center", (24, 14))
        self.add_polyline("map-surround", (8, 24), (8, 44), (40, 44), (40, 24))
        self.add_line("map-row", (8, 34), (40, 34))
        self.relate("connect", "map-row", "map-surround")
        for index, x in enumerate((18, 30)):
            self.add_line(f"fold-{index}", (x, 34), (x, 44))
            self.relate("connect", f"fold-{index}", "map-row")
            self.relate("connect", f"fold-{index}", "map-surround")
