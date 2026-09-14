"""Controls movie (movies), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '585301af-baa6-48d9-8d71-939943677ad5'
SOURCE_PATH = 'icons-json/movies/controls movie_585301af-baa6-48d9-8d71-939943677ad5.json'
AUTHOR = 'json_to_solo'

class ControlsMovie(Solo48):
    icon_id = 'controls-movie'
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
        self.add_line('e10-1', (4, 32), (4, 36))
        self.add_arc('e10-2', (4, 36), (8, 40), radius_x=4, sweep=False)
        self.add_arc('e11', (41, 40), (44, 37), radius_x=3, sweep=False)
        self.add_line('e12-1', (4, 16), (4, 13))
        self.add_arc('e12-2', (4, 13), (5, 10), radius_x=6)
        self.add_arc('e12-3', (5, 10), (8, 8), radius_x=4)
        self.add_arc('e13', (41, 8), (44, 11), radius_x=3)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e10-1', 'e10-2', 'e1', 'e11', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e12-1', 'e12-2', 'e12-3', 'e6', 'e13', 'e7')
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
