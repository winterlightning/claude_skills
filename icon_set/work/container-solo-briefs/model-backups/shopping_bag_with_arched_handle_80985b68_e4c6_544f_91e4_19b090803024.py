'Shopping bag with arched handle.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80985b68-e4c6-544f-91e4-19b090803024'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-07/bag carry_80985b68-e4c6-544f-91e4-19b090803024.svg'
AUTHOR = 'gpt-6'

class ShoppingBagWithArchedHandle(Solo48):
    icon_id = 'shopping-bag-with-arched-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('shopping', 'bag', 'with', 'arched', 'handle')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_11_17 = (11, 17)
        p_16_17 = (16, 17)
        p_32_17 = (32, 17)
        p_37_17 = (37, 17)
        p_40_39 = (40, 39)
        p_35_44 = (35, 44)
        p_13_44 = (13, 44)
        p_8_39 = (8, 39)
        p_16_13 = (16, 13)
        p_32_13 = (32, 13)
        self.add_line('rim-1', p_11_17, p_16_17)
        self.add_line('rim-2', p_16_17, p_32_17)
        self.add_line('rim-3', p_32_17, p_37_17)
        self.add_line('side-right', p_37_17, p_40_39)
        self.add_arc('corner-right', p_40_39, p_35_44, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('base', p_35_44, p_13_44)
        self.add_arc('corner-left', p_13_44, p_8_39, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('side-left', p_8_39, p_11_17)
        self.add_line('handle-left', p_16_17, p_16_13)
        self.add_arc('handle-arch', p_16_13, p_32_13, radius_x=8, radius_y=9, sweep=True, large_arc=False)
        self.add_line('handle-right', p_32_13, p_32_17)
        self.add_contour('body', 'rim-1', 'rim-2', 'rim-3', 'side-right', 'corner-right', 'base', 'corner-left', 'side-left', closed=True)
        self.add_contour('handle', 'handle-left', 'handle-arch', 'handle-right', closed=False)
        self.relate('connect', 'body', 'handle')
