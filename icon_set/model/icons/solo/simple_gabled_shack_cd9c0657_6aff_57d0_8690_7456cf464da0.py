"""A single gabled shack with overhanging eaves, rounded lower corners and central doorway. Lucide house informs continuous walls and tangent corner arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd9c0657-6aff-57d0-8690-7456cf464da0'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/shanty house_cd9c0657-6aff-57d0-8690-7456cf464da0.svg'
AUTHOR = 'gpt-6'


class SimpleGabledShack(Solo48):
    icon_id = 'simple-gabled-shack'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "places/landmarks"
    aliases = ()
    keywords = ('shack', 'house', 'home', 'shanty', 'hut', 'dwelling', 'shelter', 'gable')

    def build(self) -> None:
        # Centerline extremes (2,2)-(46,46).
        self.add_polyline("roof", (2,20), (8,15), (24,2), (40,15), (46,20))
        self.add_line("wall-right", (40,15), (40,42))
        self.add_arc("corner-right", (40,42), (36,46), radius_x=4)
        self.add_line("floor-right", (36,46), (31,46))
        self.add_line("floor-mid", (31,46), (17,46))
        self.add_line("floor-left", (17,46), (12,46))
        self.add_arc("corner-left", (12,46), (8,42), radius_x=4)
        self.add_line("wall-left", (8,42), (8,15))
        self.add_contour("walls", "wall-right", "corner-right", "floor-right", "floor-mid", "floor-left", "corner-left", "wall-left")
        self.add_polyline("door", (17,46), (17,30), (31,30), (31,46))
        self.relate("connect", "door", "walls")
        self.relate("connect", "roof", "walls")
