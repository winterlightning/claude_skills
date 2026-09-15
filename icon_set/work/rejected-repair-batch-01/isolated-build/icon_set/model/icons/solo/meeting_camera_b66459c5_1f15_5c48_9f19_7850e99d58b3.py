"""Meeting camera (office), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b66459c5-1f15-5c48-9f19-7850e99d58b3'
SOURCE_PATH = 'pictographic-primitives/office/meeting camera_b66459c5-1f15-5c48-9f19-7850e99d58b3.svg'
AUTHOR = 'gpt-6'

class MeetingCamera(Solo48):
    icon_id = 'meeting-camera'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('meeting', 'camera', 'office')

    def build(self):
        self.add_line('e0', (32, 30), (42, 38))
        self.add_line('e1', (44, 35), (44, 13))
        self.add_line('e2', (42, 12), (32, 19))
        self.add_line('e3', (32, 19), (32, 13))
        self.add_line('e6', (10, 40), (28, 40))
        self.add_line('e7', (32, 31), (32, 19))
        self.add_line('e8-1', (42, 38), (44, 36))
        self.add_arc('e8-2', (44, 36), (44, 35), radius_x=13, radius_y=13, large_arc=False, sweep=True)
        self.add_arc('e9', (44, 13), (42, 12), radius_x=2, radius_y=2, large_arc=False, sweep=False)
        self.add_arc('e10-1', (32, 13), (28, 8), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('e10-2', (28, 8), (7, 8))
        self.add_arc('e11-2', (7, 8), (4, 12), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_line('e11-3', (4, 12), (4, 34))
        self.add_arc('e12', (4, 34), (10, 40), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_arc('e13', (28, 40), (32, 31), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e8-1', 'e8-2', 'e1', 'e9', 'e2', 'e3', 'e10-1', 'e10-2', 'e11-2', 'e11-3', 'e12', 'e6', 'e13', 'e7', closed=False)
