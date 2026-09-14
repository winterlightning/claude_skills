"""Clock (office), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '282df875-ad80-4f27-9f87-f3b69a27f229'
SOURCE_PATH = 'icons-json/office/clock_282df875-ad80-4f27-9f87-f3b69a27f229.json'
AUTHOR = 'json_to_solo'

class Clock282df875(Solo48):
    icon_id = 'clock-282df875'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('clock', 'office')

    def build(self):
        self.add_line('e0', (24, 13), (24, 23))
        self.add_line('e1', (24, 23), (31, 30))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
