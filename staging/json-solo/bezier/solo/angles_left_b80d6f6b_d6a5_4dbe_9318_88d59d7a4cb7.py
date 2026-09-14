"""Angles left (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b80d6f6b-d6a5-4dbe-9318-88d59d7a4cb7'
SOURCE_PATH = 'icons-json/_uncategorized_03/angles left_b80d6f6b-d6a5-4dbe-9318-88d59d7a4cb7.json'
AUTHOR = 'json_to_solo'

class AnglesLeftUncategorized03(Solo48):
    icon_id = 'angles-left-uncategorized-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('angles', 'left', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (21, 8), (4, 24))
        self.add_line('e1', (21, 40), (4, 24))
        self.add_line('e2', (44, 24), (4, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
