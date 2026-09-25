"""Facet (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'dcf9970f-8995-424b-8e93-bc85688517b7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/facet_dcf9970f-8995-424b-8e93-bc85688517b7.svg'
AUTHOR = 'gpt-6'

class Facet(Solo48):
    icon_id = 'facet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('facet', '_uncategorized')

    def build(self):
        self.add_line('sym-e0', (24, 42), (6, 24))
        self.add_line('sym-e2', (6, 24), (24, 6))
        self.add_line('sym-e3', (24, 6), (42, 24))
        self.add_line('sym-e5', (42, 24), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e5', closed=True)
