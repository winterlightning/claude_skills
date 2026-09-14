"""Side road angle right (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25347198-3f9f-4498-af06-d3003038e769'
SOURCE_PATH = 'icons-json/transportation/side road angle right_25347198-3f9f-4498-af06-d3003038e769.json'
AUTHOR = 'json_to_solo'

class SideRoadAngleRight25347198(Solo48):
    icon_id = 'side-road-angle-right-25347198'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('side', 'road', 'angle', 'right', 'transportation')

    def build(self):
        self.add_line('e0', (8, 4), (8, 29))
        self.add_line('e1', (8, 44), (8, 29))
        self.add_line('e2', (40, 16), (8, 29))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
