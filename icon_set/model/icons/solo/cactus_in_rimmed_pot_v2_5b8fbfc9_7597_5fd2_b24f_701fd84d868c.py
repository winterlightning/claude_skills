# Variant of cactus-in-rimmed-pot; parent file remains unchanged.
'Larger, taller cactus arms with rounded tips; SQUARE (2,2)-(46,46) gives the branches more width. Unequal arm heights preserve organic asymmetry. Rimmed pot retained.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5b8fbfc9-7597-5fd2-b24f-701fd84d868c'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_5b8fbfc9-7597-5fd2-b24f-701fd84d868c.svg'
AUTHOR = 'gpt-6'

class CactusInRimmedPotVariant2(Solo48):
    icon_id = 'cactus-in-rimmed-pot-v2'
    variant_of = 'cactus-in-rimmed-pot'
    variant_label = 'Larger branches'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # SQUARE centerline extremes (2,2)-(46,46); thicker, taller arms.
        self.add_line('trunk-left-bottom', (18,30), (18,25))
        self.add_arc('left-outer', (18,25), (2,9), radius_x=16)
        self.add_line('left-rise', (2,9), (2,6))
        self.add_arc('left-cap', (2,6), (10,6), radius_x=4)
        self.add_line('left-inner-rise', (10,6), (10,9))
        self.add_arc('left-inner', (10,9), (18,17), radius_x=8, sweep=False)
        self.add_line('trunk-left-top', (18,17), (18,8))
        self.add_arc('head-left', (18,8), (24,2), radius_x=6)
        self.add_arc('head-right', (24,2), (30,8), radius_x=6)
        self.add_line('trunk-right-top', (30,8), (30,19))
        self.add_arc('right-inner', (30,19), (38,11), radius_x=8, sweep=False)
        self.add_line('right-inner-rise', (38,11), (38,8))
        self.add_arc('right-cap', (38,8), (46,8), radius_x=4)
        self.add_line('right-rise', (46,8), (46,11))
        self.add_arc('right-outer', (46,11), (30,27), radius_x=16)
        self.add_line('trunk-right-bottom', (30,27), (30,30))
        self.add_contour('cactus', 'trunk-left-bottom','left-outer','left-rise','left-cap','left-inner-rise','left-inner','trunk-left-top','head-left','head-right','trunk-right-top','right-inner','right-inner-rise','right-cap','right-rise','right-outer','trunk-right-bottom')
        self.add_polyline('rim', (10, 30), (24, 30), (38, 30), (38, 36), (34, 36), (14, 36), (10, 36), closed=True)
        self.add_polyline('pot', (14, 36), (16, 46), (32, 46), (34, 36))
        self.relate('connect', 'rim', 'pot')
        self.relate('connect', 'cactus', 'rim')
