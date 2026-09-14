"""Document (content), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e6', (8, 7), ((8.345, 5.855), (9.053, 4.018), (10.417, 4.018)), ((10.451, 4.009), (10.966, 4.009), (11, 4)))
        self.add_bezier('e7', (37, 4), ((38.12, 4), (40, 5.8), (40, 7)))
        self.add_bezier('e8', (40, 41), ((40, 42.273), (38.171, 44), (37, 44)))
        self.add_bezier('e9', (11, 44), ((9.501, 43.436), (8.463, 42.664), (8, 41)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
