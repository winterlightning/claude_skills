# Variant of flooded-house-interior; parent file remains unchanged.
"""A tall house outline has a peaked roof and a rounded lower edge. Two continuous wavy waterlines cross its lower interior from wall to wall, showing water filling the building.

Retained roof and two water levels, omitted tiny scallops; bilateral symmetry.
Construction reference: Lucide house: coherent pitched outline; repeated wave arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3e9e5afc-aca3-54a0-852a-2c588819cc61'
SOURCE_PATH = 'pictographic-primitives/weather/flood house indoor_3e9e5afc-aca3-54a0-852a-2c588819cc61.svg'
AUTHOR = 'gpt-6'

class FloodedHouseInteriorVariant2(Solo48):
    icon_id = 'flooded-house-interior-v2'
    variant_of = 'flooded-house-interior'
    variant_label = 'Roomier openings — pending review'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/weather'
    aliases = ()
    keywords = ('flood', 'house', 'water', 'indoor', 'disaster', 'inundation')

    def build(self) -> None:
        self.add_polyline('house', (8, 42), (8, 18), (24, 6), (40, 18), (40, 42), closed=True)
        self.add_arc('water-0-0', (8, 25), (24, 25), radius_x=8, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('water-0-1', (24, 25), (40, 25), radius_x=8, radius_y=2, sweep=False, large_arc=False)
        self.add_contour('water-0', 'water-0-0', 'water-0-1', closed=False)
        self.relate('connect', 'house', 'water-0')
        self.add_arc('water-1-0', (8, 36), (24, 36), radius_x=8, radius_y=2, sweep=False, large_arc=False)
        self.add_arc('water-1-1', (24, 36), (40, 36), radius_x=8, radius_y=2, sweep=False, large_arc=False)
        self.add_contour('water-1', 'water-1-0', 'water-1-1', closed=False)
        self.relate('connect', 'house', 'water-1')
