"""Document (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22698c1f-48fd-44ce-b5f2-9ebee17ac2f8'
SOURCE_PATH = 'icons-json/content/document_22698c1f-48fd-44ce-b5f2-9ebee17ac2f8.json'
AUTHOR = 'json_to_solo'

class Document22698c1f(Solo48):
    icon_id = 'document-22698c1f'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('document', 'content')

    def build(self):
        self.add_line('e0', (16, 31), (22, 31))
        self.add_line('e1', (16, 18), (32, 18))
        self.add_line('e2', (8, 41), (8, 7))
        self.add_line('e3', (11, 4), (37, 4))
        self.add_line('e4', (40, 7), (40, 41))
        self.add_line('e5', (37, 44), (11, 44))
        self.add_arc('e6', (8, 7), (11, 4), radius_x=3)
        self.add_arc('e7', (37, 4), (40, 7), radius_x=3)
        self.add_arc('e8', (40, 41), (37, 44), radius_x=3)
        self.add_arc('e9', (11, 44), (8, 41), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
