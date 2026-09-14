"""Side road right (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09dd7323-0233-4075-aa09-8cbb5b7868be'
SOURCE_PATH = 'icons-json/transportation/side road right_09dd7323-0233-4075-aa09-8cbb5b7868be.json'
AUTHOR = 'json_to_solo'

class SideRoadRight(Solo48):
    icon_id = 'side-road-right'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('side', 'road', 'right', 'transportation')

    def build(self):
        self.add_line('e0', (8, 44), (8, 4))
        self.add_line('e1', (40, 24), (8, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.relate('connect', 'c1', 'c0')
