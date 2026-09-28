"""Simple Rectangular Payment Card: independently authored container.

Construction plan: Rounded horizontal payment card with one short lower-right mark; no magnetic band in source.
Keyshape HRECT_M; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/business/card_b42901ee-f812-48ee-a415-b6ce160f17ba.svg. Lucide credit-card original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 12, 64, 52).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.
"""
from ...keyshapes import Keyshape
from ._base import Container64
from ._construction import path, rounded_rect as rect, ellipse

SOURCE_ICON_ID = 'b42901ee-f812-48ee-a415-b6ce160f17ba'
SOURCE_PATH = 'pictographic-primitives/business/card_b42901ee-f812-48ee-a415-b6ce160f17ba.svg'
AUTHOR = 'gpt-6'


class PaymentCardContainer(Container64):
    icon_id = 'payment-card-container'
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    keyshape = Keyshape.HRECT_M
    aliases = ()
    keywords = ('payment', 'card', 'container')

    def build(self):
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        rect(self,'card',2,14,62,50,5)
        line('mark',(44,40),(50,40))
