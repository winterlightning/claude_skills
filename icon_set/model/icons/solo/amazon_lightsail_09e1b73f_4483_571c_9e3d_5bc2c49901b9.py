"""Amazon lightsail (programing), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09e1b73f-4483-571c-9e3d-5bc2c49901b9'
SOURCE_PATH = 'icons-json/programing/amazon lightsail_09e1b73f-4483-571c-9e3d-5bc2c49901b9.json'
AUTHOR = 'json_to_solo'

class AmazonLightsail(Solo48):
    icon_id = 'amazon-lightsail'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('amazon', 'lightsail', 'programing')

    def build(self):
        self.add_line('e0', (28, 35), (26, 38))
        self.add_arc('e1-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e1-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_arc('e2-1', (26, 38), (16, 24), radius_x=16, sweep=False)
        self.add_arc('e2-2', (16, 24), (15, 24), radius_x=18, sweep=False)
        self.add_line('e2-3', (15, 24), (22, 19))
        self.add_arc('e2-4', (22, 19), (26, 11), radius_x=18, sweep=False)
        self.add_arc('e2-5', (26, 11), (26, 10), radius_x=23)
        self.add_arc('e2-6', (26, 10), (29, 16), radius_x=50, sweep=False)
        self.add_arc('e2-7', (29, 16), (30, 22), radius_x=27)
        self.add_arc('e2-8', (30, 22), (28, 35), radius_x=27)
        self.add_contour('c0', 'e2-1', 'e2-2', 'e2-3', 'e2-4', 'e2-5', 'e2-6', 'e2-7', 'e2-8', 'e0', closed=True)
        self.add_contour('e1', 'e1-top', 'e1-bottom', closed=True)
