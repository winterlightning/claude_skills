"""Brain (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f98adc76-41e4-410a-a9e9-a02974009658'
SOURCE_PATH = 'icons-json/artificial-intelligence/brain_f98adc76-41e4-410a-a9e9-a02974009658.json'
AUTHOR = 'json_to_solo'

class Brain(Solo48):
    icon_id = 'brain'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('brain', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (23, 11), (21, 15))
        self.add_arc('e1-1', (23, 11), (13, 10), radius_x=8, sweep=False)
        self.add_arc('e1-2', (13, 10), (9, 18), radius_x=10, sweep=False)
        self.add_line('e1-3', (9, 18), (5, 22))
        self.add_line('e1-4', (5, 22), (4, 27))
        self.add_arc('e1-5', (4, 27), (9, 35), radius_x=9, sweep=False)
        self.add_line('e1-6', (9, 35), (16, 35))
        self.add_arc('e1-7', (16, 35), (25, 38), radius_x=7, sweep=False)
        self.add_line('e1-8', (25, 38), (28, 36))
        self.add_arc('e2-1', (23, 11), (26, 9), radius_x=17)
        self.add_line('e2-2', (26, 9), (30, 8))
        self.add_arc('e2-3', (30, 8), (34, 10), radius_x=5)
        self.add_line('e2-4', (34, 10), (36, 15))
        self.add_arc('e2-5', (36, 15), (43, 20), radius_x=8)
        self.add_arc('e2-6', (43, 20), (44, 24), radius_x=10, sweep=False)
        self.add_line('e2-7', (44, 24), (41, 35))
        self.add_arc('e2-8', (41, 35), (34, 40), radius_x=8)
        self.add_arc('e2-9', (34, 40), (29, 22), radius_x=11)
        self.add_line('e3', (21, 15), (19, 22))
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e1-6', 'e1-7', 'e1-8')
        self.add_contour('c1', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e2-9')
        self.add_contour('c2', 'e0', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
