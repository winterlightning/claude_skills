# Variant of broad-leaf-seedling-in-rimmed-pot-v2; parent file remains unchanged.
'Broad leaf seedling in rimmed pot v2. Refit leaf apex to the current vertical bounds and restore eight-unit pot depth.\nOriginal subject geometry is retained and refitted to the current native keyshape. Directional asymmetry is intentional. Construction review: original drawing; sprout or bug principles for the plant and beetle.\n'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2afcf43c-09b9-5de1-9777-49c4ecd3a602'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_2afcf43c-09b9-5de1-9777-49c4ecd3a602.svg'
AUTHOR = 'gpt-6'

class BroadLeafSeedlingInRimmedPotVariant3(Solo48):
    icon_id = 'broad-leaf-seedling-in-rimmed-pot-v3'
    variant_of = 'broad-leaf-seedling-in-rimmed-pot-v2'
    variant_label = 'Roomier spacing — remaining review'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        self.add_arc('left-upper', (8, 4), (24, 20), radius_x=16, radius_y=16)
        self.add_arc('left-lower', (24, 20), (8, 4), radius_x=16, radius_y=16)
        self.add_contour('left-leaf', 'left-upper', 'left-lower', closed=True)
        self.add_arc('right-upper', (24, 23), (40, 7), radius_x=16, radius_y=16)
        self.add_arc('right-lower', (40, 7), (24, 23), radius_x=16, radius_y=16)
        self.add_contour('right-leaf', 'right-upper', 'right-lower', closed=True)
        self.add_polyline('stem', (24, 20), (24, 23), (24, 28))
        self.relate('connect', 'left-leaf', 'stem')
        self.relate('connect', 'right-leaf', 'stem')
        self.add_polyline('rim', (10, 28), (24, 28), (38, 28), (38, 36), (34, 36), (14, 36), (10, 36), closed=True)
        self.add_polyline('pot', (14, 36), (16, 44), (32, 44), (34, 36))
        self.relate('connect', 'rim', 'pot')
        self.relate('connect', 'stem', 'rim')
