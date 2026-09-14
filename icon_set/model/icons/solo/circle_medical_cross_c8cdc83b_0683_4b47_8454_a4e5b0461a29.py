"""Circle medical cross (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8cdc83b-0683-4b47-8454-a4e5b0461a29'
SOURCE_PATH = 'icons-json/state/circle medical cross_c8cdc83b-0683-4b47-8454-a4e5b0461a29.json'
AUTHOR = 'json_to_solo'

class CircleMedicalCross(Solo48):
    icon_id = 'circle-medical-cross'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circle', 'medical', 'cross', 'state')

    def build(self):
        self.add_line('e0', (24, 14), (24, 34))
        self.add_line('e1', (15, 24), (33, 24))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
