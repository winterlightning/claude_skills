"""Ceiling lamp double (lamps), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '326638cb-38f2-5e62-8dca-bfeecd92203f'
SOURCE_PATH = 'icons-json/lamps/ceiling lamp double_326638cb-38f2-5e62-8dca-bfeecd92203f.json'
AUTHOR = 'json_to_solo'

class CeilingLampDoubleLamps(Solo48):
    icon_id = 'ceiling-lamp-double-lamps'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'lamps'
    aliases = ()
    keywords = ('ceiling', 'lamp', 'double', 'lamps')

    def build(self):
        self.add_line('sym-e0', (36, 8), (24, 8))
        self.add_line('sym-e1', (24, 8), (12, 8))
        self.add_line('sym-e2', (24, 20), (24, 8))
        self.add_line('sym-e3', (24, 20), (14, 20))
        self.add_bezier('sym-e4', (14, 20), ((12.036, 20), (10, 22.305), (10, 25)))
        self.add_line('sym-e5', (10, 25), (10, 30))
        self.add_bezier('sym-e6', (10, 30), ((10.039, 29.999), (9.962, 30), (10, 30)))
        self.add_bezier('sym-e7', (10, 30), ((14.173, 30), (15.658, 35.487), (16, 40)))
        self.add_line('sym-e8', (16, 40), (4, 40))
        self.add_bezier('sym-e9', (4, 40), ((4.009, 39.914), (4, 40), (4, 40)))
        self.add_bezier('sym-e10', (4, 40), ((4, 34.892), (6.1, 30.098), (10, 30)))
        self.add_line('sym-e11', (24, 20), (34, 20))
        self.add_bezier('sym-e12', (34, 20), ((35.964, 20), (38, 22.305), (38, 25)))
        self.add_line('sym-e13', (38, 25), (38, 30))
        self.add_bezier('sym-e14', (38, 30), ((37.961, 29.999), (38.038, 30), (38, 30)))
        self.add_bezier('sym-e15', (38, 30), ((33.827, 30), (32.342, 35.487), (32, 40)))
        self.add_line('sym-e16', (32, 40), (44, 40))
        self.add_bezier('sym-e17', (44, 40), ((43.991, 39.914), (44, 40), (44, 40)))
        self.add_bezier('sym-e18', (44, 40), ((44, 34.892), (41.9, 30.098), (38, 30)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2')
        self.add_contour('sym-c2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10')
        self.add_contour('sym-c3', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
