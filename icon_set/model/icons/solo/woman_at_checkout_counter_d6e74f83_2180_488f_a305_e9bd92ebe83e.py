"""Lucide user-round: reduced figure. Paired hair extensions and V neckline distinguish the source; hair parting omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd6e74f83-2180-488f-a305-e9bd92ebe83e'
SOURCE_PATH = 'pictographic-primitives/shopping/shop cashier woman_d6e74f83-2180-488f-a305-e9bd92ebe83e.svg'
AUTHOR = 'gpt-6'

class WomanAtCheckoutCounter(Solo48):
    icon_id = 'woman-at-checkout-counter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('cashier', 'woman', 'counter', 'checkout', 'hair', 'staff', 'retail')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42); rounded hair and open V neckline.
        self.add_arc('hair-top',(16,14),(32,14),radius_x=8)
        self.add_arc('chin',(32,14),(16,14),radius_x=8)
        self.add_contour('head','hair-top','chin',closed=True)
        self.add_line('hair-right',(32,14),(34,21))
        self.add_line('hair-left',(16,14),(14,21))
        self.relate('connect','hair-right','head')
        self.relate('connect','hair-left','head')
        self.add_polyline('shirt',(12,42),(12,32),(16,31),(24,37),(32,31),(36,32),(36,42))
        self.add_polyline('counter',(6,42),(12,42),(36,42),(42,42))
        self.relate('connect','shirt','counter')
