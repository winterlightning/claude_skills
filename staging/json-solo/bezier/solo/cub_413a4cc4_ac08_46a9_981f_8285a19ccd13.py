"""Cub (_uncategorized), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '413a4cc4-ac08-46a9-981f-8285a19ccd13'
SOURCE_PATH = 'icons-json/_uncategorized_13/cub_413a4cc4-ac08-46a9-981f-8285a19ccd13.json'
AUTHOR = 'json_to_solo'

class CubUncategorized(Solo48):
    icon_id = 'cub-uncategorized'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized'
    aliases = ()
    keywords = ('cub', '_uncategorized')

    def build(self):
        self.add_line('e0', (40, 14), (40, 34))
        self.add_line('e1', (40, 34), (24, 44))
        self.add_line('e2', (8, 14), (8, 34))
        self.add_line('e3', (8, 34), (24, 44))
        self.add_line('e4', (24, 44), (24, 24))
        self.add_line('e5', (8, 14), (24, 24))
        self.add_line('e6', (24, 24), (40, 14))
        self.add_line('e7', (40, 14), (24, 4))
        self.add_line('e8', (24, 4), (8, 14))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5', 'e6', 'e7', 'e8', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'c3')
