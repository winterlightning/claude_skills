"""Clock (office), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7f654f6-570d-40dd-84e5-be7ff0923e87'
SOURCE_PATH = 'icons-json/office/clock_e7f654f6-570d-40dd-84e5-be7ff0923e87.json'
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
        self.add_line('e0', (12, 24), (24, 24))
        self.add_line('e1', (24, 24), (24, 33))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
