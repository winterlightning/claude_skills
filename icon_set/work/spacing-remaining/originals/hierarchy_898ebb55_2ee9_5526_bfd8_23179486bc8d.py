"""Hierarchy (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '898ebb55-2ee9-5526-bfd8-23179486bc8d'
SOURCE_PATH = 'icons-json/programing/hierarchy_898ebb55-2ee9-5526-bfd8-23179486bc8d.json'
AUTHOR = 'json_to_solo'

class Hierarchy898ebb55(Solo48):
    icon_id = 'hierarchy-898ebb55'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('hierarchy', 'programing')

    def build(self):
        self.add_line('e0', (32, 20), (17, 15))
        self.add_line('e1', (33, 27), (17, 33))
        self.add_arc('e2-top', (4, 34), (16, 34), radius_x=6)
        self.add_arc('e2-bottom', (16, 34), (4, 34), radius_x=6)
        self.add_arc('e3-top', (32, 23), (44, 23), radius_x=6)
        self.add_arc('e3-bottom', (44, 23), (32, 23), radius_x=6)
        self.add_arc('e4-top', (4, 14), (16, 14), radius_x=6)
        self.add_arc('e4-bottom', (16, 14), (4, 14), radius_x=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e3')
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e3')
        self.relate('connect', 'c1', 'e2')
