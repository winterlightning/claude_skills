"""Batch-03/indoor plant (decoration), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64e98c12-a497-4ac3-ad90-841c585f54e3'
SOURCE_PATH = 'icons-json/decoration/batch-03/indoor plant_64e98c12-a497-4ac3-ad90-841c585f54e3.json'
AUTHOR = 'json_to_solo'

class Batch03IndoorPlantDecoration(Solo48):
    icon_id = 'batch-03-indoor-plant-decoration'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'indoor', 'plant', 'decoration')

    def build(self):
        self.add_line('e0', (38, 27), (15, 27))
        self.add_line('e1', (10, 27), (13, 43))
        self.add_line('e2', (15, 44), (33, 44))
        self.add_line('e3', (34, 42), (36, 27))
        self.add_line('e4', (10, 27), (15, 27))
        self.add_line('e5', (14, 25), (15, 27))
        self.add_line('e6', (33, 25), (30, 27))
        self.add_line('e7', (28, 19), (28, 12))
        self.add_line('e8', (19, 16), (19, 19))
        self.add_line('e9', (13, 43), (15, 44))
        self.add_line('e10', (33, 44), (34, 42))
        self.add_arc('e11-1', (19, 19), (8, 11), radius_x=18, sweep=False)
        self.add_arc('e11-2', (8, 11), (14, 25), radius_x=26, sweep=False)
        self.add_arc('e12-1', (28, 19), (40, 11), radius_x=24)
        self.add_arc('e12-2', (40, 11), (33, 25), radius_x=25)
        self.add_arc('e13-1', (28, 12), (24, 4), radius_x=15, sweep=False)
        self.add_arc('e13-2', (24, 4), (19, 16), radius_x=17, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e9', 'e2', 'e10', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e11-1', 'e11-2', 'e5')
        self.add_contour('c4', 'e12-1', 'e12-2', 'e6')
        self.add_contour('c5', 'e7', 'e13-1', 'e13-2', 'e8')
        self.relate('connect', 'c4', 'c0')
