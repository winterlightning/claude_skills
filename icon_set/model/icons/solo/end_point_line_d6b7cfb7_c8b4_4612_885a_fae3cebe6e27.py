"""End point line (devices), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6b7cfb7-c8b4-4612-885a-fae3cebe6e27'
SOURCE_PATH = 'icons-json/devices/end point line_d6b7cfb7-c8b4-4612-885a-fae3cebe6e27.json'
AUTHOR = 'json_to_solo'

class EndPointLine(Solo48):
    icon_id = 'end-point-line'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    aliases = ()
    keywords = ('end', 'point', 'line', 'devices')

    def build(self):
        self.add_line('e0', (44, 8), (44, 24))
        self.add_line('e1', (4, 24), (44, 24))
        self.add_line('e2', (44, 40), (44, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
