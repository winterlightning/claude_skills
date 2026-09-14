"""Side road angle left (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3475f12-e1df-4f38-887e-94114fb8029a'
SOURCE_PATH = 'icons-json/transportation/side road angle left_a3475f12-e1df-4f38-887e-94114fb8029a.json'
AUTHOR = 'json_to_solo'

class SideRoadAngleLeft(Solo48):
    icon_id = 'side-road-angle-left'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('side', 'road', 'angle', 'left', 'transportation')

    def build(self):
        self.add_line('e0', (40, 4), (40, 29))
        self.add_line('e1', (8, 16), (40, 29))
        self.add_line('e2', (40, 44), (40, 29))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
