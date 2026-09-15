"""Document (content), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4b94225-2c9c-42ec-947b-c3b93395b100'
SOURCE_PATH = 'pictographic-primitives/content/document_a4b94225-2c9c-42ec-947b-c3b93395b100.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class DocumentA4b94225(Solo48):
    icon_id = 'document-a4b94225'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('document', 'content')

    def build(self):
        # Plan: restore exact straight junctions; remove short fitted corner detours.
        # Reference: existing subject and its ideal straight-edge intersections.
        self.add_line('sym-e0', (42, 30), (30, 30))
        self.add_line('sym-e1', (30, 30), (30, 42))
        self.add_line('sym-e2', (30, 42), (42, 30))
        self.add_line('sym-e3', (42, 30), (42, 6))
        self.add_line('sym-e4', (42, 6), (6, 6))
        self.add_line('sym-e9', (6, 6), (6, 42))
        self.add_line('sym-e10', (6, 42), (30, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e9', 'sym-e10', closed=False)
