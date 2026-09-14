"""Check button (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f826881-ddfc-5ecd-bbde-0b3edbefde50'
SOURCE_PATH = 'icons-json/interface-essential/check button_1f826881-ddfc-5ecd-bbde-0b3edbefde50.json'
AUTHOR = 'json_to_solo'

class CheckButton(Solo48):
    icon_id = 'check-button'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('check', 'button', 'interface-essential')

    def build(self):
        self.add_line('e0', (36, 18), (27, 31))
        self.add_line('e1', (27, 31), (22, 24))
        self.add_line('e2', (4, 38), (4, 10))
        self.add_line('e3', (6, 8), (42, 8))
        self.add_line('e4', (44, 10), (44, 38))
        self.add_line('e5', (42, 40), (7, 40))
        self.add_line('e6', (4, 10), (6, 8))
        self.add_arc('e7', (42, 8), (44, 10), radius_x=2)
        self.add_line('e8', (44, 38), (42, 40))
        self.add_line('e9', (7, 40), (4, 38))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
