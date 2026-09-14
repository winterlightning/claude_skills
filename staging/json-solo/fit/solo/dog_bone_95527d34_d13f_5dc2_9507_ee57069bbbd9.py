"""Dog bone (pets), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95527d34-d13f-5dc2-9507-ee57069bbbd9'
SOURCE_PATH = 'icons-json/pets/dog bone_95527d34-d13f-5dc2-9507-ee57069bbbd9.json'
AUTHOR = 'json_to_solo'

class DogBonePets(Solo48):
    icon_id = 'dog-bone-pets'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('dog', 'bone', 'pets')

    def build(self):
        self.add_line('sym-e0', (41, 24), (42, 24))
        self.add_arc('sym-e1', (16, 17), (12, 9), radius_x=11, sweep=False)
        self.add_line('sym-e2', (12, 9), (10, 8))
        self.add_line('sym-e4', (10, 8), (9, 8))
        self.add_arc('sym-e5-1', (9, 8), (6, 10), radius_x=5, sweep=False)
        self.add_line('sym-e5-2', (6, 10), (4, 17))
        self.add_line('sym-e6', (4, 17), (4, 20))
        self.add_arc('sym-e7', (4, 20), (6, 23), radius_x=11)
        self.add_arc('sym-e8', (6, 23), (7, 24), radius_x=6)
        self.add_arc('sym-e9', (7, 24), (6, 25), radius_x=6)
        self.add_arc('sym-e10', (6, 25), (4, 28), radius_x=11)
        self.add_line('sym-e11', (4, 28), (4, 31))
        self.add_line('sym-e12-1', (4, 31), (6, 38))
        self.add_arc('sym-e12-2', (6, 38), (9, 40), radius_x=5, sweep=False)
        self.add_arc('sym-e13', (9, 40), (10, 40), radius_x=1)
        self.add_line('sym-e15', (10, 40), (12, 39))
        self.add_arc('sym-e16', (12, 39), (16, 31), radius_x=10, sweep=False)
        self.add_line('sym-e17', (16, 31), (32, 31))
        self.add_line('sym-e18', (32, 31), (33, 36))
        self.add_arc('sym-e19', (33, 36), (38, 40), radius_x=6, sweep=False)
        self.add_line('sym-e20', (38, 40), (39, 40))
        self.add_arc('sym-e22-1', (39, 40), (42, 38), radius_x=4, sweep=False)
        self.add_line('sym-e22-2', (42, 38), (44, 31))
        self.add_line('sym-e25', (44, 31), (43, 26))
        self.add_arc('sym-e26', (43, 26), (42, 24), radius_x=28)
        self.add_arc('sym-e27', (42, 24), (43, 22), radius_x=28)
        self.add_line('sym-e28', (43, 22), (44, 17))
        self.add_line('sym-e31-1', (44, 17), (42, 10))
        self.add_arc('sym-e31-2', (42, 10), (39, 8), radius_x=4, sweep=False)
        self.add_line('sym-e33', (39, 8), (38, 8))
        self.add_arc('sym-e34', (38, 8), (33, 12), radius_x=6, sweep=False)
        self.add_arc('sym-e35', (33, 12), (32, 17), radius_x=23, sweep=False)
        self.add_line('sym-e36', (32, 17), (16, 17))
        self.add_contour('sym-c0', 'sym-e0')
        self.add_contour('sym-c1', 'sym-e1', 'sym-e2', 'sym-e4', 'sym-e5-1', 'sym-e5-2', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12-1', 'sym-e12-2', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e22-1', 'sym-e22-2', 'sym-e25', 'sym-e26')
        self.add_contour('sym-c2', 'sym-e27', 'sym-e28', 'sym-e31-1', 'sym-e31-2', 'sym-e33', 'sym-e34', 'sym-e35', 'sym-e36')
        self.relate('connect', 'sym-c1', 'sym-c2')
