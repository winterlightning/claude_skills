"""Robot (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '09313b1b-e57f-4498-907c-4a7b5fb8b7ae'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot_09313b1b-e57f-4498-907c-4a7b5fb8b7ae.svg'
AUTHOR = 'gpt-6'

class Robot(Solo48):
    icon_id = 'robot'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('robot', 'artificial-intelligence')

    def build(self):
        self.add_line('sym-e0', (32, 4), (32, 17))
        self.add_line('sym-e1', (32, 17), (37, 17))
        self.add_arc('sym-e3', (37, 17), (40, 19), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e5', (40, 19), (40, 35))
        self.add_arc('sym-e7', (40, 35), (32, 43), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_arc('sym-e8', (32, 43), (29, 44), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_line('sym-e10', (29, 44), (19, 44))
        self.add_arc('sym-e13', (19, 44), (16, 43), radius_x=8, radius_y=8, large_arc=False, sweep=True)
        self.add_arc('sym-e14', (16, 43), (8, 35), radius_x=11, radius_y=11, large_arc=False, sweep=True)
        self.add_line('sym-e15', (8, 35), (8, 19))
        self.add_arc('sym-e18', (8, 19), (11, 17), radius_x=3, radius_y=3, large_arc=False, sweep=True)
        self.add_line('sym-e20', (11, 17), (16, 17))
        self.add_line('sym-e21', (16, 17), (16, 4))
        self.add_line('sym-e22', (29, 28), (29, 31))
        self.add_line('sym-e23', (32, 17), (16, 17))
        self.add_line('sym-e25', (19, 28), (19, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e5', 'sym-e7', 'sym-e8', 'sym-e10', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e18', 'sym-e20', 'sym-e21', closed=False)
        self.add_contour('sym-c1', 'sym-e22', closed=False)
        self.add_contour('sym-c2', 'sym-e23', closed=False)
        self.add_contour('sym-c3', 'sym-e25', closed=False)
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
