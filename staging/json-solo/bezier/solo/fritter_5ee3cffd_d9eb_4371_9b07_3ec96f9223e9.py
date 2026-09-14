"""Fritter (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ee3cffd-d9eb-4371-9b07-3ec96f9223e9'
SOURCE_PATH = 'icons-json/_uncategorized_20/fritter_5ee3cffd-d9eb-4371-9b07-3ec96f9223e9.json'
AUTHOR = 'json_to_solo'

class FritterUncategorized(Solo48):
    icon_id = 'fritter-uncategorized'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('fritter', '_uncategorized')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
