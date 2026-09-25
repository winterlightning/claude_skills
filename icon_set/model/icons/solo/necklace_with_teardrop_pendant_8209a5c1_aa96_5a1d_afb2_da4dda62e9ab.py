'Necklace with teardrop pendant.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8209a5c1-aa96-5a1d-afb2-da4dda62e9ab'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/necklace jewel_8209a5c1-aa96-5a1d-afb2-da4dda62e9ab.svg'
AUTHOR = 'gpt-6'

class NecklaceWithTeardropPendant(Solo48):
    icon_id = 'necklace-with-teardrop-pendant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('necklace', 'pendant', 'teardrop', 'jewel', 'chain', 'jewellery', 'jewelry', 'accessory')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_4 = (8, 4)
        p_24_24 = (24, 24)
        p_40_4 = (40, 4)
        p_24_33 = (24, 33)
        p_20_38 = (20, 38)
        p_28_38 = (28, 38)
        self.add_arc('chain-left', p_8_4, p_24_24, radius_x=16, radius_y=20, sweep=False, large_arc=False)
        self.add_arc('chain-right', p_24_24, p_40_4, radius_x=16, radius_y=20, sweep=False, large_arc=False)
        self.add_line('drop-left', p_24_33, p_20_38)
        self.add_arc('drop-bottom', p_20_38, p_28_38, radius_x=4, radius_y=6, sweep=False, large_arc=False)
        self.add_line('drop-right', p_28_38, p_24_33)
        self.add_contour('chain', 'chain-left', 'chain-right', closed=False)
        self.add_contour('pendant', 'drop-left', 'drop-bottom', 'drop-right', closed=True)
