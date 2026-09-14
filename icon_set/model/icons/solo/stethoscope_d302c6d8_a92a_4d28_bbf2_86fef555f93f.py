"""Stethoscope (symbol), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd302c6d8-a92a-4d28-bbf2-86fef555f93f'
SOURCE_PATH = 'icons-json/symbol/stethoscope_d302c6d8-a92a-4d28-bbf2-86fef555f93f.json'
AUTHOR = 'json_to_solo'

class Stethoscope(Solo48):
    icon_id = 'stethoscope'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('stethoscope', 'symbol')

    def build(self):
        self.add_line('e0', (6, 10), (6, 17))
        self.add_line('e1', (27, 9), (27, 17))
        self.add_line('e2', (38, 21), (38, 31))
        self.add_arc('e3-top', (34, 17), (42, 17), radius_x=4)
        self.add_arc('e3-bottom', (42, 17), (34, 17), radius_x=4)
        self.add_bezier('e4', (11, 6), ((9.036, 6.695), (6, 7.447), (6, 10)))
        self.add_bezier('e5', (6, 17), ((6, 17.065), (6.008, 17.585), (6.016, 17.651)), ((6.016, 18.698), (6.344, 19.835), (6.728, 20.801)), ((8.389, 24.949), (12.713, 26.779), (17, 27)))
        self.add_bezier('e6', (22, 6), ((23.645, 6.524), (27, 6.799), (27, 9)))
        self.add_bezier('e7', (27, 17), ((27, 17.965), (26.954, 19.451), (26.643, 20.351)), ((25.088, 24.777), (21.549, 26.869), (17, 27)))
        self.add_bezier('e8', (38, 31), ((38, 36.359), (32.992, 41.992), (27.535, 41.992)), ((27.469, 41.992), (27.404, 42), (27.338, 42)), ((27.337, 42), (27.336, 42), (27.335, 42)), ((27.271, 42), (27.206, 42), (27.142, 42)), ((22.495, 42), (18.355, 38.613), (17.111, 34.211)), ((16.481, 31.961), (16.975, 29.315), (17, 27)))
        self.add_contour('c0', 'e4', 'e0', 'e5')
        self.add_contour('c1', 'e6', 'e1', 'e7')
        self.add_contour('c2', 'e2', 'e8')
        self.add_contour('e3', 'e3-top', 'e3-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c2', 'e3')
