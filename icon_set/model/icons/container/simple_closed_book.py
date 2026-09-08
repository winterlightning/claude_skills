"""A closed book has a rounded lower binding and a recessed page edge.

VRECT_L: visible bounds (8, 0, 56, 64), chosen for the subject proportions.
Lucide book: semicircular lower spine and horizontal page band; original and atomic-debug inspected.
Asymmetric binding and concave right page edge preserve the source; no features dropped.
Hosting measured with compose.py: plus blocked, heart blocked, check blocked.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class SimpleClosedBook(Container64):
    icon_id = 'simple-closed-book'
    keyshape = Keyshape.VRECT_L
    aliases = ('closed-book',)
    keywords = ('simple', 'closed', 'book')

    def build(self) -> None:
        self.add_line('cover-left', (10, 55), (10, 10))
        self.add_arc('cover-nw', (10, 10), (18, 2), radius_x=8, radius_y=8, sweep=True)
        self.add_line('cover-top', (18, 2), (54, 2))
        self.add_line('cover-right', (54, 2), (54, 48))
        self.add_line('page-top', (54, 48), (17, 48))
        self.add_arc('binding', (17, 48), (17, 62), radius_x=7, radius_y=7, sweep=False)
        self.add_line('page-bottom', (17, 62), (54, 62))
        self.add_arc('page-recess', (54, 62), (54, 48), radius_x=16, radius_y=16, sweep=True)
        self.add_contour('cover', 'cover-left', 'cover-nw', 'cover-top', 'cover-right', closed=False)
        self.add_contour('pages', 'page-top', 'binding', 'page-bottom', 'page-recess', closed=False)
        self.relate("connect", 'cover', 'pages')
