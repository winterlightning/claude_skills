"""Pie (food), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c499c017-18ac-55ef-8b3d-c050076add31'
SOURCE_PATH = 'icons-json/food/pie_c499c017-18ac-55ef-8b3d-c050076add31.json'
AUTHOR = 'json_to_solo'

class PieC499c017(Solo48):
    icon_id = 'pie-c499c017'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('pie', 'food')

    def build(self):
        self.add_line('e0', (38, 38), (26, 25))
        self.add_line('e1', (24, 23), (24, 4))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_line('e3', (26, 25), (24, 23))
        self.add_contour('c0', 'e0', 'e3', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.relate('connect', 'c0', 'e2')
        self.relate('connect', 'c0', 'e2')
