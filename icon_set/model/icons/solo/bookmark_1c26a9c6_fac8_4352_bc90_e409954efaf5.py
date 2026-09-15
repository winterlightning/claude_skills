"""Bookmark (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1c26a9c6-fac8-4352-bc90-e409954efaf5'
SOURCE_PATH = 'icons-json/interface-essential/bookmark_1c26a9c6-fac8-4352-bc90-e409954efaf5.json'
AUTHOR = 'gpt-6'

class Bookmark(Solo48):
    icon_id = 'bookmark'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('bookmark', 'interface-essential')

    def build(self):
        self.add_line('e0', (8, 44), (23, 33))
        self.add_line('e1', (26, 34), (40, 44))
        self.add_line('e2', (40, 44), (40, 7))
        self.add_line('e5', (8, 7), (8, 44))
        self.add_arc('e6', (23, 33), (26, 34), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('e7-1', (40, 7), (38, 4))
        self.add_line('e7-2', (38, 4), (11, 4))
        self.add_arc('e8', (11, 4), (8, 7), radius_x=3, radius_y=3, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e6', 'e1', 'e2', 'e7-1', 'e7-2', 'e8', 'e5', closed=True)
