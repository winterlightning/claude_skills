"""Expand 2 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2dca4f4d-e5e8-43fe-9d02-67d5e34df3aa'
SOURCE_PATH = 'icons-json/interface-essential/expand 2_2dca4f4d-e5e8-43fe-9d02-67d5e34df3aa.json'
AUTHOR = 'json_to_solo'

class Expand2InterfaceEssential(Solo48):
    icon_id = 'expand-2-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'interface-essential')

    def build(self):
        self.add_line('e0', (32, 6), (40, 6))
        self.add_line('e1', (27, 21), (42, 6))
        self.add_line('e2', (42, 16), (42, 6))
        self.add_line('e3', (19, 29), (6, 42))
        self.add_line('e4', (6, 31), (6, 42))
        self.add_line('e5', (17, 42), (6, 42))
        self.add_bezier('e6', (40, 6), ((40.548, 6), (41.452, 6), (42, 6)))
        self.add_contour('c0', 'e0', 'e6')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
