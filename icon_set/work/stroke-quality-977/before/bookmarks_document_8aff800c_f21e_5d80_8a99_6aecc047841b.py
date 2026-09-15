"""Bookmarks document (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8aff800c-f21e-5d80-8a99-6aecc047841b'
SOURCE_PATH = 'pictographic-primitives/interface-essential/bookmarks document_8aff800c-f21e-5d80-8a99-6aecc047841b.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class BookmarksDocument(Solo48):
    icon_id = 'bookmarks-document'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('bookmarks', 'document', 'interface-essential')

    def build(self):
        self.add_line('e0', (40, 25), (33, 19))
        self.add_line('e1', (33, 19), (26, 24))
        self.add_line('e2', (26, 24), (26, 4))
        self.add_line('e3', (36, 44), (12, 44))
        self.add_line('e4', (8, 40), (8, 9))
        self.add_line('e5', (11, 4), (36, 4))
        self.add_line('e6', (40, 9), (40, 40))
        self.add_arc('e7', (12, 44), (8, 40), radius_x=4)
        self.add_line('e8-1', (8, 9), (9, 5))
        self.add_arc('e8-2', (9, 5), (11, 4), radius_x=3)
        self.add_line('e9-1', (36, 4), (39, 5))
        self.add_line('e9-2', (39, 5), (40, 9))
        self.add_arc('e10', (40, 40), (36, 44), radius_x=4)
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e3', 'e7', 'e4', 'e8-1', 'e8-2', 'e5', 'e9-1', 'e9-2', 'e6', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
