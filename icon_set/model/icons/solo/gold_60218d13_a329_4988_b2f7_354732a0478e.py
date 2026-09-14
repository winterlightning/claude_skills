"""Gold (science), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '60218d13-a329-4988-b2f7-354732a0478e'
SOURCE_PATH = 'icons-json/science/gold_60218d13-a329-4988-b2f7-354732a0478e.json'
AUTHOR = 'json_to_solo'

class Gold(Solo48):
    icon_id = 'gold'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'science'
    aliases = ()
    keywords = ('gold', 'science')

    def build(self):
        self.add_line('sym-e0', (24, 38), (24, 39))
        self.add_line('sym-e1', (24, 39), (24, 40))
        self.add_line('sym-e2', (20, 24), (28, 24))
        self.add_line('sym-e3', (28, 24), (24, 39))
        self.add_line('sym-e4', (24, 39), (20, 24))
        self.add_line('sym-e5', (20, 24), (15, 24))
        self.add_line('sym-e6', (15, 24), (14, 22))
        self.add_line('sym-e7', (14, 22), (14, 20))
        self.add_line('sym-e8', (14, 20), (18, 9))
        self.add_line('sym-e9', (18, 9), (19, 8))
        self.add_line('sym-e10', (19, 8), (24, 8))
        self.add_line('sym-e11', (24, 8), (29, 8))
        self.add_line('sym-e12', (29, 8), (30, 9))
        self.add_line('sym-e13', (30, 9), (34, 20))
        self.add_arc('sym-e14', (34, 20), (34, 22), radius_x=23, sweep=False)
        self.add_line('sym-e15', (34, 22), (33, 24))
        self.add_line('sym-e16', (33, 24), (28, 24))
        self.add_line('sym-e17', (24, 39), (22, 40))
        self.add_arc('sym-e18', (22, 40), (21, 40), radius_x=26, sweep=False)
        self.add_line('sym-e19', (21, 40), (6, 40))
        self.add_arc('sym-e20', (6, 40), (4, 38), radius_x=2)
        self.add_line('sym-e22', (4, 38), (7, 25))
        self.add_line('sym-e23', (7, 25), (9, 24))
        self.add_line('sym-e24', (9, 24), (15, 24))
        self.add_line('sym-e25', (24, 39), (26, 40))
        self.add_arc('sym-e26', (26, 40), (27, 40), radius_x=29)
        self.add_line('sym-e27', (27, 40), (42, 40))
        self.add_arc('sym-e28', (42, 40), (44, 38), radius_x=2, sweep=False)
        self.add_line('sym-e30', (44, 38), (41, 25))
        self.add_line('sym-e31', (41, 25), (39, 24))
        self.add_line('sym-e32', (39, 24), (33, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1')
        self.add_contour('sym-c1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16')
        self.add_contour('sym-c2', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22', 'sym-e23', 'sym-e24')
        self.add_contour('sym-c3', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e30', 'sym-e31', 'sym-e32')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2', 'sym-c3')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c3')
        self.relate('connect', 'sym-c0', 'sym-c2')
