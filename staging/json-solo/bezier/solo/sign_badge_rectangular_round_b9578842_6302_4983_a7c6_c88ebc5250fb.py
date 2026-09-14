"""Sign badge rectangular round (maps), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b9578842-6302-4983-a7c6-c88ebc5250fb'
SOURCE_PATH = 'icons-json/maps/sign badge rectangular round_b9578842-6302-4983-a7c6-c88ebc5250fb.json'
AUTHOR = 'json_to_solo'

class SignBadgeRectangularRoundMaps(Solo48):
    icon_id = 'sign-badge-rectangular-round-maps'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'maps'
    aliases = ()
    keywords = ('sign', 'badge', 'rectangular', 'round', 'maps')

    def build(self):
        self.add_line('sym-e0', (24, 6), (40, 6))
        self.add_bezier('sym-e1', (40, 6), ((40.237, 6.098), (39.771, 6), (40, 6)))
        self.add_bezier('sym-e2', (40, 6), ((40.851, 6.548), (42, 7.945), (42, 9)))
        self.add_bezier('sym-e3', (42, 9), ((42, 9.041), (41.992, 8.959), (42, 9)))
        self.add_line('sym-e4', (42, 9), (42, 24))
        self.add_line('sym-e5', (42, 24), (42, 39))
        self.add_bezier('sym-e6', (42, 39), ((41.992, 39.041), (42, 38.959), (42, 39)))
        self.add_bezier('sym-e7', (42, 39), ((42, 40.055), (40.851, 41.452), (40, 42)))
        self.add_bezier('sym-e8', (40, 42), ((39.771, 42), (40.237, 41.902), (40, 42)))
        self.add_line('sym-e9', (40, 42), (24, 42))
        self.add_line('sym-e10', (24, 42), (8, 42))
        self.add_bezier('sym-e11', (8, 42), ((7.763, 41.902), (8.229, 42), (8, 42)))
        self.add_bezier('sym-e12', (8, 42), ((7.149, 41.452), (6, 40.055), (6, 39)))
        self.add_bezier('sym-e13', (6, 39), ((6, 38.959), (6.008, 39.041), (6, 39)))
        self.add_line('sym-e14', (6, 39), (6, 24))
        self.add_line('sym-e15', (6, 24), (6, 9))
        self.add_bezier('sym-e16', (6, 9), ((6.008, 8.959), (6, 9.041), (6, 9)))
        self.add_bezier('sym-e17', (6, 9), ((6, 7.945), (7.149, 6.548), (8, 6)))
        self.add_bezier('sym-e18', (8, 6), ((8.229, 6), (7.763, 6.098), (8, 6)))
        self.add_line('sym-e19', (8, 6), (24, 6))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', closed=True)
