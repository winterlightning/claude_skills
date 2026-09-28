'Olive laurel wreath.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'eb8a9192-a034-4f5e-9ce7-1f936af4994a'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/olive wreath_eb8a9192-a034-4f5e-9ce7-1f936af4994a.svg'
AUTHOR = 'gpt-6'

class OliveLaurelWreath(Solo48):
    icon_id = 'olive-laurel-wreath'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    categories = ('culture', 'primitives')
    aliases = ()
    keywords = ('wreath', 'laurel', 'olive', 'victory', 'greek', 'award', 'olympic', 'honour')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_19_6 = (19, 6)
        p_16_13 = (16, 13)
        p_11_27 = (11, 27)
        p_14_35 = (14, 35)
        p_24_42 = (24, 42)
        p_21_11 = (21, 11)
        p_6_19 = (6, 19)
        p_17_22 = (17, 22)
        p_6_32 = (6, 32)
        p_19_31 = (19, 31)
        p_29_6 = (29, 6)
        p_32_13 = (32, 13)
        p_37_27 = (37, 27)
        p_34_35 = (34, 35)
        p_27_11 = (27, 11)
        p_42_19 = (42, 19)
        p_31_22 = (31, 22)
        p_42_32 = (42, 32)
        p_29_31 = (29, 31)
        self.add_line('left-tip', p_19_6, p_16_13)
        self.add_arc('left-upper', p_16_13, p_11_27, radius_x=5, radius_y=15, sweep=False, large_arc=False)
        self.add_arc('left-lower', p_11_27, p_14_35, radius_x=13, radius_y=15, sweep=False, large_arc=False)
        self.add_arc('left-foot', p_14_35, p_24_42, radius_x=13, radius_y=15, sweep=False, large_arc=False)
        self.add_line('left-top-leaf', p_16_13, p_21_11)
        self.add_line('left-outer-high', p_11_27, p_6_19)
        self.add_line('left-inner-high', p_11_27, p_17_22)
        self.add_line('left-outer-low', p_14_35, p_6_32)
        self.add_line('left-inner-low', p_14_35, p_19_31)
        self.add_line('right-tip', p_29_6, p_32_13)
        self.add_arc('right-upper', p_32_13, p_37_27, radius_x=5, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('right-lower', p_37_27, p_34_35, radius_x=13, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('right-foot', p_34_35, p_24_42, radius_x=13, radius_y=15, sweep=True, large_arc=False)
        self.add_line('right-top-leaf', p_32_13, p_27_11)
        self.add_line('right-outer-high', p_37_27, p_42_19)
        self.add_line('right-inner-high', p_37_27, p_31_22)
        self.add_line('right-outer-low', p_34_35, p_42_32)
        self.add_line('right-inner-low', p_34_35, p_29_31)
        self.add_contour('left', 'left-tip', 'left-upper', 'left-lower', 'left-foot', closed=False)
        self.add_contour('right', 'right-tip', 'right-upper', 'right-lower', 'right-foot', closed=False)
        self.relate('connect', 'left', 'left-top-leaf')
        self.relate('connect', 'left', 'left-outer-high')
        self.relate('connect', 'left', 'left-inner-high')
        self.relate('connect', 'left', 'left-outer-low')
        self.relate('connect', 'left', 'left-inner-low')
        self.relate('connect', 'left-outer-high', 'left-inner-high')
        self.relate('connect', 'left-outer-low', 'left-inner-low')
        self.relate('connect', 'right', 'right-top-leaf')
        self.relate('connect', 'right', 'right-outer-high')
        self.relate('connect', 'right', 'right-inner-high')
        self.relate('connect', 'right', 'right-outer-low')
        self.relate('connect', 'right', 'right-inner-low')
        self.relate('connect', 'right-outer-high', 'right-inner-high')
        self.relate('connect', 'right-outer-low', 'right-inner-low')
        self.relate('connect', 'left', 'right')
