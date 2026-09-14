"""Baggage (travel), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dc8cbcb8-44a1-56f5-8649-885490f30b35'
SOURCE_PATH = 'icons-json/travel/baggage_dc8cbcb8-44a1-56f5-8649-885490f30b35.json'
AUTHOR = 'json_to_solo'

class BaggageTravel(Solo48):
    icon_id = 'baggage-travel'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('baggage', 'travel')

    def build(self):
        self.add_line('e0', (27, 6), (22, 6))
        self.add_line('e1', (15, 42), (15, 39))
        self.add_line('e2', (33, 42), (33, 39))
        self.add_line('e3', (6, 34), (6, 17))
        self.add_line('e4', (11, 13), (37, 13))
        self.add_line('e5', (42, 17), (42, 34))
        self.add_line('e6', (37, 39), (11, 39))
        self.add_line('e7-1', (31, 13), (30, 8))
        self.add_arc('e7-2', (30, 8), (27, 6), radius_x=4, sweep=False)
        self.add_arc('e8-1', (22, 6), (18, 8), radius_x=5, sweep=False)
        self.add_arc('e8-2', (18, 8), (17, 13), radius_x=9, sweep=False)
        self.add_arc('e9', (6, 17), (11, 13), radius_x=5)
        self.add_arc('e10', (37, 13), (42, 17), radius_x=5)
        self.add_arc('e11', (42, 34), (37, 39), radius_x=5)
        self.add_arc('e12-1', (11, 39), (6, 35), radius_x=5)
        self.add_line('e12-2', (6, 35), (6, 34))
        self.add_contour('c0', 'e7-1', 'e7-2', 'e0', 'e8-1', 'e8-2')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9', 'e4', 'e10', 'e5', 'e11', 'e6', 'e12-1', 'e12-2', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
