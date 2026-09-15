"""Trapezoid handbag with arch handle and curved flap. Lucide shopping-bag informs coherent body and handle; source flap retained.

SOLO48 SQUARE; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '935a7339-45e1-4875-b9a1-843bb0be4549'
SOURCE_PATH = 'pictographic-primitives/symbol/purse_935a7339-45e1-4875-b9a1-843bb0be4549.svg'
AUTHOR = 'gpt-6'


class Handbag(Solo48):
    icon_id = 'handbag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('handbag', 'purse', 'bag', 'fashion', 'shopping', 'accessory', 'women', 'clutch')

    def build(self) -> None:

        for j,(a,b) in enumerate(zip([(10,18),(14,18),(34,18)],[(14,18),(34,18),(38,18)]),1):
            self.add_line('body-top-'+str(j),a,b)
        self.add_line('body-right', (38,18), (42,36))
        self.add_arc('corner-right', (42,36), (36,42), radius_x=6)
        self.add_line('bottom', (36,42), (12,42))
        self.add_arc('corner-left', (12,42), (6,36), radius_x=6)
        self.add_line('body-left', (6,36), (10,18))
        self.add_contour('body','body-top-1','body-top-2','body-top-3','body-right','corner-right','bottom','corner-left','body-left',closed=True)
        self.add_line('handle-left', (14,18), (14,16))
        self.add_arc('handle-top', (14,16), (34,16), radius_x=10)
        self.add_line('handle-right', (34,16), (34,18))
        self.add_contour('handle','handle-left','handle-top','handle-right')
        self.relate('connect','body','handle')
        self.add_arc('flap', (10,18), (38,18), radius_x=14, radius_y=11, sweep=False)
        self.relate('connect','body','flap')
