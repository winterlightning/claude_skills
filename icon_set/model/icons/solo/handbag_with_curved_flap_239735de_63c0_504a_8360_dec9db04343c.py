"""A rounded handbag with an arched handle and broad curved front flap."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '239735de-63c0-504a-8360-dec9db04343c'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-01/bag elegant_239735de-63c0-504a-8360-dec9db04343c.svg'
AUTHOR = 'astra-chatgpt'


class HandbagWithCurvedFlap(Solo48):
    icon_id = 'handbag-with-curved-flap'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('bag', 'handbag', 'purse', 'flap', 'fashion', 'accessory', 'shoulder bag', 'clutch')

    def build(self) -> None:
        # VRECT_XL: authored directly to its SOLO48 centerline extremes.
        self.add_polyline('top', (5, 22), (5, 18), (14, 18), (34, 18), (43, 18), (43, 22), closed=False)
        self.add_line('right', (43, 22), (43, 38))
        self.add_arc('br', (43, 38), (35, 46), radius_x=8, radius_y=8, sweep=True)
        self.add_line('bottom', (35, 46), (13, 46))
        self.add_arc('bl', (13, 46), (5, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_line('left', (5, 38), (5, 22))
        self.add_contour('lower', 'right', 'br', 'bottom', 'bl', 'left', closed=False)
        self.relate("connect", 'top', 'lower')
        self.add_line('handle-l', (14, 18), (14, 12))
        self.add_arc('handle-arch', (14, 12), (34, 12), radius_x=10, radius_y=10, sweep=True)
        self.add_line('handle-r', (34, 12), (34, 18))
        self.add_contour('handle', 'handle-l', 'handle-arch', 'handle-r', closed=False)
        self.relate("connect", 'handle', 'top')
        self.add_arc('flap', (5, 22), (43, 22), radius_x=19, radius_y=13, sweep=False)
        self.relate("connect", 'flap', 'top')
        self.relate("connect", 'flap', 'lower')
