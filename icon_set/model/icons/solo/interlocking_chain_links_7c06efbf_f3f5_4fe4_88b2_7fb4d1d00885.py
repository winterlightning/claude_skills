'Interlocking chain links.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c06efbf-f3f5-4fe4-88b2-7fb4d1d00885'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/chain_7c06efbf-f3f5-4fe4-88b2-7fb4d1d00885.svg'
AUTHOR = 'gpt-6'

class InterlockingChainLinks(Solo48):
    icon_id = 'interlocking-chain-links'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('interlocking', 'chain', 'links')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_8 = (24, 8)
        p_14_8 = (14, 8)
        p_4_19 = (4, 19)
        p_14_30 = (14, 30)
        p_24_30 = (24, 30)
        p_24_18 = (24, 18)
        p_34_18 = (34, 18)
        p_44_29 = (44, 29)
        p_34_40 = (34, 40)
        p_24_40 = (24, 40)
        self.add_line('left-top', p_24_8, p_14_8)
        self.add_arc('left-upper', p_14_8, p_4_19, radius_x=10, radius_y=11, sweep=False, large_arc=False)
        self.add_arc('left-lower', p_4_19, p_14_30, radius_x=10, radius_y=11, sweep=False, large_arc=False)
        self.add_line('left-bottom', p_14_30, p_24_30)
        self.add_line('right-top', p_24_18, p_34_18)
        self.add_arc('right-upper', p_34_18, p_44_29, radius_x=10, radius_y=11, sweep=True, large_arc=False)
        self.add_arc('right-lower', p_44_29, p_34_40, radius_x=10, radius_y=11, sweep=True, large_arc=False)
        self.add_line('right-bottom', p_34_40, p_24_40)
        self.add_contour('left-link', 'left-top', 'left-upper', 'left-lower', 'left-bottom', closed=False)
        self.add_contour('right-link', 'right-top', 'right-upper', 'right-lower', 'right-bottom', closed=False)
