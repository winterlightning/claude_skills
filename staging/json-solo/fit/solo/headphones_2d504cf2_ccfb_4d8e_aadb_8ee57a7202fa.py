"""Headphones (audio), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa'
SOURCE_PATH = 'icons-json/audio/headphones_2d504cf2-ccfb-4d8e-aadb-8ee57a7202fa.json'
AUTHOR = 'json_to_solo'

class Headphones2d504cf2(Solo48):
    icon_id = 'headphones-2d504cf2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('headphones', 'audio')

    def build(self):
        self.add_line('e0', (42, 29), (40, 28))
        self.add_line('e1', (40, 28), (35, 28))
        self.add_line('e2', (34, 29), (34, 40))
        self.add_line('e3', (35, 42), (40, 42))
        self.add_line('e4', (42, 40), (42, 29))
        self.add_line('e5', (42, 28), (42, 22))
        self.add_line('e6', (6, 22), (6, 28))
        self.add_line('e7', (6, 31), (6, 40))
        self.add_line('e8', (8, 42), (13, 42))
        self.add_line('e9', (14, 40), (14, 29))
        self.add_line('e10', (13, 28), (8, 28))
        self.add_line('e12', (35, 28), (34, 29))
        self.add_line('e13', (34, 40), (35, 42))
        self.add_line('e14', (40, 42), (42, 40))
        self.add_arc('e15', (42, 29), (42, 28), radius_x=30)
        self.add_arc('e16-1', (42, 22), (34, 9), radius_x=17, sweep=False)
        self.add_arc('e16-2', (34, 9), (30, 7), radius_x=18, sweep=False)
        self.add_line('e16-3', (30, 7), (24, 6))
        self.add_arc('e16-4', (24, 6), (22, 6), radius_x=47)
        self.add_arc('e16-5', (22, 6), (14, 9), radius_x=17, sweep=False)
        self.add_arc('e16-6', (14, 9), (6, 22), radius_x=18, sweep=False)
        self.add_arc('e17', (6, 28), (6, 29), radius_x=70)
        self.add_line('e18', (6, 40), (8, 42))
        self.add_arc('e19', (13, 42), (14, 40), radius_x=2, sweep=False)
        self.add_line('e20', (14, 29), (13, 28))
        self.add_line('e21-1', (8, 28), (6, 29))
        self.add_line('e21-2', (6, 29), (6, 31))
        self.add_contour('c0', 'e0', 'e1', 'e12', 'e2', 'e13', 'e3', 'e14', 'e4', closed=True)
        self.add_contour('c1', 'e15', 'e5', 'e16-1', 'e16-2', 'e16-3', 'e16-4', 'e16-5', 'e16-6', 'e6', 'e17')
        self.add_contour('c2', 'e7', 'e18', 'e8', 'e19', 'e9', 'e20', 'e10', 'e21-1', 'e21-2', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c1', 'c2')
