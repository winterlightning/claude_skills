"""Wild bird eagle (animals), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a4eec1cf-c3e3-4378-acb6-422b50d1da15'
SOURCE_PATH = 'icons-json/animals/wild bird eagle_a4eec1cf-c3e3-4378-acb6-422b50d1da15.json'
AUTHOR = 'json_to_solo'

class WildBirdEagle(Solo48):
    icon_id = 'wild-bird-eagle'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('wild', 'bird', 'eagle', 'animals')

    def build(self):
        self.add_line('e0', (29, 22), (31, 19))
        self.add_line('e1', (28, 26), (28, 39))
        self.add_line('e2', (21, 40), (19, 41))
        self.add_line('e3', (13, 40), (12, 41))
        self.add_line('e4', (6, 39), (6, 17))
        self.add_line('e5', (6, 6), (22, 6))
        self.add_arc('e6-1', (28, 26), (42, 27), radius_x=18)
        self.add_line('e6-2', (42, 27), (42, 26))
        self.add_line('e6-3', (42, 26), (41, 21))
        self.add_arc('e6-4', (41, 21), (39, 18), radius_x=10, sweep=False)
        self.add_arc('e6-5', (39, 18), (32, 15), radius_x=10, sweep=False)
        self.add_arc('e7', (28, 26), (29, 22), radius_x=9)
        self.add_arc('e8', (31, 19), (32, 15), radius_x=12, sweep=False)
        self.add_arc('e9-1', (28, 39), (24, 42), radius_x=5)
        self.add_line('e9-2', (24, 42), (21, 40))
        self.add_arc('e10-1', (19, 41), (17, 42), radius_x=4)
        self.add_line('e10-2', (17, 42), (13, 40))
        self.add_arc('e11-1', (12, 41), (10, 42), radius_x=3, sweep=False)
        self.add_line('e11-2', (10, 42), (7, 41))
        self.add_line('e11-3', (7, 41), (6, 39))
        self.add_arc('e12-1', (6, 17), (9, 12), radius_x=6)
        self.add_arc('e12-2', (9, 12), (6, 6), radius_x=8)
        self.add_arc('e13-1', (22, 6), (30, 9), radius_x=13)
        self.add_arc('e13-2', (30, 9), (32, 15), radius_x=8)
        self.add_contour('c0', 'e6-1', 'e6-2', 'e6-3', 'e6-4', 'e6-5')
        self.add_contour('c1', 'e7', 'e0', 'e8')
        self.add_contour('c2', 'e1', 'e9-1', 'e9-2', 'e2', 'e10-1', 'e10-2', 'e3', 'e11-1', 'e11-2', 'e11-3', 'e4', 'e12-1', 'e12-2', 'e5', 'e13-1', 'e13-2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
