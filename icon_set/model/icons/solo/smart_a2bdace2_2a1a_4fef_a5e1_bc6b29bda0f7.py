"""Smart (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7'
SOURCE_PATH = 'icons-json/state/smart_a2bdace2-2a1a-4fef-a5e1-bc6b29bda0f7.json'
AUTHOR = 'json_to_solo'

class Smart(Solo48):
    icon_id = 'smart'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('smart', 'state')

    def build(self):
        self.add_arc('sym-e0', (24, 8), (25, 8), radius_x=1, sweep=False)
        self.add_line('sym-e1', (25, 8), (29, 9))
        self.add_arc('sym-e2', (29, 9), (44, 19), radius_x=28)
        self.add_arc('sym-e3', (24, 23), (38, 30), radius_x=18)
        self.add_arc('sym-e4', (24, 37), (30, 40), radius_x=9)
        self.add_arc('sym-e5', (24, 8), (23, 8), radius_x=1)
        self.add_line('sym-e6', (23, 8), (19, 9))
        self.add_arc('sym-e7', (19, 9), (4, 19), radius_x=28, sweep=False)
        self.add_arc('sym-e8', (24, 23), (10, 30), radius_x=18, sweep=False)
        self.add_arc('sym-e9', (24, 37), (18, 40), radius_x=9, sweep=False)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2')
        self.add_contour('sym-c1', 'sym-e3')
        self.add_contour('sym-c2', 'sym-e4')
        self.add_contour('sym-c3', 'sym-e5', 'sym-e6', 'sym-e7')
        self.add_contour('sym-c4', 'sym-e8')
        self.add_contour('sym-c5', 'sym-e9')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c4')
        self.relate('connect', 'sym-c2', 'sym-c5')
