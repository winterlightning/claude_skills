'Pair of wedding rings.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6390c0da-0b86-4e37-8062-f088fcb1ef08'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/rings couple_6390c0da-0b86-4e37-8062-f088fcb1ef08.svg'
AUTHOR = 'gpt-6'

class PairOfWeddingRings(Solo48):
    icon_id = 'pair-of-wedding-rings'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('ring', 'rings', 'wedding', 'engagement', 'couple', 'marriage', 'jewellery', 'jewelry', 'gem')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_22_32 = (22, 32)
        p_42_32 = (42, 32)
        p_6_24 = (6, 24)
        p_16_14 = (16, 14)
        p_13_32 = (13, 32)
        p_12_6 = (12, 6)
        p_20_6 = (20, 6)
        p_24_10 = (24, 10)
        p_20_14 = (20, 14)
        p_12_14 = (12, 14)
        p_8_10 = (8, 10)
        self.add_arc('front-top', p_22_32, p_42_32, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('front-bottom', p_42_32, p_22_32, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('rear-top', p_6_24, p_16_14, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('rear-bottom', p_13_32, p_6_24, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('gem-0', p_12_6, p_20_6)
        self.add_line('gem-1', p_20_6, p_24_10)
        self.add_line('gem-2', p_24_10, p_20_14)
        self.add_line('gem-3', p_20_14, p_16_14)
        self.add_line('gem-4', p_16_14, p_12_14)
        self.add_line('gem-5', p_12_14, p_8_10)
        self.add_line('gem-6', p_8_10, p_12_6)
        self.add_contour('front', 'front-top', 'front-bottom', closed=True)
        self.add_contour('rear', 'rear-bottom', 'rear-top', closed=False)
        self.add_contour('gem', 'gem-0', 'gem-1', 'gem-2', 'gem-3', 'gem-4', 'gem-5', 'gem-6', closed=True)
        self.relate('connect', 'rear', 'gem')
