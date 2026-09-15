"""Robot (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e46fb630-ba38-428c-8b2e-adf342a25e31'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot_e46fb630-ba38-428c-8b2e-adf342a25e31.svg'
AUTHOR = 'gpt-6'

class RobotE46fb630(Solo48):
    icon_id = 'robot-e46fb630'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('robot', 'artificial-intelligence')

    def build(self):
        self.add_line('sym-e0', (24, 6), (24, 17))
        self.add_line('sym-e1', (24, 17), (13, 17))
        self.add_arc('sym-e2', (13, 17), (6, 22), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('sym-e3', (6, 22), (6, 24))
        self.add_arc('sym-e4', (6, 24), (6, 25), radius_x=52, radius_y=52, large_arc=False, sweep=True)
        self.add_line('sym-e5', (6, 25), (6, 36))
        self.add_arc('sym-e8', (6, 36), (11, 42), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_line('sym-e9-1', (11, 42), (12, 42))
        self.add_arc('sym-e9-2', (12, 42), (13, 42), radius_x=10, radius_y=10, large_arc=False, sweep=True)
        self.add_line('sym-e10', (13, 42), (37, 42))
        self.add_arc('sym-e15', (37, 42), (42, 36), radius_x=7, radius_y=7, large_arc=False, sweep=False)
        self.add_arc('sym-e16', (42, 36), (42, 35), radius_x=37, radius_y=37, large_arc=False, sweep=True)
        self.add_line('sym-e17', (42, 35), (42, 25))
        self.add_arc('sym-e19', (42, 25), (42, 24), radius_x=28, radius_y=28, large_arc=False, sweep=True)
        self.add_line('sym-e20', (42, 24), (42, 22))
        self.add_arc('sym-e21', (42, 22), (35, 17), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_line('sym-e22', (35, 17), (24, 17))
        self.add_line('sym-e23', (17, 27), (17, 32))
        self.add_line('sym-e24', (31, 27), (31, 32))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e8', 'sym-e9-1', 'sym-e9-2', 'sym-e10', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', closed=False)
        self.add_contour('sym-c1', 'sym-e23', closed=False)
        self.add_contour('sym-c2', 'sym-e24', closed=False)
