"""Herbal (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd37ff2bf-eddb-475b-9f5a-3996767a114d'
SOURCE_PATH = 'icons-json/symbol/herbal_d37ff2bf-eddb-475b-9f5a-3996767a114d.json'
AUTHOR = 'json_to_solo'

class Herbal(Solo48):
    icon_id = 'herbal'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('herbal', 'symbol')

    def build(self):
        self.add_line('e0', (31, 6), (31, 18))
        self.add_line('e1', (20, 10), (20, 28))
        self.add_line('e2', (10, 21), (10, 38))
        self.add_line('e3', (6, 42), (10, 38))
        self.add_line('e4', (28, 38), (10, 38))
        self.add_line('e5', (38, 28), (20, 28))
        self.add_line('e6', (42, 18), (31, 18))
        self.add_line('e7', (38, 12), (31, 18))
        self.add_line('e8', (31, 18), (20, 28))
        self.add_line('e9', (20, 28), (10, 38))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('c8', 'e8')
        self.add_contour('c9', 'e9')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c0', 'c7')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c8')
        self.relate('connect', 'c1', 'c9')
        self.relate('connect', 'c5', 'c8')
        self.relate('connect', 'c5', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c9')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c9')
        self.relate('connect', 'c4', 'c9')
