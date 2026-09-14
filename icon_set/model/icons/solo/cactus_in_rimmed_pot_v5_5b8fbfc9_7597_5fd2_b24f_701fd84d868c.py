# Variant of cactus-in-rimmed-pot-v2; parent file remains unchanged.
"""Larger, taller cactus arms with rounded tips; SQUARE (6,6)-(42,42) gives the branches more width. Unequal arm heights preserve organic asymmetry. Rimmed pot retained."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b8fbfc9-7597-5fd2-b24f-701fd84d868c'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_5b8fbfc9-7597-5fd2-b24f-701fd84d868c.svg'
AUTHOR = 'gpt-6'

class CactusInRimmedPotVariant5(Solo48):
    icon_id = 'cactus-in-rimmed-pot-v5'
    variant_of = 'cactus-in-rimmed-pot-v2'
    variant_label = 'Roomier spacing — review 01'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        self.add_line('trunk-left-bottom', (18, 26), (18, 25))
        self.add_arc('left-arm-outer', (18, 25), (6, 14), radius_x=12, radius_y=11)
        self.add_arc('left-arm-cap', (6, 14), (16, 14), radius_x=5)
        self.add_arc('left-arm-inner', (16, 14), (18, 16), radius_x=2, sweep=False)
        self.add_line('trunk-left-top', (18, 16), (18, 12))
        self.add_arc('head-left', (18, 12), (24, 6), radius_x=6)
        self.add_arc('head-right', (24, 6), (30, 12), radius_x=6)
        self.add_line('trunk-right-top', (30, 12), (30, 16))
        self.add_arc('right-arm-inner', (30, 16), (32, 14), radius_x=2, sweep=False)
        self.add_arc('right-arm-cap', (32, 14), (42, 14), radius_x=5)
        self.add_arc('right-arm-outer', (42, 14), (30, 25), radius_x=12, radius_y=11)
        self.add_line('trunk-right-bottom', (30, 25), (30, 26))
        self.add_contour('cactus', 'trunk-left-bottom', 'left-arm-outer', 'left-arm-cap', 'left-arm-inner', 'trunk-left-top', 'head-left', 'head-right', 'trunk-right-top', 'right-arm-inner', 'right-arm-cap', 'right-arm-outer', 'trunk-right-bottom')
        self.add_polyline('rim', (10, 26), (24, 26), (38, 26), (38, 34), (34, 34), (14, 34), (10, 34), closed=True)
        self.add_polyline('pot', (14, 34), (16, 42), (32, 42), (34, 34))
        self.relate('connect', 'rim', 'pot')
        self.relate('connect', 'cactus', 'rim')
