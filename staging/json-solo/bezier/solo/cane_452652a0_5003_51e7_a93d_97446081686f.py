"""Batch-05/cane (accessories), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
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
        self.add_bezier('e1', (8, 11), ((8.02, 10.936), (8.02, 11.145), (8.04, 11.082)), ((8.04, 7.464), (14.92, 4), (23.06, 4)), ((23.063, 4), (23.066, 4), (23.068, 4)), ((23.245, 4), (23.403, 4), (23.58, 4)), ((23.9, 4), (24.24, 4.009), (24.56, 4.009)), ((32.5, 4.009), (40, 7.427), (40, 11)))
        self.add_contour('c0', 'e1', 'e0')
