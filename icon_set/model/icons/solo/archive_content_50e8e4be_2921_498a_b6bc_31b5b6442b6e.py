"""Archive (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '50e8e4be-2921-498a-b6bc-31b5b6442b6e'
SOURCE_PATH = 'pictographic-primitives/content/archive_50e8e4be-2921-498a-b6bc-31b5b6442b6e.svg'
AUTHOR = 'gpt-6'

class ArchiveContent(Solo48):
    icon_id = 'archive-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('archive', 'content')

    def build(self):
        self.add_line('e0', (16, 14), (32, 14))
        self.add_line('e1', (16, 22), (26, 22))
        self.add_line('e2', (16, 30), (29, 30))
        self.add_line('e3', (8, 44), (8, 4))
        self.add_line('e4', (8, 4), (40, 4))
        self.add_line('e6', (40, 4), (40, 44))
        self.add_line('e7', (40, 44), (8, 44))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', closed=False)
        self.add_contour('c3', 'e3', 'e4', 'e6', 'e7', closed=True)
