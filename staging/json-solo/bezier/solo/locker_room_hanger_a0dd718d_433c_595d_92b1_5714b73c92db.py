"""Locker room hanger (wayfinding), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0dd718d-433c-595d-92b1-5714b73c92db'
SOURCE_PATH = 'icons-json/wayfinding/locker room hanger_a0dd718d-433c-595d-92b1-5714b73c92db.json'
AUTHOR = 'json_to_solo'

class LockerRoomHangerWayfinding(Solo48):
    icon_id = 'locker-room-hanger-wayfinding'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'wayfinding'
    aliases = ()
    keywords = ('locker', 'room', 'hanger', 'wayfinding')

    def build(self):
        self.add_line('e0', (24, 19), (24, 22))
        self.add_line('e1', (24, 22), (6, 35))
        self.add_line('e2', (7, 40), (41, 40))
        self.add_line('e3', (42, 35), (24, 22))
        self.add_bezier('e4', (19, 12), ((19.227, 11.29), (19.873, 10.55), (20.318, 9.94)), ((21.091, 8.88), (22.536, 8.02), (23.782, 8.02)), ((23.862, 8.01), (23.943, 8), (24.023, 8)), ((24.025, 8), (24.026, 8), (24.027, 8)), ((24.091, 8.01), (24.155, 8.01), (24.218, 8.02)), ((25.091, 8.02), (25.991, 8.56), (26.636, 9.14)), ((28.564, 10.88), (29.018, 13.65), (27.564, 15.94)), ((26.564, 17.51), (25.173, 17.44), (24.155, 18.55)), ((24.045, 18.68), (24.091, 18.88), (24, 19)))
        self.add_bezier('e5', (6, 35), ((5.418, 35.413), (4, 36.728), (4, 37.532)), ((4, 37.545), (4, 37.557), (4, 37.57)), ((4, 39.03), (6.036, 39.65), (7, 40)))
        self.add_bezier('e6', (41, 40), ((42.027, 39.69), (44, 38.93), (44, 37.48)), ((44, 37.466), (44, 37.452), (44, 37.438)), ((44, 36.555), (42.653, 35.463), (42, 35)))
        self.add_contour('c0', 'e4', 'e0')
        self.add_contour('c1', 'e1', 'e5', 'e2', 'e6', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
