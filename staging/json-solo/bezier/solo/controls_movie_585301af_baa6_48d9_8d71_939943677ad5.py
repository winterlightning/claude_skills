"""Controls movie (movies), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '585301af-baa6-48d9-8d71-939943677ad5'
SOURCE_PATH = 'icons-json/movies/controls movie_585301af-baa6-48d9-8d71-939943677ad5.json'
AUTHOR = 'json_to_solo'

class ControlsMovieMovies(Solo48):
    icon_id = 'controls-movie-movies'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'movies'
    aliases = ()
    keywords = ('controls', 'movie', 'movies')

    def build(self):
        self.add_line('e0', (4, 32), (44, 32))
        self.add_line('e1', (8, 40), (41, 40))
        self.add_line('e2', (44, 37), (44, 32))
        self.add_line('e3', (4, 32), (4, 16))
        self.add_line('e4', (44, 32), (44, 16))
        self.add_line('e5', (4, 16), (44, 16))
        self.add_line('e6', (8, 8), (41, 8))
        self.add_line('e7', (44, 11), (44, 16))
        self.add_line('e8', (28, 16), (35, 8))
        self.add_line('e9', (14, 16), (21, 8))
        self.add_bezier('e10', (4, 32), ((4, 32.32), (4.018, 33.053), (4.018, 33.364)), ((4.018, 35.571), (4, 38.215), (6.2, 39.503)), ((6.618, 39.739), (7.5, 40), (8, 40)))
        self.add_bezier('e11', (41, 40), ((42.264, 40), (44, 38.171), (44, 37)))
        self.add_bezier('e12', (4, 16), ((4, 15.596), (4.018, 14.771), (4.018, 14.366)), ((4.018, 12.278), (4, 9.735), (6.136, 8.505)), ((6.5, 8.295), (7, 8.017), (7.445, 8.017)), ((7.509, 8.008), (7.936, 8.008), (8, 8)))
        self.add_bezier('e13', (41, 8), ((42.464, 8), (43.582, 9.981), (44, 11)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e10', 'e1', 'e11', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e12', 'e6', 'e13', 'e7')
        self.add_contour('c6', 'e8')
        self.add_contour('c7', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c4')
        self.relate('connect', 'c2', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c4')
        self.relate('connect', 'c6', 'c5')
        self.relate('connect', 'c7', 'c4')
        self.relate('connect', 'c7', 'c5')
