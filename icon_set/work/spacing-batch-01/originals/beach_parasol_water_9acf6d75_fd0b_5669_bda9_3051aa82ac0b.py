"""Beach parasol water (outdoors), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9acf6d75-fd0b-5669-bda9-3051aa82ac0b'
SOURCE_PATH = 'icons-json/outdoors/beach parasol water_9acf6d75-fd0b-5669-bda9-3051aa82ac0b.json'
AUTHOR = 'json_to_solo'

class BeachParasolWater(Solo48):
    icon_id = 'beach-parasol-water'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('beach', 'parasol', 'water', 'outdoors')

    def build(self):
        self.add_line('e0', (31, 32), (41, 32))
        self.add_line('e1', (20, 6), (22, 9))
        self.add_line('e2', (30, 32), (26, 21))
        self.add_line('e3', (11, 26), (40, 15))
        self.add_arc('e4', (20, 35), (31, 32), radius_x=17)
        self.add_arc('e5-1', (6, 42), (12, 39), radius_x=9, sweep=False)
        self.add_arc('e5-2', (12, 39), (18, 42), radius_x=8, sweep=False)
        self.add_line('e5-3', (18, 42), (25, 39))
        self.add_arc('e5-4', (25, 39), (30, 42), radius_x=7, sweep=False)
        self.add_line('e5-5', (30, 42), (34, 41))
        self.add_line('e5-6', (34, 41), (37, 39))
        self.add_arc('e5-7', (37, 39), (42, 42), radius_x=8, sweep=False)
        self.add_arc('e6', (40, 15), (11, 26), radius_x=16, sweep=False)
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e5-1', 'e5-2', 'e5-3', 'e5-4', 'e5-5', 'e5-6', 'e5-7')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e6', closed=True)
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c4')
