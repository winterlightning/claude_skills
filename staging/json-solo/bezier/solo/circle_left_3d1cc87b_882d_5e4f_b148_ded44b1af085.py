"""Circle left (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d1cc87b-882d-5e4f-b148-ded44b1af085'
SOURCE_PATH = 'icons-json/arrows/circle left_3d1cc87b-882d-5e4f-b148-ded44b1af085.json'
AUTHOR = 'json_to_solo'

class CircleLeftArrows(Solo48):
    icon_id = 'circle-left-arrows'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('circle', 'left', 'arrows')

    def build(self):
        self.add_line('e0', (27, 13), (16, 24))
        self.add_line('e1', (16, 24), (27, 35))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
