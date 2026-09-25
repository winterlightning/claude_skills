'A round robot vacuum is seen from above, with a small circular sensor near its upper edge. Two short diagonal brush projections extend from the lower sides of its circular body.\n\nConstruction: Circular robot with one sensor. Side brushes omitted to keep a clean radial outline; centerline radius20.\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '96e6e169-e425-5a01-9657-76e56fb484e5'
SOURCE_PATH = 'pictographic-primitives/wayfinding/cleaning robot_96e6e169-e425-5a01-9657-76e56fb484e5.svg'
AUTHOR = 'gpt-6'

class RobotVacuum(Solo48):
    icon_id = 'robot-vacuum'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    categories = ('wayfinding', 'primitives')
    aliases = ()
    keywords = ('robot', 'vacuum', 'cleaning', 'automatic', 'floor', 'appliance')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('body-top', (4, 24), (44, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('body-bottom', (44, 24), (4, 24), radius_x=20, radius_y=20, large_arc=False, sweep=True)
        self.add_arc('sensor-top', (21, 16), (27, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('sensor-bottom', (27, 16), (21, 16), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('body', 'body-top', 'body-bottom', closed=True)
        self.add_contour('sensor', 'sensor-top', 'sensor-bottom', closed=True)
