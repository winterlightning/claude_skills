"""Text flow rows (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a13af5c-a9a7-5fa9-9d87-28150cd3e8a0'
SOURCE_PATH = 'icons-json/interface-essential/text flow rows_8a13af5c-a9a7-5fa9-9d87-28150cd3e8a0.json'
AUTHOR = 'json_to_solo'

class TextFlowRows(Solo48):
    icon_id = 'text-flow-rows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'flow', 'rows', 'interface-essential')

    def build(self):
        self.add_line('e0', (31, 18), (35, 18))
        self.add_line('e1', (35, 18), (40, 18))
        self.add_line('e2', (42, 15), (42, 8))
        self.add_line('e3', (40, 6), (32, 6))
        self.add_line('e4', (31, 8), (31, 13))
        self.add_line('e5', (31, 13), (31, 18))
        self.add_line('e6', (31, 18), (18, 31))
        self.add_line('e7', (16, 30), (8, 30))
        self.add_line('e8', (6, 32), (6, 40))
        self.add_line('e9', (8, 42), (15, 42))
        self.add_line('e10', (17, 40), (17, 31))
        self.add_line('e11', (31, 12), (17, 12))
        self.add_line('e12', (17, 36), (42, 36))
        self.add_line('e13', (42, 36), (37, 41))
        self.add_line('e14', (37, 31), (42, 35))
        self.add_line('e15', (16, 6), (8, 6))
        self.add_line('e16', (6, 8), (6, 16))
        self.add_line('e17', (8, 18), (16, 18))
        self.add_line('e18', (17, 16), (17, 8))
        self.add_arc('e19-1', (40, 18), (42, 17), radius_x=2, sweep=False)
        self.add_arc('e19-2', (42, 17), (42, 15), radius_x=10)
        self.add_arc('e20', (42, 8), (40, 6), radius_x=2, sweep=False)
        self.add_arc('e21', (32, 6), (31, 8), radius_x=2, sweep=False)
        self.add_arc('e22', (17, 31), (16, 30), radius_x=2, sweep=False)
        self.add_arc('e23', (8, 30), (6, 32), radius_x=2, sweep=False)
        self.add_arc('e24', (6, 40), (8, 42), radius_x=2, sweep=False)
        self.add_arc('e25', (15, 42), (17, 40), radius_x=2, sweep=False)
        self.add_line('e26', (17, 8), (16, 6))
        self.add_arc('e27', (8, 6), (6, 8), radius_x=2, sweep=False)
        self.add_arc('e28', (6, 16), (8, 18), radius_x=2, sweep=False)
        self.add_arc('e29', (16, 18), (17, 16), radius_x=2, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e19-1', 'e19-2', 'e2', 'e20', 'e3', 'e21', 'e4', 'e5', closed=True)
        self.add_contour('c1', 'e6')
        self.add_contour('c2', 'e22', 'e7', 'e23', 'e8', 'e24', 'e9', 'e25', 'e10')
        self.add_contour('c3', 'e11')
        self.add_contour('c4', 'e12', 'e13')
        self.add_contour('c5', 'e14')
        self.add_contour('c6', 'e26', 'e15', 'e27', 'e16', 'e28', 'e17', 'e29', 'e18', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c4', 'c2')
