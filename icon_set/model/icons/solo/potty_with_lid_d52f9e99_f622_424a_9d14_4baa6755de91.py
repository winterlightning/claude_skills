'Potty with lid.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd52f9e99-f622-424a-9d14-4baa6755de91'
SOURCE_PATH = 'pictographic-primitives/babies/poo poop station waste lid_d52f9e99-f622-424a-9d14-4baa6755de91.svg'
AUTHOR = 'gpt-6'

class PottyWithLid(Solo48):
    icon_id = 'potty-with-lid'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    aliases = ()
    keywords = ('potty', 'toilet', 'training', 'baby', 'lid', 'seat', 'bathroom', 'toddler')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_11_24 = (11, 24)
        p_37_24 = (37, 24)
        p_37_32 = (37, 32)
        p_11_32 = (11, 32)
        p_15_24 = (15, 24)
        p_15_16 = (15, 16)
        p_33_16 = (33, 16)
        p_33_24 = (33, 24)
        p_11_44 = (11, 44)
        p_20_44 = (20, 44)
        p_28_44 = (28, 44)
        p_37_44 = (37, 44)
        self.add_line('seat-1', p_11_24, p_37_24)
        self.add_arc('seat-2', p_37_24, p_37_32, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('seat-3', p_37_32, p_11_32)
        self.add_arc('seat-4', p_11_32, p_11_24, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('lid-1', p_15_24, p_15_16)
        self.add_arc('lid-2', p_15_16, p_33_16, radius_x=9, radius_y=12, sweep=True, large_arc=False)
        self.add_line('lid-3', p_33_16, p_33_24)
        self.add_line('base-1', p_11_32, p_11_44)
        self.add_line('base-2', p_11_44, p_20_44)
        self.add_arc('base-3', p_20_44, p_28_44, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('base-4', p_28_44, p_37_44)
        self.add_line('base-5', p_37_44, p_37_32)
        self.add_contour('seat', 'seat-1', 'seat-2', 'seat-3', 'seat-4', closed=True)
        self.add_contour('lid', 'lid-1', 'lid-2', 'lid-3', closed=False)
        self.add_contour('base', 'base-1', 'base-2', 'base-3', 'base-4', 'base-5', closed=False)
        self.relate('connect', 'seat', 'lid')
        self.relate('connect', 'seat', 'base')
