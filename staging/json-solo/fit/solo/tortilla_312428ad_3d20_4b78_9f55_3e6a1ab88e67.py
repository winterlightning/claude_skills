"""Tortilla (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '312428ad-3d20-4b78-9f55-3e6a1ab88e67'
SOURCE_PATH = 'icons-json/_uncategorized_38/tortilla_312428ad-3d20-4b78-9f55-3e6a1ab88e67.json'
AUTHOR = 'json_to_solo'

class TortillaUncategorized(Solo48):
    icon_id = 'tortilla-uncategorized'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('tortilla', '_uncategorized')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
