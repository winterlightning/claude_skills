"""A location pin suspended above a three-panel folded map.

Plan: the pin has one oval crown, converging sides, and a central mark;
the map is a three-panel zigzag with fold positions shared top to bottom.
Lucide map-pin informed the pin silhouette; Lucide map informed the folds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "7c2df1dc-523f-47e8-98ed-1291ecbe59b3"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/map location_7c2df1dc-523f-47e8-98ed-1291ecbe59b3.svg"
AUTHOR = "gpt-6"


class FoldedMapWithLocationPin(Solo48):
    icon_id = "folded-map-with-location-pin"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/maps"
    aliases = ("map-location",)
    keywords = ("folded", "map", "location", "pin", "navigation")

    def build(self) -> None:
        self.add_arc("pin-crown", (10, 14), (38, 14), radius_x=14, radius_y=10, sweep=True)
        self.add_line("pin-right", (38, 14), (24, 24))
        self.add_line("pin-left", (24, 24), (10, 14))
        self.add_contour("pin", "pin-crown", "pin-right", "pin-left", closed=True)
        self.add_dot("pin-center", (24, 14))
        self.add_polyline("map", (8, 32), (18, 34), (30, 32),
                          (40, 34), (40, 44), (30, 42),
                          (18, 44), (8, 42), closed=True)
        self.add_line("fold-left", (18, 34), (18, 44))
        self.add_line("fold-right", (30, 32), (30, 42))
        self.relate("connect", "fold-left", "map")
        self.relate("connect", "fold-right", "map")
