"""Bomb explosive (war), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '963feaf1-4aa7-538d-a8ff-72fc466c34e8'
SOURCE_PATH = 'icons-json/war/bomb explosive_963feaf1-4aa7-538d-a8ff-72fc466c34e8.json'
AUTHOR = 'json_to_solo'

class BombExplosiveWar(Solo48):
    icon_id = 'bomb-explosive-war'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('bomb', 'explosive', 'war')

    def build(self):
        self.add_line('e0', (32, 40), (32, 17))
        self.add_line('e1', (29, 14), (24, 14))
        self.add_line('e2', (24, 42), (24, 15))
        self.add_line('e3', (16, 14), (16, 42))
        self.add_line('e4', (20, 12), (21, 8))
        self.add_line('e5', (35, 7), (37, 10))
        self.add_line('e6', (16, 14), (11, 14))
        self.add_line('e7', (8, 17), (8, 39))
        self.add_line('e8', (11, 42), (15, 42))
        self.add_arc('e9', (24, 42), (32, 40), radius_x=6, sweep=False)
        self.add_arc('e10', (32, 17), (29, 14), radius_x=3, sweep=False)
        self.add_line('e11-1', (24, 42), (23, 44))
        self.add_arc('e11-2', (23, 44), (21, 44), radius_x=3, sweep=False)
        self.add_line('e11-3', (21, 44), (16, 43))
        self.add_arc('e12-1', (24, 15), (21, 12), radius_x=3, sweep=False)
        self.add_arc('e12-2', (21, 12), (16, 14), radius_x=4, sweep=False)
        self.add_arc('e13-1', (21, 8), (23, 5), radius_x=8)
        self.add_line('e13-2', (23, 5), (29, 4))
        self.add_arc('e13-3', (29, 4), (33, 5), radius_x=9)
        self.add_arc('e13-4', (33, 5), (35, 7), radius_x=4)
        self.add_arc('e14', (37, 10), (40, 13), radius_x=7, sweep=False)
        self.add_arc('e15-1', (11, 14), (8, 16), radius_x=3, sweep=False)
        self.add_line('e15-2', (8, 16), (8, 17))
        self.add_line('e16-1', (8, 39), (8, 40))
        self.add_arc('e16-2', (8, 40), (11, 42), radius_x=3, sweep=False)
        self.add_contour('c0', 'e9', 'e0', 'e10', 'e1')
        self.add_contour('c1', 'e11-1', 'e11-2', 'e11-3')
        self.add_contour('c2', 'e2', 'e12-1', 'e12-2', 'e3')
        self.add_contour('c3', 'e4', 'e13-1', 'e13-2', 'e13-3', 'e13-4', 'e5', 'e14')
        self.add_contour('c4', 'e6', 'e15-1', 'e15-2', 'e7', 'e16-1', 'e16-2', 'e8')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c3', 'c2')
