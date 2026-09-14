"""Boat engine 1 (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8628f907-a81e-4a5c-8744-e254e02cde48'
SOURCE_PATH = 'icons-json/transportation/boat engine 1_8628f907-a81e-4a5c-8744-e254e02cde48.json'
AUTHOR = 'json_to_solo'

class BoatEngine1(Solo48):
    icon_id = 'boat-engine-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('boat', 'engine', 'transportation')

    def build(self):
        self.add_line('e0', (8, 16), (18, 16))
        self.add_line('e1', (38, 43), (38, 38))
        self.add_line('e2', (38, 33), (38, 38))
        self.add_line('e3', (26, 20), (26, 39))
        self.add_line('e4', (32, 44), (32, 38))
        self.add_line('e5', (26, 20), (32, 20))
        self.add_line('e6', (26, 20), (20, 20))
        self.add_line('e7', (32, 38), (38, 38))
        self.add_line('e8', (32, 38), (32, 20))
        self.add_line('e9', (32, 20), (38, 20))
        self.add_line('e10', (40, 19), (40, 10))
        self.add_line('e11', (34, 4), (21, 4))
        self.add_line('e12', (18, 7), (18, 16))
        self.add_arc('e13-1', (26, 39), (31, 44), radius_x=5, sweep=False)
        self.add_arc('e13-2', (31, 44), (32, 44), radius_x=33)
        self.add_arc('e14', (20, 20), (18, 16), radius_x=3)
        self.add_arc('e15', (38, 20), (40, 19), radius_x=2, sweep=False)
        self.add_arc('e16', (40, 10), (34, 4), radius_x=7, sweep=False)
        self.add_arc('e17', (21, 4), (18, 7), radius_x=3, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e13-1', 'e13-2', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6', 'e14')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e8')
        self.add_contour('c8', 'e9', 'e15', 'e10', 'e16', 'e11', 'e17', 'e12')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c7', 'c8')
