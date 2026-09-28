'Rhombus chain links.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '839e21b2-a075-461f-826c-404c48d499b9'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/chain rhombus_839e21b2-a075-461f-826c-404c48d499b9.svg'
AUTHOR = 'gpt-6'

class RhombusChainLinks(Solo48):
    icon_id = 'rhombus-chain-links'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('rhombus', 'chain', 'links')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_12_30 = (12, 30)
        p_15_33 = (15, 33)
        p_18_36 = (18, 36)
        p_12_42 = (12, 42)
        p_6_36 = (6, 36)
        p_24_18 = (24, 18)
        p_27_21 = (27, 21)
        p_30_24 = (30, 24)
        p_24_30 = (24, 30)
        p_21_27 = (21, 27)
        p_18_24 = (18, 24)
        p_36_6 = (36, 6)
        p_42_12 = (42, 12)
        p_36_18 = (36, 18)
        p_33_15 = (33, 15)
        p_30_12 = (30, 12)
        self.add_line('lower-0', p_12_30, p_15_33)
        self.add_line('lower-1', p_15_33, p_18_36)
        self.add_line('lower-2', p_18_36, p_12_42)
        self.add_line('lower-3', p_12_42, p_6_36)
        self.add_line('lower-4', p_6_36, p_12_30)
        self.add_line('middle-0', p_24_18, p_27_21)
        self.add_line('middle-1', p_27_21, p_30_24)
        self.add_line('middle-2', p_30_24, p_24_30)
        self.add_line('middle-3', p_24_30, p_21_27)
        self.add_line('middle-4', p_21_27, p_18_24)
        self.add_line('middle-5', p_18_24, p_24_18)
        self.add_line('upper-0', p_36_6, p_42_12)
        self.add_line('upper-1', p_42_12, p_36_18)
        self.add_line('upper-2', p_36_18, p_33_15)
        self.add_line('upper-3', p_33_15, p_30_12)
        self.add_line('upper-4', p_30_12, p_36_6)
        self.add_line('join-lower', p_15_33, p_21_27)
        self.add_line('join-upper', p_27_21, p_33_15)
        self.add_contour('lower', 'lower-0', 'lower-1', 'lower-2', 'lower-3', 'lower-4', closed=True)
        self.add_contour('middle', 'middle-0', 'middle-1', 'middle-2', 'middle-3', 'middle-4', 'middle-5', closed=True)
        self.add_contour('upper', 'upper-0', 'upper-1', 'upper-2', 'upper-3', 'upper-4', closed=True)
        self.relate('connect', 'lower', 'join-lower')
        self.relate('connect', 'middle', 'join-lower')
        self.relate('connect', 'middle', 'join-upper')
        self.relate('connect', 'upper', 'join-upper')
