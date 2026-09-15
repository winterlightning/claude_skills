"""Gabled shack with a single vertical door mark. SQUARE retains the roof and walls; Lucide house informs the coherent wall contour."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd9c0657-6aff-57d0-8690-7456cf464da0'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/shanty house_cd9c0657-6aff-57d0-8690-7456cf464da0.svg'
AUTHOR = 'gpt-6'

class SimpleGabledShack(Solo48):
    icon_id = 'simple-gabled-shack'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('shack', 'house', 'home', 'shanty', 'hut', 'dwelling', 'shelter', 'gable')

    def build(self) -> None:
        self.add_polyline('roof', (6, 20), (8, 15), (24, 6), (40, 15), (42, 20))
        self.add_line('wall-right', (40, 15), (40, 42))
        self.add_bezier('corner-right', (40, 42), *(((38.76239569, 42), (37.23760431, 42), (36, 42)),))
        self.add_line('floor-right', (36, 42), (31, 42))
        self.add_line('floor-mid-1', (31, 42), (24, 42))
        self.add_line('floor-mid-2', (24, 42), (17, 42))
        self.add_line('floor-left', (17, 42), (12, 42))
        self.add_bezier('corner-left', (12, 42), *(((10.76239569, 42), (9.23760431, 42), (8, 42)),))
        self.add_line('wall-left', (8, 42), (8, 15))
        self.add_contour('walls', 'wall-right', 'corner-right', 'floor-right', 'floor-mid-1', 'floor-mid-2', 'floor-left', 'corner-left', 'wall-left')
        self.add_line('door', (24, 42), (24, 30))
        self.relate('connect', 'door', 'walls')
        self.relate('connect', 'roof', 'walls')
