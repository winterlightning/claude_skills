"A child kneels and bends forward toward a small toy car at lower-left. The car has two round wheels and a raised cab, while the child's arms reach toward it.\n\nConstruction: Kneeling child reaches down to a small wheeled toy car. Bounds (4,8)-(44,40).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used."
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2b08eed-cd59-4667-ba85-d70a3d670bef'
SOURCE_PATH = 'pictographic-primitives/wayfinding/family child play car_d2b08eed-cd59-4667-ba85-d70a3d670bef.svg'
AUTHOR = 'gpt-6'

class ChildPlayingWithToyCar(Solo48):
    icon_id = 'child-playing-with-toy-car'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'wayfinding'
    aliases = ()
    keywords = ('child', 'toy', 'car', 'play', 'kneeling', 'vehicle')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_arc('person-head-top', (23, 11), (29, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('person-head-bottom', (29, 11), (23, 11), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('person-body-1', (30, 22), (36, 27))
        self.add_line('person-body-2', (36, 27), (32, 36))
        self.add_line('person-body-3', (32, 36), (44, 36))
        self.add_line('person-arm-1', (30, 22), (18, 23))
        self.add_line('toy-car-1', (7, 34), (4, 34))
        self.add_line('toy-car-2', (4, 34), (4, 26))
        self.add_line('toy-car-3', (4, 26), (10, 26))
        self.add_line('toy-car-4', (10, 26), (12, 23))
        self.add_line('toy-car-5', (12, 23), (18, 23))
        self.add_line('toy-car-6', (18, 23), (22, 34))
        self.add_arc('rear-wheel-top-joint-1', (4, 37), (7, 34), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-top-joint-2', (7, 34), (10, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('rear-wheel-bottom', (10, 37), (4, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('front-wheel-top-joint-1', (19, 37), (22, 34), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('front-wheel-top-joint-2', (22, 34), (25, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_arc('front-wheel-bottom', (25, 37), (19, 37), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_contour('person-head', 'person-head-top', 'person-head-bottom', closed=True)
        self.add_contour('person-body', 'person-body-1', 'person-body-2', 'person-body-3', closed=False)
        self.add_contour('person-arm', 'person-arm-1', closed=False)
        self.add_contour('toy-car', 'toy-car-1', 'toy-car-2', 'toy-car-3', 'toy-car-4', 'toy-car-5', 'toy-car-6', closed=False)
        self.add_contour('rear-wheel', 'rear-wheel-top-joint-1', 'rear-wheel-top-joint-2', 'rear-wheel-bottom', closed=True)
        self.add_contour('front-wheel', 'front-wheel-top-joint-1', 'front-wheel-top-joint-2', 'front-wheel-bottom', closed=True)
        self.relate('connect', 'person-body', 'person-arm')
        self.relate('connect', 'rear-wheel', 'toy-car')
        self.relate('connect', 'front-wheel', 'toy-car')
        self.relate('connect', 'person-arm', 'toy-car')
