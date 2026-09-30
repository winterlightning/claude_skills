"""A closed book has a rounded lower binding and a recessed page edge.

VRECT_L fits the upright book: ink (8,0)-(56,64), centerline (10,2)-(54,62).
Reference: supplied failed SVG; Lucide book original and atomic-debug informed
rounded spine corners and a horizontal page band. The overlapping inner binding
curl was simplified into one junction. The binding and recessed right edge
remain intentionally asymmetric.

Hosting (compose.py): check valid; plus, heart blocked.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (simple-closed-book VRECT_L -> VRECT_M). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

SOURCE_ICON_ID = 'simple-closed-book'
SOURCE_PATH = 'icon_set/dist/failed/container64/simple-closed-book.svg'
AUTHOR = 'claude-opus-5-5'


class SimpleClosedBook(Container64):
    icon_id = 'simple-closed-book'
    keyshape = Keyshape.VRECT_M
    aliases = ('closed-book',)
    keywords = ('simple', 'closed', 'book')

    def build(self) -> None:
        self.add_line('cover-left', (12, 46), (12, 12))
        self.add_arc('cover-nw', (12, 12), (20, 4), radius_x=8)
        self.add_line('cover-top', (20, 4), (52, 4))
        self.add_line('cover-right', (52, 4), (52, 46))
        self.add_arc('page-recess', (52, 46), (52, 60), radius_x=13, sweep=False)
        self.add_line('page-bottom', (52, 60), (20, 60))
        self.add_arc('binding', (20, 60), (12, 52), radius_x=8)
        self.add_line('binding-side', (12, 52), (12, 46))
        self.add_line('page-top', (12, 46), (52, 46))
        self.add_contour('cover', 'cover-left', 'cover-nw', 'cover-top', 'cover-right', 'page-recess', 'page-bottom', 'binding', 'binding-side', closed=True)
        self.relate('connect', 'page-top', 'cover')
