"""Clock (office), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ab76b4c-c88a-4586-b84f-4ffd7244d650'
SOURCE_PATH = 'icons-json/office/clock_4ab76b4c-c88a-4586-b84f-4ffd7244d650.json'
AUTHOR = 'json_to_solo'

class Clock4ab76b4c(Solo48):
    icon_id = 'clock-4ab76b4c'
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
