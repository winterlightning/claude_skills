'Larger, taller cactus arms with rounded tips; SQUARE (6,6)-(42,42) gives the branches more width. Unequal arm heights preserve organic asymmetry. Pot retained.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ca14b29-db60-5c73-9981-f223340be7a7'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-03/indoor plant_9ca14b29-db60-5c73-9981-f223340be7a7.svg'
AUTHOR = 'gpt-6'

class CactusInRoundedPot(Solo48):
    icon_id = 'cactus-in-rounded-pot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/plants'
    aliases = ()
    keywords = ('plant', 'decoration', 'foliage', 'indoor')

    def build(self) -> None:
        # SQUARE centerline extremes (6,6)-(42,42); thicker, taller arms.
        self.add_line('trunk-left-bottom', (18,30), (18,25))
        self.add_arc('left-outer', (18,25), (6,9), radius_x=16)
        self.add_line('left-rise', (6,9), (6,6))
        self.add_arc('left-cap', (6,6), (10,6), radius_x=4)
        self.add_line('left-inner-rise', (10,6), (10,9))
        self.add_arc('left-inner', (10,9), (18,17), radius_x=8, sweep=False)
        self.add_line('trunk-left-top', (18,17), (18,8))
        self.add_arc('head-left', (18,8), (24,6), radius_x=6)
        self.add_arc('head-right', (24,6), (30,8), radius_x=6)
        self.add_line('trunk-right-top', (30,8), (30,19))
        self.add_arc('right-inner', (30,19), (38,11), radius_x=8, sweep=False)
        self.add_line('right-inner-rise', (38,11), (38,8))
        self.add_arc('right-cap', (38,8), (42,8), radius_x=4)
        self.add_line('right-rise', (42,8), (42,11))
        self.add_arc('right-outer', (42,11), (30,27), radius_x=16)
        self.add_line('trunk-right-bottom', (30,27), (30,30))
        self.add_contour('cactus', 'trunk-left-bottom','left-outer','left-rise','left-cap','left-inner-rise','left-inner','trunk-left-top','head-left','head-right','trunk-right-top','right-inner','right-inner-rise','right-cap','right-rise','right-outer','trunk-right-bottom')
        self.add_polyline('mouth', (12, 30), (24, 30), (36, 30))
        self.add_line('pot-right', (36, 30), (34, 42))
        self.add_arc('bottom-right', (34, 42), (30, 42), radius_x=4)
        self.add_line('bottom', (30, 42), (18, 42))
        self.add_arc('bottom-left', (18, 42), (14, 42), radius_x=4)
        self.add_line('pot-left', (14, 42), (12, 30))
        self.add_contour('pot', 'pot-right', 'bottom-right', 'bottom', 'bottom-left', 'pot-left')
        self.relate('connect', 'mouth', 'pot')
        self.relate('connect', 'cactus', 'mouth')
