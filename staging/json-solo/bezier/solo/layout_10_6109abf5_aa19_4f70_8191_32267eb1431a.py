"""Layout 10 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6109abf5-aa19-4f70-8191-32267eb1431a'
SOURCE_PATH = 'icons-json/interface-essential/layout 10_6109abf5-aa19-4f70-8191-32267eb1431a.json'
AUTHOR = 'json_to_solo'

class Layout10InterfaceEssential(Solo48):
    icon_id = 'layout-10-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 24), (30, 24))
        self.add_line('e1', (42, 24), (42, 40))
        self.add_line('e2', (40, 42), (30, 42))
        self.add_line('e3', (42, 24), (42, 8))
        self.add_line('e4', (40, 6), (24, 6))
        self.add_line('e5', (30, 24), (30, 42))
        self.add_line('e6', (30, 24), (24, 24))
        self.add_line('e7', (30, 42), (18, 42))
        self.add_line('e8', (6, 24), (18, 24))
        self.add_line('e9', (6, 24), (6, 40))
        self.add_line('e10', (8, 42), (18, 42))
        self.add_line('e11', (6, 24), (6, 8))
        self.add_line('e12', (8, 6), (24, 6))
        self.add_line('e13', (18, 24), (18, 42))
        self.add_line('e14', (18, 24), (24, 24))
        self.add_line('e15', (24, 6), (24, 24))
        self.add_bezier('e16', (42, 40), ((42, 41.113), (41.113, 42), (40, 42)))
        self.add_bezier('e17', (42, 8), ((41.926, 7.828), (41.959, 8.086), (41.869, 7.915)), ((41.321, 6.802), (41.039, 6.45), (40, 6)))
        self.add_bezier('e18', (6, 40), ((6.565, 41.366), (6.666, 41.419), (8, 42)))
        self.add_bezier('e19', (6, 8), ((6.556, 6.634), (6.609, 6.556), (8, 6)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e16', 'e2')
        self.add_contour('c2', 'e3', 'e17', 'e4')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9', 'e18', 'e10')
        self.add_contour('c8', 'e11', 'e19', 'e12')
        self.add_contour('c9', 'e13')
        self.add_contour('c10', 'e14')
        self.add_contour('c11', 'e15')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c11', 'c2')
        self.relate('connect', 'c11', 'c8')
        self.relate('connect', 'c2', 'c8')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c4')
        self.relate('connect', 'c11', 'c4')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c10', 'c6')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c6', 'c9')
