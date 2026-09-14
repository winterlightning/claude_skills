"""Horn (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '82d50937-0e36-4f84-b67b-aafe2b74a0ce'
SOURCE_PATH = 'icons-json/transportation/horn_82d50937-0e36-4f84-b67b-aafe2b74a0ce.json'
AUTHOR = 'json_to_solo'

class Horn82d50937(Solo48):
    icon_id = 'horn-82d50937'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('horn', 'transportation')

    def build(self):
        self.add_line('e0', (29, 40), (21, 40))
        self.add_line('e1', (15, 33), (15, 25))
        self.add_line('e2', (32, 17), (15, 17))
        self.add_line('e3', (13, 17), (4, 8))
        self.add_line('e4', (4, 8), (4, 34))
        self.add_line('e5', (4, 34), (14, 25))
        self.add_line('e6', (14, 25), (36, 25))
        self.add_line('e7', (44, 34), (44, 9))
        self.add_bezier('e8', (33, 25), ((33.382, 26.92), (34.082, 29.527), (34.2, 31.564)), ((34.455, 35.985), (32.536, 39.985), (29.682, 39.985)), ((29.609, 40), (29.073, 40), (29, 40)))
        self.add_bezier('e9', (21, 40), ((20.7, 40), (20.673, 39.985), (20.364, 39.985)), ((19.6, 39.898), (18.518, 40), (17.764, 39.84)), ((15.564, 38.72), (15.145, 36.345), (15, 33)))
        self.add_bezier('e10', (44, 9), ((41.782, 11.778), (39.6, 15.2), (36.809, 16.335)), ((35.345, 16.931), (33.491, 17), (32, 17)))
        self.add_bezier('e11', (15, 17), ((14.382, 17), (13.627, 17.102), (13, 17)))
        self.add_bezier('e12', (36, 25), ((36.918, 25.844), (37.727, 27.025), (38.627, 27.971)), ((40.1, 29.513), (41.409, 31.447), (42.9, 32.945)), ((43.009, 33.047), (43.118, 33.149), (43.227, 33.251)), ((43.382, 33.353), (43.545, 33.455), (43.709, 33.556)), ((43.845, 33.687), (43.873, 33.84), (44, 34)))
        self.add_contour('c0', 'e8', 'e0', 'e9', 'e1')
        self.add_contour('c1', 'e10', 'e2', 'e11', 'e3', 'e4', 'e5', 'e6', 'e12', 'e7', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
