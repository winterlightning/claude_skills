"""Wristband (events), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd01c7ceb-a077-5369-924c-20e53e6260db'
SOURCE_PATH = 'icons-json/events/wristband_d01c7ceb-a077-5369-924c-20e53e6260db.json'
AUTHOR = 'json_to_solo'

class Wristband(Solo48):
    icon_id = 'wristband'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'events'
    aliases = ()
    keywords = ('wristband', 'events')

    def build(self):
        self.add_arc('sym-e0', (31, 38), (28, 40), radius_x=4)
        self.add_line('sym-e2', (28, 40), (26, 40))
        self.add_arc('sym-e3', (26, 40), (24, 40), radius_x=20, sweep=False)
        self.add_arc('sym-e4', (24, 40), (22, 40), radius_x=20, sweep=False)
        self.add_line('sym-e5', (22, 40), (20, 40))
        self.add_arc('sym-e7', (20, 40), (17, 38), radius_x=4)
        self.add_line('sym-e8', (17, 38), (17, 25))
        self.add_arc('sym-e9', (17, 25), (6, 21), radius_x=21)
        self.add_arc('sym-e10', (6, 21), (5, 19), radius_x=45, sweep=False)
        self.add_line('sym-e11', (5, 19), (4, 19))
        self.add_line('sym-e12', (4, 19), (4, 16))
        self.add_arc('sym-e13', (4, 16), (8, 11), radius_x=8)
        self.add_arc('sym-e14-1', (8, 11), (14, 9), radius_x=24)
        self.add_line('sym-e14-2', (14, 9), (23, 8))
        self.add_line('sym-e15', (23, 8), (24, 8))
        self.add_line('sym-e16', (24, 8), (25, 8))
        self.add_line('sym-e17-1', (25, 8), (34, 9))
        self.add_arc('sym-e17-2', (34, 9), (40, 11), radius_x=24)
        self.add_arc('sym-e18', (40, 11), (44, 16), radius_x=8)
        self.add_line('sym-e19-1', (44, 16), (44, 17))
        self.add_line('sym-e19-2', (44, 17), (44, 19))
        self.add_line('sym-e20', (44, 19), (43, 19))
        self.add_arc('sym-e21', (43, 19), (42, 21), radius_x=45, sweep=False)
        self.add_arc('sym-e22', (42, 21), (31, 25), radius_x=20)
        self.add_arc('sym-e23', (31, 25), (27, 22), radius_x=4, sweep=False)
        self.add_line('sym-e24', (27, 22), (24, 22))
        self.add_line('sym-e25', (24, 22), (21, 22))
        self.add_arc('sym-e26', (21, 22), (17, 25), radius_x=4, sweep=False)
        self.add_line('sym-e27', (31, 25), (31, 38))
        self.add_arc('sym-e28', (31, 38), (44, 30), radius_x=12, sweep=False)
        self.add_line('sym-e30', (44, 30), (44, 19))
        self.add_arc('sym-e31', (17, 38), (4, 30), radius_x=12)
        self.add_line('sym-e33', (4, 30), (4, 19))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14-1', 'sym-e14-2', 'sym-e15', 'sym-e16', 'sym-e17-1', 'sym-e17-2', 'sym-e18', 'sym-e19-1', 'sym-e19-2', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c1', 'sym-e27', 'sym-e28', 'sym-e30')
        self.add_contour('sym-c2', 'sym-e31', 'sym-e33')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
