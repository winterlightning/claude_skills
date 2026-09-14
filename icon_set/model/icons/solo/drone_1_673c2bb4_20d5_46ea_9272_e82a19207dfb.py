"""Drone 1 (technology), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '673c2bb4-20d5-46ea-9272-e82a19207dfb'
SOURCE_PATH = 'icons-json/technology/drone 1_673c2bb4-20d5-46ea-9272-e82a19207dfb.json'
AUTHOR = 'json_to_solo'

class Drone1(Solo48):
    icon_id = 'drone-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    aliases = ()
    keywords = ('drone', 'technology')

    def build(self):
        self.add_line('e0', (36, 40), (34, 40))
        self.add_line('e1', (36, 22), (41, 22))
        self.add_line('e2', (4, 8), (9, 8))
        self.add_line('e3', (15, 40), (12, 40))
        self.add_line('e4', (36, 8), (44, 8))
        self.add_line('e5', (13, 8), (9, 8))
        self.add_line('e6', (16, 14), (20, 12))
        self.add_line('e7', (33, 14), (39, 14))
        self.add_line('e8', (9, 14), (6, 15))
        self.add_line('e9', (8, 22), (12, 22))
        self.add_line('e10', (9, 14), (9, 8))
        self.add_line('e11', (39, 9), (39, 14))
        self.add_arc('e12', (31, 24), (18, 24), radius_x=13)
        self.add_arc('e13', (31, 24), (36, 40), radius_x=12)
        self.add_arc('e14', (31, 24), (36, 22), radius_x=8)
        self.add_arc('e15-1', (41, 22), (43, 21), radius_x=2, sweep=False)
        self.add_arc('e15-2', (43, 21), (44, 18), radius_x=5, sweep=False)
        self.add_line('e15-3', (44, 18), (43, 15))
        self.add_line('e15-4', (43, 15), (39, 14))
        self.add_arc('e16', (12, 40), (18, 24), radius_x=13)
        self.add_arc('e17', (9, 14), (16, 14), radius_x=22, sweep=False)
        self.add_arc('e18', (20, 12), (33, 14), radius_x=14)
        self.add_arc('e19-1', (6, 15), (4, 18), radius_x=4, sweep=False)
        self.add_arc('e19-2', (4, 18), (8, 22), radius_x=4, sweep=False)
        self.add_arc('e20', (12, 22), (18, 24), radius_x=9)
        self.add_line('e21', (40, 8), (39, 9))
        self.add_contour('c0', 'e12')
        self.add_contour('c1', 'e13', 'e0')
        self.add_contour('c2', 'e14', 'e1', 'e15-1', 'e15-2', 'e15-3', 'e15-4')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3', 'e16')
        self.add_contour('c5', 'e4')
        self.add_contour('c6', 'e5')
        self.add_contour('c7', 'e17', 'e6', 'e18', 'e7')
        self.add_contour('c8', 'e8', 'e19-1', 'e19-2', 'e9', 'e20')
        self.add_contour('c9', 'e10')
        self.add_contour('c10', 'e21', 'e11')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c8')
        self.relate('connect', 'c4', 'c8')
        self.relate('connect', 'c10', 'c2')
        self.relate('connect', 'c10', 'c7')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c3', 'c9')
        self.relate('connect', 'c6', 'c9')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c8', 'c9')
        self.relate('connect', 'c10', 'c5')
