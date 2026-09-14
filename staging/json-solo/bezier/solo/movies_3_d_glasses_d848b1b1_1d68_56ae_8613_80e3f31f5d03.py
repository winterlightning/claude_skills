"""Movies 3 d glasses (movies), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd848b1b1-1d68-56ae-8613-80e3f31f5d03'
SOURCE_PATH = 'icons-json/movies/movies 3 d glasses_d848b1b1-1d68-56ae-8613-80e3f31f5d03.json'
AUTHOR = 'json_to_solo'

class Movies3DGlassesMovies(Solo48):
    icon_id = 'movies-3-d-glasses-movies'
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
        self.add_bezier('e11', (42, 23), ((42.718, 24.108), (43.982, 24.505), (43.982, 26.24)), ((43.991, 26.314), (43.991, 25.926), (44, 26)))
        self.add_bezier('e12', (44, 35), ((44, 35.098), (43.991, 35.286), (43.991, 35.385)), ((43.991, 37.477), (42.173, 39.975), (40.609, 39.975)), ((40.527, 39.988), (40.082, 39.988), (40, 40)))
        self.add_bezier('e13', (31, 40), ((28.936, 40), (27.609, 37.551), (26.991, 35.089)), ((26.9, 34.745), (27, 34.369), (27, 34)))
        self.add_bezier('e14', (27, 26), ((27, 23.194), (28.3, 23), (30, 23)))
        self.add_bezier('e15', (36, 13), ((35.164, 11.708), (33.427, 8.012), (31.982, 8.012)), ((31.927, 8.012), (31.882, 8), (31.836, 8)), ((31.836, 8), (31.835, 8), (31.834, 8)), ((31.78, 8), (31.736, 8), (31.691, 8.012)), ((30.773, 8.012), (29.518, 9.175), (29, 10)))
        self.add_bezier('e16', (19, 10), ((18.427, 9.138), (17.064, 8.012), (16.091, 8.012)), ((16.027, 8.012), (15.955, 8), (15.882, 8)), ((15.809, 8.012), (15.745, 8.012), (15.673, 8.025)), ((15.055, 8.025), (14.473, 8.569), (14, 9)))
        self.add_bezier('e17', (21, 25), ((20.291, 23.831), (20.236, 23), (19, 23)))
        self.add_bezier('e18', (6, 23), ((5.455, 23.529), (4.727, 23.803), (4.264, 24.48)), ((4.118, 24.702), (4.136, 24.754), (4, 25)))
        self.add_bezier('e19', (4, 34), ((4, 34.689), (4.018, 35.225), (4.018, 35.914)), ((4.018, 37.846), (5.491, 40), (7, 40)))
        self.add_bezier('e20', (18, 40), ((18.091, 40), (17.818, 40), (17.909, 40)), ((18.191, 40), (18.545, 39.692), (18.791, 39.52)), ((20.655, 38.154), (21, 35.708), (21, 33)))
        self.add_contour('c0', 'e11', 'e0', 'e12', 'e1', 'e13', 'e2', 'e14', 'e3', closed=True)
        self.add_contour('c1', 'e4', 'e15')
        self.add_contour('c2', 'e16', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e17', 'e7', 'e18', 'e8', 'e19', 'e9', 'e20', 'e10', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c3', 'c0')
        self.relate('connect', 'c3', 'c4')
