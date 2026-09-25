'Necklace with oval locket.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '091b5dc9-e4c1-5cd1-b5a3-af25a4d3f1ee'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/necklace locket_091b5dc9-e4c1-5cd1-b5a3-af25a4d3f1ee.svg'
AUTHOR = 'gpt-6'

class NecklaceWithOvalLocket(Solo48):
    icon_id = 'necklace-with-oval-locket'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('necklace', 'locket', 'pendant', 'oval', 'chain', 'jewellery', 'jewelry', 'accessory')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_6 = (6, 6)
        p_24_22 = (24, 22)
        p_42_6 = (42, 6)
        p_24_27 = (24, 27)
        p_30_35 = (30, 35)
        p_24_42 = (24, 42)
        p_18_35 = (18, 35)
        self.add_arc('chain-left', p_6_6, p_24_22, radius_x=18, radius_y=16, sweep=False, large_arc=False)
        self.add_arc('chain-right', p_24_22, p_42_6, radius_x=18, radius_y=16, sweep=False, large_arc=False)
        self.add_line('bail', p_24_22, p_24_27)
        self.add_arc('locket-0', p_24_27, p_30_35, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('locket-1', p_30_35, p_24_42, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('locket-2', p_24_42, p_18_35, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('locket-3', p_18_35, p_24_27, radius_x=6, radius_y=7, sweep=True, large_arc=False)
        self.add_contour('chain', 'chain-left', 'chain-right', closed=False)
        self.add_contour('locket', 'locket-0', 'locket-1', 'locket-2', 'locket-3', closed=True)
        self.relate('connect', 'chain', 'bail')
        self.relate('connect', 'bail', 'locket')
