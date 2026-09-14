"""Nanobot (state), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd990e4b-d221-4af4-82e5-519aa93fd2a1'
SOURCE_PATH = 'icons-json/state/nanobot_dd990e4b-d221-4af4-82e5-519aa93fd2a1.json'
AUTHOR = 'json_to_solo'

class NanobotState(Solo48):
    icon_id = 'nanobot-state'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('nanobot', 'state')

    def build(self):
        self.add_line('e0', (10, 28), (10, 13))
        self.add_line('e1', (11, 11), (23, 4))
        self.add_line('e2', (25, 4), (37, 11))
        self.add_line('e3', (38, 12), (38, 29))
        self.add_line('e4', (11, 30), (23, 38))
        self.add_line('e5', (26, 38), (37, 30))
        self.add_arc('e6-top', (19, 19), (29, 19), radius_x=5)
        self.add_arc('e6-bottom', (29, 19), (19, 19), radius_x=5)
        self.add_bezier('e7', (37, 44), ((38.61, 42.191), (39.99, 40.045), (39.99, 37.627)), ((40, 37.565), (40, 37.511), (40, 37.448)), ((40, 37.447), (40, 37.446), (40, 37.445)), ((39.99, 37.318), (39.99, 37.182), (39.98, 37.055)), ((39.98, 34.582), (38.51, 31.936), (37, 30)))
        self.add_bezier('e8', (11, 30), ((10.72, 29.345), (10, 28.791), (10, 28)))
        self.add_bezier('e9', (10, 13), ((10, 12.2), (10.51, 11.582), (11, 11)))
        self.add_bezier('e10', (23, 4), ((23.67, 4), (24.33, 4), (25, 4)))
        self.add_bezier('e11', (37, 11), ((37.37, 11.309), (37.67, 11.645), (38, 12)))
        self.add_bezier('e12', (38, 29), ((38, 29.4), (37.11, 29.809), (37, 30)))
        self.add_bezier('e13', (23, 38), ((23.88, 38.236), (25.15, 38.564), (26, 38)))
        self.add_bezier('e14', (11, 30), ((9.81, 32), (8.02, 34.645), (8.02, 37.036)), ((8.01, 37.155), (8.01, 37.282), (8, 37.4)), ((8, 37.403), (8, 37.406), (8, 37.409)), ((8, 37.597), (8.01, 37.785), (8.01, 37.964)), ((8.01, 40.236), (9.6, 42.255), (11, 44)))
        self.add_contour('c0', 'e7')
        self.add_contour('c1', 'e8', 'e0', 'e9', 'e1', 'e10', 'e2', 'e11', 'e3', 'e12')
        self.add_contour('c2', 'e4', 'e13', 'e5')
        self.add_contour('c3', 'e14')
        self.add_contour('e6', 'e6-top', 'e6-bottom', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
