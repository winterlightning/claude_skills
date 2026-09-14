'A seated rider faces right on a low cycle with two visible round wheels. Both hands reach toward a raised hand crank, and the bent legs extend toward the front wheel.\n\nConstruction: Seated rider between two wheels, arms extending toward a raised hand crank. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f954029-c6f4-4eea-8610-b9a1827cde85'
SOURCE_PATH = 'pictographic-primitives/wayfinding/handcycle_6f954029-c6f4-4eea-8610-b9a1827cde85.svg'
AUTHOR = 'gpt-6'

class PersonRidingHandcycle(Solo48):
    icon_id = 'person-riding-handcycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('handcycle', 'rider', 'cycle', 'accessibility', 'mobility', 'sport')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('rear-wheel-top-joint-1', (4, 33), (11, 26), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-top-joint-2', (11, 26), (18, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-bottom', (18, 33), (4, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('front-wheel-top-joint-1', (30, 33), (37, 26), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('front-wheel-top-joint-2', (37, 26), (44, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('front-wheel-bottom', (44, 33), (30, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('person-head-top', (15, 11), (21, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (21, 11), (15, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (16, 23), (18, 26))
        self.add_line('person-body-2', (18, 26), (26, 26))
        self.add_line('person-arms-1', (16, 23), (26, 21))
        self.add_line('person-arms-2', (26, 21), (32, 18))
        self.add_line('frame-1', (11, 26), (18, 26))
        self.add_line('frame-2', (18, 26), (26, 26))
        self.add_line('frame-3', (26, 26), (37, 26))
        self.add_line('crank', (32, 18), (37, 26))
        self.add_contour('rear-wheel', 'rear-wheel-top-joint-1', 'rear-wheel-top-joint-2', 'rear-wheel-bottom', closed=True)
        self.add_contour('front-wheel', 'front-wheel-top-joint-1', 'front-wheel-top-joint-2', 'front-wheel-bottom', closed=True)
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', closed=False)
        self.add_contour('person-arms', 'person-arms-1', 'person-arms-2', closed=False)
        self.add_contour('frame', 'frame-1', 'frame-2', 'frame-3', closed=False)
        self.relate('connect', 'person-body', 'person-arms')
        self.relate('connect', 'frame', 'rear-wheel')
        self.relate('connect', 'frame', 'front-wheel')
        self.relate('connect', 'frame', 'person-body')
        self.relate('connect', 'crank', 'person-arms')
        self.relate('connect', 'crank', 'frame')
