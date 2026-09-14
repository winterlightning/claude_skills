"""Layout two colums (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a197121-e0fa-4988-b248-ee037ed6f6d6'
SOURCE_PATH = 'icons-json/interface-essential/layout two colums_0a197121-e0fa-4988-b248-ee037ed6f6d6.json'
AUTHOR = 'json_to_solo'

class LayoutTwoColumsInterfaceEssential(Solo48):
    icon_id = 'layout-two-colums-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('layout', 'two', 'colums', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 42))
        self.add_line('sym-e1', (24, 42), (40, 42))
        self.add_bezier('sym-e2', (40, 42), ((40.18, 41.926), (39.828, 42), (40, 42)))
        self.add_bezier('sym-e3', (40, 42), ((41.023, 41.509), (42, 40.162), (42, 39)))
        self.add_bezier('sym-e4', (42, 39), ((42, 38.943), (42, 39.057), (42, 39)))
        self.add_line('sym-e5', (42, 39), (42, 24))
        self.add_line('sym-e6', (42, 24), (42, 9))
        self.add_bezier('sym-e7', (42, 9), ((42, 8.943), (42, 9.057), (42, 9)))
        self.add_bezier('sym-e8', (42, 9), ((42, 7.838), (41.023, 6.491), (40, 6)))
        self.add_bezier('sym-e9', (40, 6), ((39.828, 6), (40.18, 6.074), (40, 6)))
        self.add_line('sym-e10', (40, 6), (24, 6))
        self.add_line('sym-e11', (24, 6), (8, 6))
        self.add_bezier('sym-e12', (8, 6), ((7.82, 6.074), (8.172, 6), (8, 6)))
        self.add_bezier('sym-e13', (8, 6), ((6.977, 6.491), (6, 7.838), (6, 9)))
        self.add_bezier('sym-e14', (6, 9), ((6, 9.057), (6, 8.943), (6, 9)))
        self.add_line('sym-e15', (6, 9), (6, 24))
        self.add_line('sym-e16', (6, 24), (6, 39))
        self.add_bezier('sym-e17', (6, 39), ((6, 39.057), (6, 38.943), (6, 39)))
        self.add_bezier('sym-e18', (6, 39), ((6, 40.162), (6.977, 41.509), (8, 42)))
        self.add_bezier('sym-e19', (8, 42), ((8.172, 42), (7.82, 41.926), (8, 42)))
        self.add_line('sym-e20', (8, 42), (24, 42))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
