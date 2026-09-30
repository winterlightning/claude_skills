"""A toaster enclosure with a risen bread slice and a right-hand lever.

Keyshape SQUARE: centerline extremes recorded in build below.
Lucide smartphone informs the rounded appliance shell; no useful Lucide bread-slice match was found. The source provides the bread crown and deliberate side-lever asymmetry.
Hosting (compose.py): plus valid, heart review, check valid.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (kitchen-toaster-with-bread-slice SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class KitchenToasterWithBreadSlice(Container64):
    icon_id = 'kitchen-toaster-with-bread-slice'
    keyshape = Keyshape.SQUARE
    aliases = ('toaster',)
    keywords = ('kitchen', 'toaster', 'with', 'bread', 'slice')

    def build(self) -> None:
        self.add_line('body-0', (9, 25), (51, 25))
        self.add_arc('body-1', (51, 25), (54, 28), radius_x=3)
        self.add_line('body-2', (54, 28), (54, 55))
        self.add_arc('body-3', (54, 55), (51, 58), radius_x=3)
        self.add_line('body-4', (51, 58), (9, 58))
        self.add_arc('body-5', (9, 58), (6, 55), radius_x=3)
        self.add_line('body-6', (6, 55), (6, 28))
        self.add_arc('body-7', (6, 28), (9, 25), radius_x=3)
        self.add_line('bread-left', (14, 25), (14, 18))
        self.add_arc('bread-crown-left', (14, 18), (14, 6), radius_x=6)
        self.add_line('bread-top', (14, 6), (44, 6))
        self.add_arc('bread-crown-right', (44, 6), (44, 16), radius_x=5)
        self.add_line('bread-right', (44, 16), (44, 25))
        self.add_line('lever', (54, 47), (58, 47))
        self.add_contour('body', 'body-0', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_contour('bread', 'bread-left', 'bread-crown-left', 'bread-top', 'bread-crown-right', 'bread-right')
        self.relate('connect', 'bread', 'body')
        self.relate('connect', 'lever', 'body')
