"""A closed hardcover book with a rounded spine and top page band. Deliberately asymmetric binding.

Keyshape VRECT_L; visible bounds (8, 0, 56, 64); centerline extremes (10, 2)-(54, 62).
Construction reference: Lucide book: rounded binding and horizontal page band, original and atomic-debug inspected.
Reference identity retained; minor export irregularities simplified.
Hosting measured with compose.py: plus passes, heart does not clear, check does not clear.
"""
from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class ClosedHardcoverBook(Container64):
    icon_id = 'closed-hardcover-book'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ('closed-hardcover-book-icon',)
    keywords = ('closed', 'hardcover', 'book')

    def build(self) -> None:
        self.add_line('top', (20, 2), (54, 2))
        self.add_line('page-edge', (54, 2), (54, 18))
        self.add_line('band', (54, 18), (20, 18))
        self.add_arc('spine-top', (20, 18), (20, 2), radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('head', 'top', 'page-edge', 'band', 'spine-top', closed=True)
        self.add_line('cover-right', (54, 18), (54, 62))
        self.add_line('cover-bottom', (54, 62), (20, 62))
        self.add_arc('cover-sw', (20, 62), (10, 52), radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('cover-left', (10, 52), (10, 10))
        self.add_arc('cover-nw', (10, 10), (20, 2), radius_x=10, radius_y=8, sweep=True, large_arc=False)
        self.add_contour('cover', 'cover-right', 'cover-bottom', 'cover-sw', 'cover-left', 'cover-nw', closed=False)
        self.relate("connect", 'cover', 'head')
