"""Bookmark (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fc3ca28d-5459-5622-8b36-d8ebe44e32ab'
SOURCE_PATH = 'icons-json/interface-essential/bookmark_fc3ca28d-5459-5622-8b36-d8ebe44e32ab.json'
AUTHOR = 'json_to_solo'

class BookmarkInterfaceEssential(Solo48):
    icon_id = 'bookmark-interface-essential'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('bookmark', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (40, 44), (40, 8))
        self.add_arc('sym-e1', (40, 8), (40, 7), radius_x=1)
        self.add_arc('sym-e2-1', (40, 7), (39, 5), radius_x=3, sweep=False)
        self.add_line('sym-e2-2', (39, 5), (36, 4))
        self.add_line('sym-e3', (36, 4), (24, 4))
        self.add_line('sym-e4', (24, 4), (12, 4))
        self.add_line('sym-e5-1', (12, 4), (9, 5))
        self.add_arc('sym-e5-2', (9, 5), (8, 7), radius_x=3, sweep=False)
        self.add_line('sym-e6', (8, 7), (8, 8))
        self.add_line('sym-e7', (8, 8), (8, 44))
        self.add_line('sym-e8', (8, 44), (24, 33))
        self.add_line('sym-e9', (24, 33), (40, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2-1', 'sym-e2-2', 'sym-e3', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
