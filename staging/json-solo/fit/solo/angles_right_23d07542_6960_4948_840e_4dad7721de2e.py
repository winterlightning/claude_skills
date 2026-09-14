"""Angles right (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '23d07542-6960-4948-840e-4dad7721de2e'
SOURCE_PATH = 'icons-json/_uncategorized_03/angles right_23d07542-6960-4948-840e-4dad7721de2e.json'
AUTHOR = 'json_to_solo'

class AnglesRightUncategorized03(Solo48):
    icon_id = 'angles-right-uncategorized-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('angles', 'right', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (27, 8), (44, 24))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (27, 40), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
