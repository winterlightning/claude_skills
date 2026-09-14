"""Graduation cap (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e5ae7651-62d6-4c05-b34e-faf818f521bc'
SOURCE_PATH = 'icons-json/symbol/graduation cap_e5ae7651-62d6-4c05-b34e-faf818f521bc.json'
AUTHOR = 'json_to_solo'

class GraduationCapE5ae7651(Solo48):
    icon_id = 'graduation-cap-e5ae7651'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('graduation', 'cap', 'symbol')

    def build(self):
        self.add_line('e0', (38, 21), (38, 33))
        self.add_line('e1', (10, 35), (10, 21))
        self.add_line('e2', (38, 21), (25, 27))
        self.add_line('e3', (23, 27), (10, 21))
        self.add_line('e4', (38, 21), (44, 18))
        self.add_line('e5', (44, 18), (24, 8))
        self.add_line('e6', (23, 8), (4, 18))
        self.add_line('e7', (4, 18), (10, 21))
        self.add_arc('e8-1', (38, 33), (33, 38), radius_x=7)
        self.add_line('e8-2', (33, 38), (24, 40))
        self.add_arc('e8-3', (24, 40), (18, 39), radius_x=19)
        self.add_line('e8-4', (18, 39), (10, 35))
        self.add_arc('e9', (25, 27), (23, 27), radius_x=10)
        self.add_arc('e10', (24, 8), (23, 8), radius_x=39)
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e8-3', 'e8-4', 'e1')
        self.add_contour('c1', 'e2', 'e9', 'e3')
        self.add_contour('c2', 'e4', 'e5', 'e10', 'e6', 'e7')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
