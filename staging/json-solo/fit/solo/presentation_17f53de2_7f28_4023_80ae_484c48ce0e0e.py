"""Presentation (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17f53de2-7f28-4023-80ae-484c48ce0e0e'
SOURCE_PATH = 'icons-json/office/presentation_17f53de2-7f28-4023-80ae-484c48ce0e0e.json'
AUTHOR = 'json_to_solo'

class PresentationOffice(Solo48):
    icon_id = 'presentation-office'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('presentation', 'office')

    def build(self):
        self.add_line('e0', (44, 8), (4, 8))
        self.add_line('e1', (41, 8), (41, 30))
        self.add_line('e2', (39, 32), (9, 32))
        self.add_line('e3', (7, 30), (7, 8))
        self.add_line('e4', (24, 36), (24, 32))
        self.add_arc('e5-1', (24, 36), (24, 40), radius_x=2)
        self.add_line('e5-2', (24, 40), (21, 38))
        self.add_arc('e5-3', (21, 38), (23, 36), radius_x=3)
        self.add_arc('e6', (41, 30), (39, 32), radius_x=2)
        self.add_arc('e7', (9, 32), (7, 30), radius_x=2)
        self.add_contour('c0', 'e5-1', 'e5-2', 'e5-3')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e6', 'e2', 'e7', 'e3')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c3', 'c2')
