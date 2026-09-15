"""Two triangular evergreen trees stand on opposite sides of a flat ground section. A jagged central crack separates the ground into two banks and descends toward a pointed bottom.

Reduced branch tiers and crack zigzags; two trees frame the broken ground.
Construction reference: No useful exact local match; mirrored triangle trees and angular ground fissure.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c8dbd9a-78de-4575-84ad-9b2938edb3ad'
SOURCE_PATH = 'pictographic-primitives/weather/earthquake_3c8dbd9a-78de-4575-84ad-9b2938edb3ad.svg'
AUTHOR = 'gpt-6'

class EarthquakeBetweenTrees(Solo48):
    icon_id = 'earthquake-between-trees'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('earthquake', 'tree', 'crack', 'ground', 'fissure', 'disaster')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_polyline('left-tree', (12, 8), (4, 21), (20, 21), closed=True)
        self.add_line('left-trunk', (12, 21), (12, 29))
        self.relate("connect", 'left-tree', 'left-trunk')
        self.add_polyline('right-tree', (36, 8), (28, 21), (44, 21), closed=True)
        self.add_line('right-trunk', (36, 21), (36, 29))
        self.relate("connect", 'right-tree', 'right-trunk')
        self.add_polyline('ground-left', (4, 40), (4, 29), (23, 29), (19, 34), (26, 40), closed=False)
        self.add_polyline('ground-right', (44, 40), (44, 29), (33, 29), closed=False)
        self.relate("connect", 'left-trunk', 'ground-left')
        self.relate("connect", 'right-trunk', 'ground-right')
