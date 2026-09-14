"""Expand 4 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '79549ad6-b284-4015-ad29-1892fe54fde1'
SOURCE_PATH = 'icons-json/interface-essential/expand 4_79549ad6-b284-4015-ad29-1892fe54fde1.json'
AUTHOR = 'json_to_solo'

class Expand4(Solo48):
    icon_id = 'expand-4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'interface-essential')

    def build(self):
        self.add_line('e0', (14, 6), (8, 6))
        self.add_line('e1', (6, 14), (6, 6))
        self.add_line('e2', (17, 17), (6, 6))
        self.add_line('e3', (34, 6), (40, 6))
        self.add_line('e4', (31, 17), (42, 7))
        self.add_line('e5', (42, 7), (42, 15))
        self.add_line('e6', (17, 31), (6, 42))
        self.add_line('e7', (6, 33), (6, 40))
        self.add_line('e8', (14, 42), (8, 42))
        self.add_line('e9', (31, 31), (42, 42))
        self.add_line('e10', (34, 42), (40, 42))
        self.add_line('e11', (42, 34), (42, 42))
        self.add_line('e12', (8, 6), (6, 6))
        self.add_line('e13', (6, 40), (6, 42))
        self.add_line('e14-1', (8, 42), (7, 42))
        self.add_arc('e14-2', (7, 42), (6, 42), radius_x=22, sweep=False)
        self.add_arc('e15-1', (40, 42), (41, 42), radius_x=41)
        self.add_line('e15-2', (41, 42), (42, 42))
        self.add_contour('c0', 'e0', 'e12')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7', 'e13')
        self.add_contour('c7', 'e8', 'e14-1', 'e14-2')
        self.add_contour('c8', 'e9')
        self.add_contour('c9', 'e10', 'e15-1', 'e15-2')
        self.add_contour('c10', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c10', 'c8')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c8', 'c9')
