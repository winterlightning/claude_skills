"""0 text in circle (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e3714f65-499d-4ba7-9ecb-87ecc26acfff'
SOURCE_PATH = 'icons-json/state/0 text in circle_e3714f65-499d-4ba7-9ecb-87ecc26acfff.json'
AUTHOR = 'json_to_solo'

class Icon0TextInCircle(Solo48):
    icon_id = 'icon-0-text-in-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('text', 'in', 'circle', 'state')

    def build(self):
        self.add_arc('sym-e0', (4, 24), (44, 24), radius_x=20)
        self.add_arc('sym-e1', (44, 24), (4, 24), radius_x=20)
        self.add_arc('sym-e2', (24, 12), (31, 24), radius_x=10)
        self.add_arc('sym-e5', (31, 24), (24, 36), radius_x=10)
        self.add_arc('sym-e6', (24, 36), (17, 24), radius_x=10)
        self.add_arc('sym-e9', (17, 24), (24, 12), radius_x=10)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', closed=True)
        self.add_contour('sym-c1', 'sym-e2', 'sym-e5', 'sym-e6', 'sym-e9', closed=True)
