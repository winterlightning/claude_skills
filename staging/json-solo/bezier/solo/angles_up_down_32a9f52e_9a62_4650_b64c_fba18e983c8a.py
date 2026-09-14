"""Angles up down (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '32a9f52e-9a62-4650-b64c-fba18e983c8a'
SOURCE_PATH = 'icons-json/_uncategorized_03/angles up down_32a9f52e-9a62-4650-b64c-fba18e983c8a.json'
AUTHOR = 'json_to_solo'

class AnglesUpDownUncategorized03(Solo48):
    icon_id = 'angles-up-down-uncategorized-03'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('angles', 'up', 'down', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (8, 13), (24, 4))
        self.add_line('e1', (8, 35), (24, 44))
        self.add_line('e2', (40, 35), (24, 44))
        self.add_line('e3', (40, 13), (24, 4))
        self.add_line('e4', (24, 44), (24, 4))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
