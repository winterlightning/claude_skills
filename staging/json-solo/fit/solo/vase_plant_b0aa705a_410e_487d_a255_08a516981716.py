"""Batch-05/vase plant (decoration), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b0aa705a-410e-487d-a255-08a516981716'
SOURCE_PATH = 'icons-json/decoration/batch-05/vase plant_b0aa705a-410e-487d-a255-08a516981716.json'
AUTHOR = 'json_to_solo'

class Batch05VasePlant(Solo48):
    icon_id = 'batch-05-vase-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'vase', 'plant', 'decoration')

    def build(self):
        self.add_line('e0', (24, 29), (24, 31))
        self.add_line('e1', (24, 29), (22, 21))
        self.add_line('e2', (22, 21), (18, 17))
        self.add_line('e3', (24, 29), (28, 21))
        self.add_line('e4', (28, 21), (30, 17))
        self.add_line('e5', (30, 17), (29, 11))
        self.add_line('e6', (19, 12), (18, 17))
        self.add_line('e7', (24, 31), (10, 31))
        self.add_line('e8', (10, 31), (10, 40))
        self.add_line('e9', (15, 44), (33, 44))
        self.add_line('e10', (38, 40), (38, 31))
        self.add_line('e11', (38, 31), (24, 31))
        self.add_arc('e12-1', (18, 17), (12, 11), radius_x=34, sweep=False)
        self.add_line('e12-2', (12, 11), (8, 9))
        self.add_line('e12-3', (8, 9), (8, 10))
        self.add_line('e12-4', (8, 10), (9, 19))
        self.add_arc('e12-5', (9, 19), (14, 31), radius_x=41, sweep=False)
        self.add_arc('e13-1', (34, 31), (40, 11), radius_x=37, sweep=False)
        self.add_arc('e13-2', (40, 11), (40, 9), radius_x=27)
        self.add_arc('e13-3', (40, 9), (39, 9), radius_x=1, sweep=False)
        self.add_arc('e13-4', (39, 9), (30, 17), radius_x=30, sweep=False)
        self.add_arc('e14-1', (29, 11), (24, 4), radius_x=19, sweep=False)
        self.add_arc('e14-2', (24, 4), (19, 12), radius_x=20, sweep=False)
        self.add_arc('e15', (10, 40), (15, 44), radius_x=6, sweep=False)
        self.add_arc('e16', (33, 44), (38, 40), radius_x=6, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e12-1', 'e12-2', 'e12-3', 'e12-4', 'e12-5')
        self.add_contour('c4', 'e13-1', 'e13-2', 'e13-3', 'e13-4')
        self.add_contour('c5', 'e5', 'e14-1', 'e14-2', 'e6')
        self.add_contour('c6', 'e7', 'e8', 'e15', 'e9', 'e16', 'e10', 'e11', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c6')
