"""Convertible (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '42384007-0580-5468-9fff-0d458f8b9b2e'
SOURCE_PATH = 'icons-json/transportation/convertible_42384007-0580-5468-9fff-0d458f8b9b2e.json'
AUTHOR = 'json_to_solo'

class ConvertibleTransportation(Solo48):
    icon_id = 'convertible-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('convertible', 'transportation')

    def build(self):
        self.add_line('e0', (26, 24), (20, 24))
        self.add_line('e1', (18, 22), (17, 19))
        self.add_line('e2', (16, 19), (4, 19))
        self.add_line('e3', (4, 19), (4, 31))
        self.add_line('e4', (29, 19), (25, 8))
        self.add_line('e5', (29, 19), (40, 20))
        self.add_line('e6', (44, 24), (44, 29))
        self.add_line('e7', (18, 34), (31, 34))
        self.add_line('e8', (11, 8), (11, 19))
        self.add_arc('e9-top', (8, 34), (18, 34), radius_x=5, radius_y=6)
        self.add_arc('e9-bottom', (18, 34), (8, 34), radius_x=5, radius_y=6)
        self.add_arc('e10-top', (31, 34), (41, 34), radius_x=5, radius_y=6)
        self.add_arc('e10-bottom', (41, 34), (31, 34), radius_x=5, radius_y=6)
        self.add_bezier('e11', (29, 19), ((27.818, 21.511), (28.127, 23.114), (26, 24)))
        self.add_bezier('e12', (20, 24), ((18.591, 23.458), (18.891, 23.563), (18, 22)))
        self.add_bezier('e13', (17, 19), ((16.7, 19), (16.3, 19), (16, 19)))
        self.add_bezier('e14', (4, 31), ((4.109, 31.271), (4.109, 31.926), (4.255, 32.185)), ((5.245, 34.043), (7.509, 34.062), (9, 34)))
        self.add_bezier('e15', (40, 20), ((41.718, 20.197), (43.991, 20.628), (43.991, 23.655)), ((44, 23.766), (44, 23.889), (44, 24)))
        self.add_bezier('e16', (44, 29), ((43.191, 31.757), (41.9, 32.585), (40, 34)))
        self.add_contour('c0', 'e11', 'e0', 'e12', 'e1', 'e13', 'e2', 'e3', 'e14')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e5', 'e15', 'e6', 'e16')
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('e10', 'e10-top', 'e10-bottom', closed=True)
        self.add_contour('e9', 'e9-top', 'e9-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c0', 'e9')
        self.relate('connect', 'c2', 'e10')
        self.relate('connect', 'c3', 'e9')
        self.relate('connect', 'c3', 'e10')
        self.relate('connect', 'c4', 'c0')
