"""Circle (other), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e3029e6-492a-4d27-9967-817241fd3463'
SOURCE_PATH = 'icons-json/other/circle_4e3029e6-492a-4d27-9967-817241fd3463.json'
AUTHOR = 'json_to_solo'

class Circle(Solo48):
    icon_id = 'circle'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('circle', 'other')

    def build(self):
        self.add_arc('e0-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e0-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('e0', 'e0-top', 'e0-bottom', closed=True)
