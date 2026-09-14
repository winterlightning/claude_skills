"""Brain (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74d6ac6c-9f6f-4183-9ee6-960cbc7f4216'
SOURCE_PATH = 'icons-json/artificial-intelligence/brain_74d6ac6c-9f6f-4183-9ee6-960cbc7f4216.json'
AUTHOR = 'json_to_solo'

class Brain74d6ac6c(Solo48):
    icon_id = 'brain-74d6ac6c'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('brain', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (17, 19), (15, 18))
        self.add_line('e1', (24, 8), (24, 39))
        self.add_arc('e2', (15, 18), (11, 13), radius_x=6)
        self.add_line('e3-1', (24, 8), (30, 6))
        self.add_line('e3-2', (30, 6), (35, 8))
        self.add_arc('e3-3', (35, 8), (37, 12), radius_x=7)
        self.add_line('e3-4', (37, 12), (41, 16))
        self.add_line('e3-5', (41, 16), (42, 20))
        self.add_arc('e3-6', (42, 20), (42, 27), radius_x=7, sweep=False)
        self.add_arc('e3-7', (42, 27), (40, 32), radius_x=8)
        self.add_arc('e3-8', (40, 32), (37, 36), radius_x=4, sweep=False)
        self.add_arc('e3-9', (37, 36), (30, 42), radius_x=8)
        self.add_line('e3-10', (30, 42), (26, 41))
        self.add_line('e3-11', (26, 41), (24, 39))
        self.add_line('e4-1', (24, 8), (19, 6))
        self.add_line('e4-2', (19, 6), (13, 8))
        self.add_arc('e4-3', (13, 8), (11, 13), radius_x=6, sweep=False)
        self.add_arc('e5-1', (24, 39), (19, 42), radius_x=6)
        self.add_line('e5-2', (19, 42), (15, 41))
        self.add_arc('e5-3', (15, 41), (11, 36), radius_x=8)
        self.add_arc('e5-4', (11, 36), (8, 32), radius_x=4, sweep=False)
        self.add_line('e5-5', (8, 32), (6, 27))
        self.add_arc('e5-6', (6, 27), (6, 20), radius_x=6, sweep=False)
        self.add_arc('e5-7', (6, 20), (11, 13), radius_x=8)
        self.add_arc('e6', (31, 22), (37, 28), radius_x=6)
        self.add_contour('c0', 'e0', 'e2')
        self.add_contour('c1', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5', 'e3-6', 'e3-7', 'e3-8', 'e3-9', 'e3-10', 'e3-11')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e4-1', 'e4-2', 'e4-3')
        self.add_contour('c4', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7')
        self.add_contour('c5', 'e6')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c4')
