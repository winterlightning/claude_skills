# Variant of cactus-in-rimmed-pot; parent file remains unchanged.
"""Round-topped cactus with unequal raised arms in a rimmed pot. No local Lucide cactus match; uses quarter-circle bends and semicircular tips. Source has no spines to retain."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b8fbfc9-7597-5fd2-b24f-701fd84d868c'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_5b8fbfc9-7597-5fd2-b24f-701fd84d868c.svg'
AUTHOR = 'gpt-6'

class CactusInRimmedPotVariant4(Solo48):
    icon_id = 'cactus-in-rimmed-pot-v4'
    variant_of = 'cactus-in-rimmed-pot'
    variant_label = 'Roomier spacing — review 01'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        self.add_line('trunk-left-bottom', (18, 28), (18, 22))
        self.add_arc('left-arm-outer', (18, 22), (8, 12), radius_x=10)
        self.add_arc('left-arm-cap', (8, 12), (16, 12), radius_x=4)
        self.add_arc('left-arm-inner', (16, 12), (18, 14), radius_x=2, sweep=False)
        self.add_line('trunk-left-top', (18, 14), (18, 10))
        self.add_arc('head-left', (18, 10), (24, 6), radius_x=6)
        self.add_arc('head-right', (24, 6), (30, 10), radius_x=6)
        self.add_line('trunk-right-top', (30, 10), (30, 14))
        self.add_arc('right-arm-inner', (30, 14), (32, 12), radius_x=2, sweep=False)
        self.add_arc('right-arm-cap', (32, 12), (40, 12), radius_x=4)
        self.add_arc('right-arm-outer', (40, 12), (30, 22), radius_x=10)
        self.add_line('trunk-right-bottom', (30, 22), (30, 28))
        self.add_contour('cactus', 'trunk-left-bottom', 'left-arm-outer', 'left-arm-cap', 'left-arm-inner', 'trunk-left-top', 'head-left', 'head-right', 'trunk-right-top', 'right-arm-inner', 'right-arm-cap', 'right-arm-outer', 'trunk-right-bottom')
        self.add_polyline('rim', (10, 28), (24, 28), (38, 28), (38, 36), (34, 36), (14, 36), (10, 36), closed=True)
        self.add_polyline('pot', (14, 36), (16, 42), (32, 42), (34, 36))
        self.relate('connect', 'rim', 'pot')
        self.relate('connect', 'cactus', 'rim')
