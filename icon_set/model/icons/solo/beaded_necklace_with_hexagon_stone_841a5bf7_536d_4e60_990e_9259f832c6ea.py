'Beaded necklace with hexagon stone.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '841a5bf7-536d-4e60-990e-9259f832c6ea'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-05/necklace stone_841a5bf7-536d-4e60-990e-9259f832c6ea.svg'
AUTHOR = 'gpt-6'

class BeadedNecklaceWithHexagonStone(Solo48):
    icon_id = 'beaded-necklace-with-hexagon-stone'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('necklace', 'bead', 'stone', 'hexagon', 'gem', 'jewellery', 'jewelry', 'pendant', 'accessory')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_10 = (6, 10)
        p_14_10 = (14, 10)
        p_34_10 = (34, 10)
        p_42_10 = (42, 10)
        p_10_14 = (10, 14)
        p_24_26 = (24, 26)
        p_38_14 = (38, 14)
        p_33_32 = (33, 32)
        p_33_36 = (33, 36)
        p_24_42 = (24, 42)
        p_15_36 = (15, 36)
        p_15_32 = (15, 32)
        self.add_arc('bead-left-top', p_6_10, p_14_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('bead-left-bottom', p_14_10, p_6_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('bead-right-top', p_34_10, p_42_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('bead-right-bottom', p_42_10, p_34_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('wire-left', p_10_14, p_24_26)
        self.add_line('wire-right', p_38_14, p_24_26)
        self.add_line('stone-0', p_24_26, p_33_32)
        self.add_line('stone-1', p_33_32, p_33_36)
        self.add_line('stone-2', p_33_36, p_24_42)
        self.add_line('stone-3', p_24_42, p_15_36)
        self.add_line('stone-4', p_15_36, p_15_32)
        self.add_line('stone-5', p_15_32, p_24_26)
        self.add_contour('bead-left', 'bead-left-top', 'bead-left-bottom', closed=True)
        self.add_contour('bead-right', 'bead-right-top', 'bead-right-bottom', closed=True)
        self.add_contour('stone', 'stone-0', 'stone-1', 'stone-2', 'stone-3', 'stone-4', 'stone-5', closed=True)
        self.relate('connect', 'bead-left', 'wire-left')
        self.relate('connect', 'bead-right', 'wire-right')
        self.relate('connect', 'wire-left', 'wire-right')
        self.relate('connect', 'wire-left', 'stone')
        self.relate('connect', 'wire-right', 'stone')
