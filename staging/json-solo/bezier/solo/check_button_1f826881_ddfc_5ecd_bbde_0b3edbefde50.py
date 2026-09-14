"""Check button (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f826881-ddfc-5ecd-bbde-0b3edbefde50'
SOURCE_PATH = 'icons-json/interface-essential/check button_1f826881-ddfc-5ecd-bbde-0b3edbefde50.json'
AUTHOR = 'json_to_solo'

class CheckButtonInterfaceEssential(Solo48):
    icon_id = 'check-button-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('check', 'button', 'interface-essential')

    def build(self):
        self.add_line('e0', (36, 18), (27, 31))
        self.add_line('e1', (27, 31), (22, 24))
        self.add_line('e2', (4, 38), (4, 10))
        self.add_line('e3', (6, 8), (42, 8))
        self.add_line('e4', (44, 10), (44, 38))
        self.add_line('e5', (42, 40), (7, 40))
        self.add_bezier('e6', (4, 10), ((4, 8.462), (5.145, 8.418), (6, 8)))
        self.add_bezier('e7', (42, 8), ((42.064, 8), (42.318, 8), (42.382, 8)), ((43.418, 8), (43.718, 9.015), (44, 10)))
        self.add_bezier('e8', (44, 38), ((43.427, 39.797), (43.336, 39.237), (42, 40)))
        self.add_bezier('e9', (7, 40), ((6.882, 40), (6.491, 40), (6.373, 40)), ((5.527, 40), (4.936, 39.606), (4.382, 38.794)), ((4.345, 38.732), (4, 38.24), (4, 38.154)), ((4, 37.957), (4, 38.209), (4, 38)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
