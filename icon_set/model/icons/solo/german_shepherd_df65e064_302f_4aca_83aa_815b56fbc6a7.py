"""German shepherd (pets), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df65e064-302f-4aca-83aa-815b56fbc6a7'
SOURCE_PATH = 'icons-json/pets/german shepherd_df65e064-302f-4aca-83aa-815b56fbc6a7.json'
AUTHOR = 'json_to_solo'

class GermanShepherd(Solo48):
    icon_id = 'german-shepherd'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('german', 'shepherd', 'pets')

    def build(self):
        self.add_line('sym-e0', (12, 44), (9, 39))
        self.add_line('sym-e1', (9, 39), (8, 36))
        self.add_line('sym-e4', (8, 36), (12, 23))
        self.add_arc('sym-e6', (12, 23), (11, 20), radius_x=9)
        self.add_arc('sym-e7', (11, 20), (10, 13), radius_x=7)
        self.add_line('sym-e8', (10, 13), (12, 5))
        self.add_line('sym-e9', (12, 5), (14, 4))
        self.add_line('sym-e11', (14, 4), (15, 4))
        self.add_line('sym-e12', (15, 4), (17, 9))
        self.add_arc('sym-e13', (17, 9), (20, 16), radius_x=26, sweep=False)
        self.add_line('sym-e14', (20, 16), (24, 16))
        self.add_line('sym-e15', (24, 16), (28, 16))
        self.add_arc('sym-e16', (28, 16), (31, 9), radius_x=26)
        self.add_line('sym-e17', (31, 9), (33, 4))
        self.add_line('sym-e18', (33, 4), (34, 4))
        self.add_line('sym-e20', (34, 4), (36, 5))
        self.add_line('sym-e21', (36, 5), (38, 13))
        self.add_arc('sym-e22', (38, 13), (37, 20), radius_x=7)
        self.add_line('sym-e23', (37, 20), (36, 23))
        self.add_line('sym-e25', (36, 23), (40, 36))
        self.add_line('sym-e28', (40, 36), (39, 39))
        self.add_line('sym-e29', (39, 39), (36, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e4', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e25', 'sym-e28', 'sym-e29')
