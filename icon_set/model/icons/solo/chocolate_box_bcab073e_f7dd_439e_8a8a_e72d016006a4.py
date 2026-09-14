"""Chocolate box (romance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bcab073e-f7dd-439e-8a8a-e72d016006a4'
SOURCE_PATH = 'icons-json/romance/chocolate box_bcab073e-f7dd-439e-8a8a-e72d016006a4.json'
AUTHOR = 'json_to_solo'

class ChocolateBox(Solo48):
    icon_id = 'chocolate-box'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('chocolate', 'box', 'romance')

    def build(self):
        self.add_line('e0', (24, 40), (24, 32))
        self.add_line('e1', (24, 40), (6, 28))
        self.add_line('e2', (4, 25), (4, 17))
        self.add_line('e3', (24, 40), (41, 28))
        self.add_line('e4', (44, 24), (44, 20))
        self.add_line('e5', (44, 20), (44, 17))
        self.add_line('e6', (44, 17), (40, 20))
        self.add_line('e7', (40, 20), (24, 32))
        self.add_line('e8', (4, 17), (8, 20))
        self.add_line('e9', (8, 20), (24, 32))
        self.add_arc('e10', (6, 28), (4, 25), radius_x=4)
        self.add_arc('e11', (41, 28), (44, 24), radius_x=7, sweep=False)
        self.add_line('e12-1', (44, 17), (44, 13))
        self.add_arc('e12-2', (44, 13), (41, 10), radius_x=8, sweep=False)
        self.add_line('e12-3', (41, 10), (34, 8))
        self.add_line('e12-4', (34, 8), (28, 9))
        self.add_arc('e12-5', (28, 9), (25, 11), radius_x=10, sweep=False)
        self.add_line('e12-6', (25, 11), (24, 12))
        self.add_arc('e12-7', (24, 12), (20, 9), radius_x=15, sweep=False)
        self.add_line('e12-8', (20, 9), (14, 8))
        self.add_arc('e12-9', (14, 8), (7, 10), radius_x=14, sweep=False)
        self.add_arc('e12-10', (7, 10), (4, 15), radius_x=6, sweep=False)
        self.add_line('e12-11', (4, 15), (4, 17))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e10', 'e2')
        self.add_contour('c2', 'e3', 'e11', 'e4', 'e5')
        self.add_contour('c3', 'e6', 'e7')
        self.add_contour('c4', 'e12-1', 'e12-2', 'e12-3', 'e12-4', 'e12-5', 'e12-6', 'e12-7', 'e12-8', 'e12-9', 'e12-10', 'e12-11')
        self.add_contour('c5', 'e8', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
