"""File paper document (files), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94195673-5dbd-5579-91d7-d7c5ee83aa98'
SOURCE_PATH = 'icons-json/files/file paper document_94195673-5dbd-5579-91d7-d7c5ee83aa98.json'
AUTHOR = 'json_to_solo'

class FilePaperDocument(Solo48):
    icon_id = 'file-paper-document'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('file', 'paper', 'document', 'files')

    def build(self):
        self.add_line('e0', (40, 15), (29, 4))
        self.add_line('e1', (40, 15), (40, 41))
        self.add_line('e2', (37, 44), (11, 44))
        self.add_line('e3', (8, 41), (8, 6))
        self.add_line('e4', (10, 4), (29, 4))
        self.add_line('e5', (29, 4), (29, 11))
        self.add_line('e6', (32, 15), (40, 15))
        self.add_line('e7-1', (40, 41), (40, 42))
        self.add_arc('e7-2', (40, 42), (38, 44), radius_x=2)
        self.add_line('e7-3', (38, 44), (37, 44))
        self.add_arc('e8', (11, 44), (8, 41), radius_x=3)
        self.add_arc('e9', (8, 6), (10, 4), radius_x=2)
        self.add_arc('e10', (29, 11), (32, 15), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e7-1', 'e7-2', 'e7-3', 'e2', 'e8', 'e3', 'e9', 'e4', 'e5', 'e10', 'e6', closed=True)
        self.relate('connect', 'c0', 'c1')
