"""Be (text u) (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f17d3767-756e-40e4-a1d9-8b2fc618d58d'
SOURCE_PATH = 'icons-json/symbol/be (text u)_f17d3767-756e-40e4-a1d9-8b2fc618d58d.json'
AUTHOR = 'json_to_solo'

class BeTextU(Solo48):
    icon_id = 'be-text-u'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('be', 'text', 'u', 'symbol')

    def build(self):
        self.add_line('e0', (15, 4), (8, 4))
        self.add_line('e1', (8, 4), (8, 27))
        self.add_line('e2', (8, 27), (13, 27))
        self.add_line('e3', (16, 15), (8, 15))
        self.add_line('e4', (8, 44), (40, 44))
        self.add_arc('e5-1', (13, 27), (21, 22), radius_x=7, sweep=False)
        self.add_arc('e5-2', (21, 22), (16, 15), radius_x=6, sweep=False)
        self.add_arc('e5-3', (16, 15), (20, 8), radius_x=6, sweep=False)
        self.add_arc('e5-4', (20, 8), (15, 4), radius_x=6, sweep=False)
        self.add_arc('e6-1', (30, 19), (40, 17), radius_x=7, sweep=False)
        self.add_arc('e6-2', (40, 17), (32, 13), radius_x=5, sweep=False)
        self.add_arc('e6-3', (32, 13), (30, 23), radius_x=9, sweep=False)
        self.add_arc('e6-4', (30, 23), (37, 26), radius_x=5, sweep=False)
        self.add_arc('e6-5', (37, 26), (40, 23), radius_x=4, sweep=False)
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e5-1', 'e5-2', 'e5-3', 'e5-4', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5')
        self.add_contour('c3', 'e4')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c1', 'c0')
