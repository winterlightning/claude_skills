"""Decrease indent (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f325664-3e72-5b8f-81d3-f3c37299170c'
SOURCE_PATH = 'icons-json/interface-essential/decrease indent_1f325664-3e72-5b8f-81d3-f3c37299170c.json'
AUTHOR = 'json_to_solo'

class DecreaseIndentInterfaceEssential(Solo48):
    icon_id = 'decrease-indent-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('decrease', 'indent', 'interface-essential')

    def build(self):
        self.add_line('e0', (4, 8), (23, 8))
        self.add_line('e1', (4, 19), (23, 19))
        self.add_line('e2', (4, 29), (23, 29))
        self.add_line('e3', (4, 40), (23, 40))
        self.add_line('e4', (44, 17), (32, 25))
        self.add_line('e5', (32, 25), (44, 34))
        self.add_line('e6', (44, 34), (44, 17))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5', 'e6', closed=True)
