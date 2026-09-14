"""Amazon connect (programing), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00b02f02-c0d5-4245-8a8e-8f209b070186'
SOURCE_PATH = 'icons-json/programing/amazon connect_00b02f02-c0d5-4245-8a8e-8f209b070186.json'
AUTHOR = 'json_to_solo'

class AmazonConnectPrograming(Solo48):
    icon_id = 'amazon-connect-programing'
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
        self.add_bezier('sym-e4', (28, 19), ((28.536, 17.93), (28.773, 17.22), (29, 16)))
        self.add_bezier('sym-e5', (29, 16), ((29.662, 12.516), (27.454, 8), (24, 8)))
        self.add_bezier('sym-e6', (24, 8), ((20.546, 8), (18.338, 12.516), (19, 16)))
        self.add_bezier('sym-e7', (19, 16), ((19.227, 17.22), (19.464, 17.93), (20, 19)))
        self.add_bezier('sym-e8', (20, 19), ((21.609, 19.925), (22.986, 20), (24, 20)))
        self.add_bezier('sym-e9', (24, 20), ((25.014, 20), (26.391, 19.925), (28, 19)))
        self.add_line('sym-e10', (28, 19), (36, 30))
        self.add_line('sym-e11', (20, 19), (12, 30))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', closed=True)
        self.add_contour('sym-c2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c2', 'sym-c3')
