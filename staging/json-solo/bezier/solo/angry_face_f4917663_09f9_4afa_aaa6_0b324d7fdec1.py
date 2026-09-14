"""Angry face (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4917663-09f9-4afa-aaa6-0b324d7fdec1'
SOURCE_PATH = 'icons-json/symbol/angry face_f4917663-09f9-4afa-aaa6-0b324d7fdec1.json'
AUTHOR = 'json_to_solo'

class AngryFaceF4917663(Solo48):
    icon_id = 'angry-face-f4917663'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('angry', 'face', 'symbol')

    def build(self):
        self.add_line('sym-e0', (30, 13), (42, 6))
        self.add_line('sym-e1', (36, 20), (39, 18))
        self.add_bezier('sym-e2', (39, 18), ((38.182, 18.548), (36.818, 19.452), (36, 20)))
        self.add_line('sym-e3', (39, 18), (39, 18))
        self.add_bezier('sym-e4', (24, 26), ((28.954, 25.976), (34.013, 28.485), (37, 33)))
        self.add_bezier('sym-e5', (37, 33), ((38.702, 35.577), (39.714, 38.956), (40, 42)))
        self.add_line('sym-e6', (18, 13), (6, 6))
        self.add_line('sym-e7', (12, 20), (9, 18))
        self.add_bezier('sym-e8', (9, 18), ((9.818, 18.548), (11.182, 19.452), (12, 20)))
        self.add_line('sym-e9', (9, 18), (9, 18))
        self.add_bezier('sym-e10', (24, 26), ((19.046, 25.976), (13.987, 28.485), (11, 33)))
        self.add_bezier('sym-e11', (11, 33), ((9.298, 35.577), (8.286, 38.956), (8, 42)))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', closed=True)
        self.add_contour('sym-c2', 'sym-e3', closed=True)
        self.add_contour('sym-c3', 'sym-e4', 'sym-e5')
        self.add_contour('sym-c4', 'sym-e6')
        self.add_contour('sym-c5', 'sym-e7', 'sym-e8', closed=True)
        self.add_contour('sym-c6', 'sym-e9', closed=True)
        self.add_contour('sym-c7', 'sym-e10', 'sym-e11')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c3', 'sym-c7')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c5', 'sym-c6')
        self.relate('connect', 'sym-c1', 'sym-c2')
