"""Document (content), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2afb23ce-4e0f-4134-904c-f44465702894'
SOURCE_PATH = 'icons-json/content/document_2afb23ce-4e0f-4134-904c-f44465702894.json'
AUTHOR = 'json_to_solo'

class DocumentContent(Solo48):
    icon_id = 'document-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('document', 'content')

    def build(self):
        self.add_line('e0', (16, 21), (29, 21))
        self.add_line('e1', (16, 29), (22, 29))
        self.add_line('e2', (16, 13), (32, 13))
        self.add_line('e3', (8, 41), (8, 7))
        self.add_line('e4', (11, 4), (37, 4))
        self.add_line('e5', (40, 7), (40, 41))
        self.add_line('e6', (37, 44), (11, 44))
        self.add_arc('e7', (8, 7), (11, 4), radius_x=3)
        self.add_arc('e8', (37, 4), (40, 7), radius_x=3)
        self.add_arc('e9', (40, 41), (37, 44), radius_x=3)
        self.add_arc('e10', (11, 44), (8, 41), radius_x=4)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
