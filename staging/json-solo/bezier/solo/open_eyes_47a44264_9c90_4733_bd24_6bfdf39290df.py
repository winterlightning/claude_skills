"""Open eyes (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '47a44264-9c90-4733-bd24-6bfdf39290df'
SOURCE_PATH = 'icons-json/interface-essential/open eyes_47a44264-9c90-4733-bd24-6bfdf39290df.json'
AUTHOR = 'json_to_solo'

class OpenEyesInterfaceEssential(Solo48):
    icon_id = 'open-eyes-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('open', 'eyes', 'interface-essential')

    def build(self):
        self.add_arc('sym-e0', (19, 24), (29, 24), radius_x=5, radius_y=7)
        self.add_arc('sym-e1', (29, 24), (19, 24), radius_x=5, radius_y=7)
        self.add_bezier('sym-e2', (4, 24), ((4.097, 23.224), (7.482, 19.666), (8, 19)))
        self.add_bezier('sym-e3', (8, 19), ((11.882, 13.966), (17.418, 8), (23, 8)))
        self.add_bezier('sym-e4', (23, 8), ((23.155, 8), (23.845, 8), (24, 8)))
        self.add_bezier('sym-e5', (24, 8), ((24.101, 8), (23.9, 8), (24, 8)))
        self.add_bezier('sym-e6', (24, 8), ((24.1, 8), (23.899, 8), (24, 8)))
        self.add_bezier('sym-e7', (24, 8), ((24.155, 8), (24.845, 8), (25, 8)))
        self.add_bezier('sym-e8', (25, 8), ((30.582, 8), (36.118, 13.966), (40, 19)))
        self.add_bezier('sym-e9', (40, 19), ((40.518, 19.666), (43.903, 23.224), (44, 24)))
        self.add_bezier('sym-e10', (44, 24), ((43.903, 24.776), (40.518, 28.334), (40, 29)))
        self.add_bezier('sym-e11', (40, 29), ((36.118, 34.034), (30.582, 40), (25, 40)))
        self.add_bezier('sym-e12', (25, 40), ((24.845, 40), (24.155, 40), (24, 40)))
        self.add_bezier('sym-e13', (24, 40), ((23.899, 40), (24.1, 40), (24, 40)))
        self.add_bezier('sym-e14', (24, 40), ((23.9, 40), (24.101, 40), (24, 40)))
        self.add_bezier('sym-e15', (24, 40), ((23.845, 40), (23.155, 40), (23, 40)))
        self.add_bezier('sym-e16', (23, 40), ((17.418, 40), (11.882, 34.034), (8, 29)))
        self.add_bezier('sym-e17', (8, 29), ((7.482, 28.334), (4.097, 24.776), (4, 24)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', closed=True)
