"""Gpon splitter 1 (networks), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9aef2fa3-a180-440e-8f69-2d6f71b6f2b3'
SOURCE_PATH = 'icons-json/networks/gpon splitter 1_9aef2fa3-a180-440e-8f69-2d6f71b6f2b3.json'
AUTHOR = 'json_to_solo'

class GponSplitter1Networks(Solo48):
    icon_id = 'gpon-splitter-1-networks'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'networks'
    aliases = ()
    keywords = ('gpon', 'splitter', 'networks')

    def build(self):
        self.add_line('e0', (32, 8), (39, 8))
        self.add_line('e1', (4, 24), (15, 24))
        self.add_line('e2', (33, 40), (39, 40))
        self.add_line('e3', (39, 34), (39, 40))
        self.add_line('e4', (40, 27), (44, 24))
        self.add_line('e5', (40, 21), (44, 24))
        self.add_line('e6', (39, 14), (39, 10))
        self.add_line('e7', (23, 21), (39, 8))
        self.add_line('e8', (39, 40), (23, 27))
        self.add_line('e9', (24, 24), (44, 24))
        self.add_arc('e10-top', (14, 24), (24, 24), radius_x=5, radius_y=4)
        self.add_arc('e10-bottom', (24, 24), (14, 24), radius_x=5, radius_y=4)
        self.add_line('e11', (39, 10), (39, 8))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e11')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c3', 'c8')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c9')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c1', 'e10')
        self.relate('connect', 'c7', 'e10')
        self.relate('connect', 'c8', 'e10')
        self.relate('connect', 'c9', 'e10')
