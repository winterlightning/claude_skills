"""Square circle (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '572c8adc-4237-4879-b02b-30d084c17f24'
SOURCE_PATH = 'icons-json/state/square circle_572c8adc-4237-4879-b02b-30d084c17f24.json'
AUTHOR = 'json_to_solo'

class SquareCircle(Solo48):
    icon_id = 'square-circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('square', 'circle', 'state')

    def build(self):
        self.add_line('e0', (17, 31), (17, 17))
        self.add_line('e1', (17, 17), (31, 17))
        self.add_line('e2', (31, 17), (31, 31))
        self.add_line('e3', (31, 31), (17, 31))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
