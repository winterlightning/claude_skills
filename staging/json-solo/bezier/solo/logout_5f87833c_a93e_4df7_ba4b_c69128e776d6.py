"""Logout (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. CIRCLE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f87833c-a93e-4df7-ba4b-c69128e776d6'
SOURCE_PATH = 'icons-json/interface-essential/logout_5f87833c-a93e-4df7-ba4b-c69128e776d6.json'
AUTHOR = 'json_to_solo'

class LogoutInterfaceEssential(Solo48):
    icon_id = 'logout-interface-essential'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('logout', 'interface-essential')

    def build(self):
        self.add_line('e0', (27, 17), (34, 24))
        self.add_line('e1', (12, 24), (34, 24))
        self.add_line('e2', (28, 31), (34, 24))
        self.add_arc('e3-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e3-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
