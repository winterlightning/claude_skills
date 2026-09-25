'Handbag with curved flap.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '239735de-63c0-504a-8360-dec9db04343c'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/bag elegant_239735de-63c0-504a-8360-dec9db04343c.svg'
AUTHOR = 'gpt-6'

class HandbagWithCurvedFlap(Solo48):
    icon_id = 'handbag-with-curved-flap'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('bag', 'handbag', 'purse', 'flap', 'fashion', 'accessory', 'shoulder bag', 'clutch')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_22 = (8, 22)
        p_8_19 = (8, 19)
        p_16_19 = (16, 19)
        p_32_19 = (32, 19)
        p_40_19 = (40, 19)
        p_40_22 = (40, 22)
        p_40_37 = (40, 37)
        p_33_44 = (33, 44)
        p_15_44 = (15, 44)
        p_8_37 = (8, 37)
        p_16_13 = (16, 13)
        p_32_13 = (32, 13)
        self.add_line('top-1', p_8_22, p_8_19)
        self.add_line('top-2', p_8_19, p_16_19)
        self.add_line('top-3', p_16_19, p_32_19)
        self.add_line('top-4', p_32_19, p_40_19)
        self.add_line('top-5', p_40_19, p_40_22)
        self.add_line('right', p_40_22, p_40_37)
        self.add_arc('br', p_40_37, p_33_44, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('bottom', p_33_44, p_15_44)
        self.add_arc('bl', p_15_44, p_8_37, radius_x=7, radius_y=7, sweep=True, large_arc=False)
        self.add_line('left', p_8_37, p_8_22)
        self.add_line('handle-l', p_16_19, p_16_13)
        self.add_arc('handle-arch', p_16_13, p_32_13, radius_x=8, radius_y=9, sweep=True, large_arc=False)
        self.add_line('handle-r', p_32_13, p_32_19)
        self.add_arc('flap', p_8_22, p_40_22, radius_x=16, radius_y=12, sweep=False, large_arc=False)
        self.add_contour('top', 'top-1', 'top-2', 'top-3', 'top-4', 'top-5', closed=False)
        self.add_contour('lower', 'right', 'br', 'bottom', 'bl', 'left', closed=False)
        self.add_contour('handle', 'handle-l', 'handle-arch', 'handle-r', closed=False)
        self.relate('connect', 'top', 'lower')
        self.relate('connect', 'handle', 'top')
        self.relate('connect', 'flap', 'top')
        self.relate('connect', 'flap', 'lower')
