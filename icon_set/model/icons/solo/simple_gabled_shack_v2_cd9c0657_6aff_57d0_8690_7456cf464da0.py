# Variant of simple-gabled-shack; parent file remains unchanged.
"""Gabled shack with a single vertical door mark. SQUARE retains the roof and walls; Lucide house informs the coherent wall contour."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'cd9c0657-6aff-57d0-8690-7456cf464da0'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-06/shanty house_cd9c0657-6aff-57d0-8690-7456cf464da0.svg'
AUTHOR = 'gpt-6'

class SimpleGabledShackVariant2(Solo48):
    icon_id = 'simple-gabled-shack-v2'
    variant_of = 'simple-gabled-shack'
    variant_label = 'Single door line'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('shack', 'house', 'home', 'shanty', 'hut', 'dwelling', 'shelter', 'gable')

    def build(self) -> None:
        self.add_polyline('roof', (2, 20), (8, 15), (24, 2), (40, 15), (46, 20))
        self.add_line('wall-right', (40, 15), (40, 42))
        self.add_arc('corner-right', (40, 42), (36, 46), radius_x=4)
        self.add_line('floor-right', (36, 46), (31, 46))
        self.add_line('floor-mid-1', (31, 46), (24, 46))
        self.add_line('floor-mid-2', (24, 46), (17, 46))
        self.add_line('floor-left', (17, 46), (12, 46))
        self.add_arc('corner-left', (12, 46), (8, 42), radius_x=4)
        self.add_line('wall-left', (8, 42), (8, 15))
        self.add_contour('walls', 'wall-right', 'corner-right', 'floor-right', 'floor-mid-1', 'floor-mid-2', 'floor-left', 'corner-left', 'wall-left')
        self.add_line('door', (24, 46), (24, 30))
        self.relate('connect', 'door', 'walls')
        self.relate('connect', 'roof', 'walls')
