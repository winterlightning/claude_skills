"""Document (files), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ee647811-20d2-4d87-9000-0d11db8aa255'
SOURCE_PATH = 'icons-json/files/document_ee647811-20d2-4d87-9000-0d11db8aa255.json'
AUTHOR = 'gpt-6'

class DocumentFiles(Solo48):
    icon_id = 'document-files'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'files'
    aliases = ()
    keywords = ('document', 'files')

    def build(self):
        self.add_line('e0', (19, 19), (29, 19))
        self.add_line('e1', (18, 31), (29, 31))
        self.add_line('e2', (40, 44), (8, 44))
        self.add_line('e3', (8, 44), (8, 4))
        self.add_line('e4', (8, 4), (31, 4))
        self.add_line('e5', (32, 5), (39, 11))
        self.add_line('e6', (40, 13), (40, 44))
        self.add_line('e8', (31, 4), (32, 5))
        self.add_line('e9', (39, 11), (40, 13))
        self.add_contour('c0', 'e0', closed=False)
        self.add_contour('c1', 'e1', closed=False)
        self.add_contour('c2', 'e2', 'e3', 'e4', 'e8', 'e5', 'e9', 'e6', closed=True)
