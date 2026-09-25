'A low recumbent handcycle is shown from the side without a rider. Two round wheels connect through a long horizontal frame, with an angled seat back and a raised front crank assembly.\n\nConstruction: Two equal wheels, low frame, reclined seat and raised front crank. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e63d81a-e416-4ca7-957e-b45b2694d38d'
SOURCE_PATH = 'pictographic-primitives/wayfinding/racing handcycle_2e63d81a-e416-4ca7-957e-b45b2694d38d.svg'
AUTHOR = 'gpt-6'

class RecumbentHandcycle(Solo48):
    icon_id = 'recumbent-handcycle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('handcycle', 'recumbent', 'cycle', 'racing', 'mobility', 'wheels')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('rear-wheel-top-joint-1', (4, 33), (11, 26), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-top-joint-2', (11, 26), (18, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-bottom', (18, 33), (4, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('front-wheel-top-joint-1', (30, 33), (37, 26), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('front-wheel-top-joint-2', (37, 26), (44, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('front-wheel-bottom', (44, 33), (30, 33), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('frame-1', (11, 26), (22, 26))
        self.add_line('frame-2', (22, 26), (37, 26))
        self.add_line('seat', (22, 26), (14, 8))
        self.add_line('crank', (37, 26), (30, 8))
        self.add_contour('rear-wheel', 'rear-wheel-top-joint-1', 'rear-wheel-top-joint-2', 'rear-wheel-bottom', closed=True)
        self.add_contour('front-wheel', 'front-wheel-top-joint-1', 'front-wheel-top-joint-2', 'front-wheel-bottom', closed=True)
        self.add_contour('frame', 'frame-1', 'frame-2', closed=False)
        self.relate('connect', 'frame', 'rear-wheel')
        self.relate('connect', 'frame', 'front-wheel')
        self.relate('connect', 'seat', 'frame')
        self.relate('connect', 'crank', 'frame')
        self.relate('connect', 'crank', 'front-wheel')
