"""Dating lips (romance), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8077f630-37ed-409c-b63e-a8b7f1a3579d'
SOURCE_PATH = 'icons-json/romance/dating lips_8077f630-37ed-409c-b63e-a8b7f1a3579d.json'
AUTHOR = 'json_to_solo'

class DatingLipsRomance(Solo48):
    icon_id = 'dating-lips-romance'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'romance'
    aliases = ()
    keywords = ('dating', 'lips', 'romance')

    def build(self):
        self.add_line('sym-e0', (4, 23), (19, 23))
        self.add_line('sym-e2', (19, 23), (23, 24))
        self.add_arc('sym-e3', (23, 24), (24, 24), radius_x=2, sweep=False)
        self.add_arc('sym-e5', (24, 24), (25, 24), radius_x=2, sweep=False)
        self.add_line('sym-e6', (25, 24), (29, 23))
        self.add_line('sym-e8', (29, 23), (44, 23))
        self.add_line('sym-e9', (44, 23), (40, 30))
        self.add_line('sym-e10', (40, 30), (38, 33))
        self.add_arc('sym-e11', (38, 33), (25, 40), radius_x=21)
        self.add_arc('sym-e12', (25, 40), (24, 40), radius_x=27, sweep=False)
        self.add_line('sym-e17', (24, 40), (23, 40))
        self.add_arc('sym-e18', (23, 40), (10, 33), radius_x=21)
        self.add_arc('sym-e19', (10, 33), (8, 30), radius_x=11)
        self.add_line('sym-e20', (8, 30), (4, 23))
        self.add_line('sym-e21', (4, 23), (9, 15))
        self.add_arc('sym-e22', (9, 15), (18, 8), radius_x=17)
        self.add_line('sym-e24', (18, 8), (22, 10))
        self.add_arc('sym-e25', (22, 10), (24, 12), radius_x=6, sweep=False)
        self.add_arc('sym-e26', (24, 12), (26, 10), radius_x=5, sweep=False)
        self.add_line('sym-e27', (26, 10), (30, 8))
        self.add_arc('sym-e29', (30, 8), (39, 15), radius_x=16)
        self.add_line('sym-e30', (39, 15), (44, 23))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e2', 'sym-e3', 'sym-e5', 'sym-e6', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e29', 'sym-e30')
