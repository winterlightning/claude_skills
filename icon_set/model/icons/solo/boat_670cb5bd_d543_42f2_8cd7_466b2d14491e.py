"""Boat (transportation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '670cb5bd-d543-42f2-8cd7-466b2d14491e'
SOURCE_PATH = 'icons-json/transportation/boat_670cb5bd-d543-42f2-8cd7-466b2d14491e.json'
AUTHOR = 'json_to_solo'

class BoatTransportation(Solo48):
    icon_id = 'boat-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('boat', 'transportation')

    def build(self):
        self.add_line('e0', (34, 22), (30, 8))
        self.add_line('e1', (30, 8), (12, 8))
        self.add_line('e2', (12, 8), (9, 22))
        self.add_line('e3', (4, 28), (4, 22))
        self.add_line('e4', (4, 22), (44, 22))
        self.add_bezier('e5', (44, 22), ((42.909, 26.702), (41.709, 30.917), (40.273, 35.471)), ((40.064, 36.148), (39.482, 38.412), (39.182, 38.806)), ((38.791, 39.348), (37.909, 39.643), (37.364, 39.655)), ((36.055, 39.692), (34.8, 38.006), (33.855, 36.997)), ((33.718, 36.849), (32.536, 35.532), (32.518, 35.532)), ((32.445, 35.545), (30.9, 37.735), (30.582, 38.043)), ((29.045, 39.532), (26.991, 40), (25.127, 39.68)), ((23.727, 39.335), (22.4, 38.671), (21.273, 37.489)), ((21.009, 37.218), (19.6, 35.471), (19.491, 35.471)), ((19.318, 35.458), (17.336, 37.44), (16.973, 37.76)), ((15.445, 39.077), (13.709, 39.975), (11.873, 39.975)), ((11.755, 39.988), (11.627, 39.988), (11.509, 40)), ((11.508, 40), (11.507, 40), (11.506, 40)), ((11.434, 40), (11.362, 39.988), (11.291, 39.988)), ((6.227, 39.988), (4, 34.031), (4, 28)))
        self.add_contour('c0', 'e0', 'e1', 'e2')
        self.add_contour('c1', 'e5', 'e3', 'e4', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
