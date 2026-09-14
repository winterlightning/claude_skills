"""Dot (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '81cfae2c-6dfd-4740-b953-c3890ecd3c6f'
SOURCE_PATH = 'icons-json/_uncategorized_15/dot_81cfae2c-6dfd-4740-b953-c3890ecd3c6f.json'
AUTHOR = 'json_to_solo'

class Dot(Solo48):
    icon_id = 'dot-uncategorized'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('dot', '_uncategorized')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
