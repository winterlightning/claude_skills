"""Document (content), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4b94225-2c9c-42ec-947b-c3b93395b100'
SOURCE_PATH = 'icons-json/content/document_a4b94225-2c9c-42ec-947b-c3b93395b100.json'
AUTHOR = 'json_to_solo'

class Document(Solo48):
    icon_id = 'document'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('document', 'content')

    def build(self):
        self.add_line('sym-e0', (42, 30), (30, 30))
        self.add_line('sym-e1', (30, 30), (30, 42))
        self.add_line('sym-e2', (30, 42), (42, 30))
        self.add_line('sym-e3', (42, 30), (42, 6))
        self.add_line('sym-e4', (42, 6), (8, 6))
        self.add_bezier('sym-e5', (8, 6), ((7.697, 6), (8.303, 6), (8, 6)))
        self.add_bezier('sym-e6', (8, 6), ((7.639, 6), (7.296, 6.704), (7, 7)))
        self.add_bezier('sym-e7', (7, 7), ((6.704, 7.296), (6, 7.639), (6, 8)))
        self.add_bezier('sym-e8', (6, 8), ((6, 8.303), (6, 7.697), (6, 8)))
        self.add_line('sym-e9', (6, 8), (6, 42))
        self.add_line('sym-e10', (6, 42), (30, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
