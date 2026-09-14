"""Bark (transportation), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '319e2aa3-098e-5a2f-a08e-fb155dc163cb'
SOURCE_PATH = 'icons-json/transportation/bark_319e2aa3-098e-5a2f-a08e-fb155dc163cb.json'
AUTHOR = 'json_to_solo'

class BarkTransportation(Solo48):
    icon_id = 'bark-transportation'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('bark', 'transportation')

    def build(self):
        self.add_line('e0', (22, 34), (22, 8))
        self.add_line('e1', (22, 8), (11, 28))
        self.add_line('e2', (11, 28), (37, 28))
        self.add_line('e3', (22, 6), (22, 12))
        self.add_line('e4', (31, 42), (13, 42))
        self.add_line('e5', (6, 34), (42, 34))
        self.add_line('e6-1', (37, 28), (30, 16))
        self.add_arc('e6-2', (30, 16), (22, 6), radius_x=64, sweep=False)
        self.add_arc('e7', (42, 34), (31, 42), radius_x=15)
        self.add_arc('e8-1', (13, 42), (8, 39), radius_x=6)
        self.add_arc('e8-2', (8, 39), (6, 34), radius_x=17)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e6-1', 'e6-2', 'e3')
        self.add_contour('c2', 'e7', 'e4', 'e8-1', 'e8-2', 'e5', closed=True)
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c0')
