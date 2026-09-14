"""Filter setting three controller (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9c465cc-a00b-5072-935a-cefba43750ea'
SOURCE_PATH = 'icons-json/interface-essential/filter setting three controller_a9c465cc-a00b-5072-935a-cefba43750ea.json'
AUTHOR = 'json_to_solo'

class FilterSettingThreeControllerInterfaceEssential(Solo48):
    icon_id = 'filter-setting-three-controller-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('filter', 'setting', 'three', 'controller', 'interface-essential')

    def build(self):
        self.add_line('e0', (37, 11), (42, 11))
        self.add_line('e1', (6, 11), (27, 11))
        self.add_line('e2', (6, 24), (13, 24))
        self.add_line('e3', (22, 24), (42, 24))
        self.add_line('e4', (37, 37), (42, 37))
        self.add_line('e5', (27, 37), (6, 37))
        self.add_arc('e6-top', (27, 11), (37, 11), radius_x=5)
        self.add_arc('e6-bottom', (37, 11), (27, 11), radius_x=5)
        self.add_arc('e7-top', (27, 37), (37, 37), radius_x=5)
        self.add_arc('e7-bottom', (37, 37), (27, 37), radius_x=5)
        self.add_arc('e8-top', (12, 24), (22, 24), radius_x=5)
        self.add_arc('e8-bottom', (22, 24), (12, 24), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.add_contour('e7', 'e7-top', 'e7-bottom', closed=True)
        self.relate('connect', 'c0', 'e6')
        self.relate('connect', 'c1', 'e6')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c4', 'e7')
        self.relate('connect', 'c5', 'e7')
