"""Wave forward (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e127ddf8-ee9b-5545-b197-daeac78ecea8'
SOURCE_PATH = 'icons-json/interface-essential/wave forward_e127ddf8-ee9b-5545-b197-daeac78ecea8.json'
AUTHOR = 'json_to_solo'

class WaveForwardE127ddf8(Solo48):
    icon_id = 'wave-forward-e127ddf8'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('wave', 'forward', 'interface-essential')

    def build(self):
        self.add_bezier('sym-e0', (40, 24), ((40, 23.64), (40, 23.361), (40, 23)))
        self.add_bezier('sym-e1', (40, 23), ((40, 18.482), (36.984, 13.882), (33, 10)))
        self.add_bezier('sym-e2', (33, 10), ((31.016, 8.082), (28.384, 5.755), (26, 4)))
        self.add_bezier('sym-e3', (26, 4), ((25.776, 4), (26.24, 4.155), (26, 4)))
        self.add_bezier('sym-e4', (8, 11), ((8.928, 11.636), (10.136, 12.3), (11, 13)))
        self.add_bezier('sym-e5', (11, 13), ((14.891, 16.114), (17, 20.173), (17, 24)))
        self.add_bezier('sym-e6', (17, 24), ((17, 27.827), (14.891, 31.886), (11, 35)))
        self.add_bezier('sym-e7', (11, 35), ((10.136, 35.7), (8.928, 36.364), (8, 37)))
        self.add_bezier('sym-e8', (40, 24), ((40, 24.36), (40, 24.639), (40, 25)))
        self.add_bezier('sym-e9', (40, 25), ((40, 29.518), (36.984, 34.118), (33, 38)))
        self.add_bezier('sym-e10', (33, 38), ((31.016, 39.918), (28.384, 42.245), (26, 44)))
        self.add_bezier('sym-e11', (26, 44), ((25.776, 44), (26.24, 43.845), (26, 44)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3')
        self.add_contour('sym-c1', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c2', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11')
        self.relate('connect', 'sym-c0', 'sym-c2')
