"""Locker room hanger (wayfinding), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0dd718d-433c-595d-92b1-5714b73c92db'
SOURCE_PATH = 'icons-json/wayfinding/locker room hanger_a0dd718d-433c-595d-92b1-5714b73c92db.json'
AUTHOR = 'json_to_solo'

class LockerRoomHanger(Solo48):
    icon_id = 'locker-room-hanger'
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
        self.add_line('e4-1', (19, 12), (21, 9))
        self.add_arc('e4-2', (21, 9), (24, 8), radius_x=5)
        self.add_arc('e4-3', (24, 8), (28, 15), radius_x=5)
        self.add_line('e4-4', (28, 15), (24, 19))
        self.add_arc('e5-1', (6, 35), (4, 38), radius_x=4, sweep=False)
        self.add_arc('e5-2', (4, 38), (7, 40), radius_x=4, sweep=False)
        self.add_arc('e6-1', (41, 40), (44, 37), radius_x=3, sweep=False)
        self.add_line('e6-2', (44, 37), (42, 35))
        self.add_contour('c0', 'e4-1', 'e4-2', 'e4-3', 'e4-4', 'e0')
        self.add_contour('c1', 'e1', 'e5-1', 'e5-2', 'e2', 'e6-1', 'e6-2', 'e3', closed=True)
        self.relate('connect', 'c0', 'c1')
