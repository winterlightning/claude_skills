"An athlete leans forward over the large rear wheel of a racing wheelchair. A long low frame stretches to a smaller front wheel on the right, with the rider's arm bent beside the rear hub.\n\nConstruction: Forward-leaning rider over a large rear wheel, with a low frame and smaller front wheel. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8f74edf-e2a9-5723-af01-98497dfde2e0'
SOURCE_PATH = 'pictographic-primitives/wayfinding/racing wheelchair_e8f74edf-e2a9-5723-af01-98497dfde2e0.svg'
AUTHOR = 'gpt-6'

class RacingWheelchairAthlete(Solo48):
    icon_id = 'racing-wheelchair-athlete'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('racing', 'wheelchair', 'athlete', 'sport', 'mobility', 'accessibility')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('rear-wheel-top-joint-1', (4, 30), (14, 20), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-top-joint-2', (14, 20), (24, 30), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-bottom', (24, 30), (4, 30), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_arc('front-wheel-top', (32, 34), (44, 34), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('front-wheel-bottom', (44, 34), (32, 34), radius_x=6, radius_y=6, large_arc=False, sweep=True)
        self.add_arc('head-top', (27, 11), (33, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('head-bottom', (33, 11), (27, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('rider-1', (26, 23), (14, 20))
        self.add_line('rider-2', (14, 20), (18, 30))
        self.add_line('frame', (24, 30), (32, 34))
        self.add_contour('rear-wheel', 'rear-wheel-top-joint-1', 'rear-wheel-top-joint-2', 'rear-wheel-bottom', closed=True)
        self.add_contour('front-wheel', 'front-wheel-top', 'front-wheel-bottom', closed=True)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('rider', 'rider-1', 'rider-2', closed=False)
        self.relate('connect', 'frame', 'rear-wheel')
        self.relate('connect', 'frame', 'front-wheel')
        self.relate('connect', 'rider', 'rear-wheel')
