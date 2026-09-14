"""Dollar sign (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7930e153-2438-44ec-8db7-960bb9aa10cc'
SOURCE_PATH = 'icons-json/state/dollar sign_7930e153-2438-44ec-8db7-960bb9aa10cc.json'
AUTHOR = 'json_to_solo'

class DollarSignState(Solo48):
    icon_id = 'dollar-sign-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('dollar', 'sign', 'state')

    def build(self):
        self.add_line('e0', (24, 4), (24, 8))
        self.add_line('e1', (24, 44), (24, 40))
        self.add_line('e2', (24, 8), (24, 23))
        self.add_line('e3', (24, 40), (24, 23))
        self.add_bezier('e4', (8, 32), ((8, 32.045), (8.015, 32.282), (8.015, 32.327)), ((8.015, 33.864), (9.324, 35.245), (10.589, 36.445)), ((13.615, 39.273), (18.793, 39.527), (24, 40)))
        self.add_bezier('e5', (39, 15), ((37.705, 11.836), (34.065, 9.191), (28.945, 8.191)), ((27.389, 7.891), (25.571, 8.155), (24, 8)))
        self.add_bezier('e6', (24, 8), ((20.524, 8.282), (17.295, 8.164), (14.385, 9.473)), ((9.018, 11.891), (8, 17.264), (12.16, 20.382)), ((15.2, 22.327), (20, 22.445), (24, 23)))
        self.add_bezier('e7', (24, 40), ((30.109, 39.455), (35.782, 38.873), (38.705, 35.1)), ((39.418, 34.182), (39.985, 33.073), (39.985, 32.036)), ((39.985, 31.965), (40, 31.902), (40, 31.831)), ((40, 31.83), (40, 31.828), (40, 31.827)), ((40, 31.573), (39.985, 31.309), (39.985, 31.055)), ((39.985, 27.809), (35.607, 25.236), (31.084, 24.136)), ((28.785, 23.582), (26.429, 23.264), (24, 23)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e5')
        self.add_contour('c4', 'e6')
        self.add_contour('c5', 'e2')
        self.add_contour('c6', 'e7')
        self.add_contour('c7', 'e3')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c0', 'c4')
        self.relate('connect', 'c0', 'c5')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c6')
        self.relate('connect', 'c1', 'c7')
        self.relate('connect', 'c2', 'c6')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c6', 'c7')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c4', 'c7')
        self.relate('connect', 'c5', 'c6')
        self.relate('connect', 'c5', 'c7')
        self.relate('connect', 'c6', 'c7')
