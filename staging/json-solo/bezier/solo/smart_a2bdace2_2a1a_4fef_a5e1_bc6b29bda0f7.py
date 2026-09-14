"""Smart (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7'
SOURCE_PATH = 'icons-json/state/smart_a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7.json'
AUTHOR = 'json_to_solo'

class SmartState(Solo48):
    icon_id = 'smart-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('smart', 'state')

    def build(self):
        self.add_bezier('sym-e0', (24, 8), ((24.33, 8), (24.668, 8), (25, 8)))
        self.add_bezier('sym-e1', (25, 8), ((26.227, 8), (27.791, 8.717), (29, 9)))
        self.add_bezier('sym-e2', (29, 9), ((35.218, 10.44), (39.318, 13.4), (44, 19)))
        self.add_bezier('sym-e3', (24, 23), ((29.537, 23), (33.747, 25.213), (38, 30)))
        self.add_bezier('sym-e4', (24, 37), ((26.139, 37), (27.914, 38.135), (30, 40)))
        self.add_bezier('sym-e5', (24, 8), ((23.67, 8), (23.332, 8), (23, 8)))
        self.add_bezier('sym-e6', (23, 8), ((21.773, 8), (20.209, 8.717), (19, 9)))
        self.add_bezier('sym-e7', (19, 9), ((12.782, 10.44), (8.682, 13.4), (4, 19)))
        self.add_bezier('sym-e8', (24, 23), ((18.463, 23), (14.253, 25.213), (10, 30)))
        self.add_bezier('sym-e9', (24, 37), ((21.861, 37), (20.086, 38.135), (18, 40)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c4', 'sym-e8')
        self.add_contour('sym-c5', 'sym-e9')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c5')
