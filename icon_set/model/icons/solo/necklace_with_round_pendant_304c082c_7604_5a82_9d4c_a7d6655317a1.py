'Necklace with round pendant.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '304c082c-7604-5a82-9d4c-a7d6655317a1'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/accessories necklace_304c082c-7604-5a82-9d4c-a7d6655317a1.svg'
AUTHOR = 'gpt-6'

class NecklaceWithRoundPendant(Solo48):
    icon_id = 'necklace-with-round-pendant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    categories = ('primitives', 'accessories')
    aliases = ()
    keywords = ('necklace', 'with', 'round', 'pendant')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_4 = (8, 4)
        p_8_16 = (8, 16)
        p_24_33 = (24, 33)
        p_40_16 = (40, 16)
        p_40_4 = (40, 4)
        p_24_44 = (24, 44)
        self.add_line('chain-left', p_8_4, p_8_16)
        self.add_arc('chain-left-bend', p_8_16, p_24_33, radius_x=16, radius_y=17, sweep=False, large_arc=False)
        self.add_arc('chain-right-bend', p_24_33, p_40_16, radius_x=16, radius_y=17, sweep=False, large_arc=False)
        self.add_line('chain-right', p_40_16, p_40_4)
        self.add_arc('pendant-right', p_24_33, p_24_44, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('pendant-left', p_24_44, p_24_33, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_contour('chain', 'chain-left', 'chain-left-bend', 'chain-right-bend', 'chain-right', closed=False)
        self.add_contour('pendant', 'pendant-right', 'pendant-left', closed=True)
        self.relate('connect', 'chain', 'pendant')
