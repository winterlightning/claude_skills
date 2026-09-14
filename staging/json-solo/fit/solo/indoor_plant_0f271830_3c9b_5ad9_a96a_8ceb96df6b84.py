"""Batch-03/indoor plant (decoration), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0f271830-3c9b-5ad9-a96a-8ceb96df6b84'
SOURCE_PATH = 'icons-json/decoration/batch-03/indoor plant_0f271830-3c9b-5ad9-a96a-8ceb96df6b84.json'
AUTHOR = 'json_to_solo'

class Batch03IndoorPlant(Solo48):
    icon_id = 'batch-03-indoor-plant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('batch', 'indoor', 'plant', 'decoration')

    def build(self):
        self.add_line('e0', (34, 23), (28, 29))
        self.add_line('e1', (31, 44), (19, 44))
        self.add_line('e2', (13, 40), (12, 29))
        self.add_line('e3', (12, 29), (36, 29))
        self.add_line('e4', (36, 29), (35, 40))
        self.add_arc('e5-1', (22, 29), (8, 11), radius_x=21)
        self.add_line('e5-2', (8, 11), (8, 10))
        self.add_arc('e6-1', (26, 19), (24, 4), radius_x=12, sweep=False)
        self.add_arc('e6-2', (24, 4), (22, 19), radius_x=12, sweep=False)
        self.add_arc('e7-1', (26, 19), (40, 11), radius_x=22)
        self.add_arc('e7-2', (40, 11), (34, 23), radius_x=15)
        self.add_arc('e8', (22, 19), (8, 10), radius_x=28, sweep=False)
        self.add_arc('e9', (35, 40), (31, 44), radius_x=4)
        self.add_arc('e10', (19, 44), (13, 40), radius_x=7)
        self.add_contour('c0', 'e5-1', 'e5-2')
        self.add_contour('c1', 'e6-1', 'e6-2')
        self.add_contour('c2', 'e7-1', 'e7-2', 'e0')
        self.add_contour('c3', 'e8')
        self.add_contour('c4', 'e9', 'e1', 'e10', 'e2', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c2', 'c4')
