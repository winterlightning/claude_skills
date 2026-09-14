"""Batch-05/cane (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '452652a0-5003-51e7-a93d-97446081686f'
SOURCE_PATH = 'icons-json/accessories/batch-05/cane_452652a0-5003-51e7-a93d-97446081686f.json'
AUTHOR = 'json_to_solo'

class Batch05Cane(Solo48):
    icon_id = 'batch-05-cane'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'cane', 'accessories')

    def build(self):
        self.add_line('e0', (40, 11), (40, 44))
        self.add_arc('e1-1', (8, 11), (11, 7), radius_x=5)
        self.add_arc('e1-2', (11, 7), (16, 5), radius_x=18)
        self.add_arc('e1-3', (16, 5), (23, 4), radius_x=27)
        self.add_line('e1-4', (23, 4), (32, 5))
        self.add_arc('e1-5', (32, 5), (40, 11), radius_x=10)
        self.add_contour('c0', 'e1-1', 'e1-2', 'e1-3', 'e1-4', 'e1-5', 'e0')
