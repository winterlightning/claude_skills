"""Two image (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00bf1033-7ed9-48a1-92ef-7122ca973175'
SOURCE_PATH = 'icons-json/state/two image_00bf1033-7ed9-48a1-92ef-7122ca973175.json'
AUTHOR = 'json_to_solo'

class TwoImageState(Solo48):
    icon_id = 'two-image-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('two', 'image', 'state')

    def build(self):
        self.add_line('e0', (44, 40), (4, 40))
        self.add_line('e1', (8, 40), (17, 23))
        self.add_line('e2', (17, 23), (23, 35))
        self.add_line('e3', (23, 35), (31, 20))
        self.add_line('e4', (31, 20), (42, 40))
        self.add_line('e5', (4, 40), (4, 8))
        self.add_line('e6', (4, 8), (43, 8))
        self.add_line('e7', (43, 8), (44, 40))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e3', 'e4')
        self.add_contour('c2', 'e5', 'e6', 'e7')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
