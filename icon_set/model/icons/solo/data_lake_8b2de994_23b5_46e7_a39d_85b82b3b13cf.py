"""Data lake (programing), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b2de994-23b5-46e7-a39d-85b82b3b13cf'
SOURCE_PATH = 'icons-json/programing/data lake_8b2de994-23b5-46e7-a39d-85b82b3b13cf.json'
AUTHOR = 'json_to_solo'

class DataLake(Solo48):
    icon_id = 'data-lake'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('data', 'lake', 'programing')

    def build(self):
        self.add_arc('sym-e0', (40, 32), (32, 34), radius_x=8)
        self.add_line('sym-e1', (32, 34), (30, 32))
        self.add_arc('sym-e2', (30, 32), (29, 32), radius_x=6, sweep=False)
        self.add_line('sym-e4', (29, 32), (26, 34))
        self.add_line('sym-e5', (26, 34), (24, 34))
        self.add_line('sym-e6', (24, 34), (22, 34))
        self.add_arc('sym-e7', (22, 34), (19, 32), radius_x=7)
        self.add_arc('sym-e9', (19, 32), (18, 32), radius_x=6, sweep=False)
        self.add_line('sym-e10', (18, 32), (16, 34))
        self.add_arc('sym-e11', (16, 34), (8, 32), radius_x=8)
        self.add_line('sym-e12', (8, 32), (8, 39))
        self.add_line('sym-e14', (8, 39), (11, 42))
        self.add_line('sym-e15', (11, 42), (23, 44))
        self.add_line('sym-e17', (23, 44), (24, 44))
        self.add_arc('sym-e18', (24, 44), (25, 44), radius_x=29)
        self.add_line('sym-e20', (25, 44), (37, 42))
        self.add_line('sym-e21', (37, 42), (40, 39))
        self.add_line('sym-e23', (40, 39), (40, 32))
        self.add_line('sym-e24', (40, 32), (40, 22))
        self.add_arc('sym-e25', (40, 22), (32, 24), radius_x=8)
        self.add_arc('sym-e26', (32, 24), (30, 23), radius_x=8)
        self.add_line('sym-e27', (30, 23), (29, 22))
        self.add_arc('sym-e28', (29, 22), (28, 23), radius_x=8)
        self.add_arc('sym-e29', (28, 23), (24, 24), radius_x=7)
        self.add_arc('sym-e30', (24, 24), (20, 23), radius_x=7)
        self.add_arc('sym-e31', (20, 23), (19, 22), radius_x=8)
        self.add_line('sym-e32', (19, 22), (18, 23))
        self.add_arc('sym-e33', (18, 23), (16, 24), radius_x=8)
        self.add_arc('sym-e34', (16, 24), (8, 22), radius_x=8)
        self.add_line('sym-e35', (8, 22), (8, 32))
        self.add_line('sym-e36', (40, 22), (40, 11))
        self.add_arc('sym-e37', (40, 11), (37, 13), radius_x=17, sweep=False)
        self.add_arc('sym-e38', (37, 13), (24, 16), radius_x=31)
        self.add_arc('sym-e39', (24, 16), (11, 13), radius_x=31)
        self.add_arc('sym-e40', (11, 13), (8, 11), radius_x=17, sweep=False)
        self.add_line('sym-e41', (8, 11), (8, 22))
        self.add_line('sym-e42', (40, 11), (40, 9))
        self.add_line('sym-e43', (40, 9), (39, 8))
        self.add_arc('sym-e44-1', (39, 8), (33, 5), radius_x=14, sweep=False)
        self.add_arc('sym-e44-2', (33, 5), (25, 4), radius_x=36, sweep=False)
        self.add_arc('sym-e45', (25, 4), (24, 4), radius_x=76)
        self.add_arc('sym-e48', (24, 4), (23, 4), radius_x=69)
        self.add_arc('sym-e49-1', (23, 4), (15, 5), radius_x=36, sweep=False)
        self.add_arc('sym-e49-2', (15, 5), (9, 8), radius_x=14, sweep=False)
        self.add_line('sym-e50', (9, 8), (8, 9))
        self.add_line('sym-e51', (8, 9), (8, 11))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e14', 'sym-e15', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35')
        self.add_contour('sym-c1', 'sym-e36', 'sym-e37', 'sym-e38', 'sym-e39', 'sym-e40', 'sym-e41')
        self.add_contour('sym-c2', 'sym-e42', 'sym-e43', 'sym-e44-1', 'sym-e44-2', 'sym-e45', 'sym-e48', 'sym-e49-1', 'sym-e49-2', 'sym-e50', 'sym-e51')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
