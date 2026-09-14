"""Drawer (office), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8ace3035-2a2b-4dd5-8701-5613849d5c8d'
SOURCE_PATH = 'icons-json/office/drawer_8ace3035-2a2b-4dd5-8701-5613849d5c8d.json'
AUTHOR = 'json_to_solo'

class Drawer8ace3035(Solo48):
    icon_id = 'drawer-8ace3035'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('drawer', 'office')

    def build(self):
        self.add_line('e0', (41, 22), (7, 22))
        self.add_line('e1', (41, 40), (41, 8))
        self.add_line('e2', (41, 35), (7, 35))
        self.add_line('e3', (7, 8), (7, 40))
        self.add_line('e4', (44, 8), (4, 8))
        self.add_line('e5', (24, 22), (24, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c1')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c5', 'c0')
        self.relate('connect', 'c5', 'c4')
