"""Delicata squash (food), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39f7021c-7064-4587-a19c-afa4eab4412a'
SOURCE_PATH = 'icons-json/food/delicata squash_39f7021c-7064-4587-a19c-afa4eab4412a.json'
AUTHOR = 'json_to_solo'

class DelicataSquash(Solo48):
    icon_id = 'delicata-squash'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('delicata', 'squash', 'food')

    def build(self):
        self.add_line('e0', (42, 6), (38, 10))
        self.add_bezier('e1', (37, 11), ((32.582, 13.962), (28.991, 17.635), (25.244, 21.382)), ((19.279, 27.346), (13.899, 33.97), (8, 40)))
        self.add_bezier('e2', (8, 40), ((9.685, 41.317), (11.138, 41.992), (13.364, 41.992)), ((13.517, 41.992), (13.67, 42), (13.831, 42)), ((13.833, 42), (13.836, 42), (13.838, 42)), ((13.961, 42), (14.092, 41.992), (14.223, 41.992)), ((17.119, 41.992), (20.506, 40.511), (22.92, 38.997)), ((28.876, 35.275), (34.726, 29.482), (37.647, 23.018)), ((39.005, 20.015), (40.364, 16.055), (39.374, 12.734)), ((39.071, 11.744), (38.581, 10.851), (38, 10)))
        self.add_bezier('e3', (8, 40), ((7.116, 38.609), (6.008, 36.796), (6.008, 35.103)), ((6.008, 34.982), (6, 34.861), (6, 34.74)), ((6, 34.738), (6, 34.736), (6, 34.735)), ((6, 34.432), (6.008, 34.129), (6.008, 33.818)), ((6.008, 30.75), (7.227, 27.731), (8.692, 25.088)), ((9.69, 23.288), (10.909, 21.578), (12.235, 20.007)), ((17.111, 14.231), (26.626, 6.499), (34.849, 8.635)), ((35.995, 8.929), (36.994, 9.386), (38, 10)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
