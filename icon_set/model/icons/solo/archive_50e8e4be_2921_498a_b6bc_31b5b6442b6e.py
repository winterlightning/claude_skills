"""Archive (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50e8e4be-2921-498a-b6bc-31b5b6442b6e'
SOURCE_PATH = 'icons-json/content/archive_50e8e4be-2921-498a-b6bc-31b5b6442b6e.json'
AUTHOR = 'json_to_solo'

class ArchiveContent(Solo48):
    icon_id = 'archive-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('archive', 'content')

    def build(self):
        self.add_line('e0', (16, 14), (32, 14))
        self.add_line('e1', (16, 22), (26, 22))
        self.add_line('e2', (16, 30), (29, 30))
        self.add_line('e3', (8, 44), (8, 6))
        self.add_line('e4', (8, 4), (37, 4))
        self.add_line('e5', (37, 4), (40, 4))
        self.add_line('e6', (40, 4), (40, 44))
        self.add_line('e7', (40, 44), (8, 44))
        self.add_line('e8', (8, 6), (8, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e8', 'e4', 'e5', 'e6', 'e7', closed=True)
