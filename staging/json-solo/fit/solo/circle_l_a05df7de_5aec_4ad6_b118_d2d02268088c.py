"""Circle l (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a05df7de-5aec-4ad6-b118-d2d02268088c'
SOURCE_PATH = 'icons-json/state/circle L_a05df7de-5aec-4ad6-b118-d2d02268088c.json'
AUTHOR = 'json_to_solo'

class CircleLState(Solo48):
    icon_id = 'circle-l-state'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circle', 'l', 'state')

    def build(self):
        self.add_line('e0', (19, 14), (19, 34))
        self.add_line('e1', (19, 34), (29, 34))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
