"""Amazon connect (programing), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00b02f02-c0d5-4245-8a8e-8f209b070186'
SOURCE_PATH = 'icons-json/programing/amazon connect_00b02f02-c0d5-4245-8a8e-8f209b070186.json'
AUTHOR = 'json_to_solo'

class AmazonConnect(Solo48):
    icon_id = 'amazon-connect'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'connect', 'programing')

    def build(self):
        self.add_arc('sym-e0', (35, 35), (44, 35), radius_x=5)
        self.add_arc('sym-e1', (44, 35), (35, 35), radius_x=5)
        self.add_arc('sym-e2', (13, 35), (4, 35), radius_x=5, sweep=False)
        self.add_arc('sym-e3', (4, 35), (13, 35), radius_x=5, sweep=False)
        self.add_line('sym-e4', (28, 19), (29, 16))
        self.add_arc('sym-e5', (29, 16), (24, 8), radius_x=6, sweep=False)
        self.add_arc('sym-e6', (24, 8), (19, 16), radius_x=7, sweep=False)
        self.add_line('sym-e7', (19, 16), (20, 19))
        self.add_arc('sym-e8', (20, 19), (24, 20), radius_x=7, sweep=False)
        self.add_arc('sym-e9', (24, 20), (28, 19), radius_x=7, sweep=False)
        self.add_line('sym-e10', (28, 19), (36, 30))
        self.add_line('sym-e11', (20, 19), (12, 30))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
