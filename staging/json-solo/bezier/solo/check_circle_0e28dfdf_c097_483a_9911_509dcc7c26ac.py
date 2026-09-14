"""Check circle (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e28dfdf-c097-483a-9911-509dcc7c26ac'
SOURCE_PATH = 'icons-json/interface-essential/check circle_0e28dfdf-c097-483a-9911-509dcc7c26ac.json'
AUTHOR = 'json_to_solo'

class CheckCircleInterfaceEssential(Solo48):
    icon_id = 'check-circle-interface-essential'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('check', 'circle', 'interface-essential')

    def build(self):
        self.add_line('e0', (32, 15), (19, 31))
        self.add_line('e1', (19, 31), (14, 27))
        self.add_arc('e2-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e2-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('e2', 'e2-top', 'e2-bottom', closed=True)
