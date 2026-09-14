"""Bookmark (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc3ca28d-5459-5622-8b36-d8ebe44e32ab'
SOURCE_PATH = 'icons-json/interface-essential/bookmark_fc3ca28d-5459-5622-8b36-d8ebe44e32ab.json'
AUTHOR = 'json_to_solo'

class BookmarkFc3ca28d(Solo48):
    icon_id = 'bookmark-fc3ca28d'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('bookmark', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (40, 44), (40, 8))
        self.add_bezier('sym-e1', (40, 8), ((39.988, 7.855), (40, 7.145), (40, 7)))
        self.add_bezier('sym-e2', (40, 7), ((40, 5.564), (38.142, 4), (36, 4)))
        self.add_line('sym-e3', (36, 4), (24, 4))
        self.add_line('sym-e4', (24, 4), (12, 4))
        self.add_bezier('sym-e5', (12, 4), ((9.858, 4), (8, 5.564), (8, 7)))
        self.add_bezier('sym-e6', (8, 7), ((8, 7.145), (8.012, 7.855), (8, 8)))
        self.add_line('sym-e7', (8, 8), (8, 44))
        self.add_line('sym-e8', (8, 44), (24, 33))
        self.add_line('sym-e9', (24, 33), (40, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
