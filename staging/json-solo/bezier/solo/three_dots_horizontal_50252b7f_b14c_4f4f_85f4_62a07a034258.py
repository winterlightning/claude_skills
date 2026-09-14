"""Three dots horizontal (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50252b7f-b14c-4f4f-85f4-62a07a034258'
SOURCE_PATH = 'icons-json/state/three dots horizontal_50252b7f-b14c-4f4f-85f4-62a07a034258.json'
AUTHOR = 'json_to_solo'

class ThreeDotsHorizontalState(Solo48):
    icon_id = 'three-dots-horizontal-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('three', 'dots', 'horizontal', 'state')

    def build(self):
        self.add_line('sym-e0', (24, 24), (24, 24))
        self.add_line('sym-e1', (24, 40), (40, 40))
        self.add_bezier('sym-e2', (40, 40), ((40.164, 40), (40.845, 40), (41, 40)))
        self.add_bezier('sym-e3', (41, 40), ((42.445, 40), (44, 38.117), (44, 36)))
        self.add_line('sym-e4', (44, 36), (44, 12))
        self.add_bezier('sym-e5', (44, 12), ((44, 10.351), (42.827, 8.948), (42, 8)))
        self.add_line('sym-e6', (42, 8), (24, 8))
        self.add_line('sym-e7', (24, 8), (6, 8))
        self.add_bezier('sym-e8', (6, 8), ((5.173, 8.948), (4, 10.351), (4, 12)))
        self.add_line('sym-e9', (4, 12), (4, 36))
        self.add_bezier('sym-e10', (4, 36), ((4, 38.117), (5.555, 40), (7, 40)))
        self.add_bezier('sym-e11', (7, 40), ((7.155, 40), (7.836, 40), (8, 40)))
        self.add_line('sym-e12', (8, 40), (24, 40))
        self.add_line('sym-e13', (35, 24), (35, 24))
        self.add_line('sym-e14', (13, 24), (13, 24))
        self.add_contour('sym-c0', 'sym-e0', closed=True)
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', closed=True)
        self.add_contour('sym-c2', 'sym-e13')
        self.add_contour('sym-c3', 'sym-e14')
