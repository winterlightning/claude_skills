"""Skiing snow scooter (sports), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0980517-7981-47f9-b740-8ade748f0d74'
SOURCE_PATH = 'icons-json/sports/skiing snow scooter_a0980517-7981-47f9-b740-8ade748f0d74.json'
AUTHOR = 'json_to_solo'

class SkiingSnowScooterSports(Solo48):
    icon_id = 'skiing-snow-scooter-sports'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('skiing', 'snow', 'scooter', 'sports')

    def build(self):
        self.add_line('e0', (33, 25), (41, 25))
        self.add_line('e1', (21, 8), (27, 8))
        self.add_line('e2', (30, 40), (37, 40))
        self.add_line('e3', (44, 36), (42, 39))
        self.add_line('e4', (42, 39), (40, 40))
        self.add_line('e5', (40, 40), (37, 40))
        self.add_line('e6', (33, 33), (37, 40))
        self.add_line('e7', (33, 33), (26, 33))
        self.add_line('e8', (20, 33), (26, 33))
        self.add_line('e9', (13, 29), (6, 34))
        self.add_line('e10', (7, 40), (21, 40))
        self.add_line('e11', (13, 29), (5, 20))
        self.add_line('e12', (6, 15), (11, 15))
        self.add_line('e13', (12, 15), (16, 19))
        self.add_line('e14', (36, 17), (41, 25))
        self.add_arc('e15', (27, 8), (31, 14), radius_x=10)
        self.add_arc('e16-1', (33, 33), (41, 31), radius_x=8, sweep=False)
        self.add_arc('e16-2', (41, 31), (41, 25), radius_x=6, sweep=False)
        self.add_line('e17', (13, 29), (20, 33))
        self.add_arc('e18', (6, 34), (7, 40), radius_x=4, sweep=False)
        self.add_arc('e19', (21, 40), (26, 33), radius_x=9, sweep=False)
        self.add_arc('e20-1', (5, 20), (4, 18), radius_x=5)
        self.add_line('e20-2', (4, 18), (6, 15))
        self.add_line('e21', (11, 15), (12, 15))
        self.add_arc('e22-1', (16, 19), (24, 19), radius_x=13, sweep=False)
        self.add_arc('e22-2', (24, 19), (28, 15), radius_x=10, sweep=False)
        self.add_line('e22-3', (28, 15), (31, 14))
        self.add_arc('e23', (31, 14), (36, 17), radius_x=5)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e15')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e4', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e16-1', 'e16-2')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e17', 'e8')
        self.add_contour('c8', 'e9', 'e18', 'e10', 'e19')
        self.add_contour('c9', 'e11', 'e20-1', 'e20-2', 'e12', 'e21', 'e13', 'e22-1', 'e22-2', 'e22-3')
        self.add_contour('c10', 'e23', 'e14')
        self.relate('connect', 'c0', 'c10')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c10', 'c5')
        self.relate('connect', 'c1', 'c10')
        self.relate('connect', 'c1', 'c9')
        self.relate('connect', 'c10', 'c9')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c8', 'c9')
