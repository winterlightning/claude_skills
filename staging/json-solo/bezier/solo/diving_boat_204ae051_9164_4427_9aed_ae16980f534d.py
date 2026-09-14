"""Diving boat (recreation), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '204ae051-9164-4427-9aed-ae16980f534d'
SOURCE_PATH = 'icons-json/recreation/diving boat_204ae051-9164-4427-9aed-ae16980f534d.json'
AUTHOR = 'json_to_solo'

class DivingBoatRecreation(Solo48):
    icon_id = 'diving-boat-recreation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'recreation'
    aliases = ()
    keywords = ('diving', 'boat', 'recreation')

    def build(self):
        self.add_line('e0', (16, 8), (19, 15))
        self.add_line('e1', (19, 15), (14, 18))
        self.add_line('e2', (11, 33), (37, 18))
        self.add_line('e3', (23, 12), (19, 15))
        self.add_line('e4', (19, 15), (23, 26))
        self.add_line('e5', (4, 40), (6, 40))
        self.add_bezier('e6', (37, 18), ((37.991, 23.94), (37.045, 27.48), (35, 33)))
        self.add_bezier('e7', (6, 40), ((6.764, 39.62), (7.309, 39.26), (7.945, 38.65)), ((8.164, 38.45), (8.373, 38.25), (8.582, 38.05)), ((8.936, 38.32), (9.282, 38.59), (9.636, 38.87)), ((10.491, 39.53), (11.618, 39.99), (12.673, 39.99)), ((12.882, 39.99), (13.091, 40), (13.291, 40)), ((13.427, 40), (13.564, 39.99), (13.7, 39.99)), ((15.118, 39.99), (16.491, 39.32), (17.555, 38.33)), ((17.9, 38.01), (19.027, 36.55), (19.118, 36.55)), ((19.191, 36.55), (20.318, 38.03), (20.645, 38.36)), ((21.618, 39.33), (22.9, 39.99), (24.227, 39.99)), ((25.664, 39.99), (27.018, 39.23), (28.045, 38.15)), ((28.4, 37.78), (29.527, 36.22), (29.636, 36.21)), ((29.645, 36.21), (30.718, 37.68), (30.982, 38)), ((31.882, 39.09), (33.3, 39.99), (34.682, 39.99)), ((34.782, 39.99), (34.873, 39.99), (34.973, 39.99)), ((36.255, 39.99), (37.573, 39.28), (38.5, 38.33)), ((38.818, 38), (39.909, 36.61), (39.982, 36.61)), ((40.245, 36.97), (40.509, 37.32), (40.773, 37.68)), ((40.845, 37.78), (40.927, 37.87), (41.009, 37.97)), ((41.855, 39), (42.836, 39.54), (44, 40)))
        self.add_contour('c0', 'e0', 'e1')
        self.add_contour('c1', 'e2', 'e6')
        self.add_contour('c2', 'e3', 'e4')
        self.add_contour('c3', 'e5', 'e7')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c2', 'c1')
