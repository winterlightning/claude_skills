"""Field corner kick (sports), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c9ec94c5-4ddc-4911-8248-43fbc7fa3b42'
SOURCE_PATH = 'icons-json/sports/field corner kick_c9ec94c5-4ddc-4911-8248-43fbc7fa3b42.json'
AUTHOR = 'json_to_solo'

class FieldCornerKickSports(Solo48):
    icon_id = 'field-corner-kick-sports'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('field', 'corner', 'kick', 'sports')

    def build(self):
        self.add_line('e0', (21, 4), (21, 17))
        self.add_line('e1', (8, 42), (14, 39))
        self.add_line('e2', (40, 44), (30, 39))
        self.add_line('e3', (21, 34), (30, 39))
        self.add_line('e4', (21, 34), (14, 39))
        self.add_line('e5', (21, 34), (21, 17))
        self.add_line('e6', (28, 4), (33, 6))
        self.add_line('e7', (40, 5), (40, 16))
        self.add_line('e8', (33, 18), (28, 16))
        self.add_bezier('e9', (21, 6), ((21.615, 5.573), (23.823, 4), (24.657, 4)), ((24.691, 4), (24.724, 4), (24.766, 4)), ((25.912, 4), (26.846, 4), (28, 4)))
        self.add_bezier('e10', (33, 6), ((35.232, 6.8), (37.937, 5.955), (40, 5)))
        self.add_bezier('e11', (40, 16), ((38.004, 17.064), (35.316, 18.836), (33, 18)))
        self.add_bezier('e12', (28, 16), ((25.549, 15.118), (23.232, 15.773), (21, 17)))
        self.add_bezier('e13', (30, 39), ((29.048, 39.745), (28.017, 40.073), (26.964, 40.655)), ((23.798, 42.409), (19.958, 42.455), (16.792, 40.655)), ((15.747, 40.064), (14.935, 39.764), (14, 39)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e9', 'e6', 'e10', 'e7', 'e11', 'e8', 'e12')
        self.add_contour('c7', 'e13')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c7')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c6', 'c0')
