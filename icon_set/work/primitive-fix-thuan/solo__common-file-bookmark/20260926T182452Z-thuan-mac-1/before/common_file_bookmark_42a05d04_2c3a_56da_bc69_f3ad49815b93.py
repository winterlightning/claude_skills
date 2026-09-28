"""Common file bookmark (files), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '42a05d04-2c3a-56da-bc69-f3ad49815b93'
SOURCE_PATH = 'pictographic-primitives/files/common file bookmark_42a05d04-2c3a-56da-bc69-f3ad49815b93.svg'
AUTHOR = 'gpt-6'

class CommonFileBookmark(Solo48):
    icon_id = 'common-file-bookmark'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    categories = ('files', 'primitives')
    aliases = ()
    keywords = ('common', 'file', 'bookmark', 'files')

    def build(self):
        self.add_line('e0', (40, 20), (35, 17))
        self.add_line('e1', (35, 17), (31, 20))
        self.add_line('e2', (31, 20), (31, 4))
        self.add_line('e3', (40, 9), (40, 40))
        self.add_line('e4', (37, 44), (12, 44))
        self.add_line('e6', (11, 4), (37, 4))
        self.add_line('e7-1', (40, 40), (39, 43))
        self.add_line('e7-2', (39, 43), (37, 44))
        self.add_arc('e8-1', (12, 44), (8, 40), radius_x=4, radius_y=4, large_arc=False, sweep=True)
        self.add_line('e8-2', (8, 40), (8, 8))
        self.add_line('e9-1', (8, 8), (9, 5))
        self.add_line('e9-2', (9, 5), (11, 4))
        self.add_line('e10-1', (37, 4), (39, 5))
        self.add_line('e10-2', (39, 5), (40, 8))
        self.add_arc('e10-3', (40, 8), (40, 9), radius_x=20, radius_y=20, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=False)
        self.add_contour('c1', 'e3', 'e7-1', 'e7-2', 'e4', 'e8-1', 'e8-2', 'e9-1', 'e9-2', 'e6', 'e10-1', 'e10-2', 'e10-3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
