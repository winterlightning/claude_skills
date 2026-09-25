"""Lucide user-round: circular head and rounded shoulders. Counter and central tie stroke retained; hairline and tiny tie knot omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd683d815-fbf5-4ebb-949e-95f3cd387592'
SOURCE_PATH = 'pictographic-primitives/shopping/shop cashier man_d683d815-fbf5-4ebb-949e-95f3cd387592.svg'
AUTHOR = 'gpt-6'

class ManAtCheckoutCounter(Solo48):
    icon_id = 'man-at-checkout-counter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "shopping"
    categories = ("shopping", "primitives")
    aliases = ()
    keywords = ('cashier', 'man', 'counter', 'checkout', 'tie', 'staff', 'retail')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). Shared torso axis x=24.
        self.add_arc('head-a',(19,11),(29,11),radius_x=5)
        self.add_arc('head-b',(29,11),(19,11),radius_x=5)
        self.add_contour('head','head-a','head-b',closed=True)
        self.add_line('left',(12,36),(12,29))
        self.add_arc('ls',(12,29),(16,25),radius_x=4)
        self.add_line('top-1',(16,25),(24,25))
        self.add_line('top-2',(24,25),(32,25))
        self.add_arc('rs',(32,25),(36,29),radius_x=4)
        self.add_line('right',(36,29),(36,36))
        self.add_contour('shirt','left','ls','top-1','top-2','rs','right')
        self.add_polyline('counter',(6,42),(6,36),(12,36),(24,36),(36,36),(42,36),(42,42))
        self.relate('connect','shirt','counter')
        self.add_line('tie',(24,25),(24,36))
        self.relate('connect','tie','shirt')
        self.relate('connect','tie','counter')
