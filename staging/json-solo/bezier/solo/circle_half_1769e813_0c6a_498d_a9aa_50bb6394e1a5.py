"""Circle half (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1769e813-0c6a-498d-a9aa-50bb6394e1a5'
SOURCE_PATH = 'icons-json/_uncategorized_11/circle half_1769e813-0c6a-498d-a9aa-50bb6394e1a5.json'
AUTHOR = 'json_to_solo'

class CircleHalfUncategorized(Solo48):
    icon_id = 'circle-half-uncategorized'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('circle', 'half', '_uncategorized')

    def build(self):
        self.add_line('e0', (24, 4), (24, 44))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
        self.relate('connect', 'c0', 'e1')
        self.relate('connect', 'c0', 'e1')
