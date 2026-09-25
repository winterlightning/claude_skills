# Refinement: Place the supporting fingers beneath the heart with full clearance.
# Repair: Lower the supporting fingertips away from the heart lobe.
"""An upward palm supports a heart with a folded thumb; the open left wrist remains asymmetric.

Construction references: Lucide heart, hand-heart, sprout and balloon as applicable.
SOLO48 live-contract centerline bounds: VRECT_L (8,4)-(40,44),
HRECT_L (4,8)-(44,40), SQUARE (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '045520ca-f23a-531a-b54e-ce7bc4cbf52e'
SOURCE_PATH = 'pictographic-primitives/romance/love heart hold_045520ca-f23a-531a-b54e-ce7bc4cbf52e.svg'
AUTHOR = 'gpt-6'

class HandHoldingHeart(Solo48):
    icon_id = 'hand-holding-heart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('hand', 'heart', 'holding', 'care', 'love', 'romance')

    def build(self) -> None:

        def heart(n, cx, y, r, tip):
            self.add_arc(n + '-l', (cx, y), (cx - 2 * r, y), radius_x=r, sweep=False)
            self.add_arc(n + '-shl', (cx - 2 * r, y), (cx - 2 * r + 2, y + 4), radius_x=5, sweep=False)
            self.add_line(n + '-sl', (cx - 2 * r + 2, y + 4), (cx, tip))
            self.add_line(n + '-sr', (cx, tip), (cx + 2 * r - 2, y + 4))
            self.add_arc(n + '-shr', (cx + 2 * r - 2, y + 4), (cx + 2 * r, y), radius_x=5, sweep=False)
            self.add_arc(n + '-r', (cx + 2 * r, y), (cx, y), radius_x=r, sweep=False)
            self.add_contour(n, n + '-l', n + '-shl', n + '-sl', n + '-sr', n + '-shr', n + '-r', closed=True)
        heart('heart', 24, 14, 6, 24)
        self.add_arc('palm-upper', (4, 28), (20, 24), radius_x=16, radius_y=8)
        self.add_line('thumb-top-l', (20, 24), (24, 24))
        self.add_line('thumb-top-r', (24, 24), (28, 24))
        self.add_arc('thumb-tip-upper', (28, 24), (32, 28), radius_x=4)
        self.add_arc('thumb-tip-lower', (32, 28), (28, 32), radius_x=4)
        self.add_line('thumb-bottom', (28, 32), (18, 32))
        self.add_contour('thumb', 'palm-upper', 'thumb-top-l', 'thumb-top-r', 'thumb-tip-upper', 'thumb-tip-lower', 'thumb-bottom')
        self.relate('connect', 'heart', 'thumb')
        self.add_line('fingers-upper', (32, 28), (38, 28))
        self.add_arc('fingertips', (38, 28), (44, 32), radius_x=6)
        self.add_line('fingers-lower', (44, 32), (34, 40))
        self.add_line('palm-base', (34, 40), (12, 40))
        self.add_line('wrist-lower', (12, 40), (4, 38))
        self.add_contour('hand', 'fingers-upper', 'fingertips', 'fingers-lower', 'palm-base', 'wrist-lower')
        self.relate('connect', 'thumb', 'hand')
