"""Facet (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dcf9970f-8995-424b-8e93-bc85688517b7'
SOURCE_PATH = 'icons-json/_uncategorized_18/facet_dcf9970f-8995-424b-8e93-bc85688517b7.json'
AUTHOR = 'json_to_solo'

class FacetUncategorized(Solo48):
    icon_id = 'facet-uncategorized'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('facet', '_uncategorized')

    def build(self):
        self.add_line('sym-e0', (24, 42), (15, 33))
        self.add_line('sym-e1', (15, 33), (6, 24))
        self.add_line('sym-e2', (6, 24), (24, 6))
        self.add_line('sym-e3', (24, 6), (33, 15))
        self.add_line('sym-e4', (33, 15), (42, 24))
        self.add_line('sym-e5', (42, 24), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', closed=True)
