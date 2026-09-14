"""Filter setting two controller (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '92577e4c-a752-598a-8a53-eca897b2e3f8'
SOURCE_PATH = 'icons-json/interface-essential/filter setting two controller_92577e4c-a752-598a-8a53-eca897b2e3f8.json'
AUTHOR = 'json_to_solo'

class FilterSettingTwoController(Solo48):
    icon_id = 'filter-setting-two-controller'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('filter', 'setting', 'two', 'controller', 'interface-essential')

    def build(self):
        self.add_line('e0', (21, 13), (44, 13))
        self.add_line('e1', (12, 13), (4, 13))
        self.add_line('e2', (37, 35), (44, 35))
        self.add_line('e3', (28, 35), (4, 35))
        self.add_arc('e4-top', (27, 35), (37, 35), radius_x=5)
        self.add_arc('e4-bottom', (37, 35), (27, 35), radius_x=5)
        self.add_arc('e5-top', (12, 13), (22, 13), radius_x=5)
        self.add_arc('e5-bottom', (22, 13), (12, 13), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c3', 'e4')
