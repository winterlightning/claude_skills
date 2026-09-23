"""A folded map with two staggered location markers.

Plan: the map panel has shared fold spacing; two identical teardrop markers
are staggered diagonally, with the right tip meeting the map's upper edge.
Lucide map-pin informed the two pointed silhouettes; Lucide map informed folds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "4a6fa657-5f3d-4ab6-8949-77cda8ee6030"
SOURCE_PATH = "pictographic-primitives/_uncategorized_26/map marks_4a6fa657-5f3d-4ab6-8949-77cda8ee6030.svg"
AUTHOR = "gpt-6"


class MapWithTwoLocationPins(Solo48):
    icon_id = "map-with-two-location-pins"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/maps"
    aliases = ("map-marks",)
    keywords = ("map", "pins", "locations", "route")

    def build(self) -> None:
        for index, (cx, cy, tip_y) in enumerate(((14, 13, 26), (35, 21, 34))):
            self.add_arc(f"pin-crown-{index}", (cx-6, cy), (cx+6, cy),
                         radius_x=6, radius_y=7, sweep=True)
            self.add_line(f"pin-right-{index}", (cx+6, cy), (cx, tip_y))
            self.add_line(f"pin-left-{index}", (cx, tip_y), (cx-6, cy))
            self.add_contour(f"pin-{index}", f"pin-crown-{index}",
                             f"pin-right-{index}", f"pin-left-{index}", closed=True)
        self.add_polyline("map", (6, 34), (18, 34), (26, 34),
                          (35, 34), (42, 34), (42, 42),
                          (26, 42), (18, 42), (6, 42), closed=True)
        for index, x in enumerate((18, 26)):
            self.add_line(f"fold-{index}", (x, 34), (x, 42))
            self.relate("connect", f"fold-{index}", "map")
        self.relate("connect", "pin-1", "map")
