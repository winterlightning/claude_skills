"""Man construction (avatars), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e34e75b6-7322-4658-bc40-c90c4e98051e'
SOURCE_PATH = 'icons-json/avatars/man construction_e34e75b6-7322-4658-bc40-c90c4e98051e.json'
AUTHOR = 'json_to_solo'

class ManConstructionAvatars(Solo48):
    icon_id = 'man-construction-avatars'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('man', 'construction', 'avatars')

    def build(self):
        self.add_line('sym-e0', (26, 23), (22, 23))
        self.add_line('sym-e1', (22, 23), (17, 9))
        self.add_arc('sym-e2', (17, 9), (14, 12), radius_x=31)
        self.add_arc('sym-e3', (14, 12), (9, 23), radius_x=17, sweep=False)
        self.add_line('sym-e4', (9, 23), (6, 23))
        self.add_line('sym-e5', (42, 23), (39, 23))
        self.add_arc('sym-e6', (39, 23), (34, 12), radius_x=17, sweep=False)
        self.add_arc('sym-e7', (34, 12), (31, 9), radius_x=31)
        self.add_line('sym-e8', (31, 9), (26, 23))
        self.add_line('sym-e9', (26, 23), (39, 23))
        self.add_line('sym-e10', (39, 23), (39, 28))
        self.add_line('sym-e11', (39, 28), (38, 32))
        self.add_arc('sym-e12', (38, 32), (24, 42), radius_x=15)
        self.add_arc('sym-e17', (24, 42), (10, 32), radius_x=15)
        self.add_arc('sym-e18', (10, 32), (9, 28), radius_x=12)
        self.add_line('sym-e19', (9, 28), (9, 23))
        self.add_line('sym-e20', (9, 23), (22, 23))
        self.add_line('sym-e21', (31, 9), (31, 8))
        self.add_arc('sym-e22', (31, 8), (29, 7), radius_x=4, sweep=False)
        self.add_arc('sym-e23', (29, 7), (25, 6), radius_x=22)
        self.add_line('sym-e24', (25, 6), (24, 6))
        self.add_line('sym-e29', (24, 6), (23, 6))
        self.add_arc('sym-e30', (23, 6), (19, 7), radius_x=22)
        self.add_line('sym-e31', (19, 7), (17, 8))
        self.add_line('sym-e32', (17, 8), (17, 9))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4')
        self.add_contour('sym-c1', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20')
        self.add_contour('sym-c2', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c2')
        self.relate('connect', 'sym-c1', 'sym-c2')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
        self.relate('connect', 'sym-c0', 'sym-c1')
