"""Target (war), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa35ca2e-3882-40aa-94b0-a993fab50043'
SOURCE_PATH = 'icons-json/war/target_fa35ca2e-3882-40aa-94b0-a993fab50043.json'
AUTHOR = 'json_to_solo'

class Target(Solo48):
    icon_id = 'target'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('target', 'war')

    def build(self):
        self.add_line('e0', (24, 14), (24, 10))
        self.add_line('e1', (35, 24), (42, 24))
        self.add_line('e2', (24, 34), (24, 42))
        self.add_line('e3', (13, 24), (9, 24))
        self.add_line('e4', (24, 6), (24, 10))
        self.add_line('e5', (6, 24), (9, 24))
        self.add_line('e6', (21, 10), (26, 10))
        self.add_line('e7', (38, 22), (38, 26))
        self.add_bezier('e8', (26, 10), ((26.45, 10), (27.445, 10.295), (27.878, 10.402)), ((32.419, 11.506), (35.913, 15.311), (37.295, 19.705)), ((37.557, 20.515), (38, 21.141), (38, 22)))
        self.add_bezier('e9', (38, 26), ((38, 26.933), (37.574, 28.459), (37.287, 29.326)), ((35.692, 34.268), (31.421, 37.647), (26.348, 38.49)), ((25.555, 38.621), (24.769, 38.752), (23.975, 38.891)), ((23.157, 38.752), (22.347, 38.613), (21.529, 38.474)), ((15.785, 37.475), (11.097, 32.771), (9.911, 27.085)), ((9.698, 26.054), (9.485, 25.031), (9.273, 24)), ((9.428, 23.247), (9.575, 22.503), (9.731, 21.75)), ((10.598, 17.52), (12.562, 14.206), (16.26, 11.858)), ((17.381, 11.146), (19.65, 10), (21, 10)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6', 'e8', 'e7', 'e9', closed=True)
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c3', 'c6')
        self.relate('connect', 'c5', 'c6')
