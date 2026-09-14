"""Robot (artificial-intelligence), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09313b1b-e57f-4498-907c-4a7b5fb8b7ae'
SOURCE_PATH = 'icons-json/artificial-intelligence/robot_09313b1b-e57f-4498-907c-4a7b5fb8b7ae.json'
AUTHOR = 'json_to_solo'

class Robot09313b1b(Solo48):
    icon_id = 'robot-09313b1b'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    aliases = ()
    keywords = ('robot', 'artificial-intelligence')

    def build(self):
        self.add_line('sym-e0', (32, 4), (32, 17))
        self.add_line('sym-e1', (32, 17), (37, 17))
        self.add_bezier('sym-e2', (37, 17), ((37.135, 16.973), (36.865, 17.036), (37, 17)))
        self.add_bezier('sym-e3', (37, 17), ((38.246, 17.109), (40, 17.418), (40, 19)))
        self.add_bezier('sym-e4', (40, 19), ((40, 19.064), (40, 18.936), (40, 19)))
        self.add_line('sym-e5', (40, 19), (40, 33))
        self.add_bezier('sym-e6', (40, 33), ((40, 33.582), (40, 34.436), (40, 35)))
        self.add_bezier('sym-e7', (40, 35), ((39.124, 39.018), (35.688, 41.836), (32, 43)))
        self.add_bezier('sym-e8', (32, 43), ((31.158, 43.273), (29.893, 44), (29, 44)))
        self.add_bezier('sym-e9', (29, 44), ((28.865, 44), (29.135, 43.991), (29, 44)))
        self.add_line('sym-e10', (29, 44), (24, 44))
        self.add_line('sym-e11', (24, 44), (19, 44))
        self.add_bezier('sym-e12', (19, 44), ((18.865, 43.991), (19.135, 44), (19, 44)))
        self.add_bezier('sym-e13', (19, 44), ((18.107, 44), (16.842, 43.273), (16, 43)))
        self.add_bezier('sym-e14', (16, 43), ((12.312, 41.836), (8.876, 39.018), (8, 35)))
        self.add_bezier('sym-e15', (8, 35), ((8, 34.436), (8, 33.582), (8, 33)))
        self.add_line('sym-e16', (8, 33), (8, 19))
        self.add_bezier('sym-e17', (8, 19), ((8, 18.936), (8, 19.064), (8, 19)))
        self.add_bezier('sym-e18', (8, 19), ((8, 17.418), (9.754, 17.109), (11, 17)))
        self.add_bezier('sym-e19', (11, 17), ((11.135, 17.036), (10.865, 16.973), (11, 17)))
        self.add_line('sym-e20', (11, 17), (16, 17))
        self.add_line('sym-e21', (16, 17), (16, 4))
        self.add_line('sym-e22', (29, 28), (29, 31))
        self.add_line('sym-e23', (32, 17), (24, 17))
        self.add_line('sym-e24', (24, 17), (16, 17))
        self.add_line('sym-e25', (19, 28), (19, 31))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21')
        self.add_contour('sym-c1', 'sym-e22')
        self.add_contour('sym-c2', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c3', 'sym-e25')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
