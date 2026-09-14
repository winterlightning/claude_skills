"""Bed (state), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '300dd66a-1ed3-4055-80d4-1d8fabe4b3ef'
SOURCE_PATH = 'icons-json/state/bed_300dd66a-1ed3-4055-80d4-1d8fabe4b3ef.json'
AUTHOR = 'json_to_solo'

class Bed(Solo48):
    icon_id = 'bed'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('bed', 'state')

    def build(self):
        self.add_line('e0', (44, 23), (4, 23))
        self.add_line('e1', (44, 34), (4, 34))
        self.add_line('e2', (4, 33), (4, 8))
        self.add_line('e3', (4, 40), (4, 33))
        self.add_line('e4', (44, 40), (44, 23))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c3')
