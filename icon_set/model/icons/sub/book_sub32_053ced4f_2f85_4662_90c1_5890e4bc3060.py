"""Independent 32px profile of book.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '053ced4f-2f85-4662-90c1-5890e4bc3060'
SOURCE_PATH = 'pictographic-primitives/content/book_053ced4f-2f85-4662-90c1-5890e4bc3060.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('053ced4f-2f85-4662-90c1-5890e4bc3060', 'pictographic-primitives/content/book_053ced4f-2f85-4662-90c1-5890e4bc3060.svg'),)
PROFILE_SOURCE_KEYS = ('solo/book',)
SOLO_SOURCE_ICON_IDS = ('book',)
REFERENCE_EXPORT_SHA256 = '9585b639e924f1ca0fa327a7aa93e16afc4cef269ff6744162679e68debc9448'

class Drawing(Sub32):
    icon_id = 'book-sub32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'content'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (27, 2), (9, 2))
        self.add_arc('p1-r1-2', (9, 2), (5, 6), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-3', (5, 6), (5, 9))
        self.add_line('p1-r1-4', (5, 9), (5, 26))
        self.add_arc('p1-r1-5', (5, 26), (9, 30), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p1-r1-6', (9, 30), (27, 30))
        self.add_line('p1-r1-7', (27, 30), (27, 10))
        self.add_line('p1-r1-8', (27, 10), (27, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (5, 6), (9, 10), radius_x=4, radius_y=4, large_arc=False, sweep=False)
        self.add_line('p2-r1-2', (9, 10), (27, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.relate("connect", 'p1-r1-2', 'p2-r1-1')
        self.relate("connect", 'p1-r1-3', 'p2-r1-1')
        self.relate("connect", 'p1-r1-7', 'p2-r1-2')
        self.relate("connect", 'p1-r1-8', 'p2-r1-2')
