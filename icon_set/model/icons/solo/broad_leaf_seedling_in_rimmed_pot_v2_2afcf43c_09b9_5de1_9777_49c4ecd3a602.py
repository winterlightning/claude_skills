# Variant of broad-leaf-seedling-in-rimmed-pot; parent file remains unchanged.
"""Two broad pointed leaves on a stem in a rimmed pot. Lucide sprout informs paired arc leaves, with intentional stagger retained from source."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2afcf43c-09b9-5de1-9777-49c4ecd3a602'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_2afcf43c-09b9-5de1-9777-49c4ecd3a602.svg'
AUTHOR = 'gpt-6'

class BroadLeafSeedlingInRimmedPotVariant2(Solo48):
    icon_id = 'broad-leaf-seedling-in-rimmed-pot-v2'
    variant_of = 'broad-leaf-seedling-in-rimmed-pot'
    variant_label = 'Roomier spacing — review 01'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        self.add_arc('left-upper', (8, 6), (24, 20), radius_x=16, radius_y=16)
        self.add_arc('left-lower', (24, 20), (8, 6), radius_x=16, radius_y=16)
        self.add_contour('left-leaf', 'left-upper', 'left-lower', closed=True)
        self.add_arc('right-upper', (24, 23), (40, 7), radius_x=16, radius_y=16)
        self.add_arc('right-lower', (40, 7), (24, 23), radius_x=16, radius_y=16)
        self.add_contour('right-leaf', 'right-upper', 'right-lower', closed=True)
        self.add_polyline('stem', (24, 20), (24, 23), (24, 28))
        self.relate('connect', 'left-leaf', 'stem')
        self.relate('connect', 'right-leaf', 'stem')
        self.add_polyline('rim', (10, 28), (24, 28), (38, 28), (38, 36), (34, 36), (14, 36), (10, 36), closed=True)
        self.add_polyline('pot', (14, 36), (16, 42), (32, 42), (34, 36))
        self.relate('connect', 'rim', 'pot')
        self.relate('connect', 'stem', 'rim')
