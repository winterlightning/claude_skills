"""Dress (clothes), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d38ebdf-a077-54d8-b2cd-fd37cdddfcde'
SOURCE_PATH = 'icons-json/clothes/dress_6d38ebdf-a077-54d8-b2cd-fd37cdddfcde.json'
AUTHOR = 'json_to_solo'

class Dress6d38ebdf(Solo48):
    icon_id = 'dress-6d38ebdf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    aliases = ()
    keywords = ('dress', 'clothes')

    def build(self):
        self.add_line('e0', (33, 9), (33, 4))
        self.add_line('e1', (16, 9), (16, 4))
        self.add_arc('e2-1', (33, 9), (34, 11), radius_x=2)
        self.add_line('e2-2', (34, 11), (32, 20))
        self.add_arc('e2-3', (32, 20), (40, 41), radius_x=77)
        self.add_line('e2-4', (40, 41), (24, 44))
        self.add_line('e2-5', (24, 44), (8, 41))
        self.add_arc('e2-6', (8, 41), (12, 29), radius_x=76)
        self.add_arc('e2-7', (12, 29), (16, 21), radius_x=58)
        self.add_arc('e2-8', (16, 21), (15, 12), radius_x=11, sweep=False)
        self.add_arc('e2-9', (15, 12), (16, 9), radius_x=3)
        self.add_arc('e3', (33, 9), (24, 11), radius_x=12, sweep=False)
        self.add_arc('e4', (16, 9), (24, 11), radius_x=9)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e0')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e1')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
