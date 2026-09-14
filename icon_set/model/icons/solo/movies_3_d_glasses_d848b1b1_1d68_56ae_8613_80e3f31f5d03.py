"""Movies 3 d glasses (movies), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd848b1b1-1d68-56ae-8613-80e3f31f5d03'
SOURCE_PATH = 'icons-json/movies/movies 3 d glasses_d848b1b1-1d68-56ae-8613-80e3f31f5d03.json'
AUTHOR = 'json_to_solo'

class Movies3DGlasses(Solo48):
    icon_id = 'movies-3-d-glasses'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'movies'
    aliases = ()
    keywords = ('movies', 'd', 'glasses')

    def build(self):
        self.add_line('e0', (44, 26), (44, 35))
        self.add_line('e1', (40, 40), (31, 40))
        self.add_line('e2', (27, 34), (27, 26))
        self.add_line('e3', (30, 23), (42, 23))
        self.add_line('e4', (42, 23), (36, 13))
        self.add_line('e5', (14, 9), (6, 23))
        self.add_line('e6', (27, 28), (21, 28))
        self.add_line('e7', (19, 23), (6, 23))
        self.add_line('e8', (4, 25), (4, 34))
        self.add_line('e9', (7, 40), (18, 40))
        self.add_line('e10', (21, 33), (21, 25))
        self.add_line('e11', (42, 23), (44, 26))
        self.add_arc('e12-1', (44, 35), (43, 38), radius_x=5)
        self.add_arc('e12-2', (43, 38), (40, 40), radius_x=4)
        self.add_arc('e13', (31, 40), (27, 34), radius_x=6)
        self.add_arc('e14', (27, 26), (30, 23), radius_x=3)
        self.add_arc('e15-1', (36, 13), (32, 8), radius_x=7, sweep=False)
        self.add_line('e15-2', (32, 8), (29, 10))
        self.add_arc('e16-1', (19, 10), (16, 8), radius_x=4)
        self.add_arc('e16-2', (16, 8), (14, 9), radius_x=3, sweep=False)
        self.add_line('e17', (21, 25), (19, 23))
        self.add_arc('e18', (6, 23), (4, 25), radius_x=4, sweep=False)
        self.add_line('e19-1', (4, 34), (5, 39))
        self.add_arc('e19-2', (5, 39), (7, 40), radius_x=3, sweep=False)
        self.add_arc('e20', (18, 40), (21, 33), radius_x=6, sweep=False)
        self.add_contour('c0', 'e11', 'e0', 'e12-1', 'e12-2', 'e1', 'e13', 'e2', 'e14', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e15-1', 'e15-2')
        self.add_contour('c2', 'e16-1', 'e16-2', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e17', 'e7', 'e18', 'e8', 'e19-1', 'e19-2', 'e9', 'e20', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c4')
