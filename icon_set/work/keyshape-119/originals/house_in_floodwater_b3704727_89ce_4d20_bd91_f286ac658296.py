"""The upper portion of a house rises above two horizontal rows of waves. Its broad pitched roof and single square window remain visible while the lower walls disappear at the waterline.

Omitted the small square window to retain open space under the pitched roof; retained two waterlines.
Construction reference: Lucide house: continuous roof and walls; repeated scalloped water.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3704727-89ce-4d20-bd91-f286ac658296'
SOURCE_PATH = 'pictographic-primitives/weather/flood house_b3704727-89ce-4d20-bd91-f286ac658296.svg'
AUTHOR = 'gpt-6'

class HouseInFloodwater(Solo48):
    icon_id = 'house-in-floodwater'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/weather"
    aliases = ()
    keywords = ('flood', 'house', 'water', 'wave', 'disaster', 'inundation')

    def build(self) -> None:
        # Live HRECT_XL visible bounds: (2, 6, 46, 42).
        self.add_polyline('house', (10, 30), (10, 19), (24, 8), (38, 19), (38, 30), closed=False)
        self.add_line('water-left', (6, 30), (10, 30))
        self.add_arc('water-a', (10, 30), (24, 30), radius_x=7, radius_y=1, sweep=False, large_arc=False)
        self.add_arc('water-b', (24, 30), (38, 30), radius_x=7, radius_y=1, sweep=False, large_arc=False)
        self.add_line('water-right', (38, 30), (42, 30))
        self.add_contour('surface', 'water-left', 'water-a', 'water-b', 'water-right', closed=False)
        self.relate("connect", 'house', 'surface')
        self.add_arc('lower-a', (6, 39), (24, 39), radius_x=10, radius_y=1, sweep=False, large_arc=False)
        self.add_arc('lower-b', (24, 39), (42, 39), radius_x=10, radius_y=1, sweep=False, large_arc=False)
        self.add_contour('lower', 'lower-a', 'lower-b', closed=False)
