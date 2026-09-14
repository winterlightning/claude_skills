"""Arrow rectangle right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6617292-aa59-5ace-9d1d-64e58b69ae47'
SOURCE_PATH = 'icons-json/arrows/arrow rectangle right_f6617292-aa59-5ace-9d1d-64e58b69ae47.json'
AUTHOR = 'json_to_solo'

class ArrowRectangleRightArrows(Solo48):
    icon_id = 'arrow-rectangle-right-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'rectangle', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (22, 32), (30, 24))
        self.add_line('e1', (30, 24), (22, 15))
        self.add_line('e2', (13, 6), (35, 6))
        self.add_line('e3', (42, 15), (42, 35))
        self.add_line('e4', (33, 42), (11, 42))
        self.add_line('e5', (6, 35), (6, 10))
        self.add_bezier('e6', (35, 6), ((35.131, 6), (35.708, 6.008), (35.839, 6.008)), ((39.087, 6.008), (41.984, 8.864), (41.984, 12.12)), ((41.984, 12.938), (42, 13.756), (42, 14.575)), ((42, 14.714), (42, 14.861), (42, 15)))
        self.add_bezier('e7', (42, 35), ((42, 35.147), (41.984, 35.741), (41.984, 35.888)), ((41.984, 38.883), (39.423, 41.247), (36.665, 41.885)), ((36.125, 42), (35.52, 41.984), (34.98, 41.984)), ((34.456, 41.984), (33.933, 42), (33.417, 42)), ((33.278, 42), (33.139, 42), (33, 42)))
        self.add_bezier('e8', (11, 42), ((10.869, 42), (10.655, 41.992), (10.525, 41.992)), ((8.381, 41.992), (6.622, 40.11), (6.147, 38.122)), ((6.008, 37.541), (6.008, 36.845), (6.008, 36.24)), ((6.008, 36.068), (6, 35.896), (6, 35.733)), ((6, 35.635), (6, 35.09), (6, 35)))
        self.add_bezier('e9', (6, 10), ((6.008, 9.869), (6.008, 9.829), (6.016, 9.698)), ((6.016, 7.923), (7.669, 6.016), (9.485, 6.016)), ((10.099, 6.016), (10.705, 6), (11.31, 6)), ((11.997, 6), (12.321, 6), (13, 6)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', closed=True)
