"""0 text in circle (state), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3714f65-499d-4ba7-9ecb-87ecc26acfff'
SOURCE_PATH = 'icons-json/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.json'
AUTHOR = 'json_to_solo'

class Icon0TextInCircleState(Solo48):
    icon_id = 'icon-0-text-in-circle-state'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('text', 'in', 'circle', 'state')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_bezier('sym-e2', (24, 12), ((29.568, 12.072), (31, 19.296), (31, 24)))
        self.add_bezier('sym-e3', (31, 24), ((31, 24.004), (31, 23.996), (31, 24)))
        self.add_bezier('sym-e4', (31, 24), ((31, 24.004), (31, 23.996), (31, 24)))
        self.add_bezier('sym-e5', (31, 24), ((31, 28.704), (29.568, 35.928), (24, 36)))
        self.add_bezier('sym-e6', (24, 36), ((18.432, 35.928), (17, 28.704), (17, 24)))
        self.add_bezier('sym-e7', (17, 24), ((17, 23.996), (17, 24.004), (17, 24)))
        self.add_bezier('sym-e8', (17, 24), ((17, 23.996), (17, 24.004), (17, 24)))
        self.add_bezier('sym-e9', (17, 24), ((17, 19.296), (18.432, 12.072), (24, 12)))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', closed=True)
