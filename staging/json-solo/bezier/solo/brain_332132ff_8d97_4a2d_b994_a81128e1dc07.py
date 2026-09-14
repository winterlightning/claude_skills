"""Brain (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '332132ff-8d97-4a2d-b994-a81128e1dc07'
SOURCE_PATH = 'icons-json/artificial-intelligence/brain_332132ff-8d97-4a2d-b994-a81128e1dc07.json'
AUTHOR = 'json_to_solo'

class Brain332132ff(Solo48):
    icon_id = 'brain-332132ff'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('brain', 'artificial-intelligence')

    def build(self):
        self.add_line('e0', (26, 8), (24, 10))
        self.add_line('e1', (24, 10), (24, 39))
        self.add_line('e2', (40, 30), (38, 31))
        self.add_bezier('e3', (35, 13), ((34.91, 10.439), (33.655, 8.029), (31.364, 6.72)), ((30.799, 6.393), (30.03, 6), (29.359, 6)), ((29.358, 6), (29.356, 6), (29.355, 6)), ((29.266, 6), (29.178, 6), (29.097, 6)), ((29.015, 6), (28.942, 6), (28.86, 6.008)), ((27.78, 6.008), (26.614, 7.084), (26, 8)))
        self.add_bezier('e4', (35, 13), ((35.753, 13.237), (36.322, 12.905), (37.025, 13.274)), ((38.744, 14.174), (39.987, 15.998), (40.077, 17.945)), ((40.118, 18.87), (40.229, 20.125), (40, 21)))
        self.add_bezier('e5', (35, 13), ((34.059, 14.955), (33.127, 15.534), (31, 16)))
        self.add_bezier('e6', (24, 10), ((22.928, 8.233), (21.406, 6.008), (19.034, 6.008)), ((18.952, 6), (18.878, 6), (18.805, 6)), ((18.723, 6), (18.641, 6.008), (18.559, 6.008)), ((17.921, 6.008), (17.078, 6.556), (16.571, 6.9)), ((14.231, 8.479), (13.049, 10.104), (13, 13)))
        self.add_bezier('e7', (40, 21), ((37.717, 22.89), (35.888, 22.957), (33, 22)))
        self.add_bezier('e8', (40, 21), ((41.154, 22.006), (42, 22.814), (42, 24.507)), ((42, 24.508), (42, 24.51), (42, 24.511)), ((42, 24.583), (42, 24.648), (42, 24.72)), ((41.992, 24.851), (41.992, 24.99), (41.984, 25.121)), ((41.984, 27.076), (41.415, 28.789), (40, 30)))
        self.add_bezier('e9', (38, 31), ((38.254, 31.9), (38.506, 32.395), (38.564, 33.335)), ((38.695, 35.504), (37.696, 37.803), (35.504, 38.531)), ((34.465, 38.866), (33.047, 39.033), (32, 39)))
        self.add_bezier('e10', (32, 39), ((31.231, 40.735), (30.267, 42), (28.165, 42)), ((26.16, 42), (24.99, 40.432), (24, 39)))
        self.add_bezier('e11', (32, 39), ((32.074, 37.118), (32.317, 36.334), (31, 35)))
        self.add_bezier('e12', (24, 39), ((23.141, 40.268), (21.897, 41.992), (20.122, 41.992)), ((20.049, 42), (19.985, 42), (19.913, 42)), ((19.911, 42), (19.91, 42), (19.909, 42)), ((19.844, 42), (19.77, 42), (19.696, 41.992)), ((17.659, 41.992), (16.761, 40.62), (16, 39)))
        self.add_bezier('e13', (13, 13), ((8.844, 13.884), (6.388, 16.827), (8, 21)))
        self.add_bezier('e14', (13, 13), ((13.925, 14.964), (14.93, 15.444), (17, 16)))
        self.add_bezier('e15', (16, 39), ((15.035, 39.025), (13.724, 38.842), (12.791, 38.539)), ((10.762, 37.885), (9.42, 36.011), (9.387, 33.867)), ((9.371, 32.722), (9.648, 32.064), (10, 31)))
        self.add_bezier('e16', (16, 39), ((15.992, 37.159), (15.748, 36.334), (17, 35)))
        self.add_bezier('e17', (9, 31), ((6.66, 29.715), (6.008, 28.091), (6.008, 25.35)), ((6.008, 25.278), (6, 25.213), (6, 25.141)), ((6, 25.14), (6, 25.138), (6, 25.137)), ((6, 23.01), (6.511, 22.375), (8, 21)))
        self.add_bezier('e18', (8, 21), ((10.013, 22.939), (12.275, 23.072), (15, 22)))
        self.add_bezier('e19', (35, 30), ((36.195, 30.761), (36.601, 31), (38, 31)))
        self.add_bezier('e20', (10, 31), ((11.432, 31.074), (11.83, 30.851), (13, 30)))
        self.add_contour('c0', 'e3', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5')
        self.add_contour('c3', 'e6')
        self.add_contour('c4', 'e1')
        self.add_contour('c5', 'e7')
        self.add_contour('c6', 'e8', 'e2', 'e9')
        self.add_contour('c7', 'e10')
        self.add_contour('c8', 'e11')
        self.add_contour('c9', 'e12')
        self.add_contour('c10', 'e13')
        self.add_contour('c11', 'e14')
        self.add_contour('c12', 'e15')
        self.add_contour('c13', 'e16')
        self.add_contour('c14', 'e17')
        self.add_contour('c15', 'e18')
        self.add_contour('c16', 'e19')
        self.add_contour('c17', 'e20')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c10', 'c11')
        self.relate('connect', 'c10', 'c3')
        self.relate('connect', 'c11', 'c3')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c4', 'c9')
        self.relate('connect', 'c7', 'c9')
        self.relate('connect', 'c16', 'c6')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c6', 'c8')
        self.relate('connect', 'c7', 'c8')
        self.relate('connect', 'c12', 'c13')
        self.relate('connect', 'c12', 'c9')
        self.relate('connect', 'c13', 'c9')
        self.relate('connect', 'c10', 'c14')
        self.relate('connect', 'c10', 'c15')
        self.relate('connect', 'c14', 'c15')
