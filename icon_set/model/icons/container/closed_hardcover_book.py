"""A closed hardcover book with a rounded spine and a top page band.

VRECT_L fits the upright book: ink (8,0)-(56,64), centerline (10,2)-(54,62).
Reference: supplied failed SVG; Lucide book original and atomic-debug informed
rounded binding corners and a horizontal page band. The doubled inner spine
curl was removed so the binding has one clear outline. The binding remains
intentionally asymmetric.

Hosting (compose.py): plus valid; heart, check blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (closed-hardcover-book VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from ...keyshapes import Keyshape
from ._base import Container64

SOURCE_ICON_ID = 'closed-hardcover-book'
SOURCE_PATH = 'icon_set/dist/failed/container64/closed-hardcover-book.svg'
AUTHOR = 'claude-opus-5-5'


class ClosedHardcoverBook(Container64):
    icon_id = 'closed-hardcover-book'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ('closed-hardcover-book-icon',)
    keywords = ('closed', 'hardcover', 'book')

    def build(self) -> None:
        self.add_line('top', (20, 4), (52, 4))
        self.add_line('right-upper', (52, 4), (52, 20))
        self.add_line('right-lower', (52, 20), (52, 60))
        self.add_line('bottom', (52, 60), (20, 60))
        self.add_arc('spine-bottom', (20, 60), (12, 52), radius_x=8)
        self.add_line('left-lower', (12, 52), (12, 20))
        self.add_line('left-upper', (12, 20), (12, 12))
        self.add_arc('spine-top', (12, 12), (20, 4), radius_x=8)
        self.add_line('page-band', (12, 20), (52, 20))
        self.add_contour('cover', 'top', 'right-upper', 'right-lower', 'bottom', 'spine-bottom', 'left-lower', 'left-upper', 'spine-top', closed=True)
        self.relate('connect', 'page-band', 'cover')
