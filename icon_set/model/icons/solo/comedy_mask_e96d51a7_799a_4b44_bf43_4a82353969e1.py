"""Comedy Mask. Reduces arched eyes to clear dots and omits the small corner ring, preserving the theatrical face and broad smile.

VRECT_L visible extremes (6, 2, 42, 46); centerlines (8, 4, 40, 44).
Lucide drama: shield-like face, simple eyes and curved smile; supplied source determines the single comedy mask.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e96d51a7-799a-4b44-bf43-4a82353969e1'
SOURCE_PATH = 'pictographic-primitives/symbol/comedy mask with curve line_e96d51a7-799a-4b44-bf43-4a82353969e1.svg'
AUTHOR = 'gpt-6'


class ComedyMask(Solo48):
    icon_id = 'comedy-mask'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('comedy', 'mask', 'theatre', 'drama', 'happy', 'performance', 'acting', 'smile')

    def build(self) -> None:
        self.add_arc('top', (8, 4), (40, 4), radius_x=40, radius_y=12, sweep=False)
        self.add_line('right', (40, 4), (40, 28))
        self.add_arc('chin-right', (40, 28), (24, 44), radius_x=16, radius_y=16, sweep=True)
        self.add_arc('chin-left', (24, 44), (8, 28), radius_x=16, radius_y=16, sweep=True)
        self.add_line('left', (8, 28), (8, 4))
        self.add_contour('mask', 'top', 'right', 'chin-right', 'chin-left', 'left', closed=True)
        self.add_dot('eye-left', (18, 17))
        self.add_dot('eye-right', (30, 17))
        self.add_arc('smile', (30, 29), (18, 29), radius_x=6, radius_y=3, sweep=True)
