"""Expand full (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '523b51cb-a6d4-4558-96b7-d551864cbbf5'
SOURCE_PATH = 'icons-json/interface-essential/expand full_523b51cb-a6d4-4558-96b7-d551864cbbf5.json'
AUTHOR = 'json_to_solo'

class ExpandFullInterfaceEssential(Solo48):
    icon_id = 'expand-full-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('expand', 'full', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 14), (6, 8))
        self.add_line('e1', (8, 6), (14, 6))
        self.add_line('e2', (34, 6), (40, 6))
        self.add_line('e3', (42, 8), (42, 14))
        self.add_line('e4', (6, 35), (6, 40))
        self.add_line('e5', (8, 42), (14, 42))
        self.add_line('e6', (34, 42), (40, 42))
        self.add_line('e7', (42, 40), (42, 35))
        self.add_line('e8', (31, 30), (16, 30))
        self.add_line('e9', (15, 28), (15, 20))
        self.add_line('e10', (17, 18), (31, 18))
        self.add_line('e11', (33, 20), (33, 28))
        self.add_bezier('e12', (6, 8), ((6.074, 7.845), (6.033, 7.383), (6.09, 7.219)), ((6.352, 6.499), (7.403, 6.286), (8, 6)))
        self.add_bezier('e13', (40, 6), ((40.155, 6.074), (40.625, 6.033), (40.789, 6.09)), ((41.165, 6.229), (41.746, 6.826), (41.902, 7.195)), ((41.975, 7.375), (41.91, 7.828), (42, 8)))
        self.add_bezier('e14', (6, 40), ((6.491, 41.072), (6.928, 41.517), (8, 42)))
        self.add_bezier('e15', (40, 42), ((41.039, 41.525), (41.501, 41.023), (42, 40)))
        self.add_bezier('e16', (16, 30), ((15.329, 29.329), (15.147, 28.925), (15, 28)))
        self.add_bezier('e17', (15, 20), ((15.45, 18.969), (15.953, 18.425), (17, 18)))
        self.add_bezier('e18', (31, 18), ((32.015, 18.458), (32.534, 18.985), (33, 20)))
        self.add_bezier('e19', (33, 28), ((32.517, 29.129), (32.113, 29.542), (31, 30)))
        self.add_contour('c0', 'e0', 'e12', 'e1')
        self.add_contour('c1', 'e2', 'e13', 'e3')
        self.add_contour('c2', 'e4', 'e14', 'e5')
        self.add_contour('c3', 'e6', 'e15', 'e7')
        self.add_contour('c4', 'e8', 'e16', 'e9', 'e17', 'e10', 'e18', 'e11', 'e19', closed=True)
