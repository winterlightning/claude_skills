"""Armchair (furnitures), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '049cac05-52fa-5b8f-9a6e-d5ee4caeceb0'
SOURCE_PATH = 'icons-json/furnitures/armchair_049cac05-52fa-5b8f-9a6e-d5ee4caeceb0.json'
AUTHOR = 'json_to_solo'

class ArmchairFurnitures(Solo48):
    icon_id = 'armchair-furnitures'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('armchair', 'furnitures')

    def build(self):
        self.add_line('e0', (35, 39), (13, 39))
        self.add_line('e1', (14, 42), (14, 39))
        self.add_line('e2', (34, 42), (34, 39))
        self.add_arc('e3-1', (38, 33), (30, 29), radius_x=12, sweep=False)
        self.add_arc('e3-2', (30, 29), (11, 33), radius_x=19, sweep=False)
        self.add_arc('e4', (38, 33), (35, 39), radius_x=4)
        self.add_arc('e5', (13, 39), (11, 33), radius_x=4)
        self.add_arc('e6-1', (38, 33), (41, 31), radius_x=6, sweep=False)
        self.add_line('e6-2', (41, 31), (42, 28))
        self.add_arc('e6-3', (42, 28), (36, 23), radius_x=6, sweep=False)
        self.add_arc('e7-1', (36, 23), (36, 13), radius_x=12, sweep=False)
        self.add_arc('e7-2', (36, 13), (24, 6), radius_x=14, sweep=False)
        self.add_arc('e7-3', (24, 6), (12, 23), radius_x=13, sweep=False)
        self.add_arc('e8', (36, 23), (33, 30), radius_x=5, sweep=False)
        self.add_arc('e9-1', (15, 30), (12, 23), radius_x=5, sweep=False)
        self.add_arc('e9-2', (12, 23), (6, 28), radius_x=6, sweep=False)
        self.add_arc('e9-3', (6, 28), (11, 33), radius_x=6, sweep=False)
        self.add_contour('c0', 'e3-1', 'e3-2')
        self.add_contour('c1', 'e4', 'e0', 'e5')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e6-3')
        self.add_contour('c3', 'e7-1', 'e7-2', 'e7-3')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9-1', 'e9-2', 'e9-3')
        self.add_contour('c6', 'e1')
        self.add_contour('c7', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c0')
        self.relate('connect', 'c5', 'c0')
        self.relate('connect', 'c6', 'c1')
        self.relate('connect', 'c7', 'c1')
