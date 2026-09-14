"""Circle equal (state), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '204ecec0-870d-4feb-9da5-e8ed98b8f9c3'
SOURCE_PATH = 'icons-json/state/circle equal_204ecec0-870d-4feb-9da5-e8ed98b8f9c3.json'
AUTHOR = 'json_to_solo'

class CircleEqual(Solo48):
    icon_id = 'circle-equal'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('circle', 'equal', 'state')

    def build(self):
        self.add_line('e0', (14, 19), (34, 19))
        self.add_line('e1', (14, 29), (34, 29))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
