"""Clock (office), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f37004b-ad82-4bff-ba0a-63d3fdc12e97'
SOURCE_PATH = 'icons-json/office/clock_9f37004b-ad82-4bff-ba0a-63d3fdc12e97.json'
AUTHOR = 'json_to_solo'

class Clock(Solo48):
    icon_id = 'clock'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('clock', 'office')

    def build(self):
        self.add_line('e0', (24, 12), (24, 26))
        self.add_line('e1', (24, 26), (30, 26))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
