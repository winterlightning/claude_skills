"""Simple Rectangular Payment Card: independently authored container.

Construction plan: Rounded horizontal payment card with one short lower-right mark; no magnetic band in source.
Keyshape HRECT_M; extremes are the profile's exact keyshape bounds.
Reference: pictographic-primitives/business/card_b42901ee-f812-48ee-a415-b6ce160f17ba.svg. Lucide credit-card original and atomic-debug inspected.
No source coordinates or solo geometry were scaled. Native size is 64.

Visible keyshape extremes: (0, 12, 64, 52).
Hosting measured with compose.py: plus does not clear, heart does not clear, check passes.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (payment-card-container HRECT_M -> HRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'b42901ee-f812-48ee-a415-b6ce160f17ba'
SOURCE_PATH = 'pictographic-primitives/business/card_b42901ee-f812-48ee-a415-b6ce160f17ba.svg'
AUTHOR = 'claude-opus-5-5'


class PaymentCardContainer(Container64):
    icon_id = 'payment-card-container'
    keyshape = Keyshape.HRECT_M
    category = 'business'
    categories = ('business', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('payment', 'card', 'container')

    def build(self) -> None:
        self.add_line('card-0', (9, 12), (55, 12))
        self.add_arc('card-1', (55, 12), (60, 17), radius_x=5)
        self.add_line('card-2', (60, 17), (60, 47))
        self.add_arc('card-3', (60, 47), (55, 52), radius_x=5)
        self.add_line('card-4', (55, 52), (9, 52))
        self.add_arc('card-5', (9, 52), (4, 47), radius_x=5)
        self.add_line('card-6', (4, 47), (4, 17))
        self.add_arc('card-7', (4, 17), (9, 12), radius_x=5)
        self.add_line('mark', (42, 42), (48, 42))
        self.add_contour('card', 'card-0', 'card-1', 'card-2', 'card-3', 'card-4', 'card-5', 'card-6', 'card-7', closed=True)
