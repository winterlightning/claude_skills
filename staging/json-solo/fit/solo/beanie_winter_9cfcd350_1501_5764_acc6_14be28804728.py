"""Batch-03/beanie winter (accessories), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9cfcd350-1501-5764-acc6-14be28804728'
SOURCE_PATH = 'icons-json/accessories/batch-03/beanie winter_9cfcd350-1501-5764-acc6-14be28804728.json'
AUTHOR = 'json_to_solo'

class Batch03BeanieWinter(Solo48):
    icon_id = 'batch-03-beanie-winter'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'accessories'
    aliases = ()
    keywords = ('batch', 'beanie', 'winter', 'accessories')

    def build(self):
        self.add_line('e0', (30, 31), (8, 31))
        self.add_line('e1', (6, 35), (6, 40))
        self.add_line('e2', (9, 42), (38, 42))
        self.add_line('e3', (42, 39), (42, 35))
        self.add_line('e4', (38, 31), (30, 31))
        self.add_line('e5', (30, 31), (30, 42))
        self.add_line('e6', (17, 31), (17, 42))
        self.add_arc('e7-1', (40, 32), (25, 14), radius_x=17, sweep=False)
        self.add_arc('e7-2', (25, 14), (8, 31), radius_x=16, sweep=False)
        self.add_arc('e8-1', (26, 14), (28, 10), radius_x=5, sweep=False)
        self.add_arc('e8-2', (28, 10), (24, 6), radius_x=4, sweep=False)
        self.add_arc('e8-3', (24, 6), (20, 9), radius_x=5, sweep=False)
        self.add_arc('e8-4', (20, 9), (22, 14), radius_x=5, sweep=False)
        self.add_line('e9', (8, 31), (6, 35))
        self.add_arc('e10', (6, 40), (9, 42), radius_x=4, sweep=False)
        self.add_arc('e11-1', (38, 42), (41, 41), radius_x=5, sweep=False)
        self.add_line('e11-2', (41, 41), (42, 39))
        self.add_line('e12-1', (42, 35), (41, 33))
        self.add_line('e12-2', (41, 33), (38, 31))
        self.add_contour('c0', 'e7-1', 'e7-2')
        self.add_contour('c1', 'e8-1', 'e8-2', 'e8-3', 'e8-4')
        self.add_contour('c2', 'e0', 'e9', 'e1', 'e10', 'e2', 'e11-1', 'e11-2', 'e3', 'e12-1', 'e12-2', 'e4', 'e5')
        self.add_contour('c3', 'e6')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c3', 'c2')
        self.relate('connect', 'c3', 'c2')
