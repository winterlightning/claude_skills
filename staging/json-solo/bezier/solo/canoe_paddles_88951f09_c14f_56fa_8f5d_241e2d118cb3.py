"""Canoe paddles (outdoors), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '88951f09-c14f-56fa-8f5d-241e2d118cb3'
SOURCE_PATH = 'icons-json/outdoors/canoe paddles_88951f09-c14f-56fa-8f5d-241e2d118cb3.json'
AUTHOR = 'json_to_solo'

class CanoePaddles88951f09(Solo48):
    icon_id = 'canoe-paddles-88951f09'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('canoe', 'paddles', 'outdoors')

    def build(self):
        self.add_line('e0', (40, 31), (40, 37))
        self.add_line('e1', (28, 39), (28, 32))
        self.add_line('e2', (30, 28), (34, 24))
        self.add_line('e3', (34, 24), (34, 4))
        self.add_line('e4', (20, 18), (20, 8))
        self.add_line('e5', (8, 9), (8, 17))
        self.add_line('e6', (10, 20), (14, 24))
        self.add_line('e7', (14, 24), (14, 43))
        self.add_line('e8', (20, 10), (8, 10))
        self.add_line('e9', (40, 38), (28, 38))
        self.add_bezier('e10', (34, 24), ((35.76, 25.509), (40, 28.736), (40, 31)))
        self.add_bezier('e11', (40, 37), ((40, 37.3), (40, 37.336), (40, 37.636)), ((39.988, 37.764), (39.988, 37.891), (39.975, 38.018)), ((39.975, 40.764), (39.003, 43.991), (34.351, 43.991)), ((34.08, 43.991), (33.809, 44), (33.538, 44)), ((33.535, 44), (33.532, 44), (33.529, 44)), ((33.335, 44), (33.142, 44), (32.948, 43.991)), ((29.538, 43.991), (28, 41.273), (28, 39)))
        self.add_bezier('e12', (28, 32), ((28, 30.073), (28.486, 29.491), (30, 28)))
        self.add_bezier('e13', (14, 24), ((15.822, 22.482), (20, 20.282), (20, 18)))
        self.add_bezier('e14', (20, 8), ((20, 6.109), (17.083, 4.018), (14.72, 4.018)), ((14.658, 4.009), (14.597, 4.009), (14.535, 4)), ((14.338, 4), (14.154, 4.009), (13.957, 4.009)), ((10.818, 4.009), (8, 5.845), (8, 8.236)), ((8, 8.345), (8, 8.9), (8, 9)))
        self.add_bezier('e15', (8, 17), ((8, 17.145), (8, 17.018), (8.012, 17.155)), ((8.012, 18.527), (8.978, 19), (10, 20)))
        self.add_contour('c0', 'e10', 'e0', 'e11', 'e1', 'e12', 'e2', closed=True)
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e13', 'e4', 'e14', 'e5', 'e15', 'e6', closed=True)
        self.add_contour('c3', 'e7')
        self.add_contour('c4', 'e8')
        self.add_contour('c5', 'e9')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c2')
        self.relate('connect', 'c4', 'c2')
        self.relate('connect', 'c5', 'c0')
        self.relate('connect', 'c5', 'c0')
