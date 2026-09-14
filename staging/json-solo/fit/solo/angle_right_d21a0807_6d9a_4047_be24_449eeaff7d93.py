"""Angle right (_uncategorized_03), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd21a0807-6d9a-4047-be24-449eeaff7d93'
SOURCE_PATH = 'icons-json/_uncategorized_03/angle right_d21a0807-6d9a-4047-be24-449eeaff7d93.json'
AUTHOR = 'json_to_solo'

class AngleRightUncategorized03(Solo48):
    icon_id = 'angle-right-uncategorized-03'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = '_uncategorized_03'
    aliases = ()
    keywords = ('angle', 'right', '_uncategorized_03')

    def build(self):
        self.add_line('e0', (27, 8), (44, 24))
        self.add_line('e1', (4, 24), (39, 24))
        self.add_line('e2', (39, 24), (44, 24))
        self.add_line('e3', (27, 40), (41, 27))
        self.add_line('e4', (41, 27), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
