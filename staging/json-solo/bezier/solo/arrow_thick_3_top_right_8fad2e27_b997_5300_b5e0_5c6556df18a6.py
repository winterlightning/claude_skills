"""Arrow thick 3 top right (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fad2e27-b997-5300-b5e0-5c6556df18a6'
SOURCE_PATH = 'icons-json/arrows/arrow thick 3 top right_8fad2e27-b997-5300-b5e0-5c6556df18a6.json'
AUTHOR = 'json_to_solo'

class ArrowThick3TopRightArrows(Solo48):
    icon_id = 'arrow-thick-3-top-right-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('arrow', 'thick', 'top', 'right', 'arrows')

    def build(self):
        self.add_line('e0', (13, 40), (33, 22))
        self.add_line('e1', (33, 22), (33, 36))
        self.add_line('e2', (42, 36), (42, 6))
        self.add_line('e3', (42, 6), (14, 6))
        self.add_line('e4', (12, 15), (27, 15))
        self.add_line('e5', (27, 15), (8, 34))
        self.add_bezier('e6', (8, 34), ((7.1, 34.867), (6.008, 35.61), (6.008, 36.927)), ((6.008, 37.058), (6, 37.189), (6, 37.32)), ((6, 37.525), (6.008, 37.721), (6.008, 37.925)), ((6.008, 39.848), (7.915, 41.984), (9.895, 41.984)), ((10.031, 41.992), (10.16, 42), (10.289, 42)), ((10.291, 42), (10.293, 42), (10.295, 42)), ((11.335, 42), (12.28, 40.687), (13, 40)))
        self.add_bezier('e7', (33, 36), ((33, 37.604), (33.475, 39.578), (34.792, 40.609)), ((37.058, 42), (40.715, 41.517), (41.746, 38.768)), ((41.967, 38.179), (41.992, 37.435), (41.992, 36.813)), ((41.992, 36.731), (42, 36.641), (42, 36.551)), ((42, 36.461), (42, 36.09), (42, 36)))
        self.add_bezier('e8', (14, 6), ((13.403, 6), (12.987, 6.016), (12.382, 6.016)), ((10.025, 6.016), (8.291, 6.139), (6.818, 8.234)), ((6.376, 8.855), (6.008, 9.51), (6.008, 10.295)), ((6.008, 10.361), (6, 10.435), (6, 10.5)), ((6, 10.501), (6, 10.502), (6, 10.503)), ((6, 10.568), (6, 10.64), (6, 10.705)), ((6, 11.335), (6.295, 11.883), (6.614, 12.406)), ((7.816, 14.395), (9.758, 15), (12, 15)))
        self.add_contour('c0', 'e6', 'e0', 'e1', 'e7', 'e2', 'e3', 'e8', 'e4', 'e5', closed=True)
