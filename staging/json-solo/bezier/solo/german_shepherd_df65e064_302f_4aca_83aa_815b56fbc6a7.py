"""German shepherd (pets), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'df65e064-302f-4aca-83aa-815b56fbc6a7'
SOURCE_PATH = 'icons-json/pets/german shepherd_df65e064-302f-4aca-83aa-815b56fbc6a7.json'
AUTHOR = 'json_to_solo'

class GermanShepherdPets(Solo48):
    icon_id = 'german-shepherd-pets'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'pets'
    aliases = ()
    keywords = ('german', 'shepherd', 'pets')

    def build(self):
        self.add_line('sym-e0', (12, 44), (9, 39))
        self.add_bezier('sym-e1', (9, 39), ((8.613, 38.364), (8, 36.791), (8, 36)))
        self.add_bezier('sym-e2', (8, 36), ((8, 35.9), (8, 36.1), (8, 36)))
        self.add_bezier('sym-e3', (8, 36), ((8, 35.936), (8, 36.064), (8, 36)))
        self.add_line('sym-e4', (8, 36), (12, 23))
        self.add_bezier('sym-e5', (12, 23), ((11.941, 22.845), (12.067, 23.173), (12, 23)))
        self.add_bezier('sym-e6', (12, 23), ((11.688, 22.255), (11.438, 20.673), (11, 20)))
        self.add_bezier('sym-e7', (11, 20), ((9.4, 17.545), (9.141, 15.791), (10, 13)))
        self.add_line('sym-e8', (10, 13), (12, 5))
        self.add_bezier('sym-e9', (12, 5), ((12.396, 4.655), (13.419, 4), (14, 4)))
        self.add_bezier('sym-e10', (14, 4), ((14.051, 4), (13.941, 4), (14, 4)))
        self.add_bezier('sym-e11', (14, 4), ((14.312, 4), (14.688, 4), (15, 4)))
        self.add_line('sym-e12', (15, 4), (17, 9))
        self.add_bezier('sym-e13', (17, 9), ((17.985, 11.127), (19.512, 13.655), (20, 16)))
        self.add_line('sym-e14', (20, 16), (24, 16))
        self.add_line('sym-e15', (24, 16), (28, 16))
        self.add_bezier('sym-e16', (28, 16), ((28.488, 13.655), (30.015, 11.127), (31, 9)))
        self.add_line('sym-e17', (31, 9), (33, 4))
        self.add_bezier('sym-e18', (33, 4), ((33.312, 4), (33.688, 4), (34, 4)))
        self.add_bezier('sym-e19', (34, 4), ((34.059, 4), (33.949, 4), (34, 4)))
        self.add_bezier('sym-e20', (34, 4), ((34.581, 4), (35.604, 4.655), (36, 5)))
        self.add_line('sym-e21', (36, 5), (38, 13))
        self.add_bezier('sym-e22', (38, 13), ((38.859, 15.791), (38.6, 17.545), (37, 20)))
        self.add_bezier('sym-e23', (37, 20), ((36.562, 20.673), (36.312, 22.255), (36, 23)))
        self.add_bezier('sym-e24', (36, 23), ((35.933, 23.173), (36.059, 22.845), (36, 23)))
        self.add_line('sym-e25', (36, 23), (40, 36))
        self.add_bezier('sym-e26', (40, 36), ((40, 36.064), (40, 35.936), (40, 36)))
        self.add_bezier('sym-e27', (40, 36), ((40, 36.1), (40, 35.9), (40, 36)))
        self.add_bezier('sym-e28', (40, 36), ((40, 36.791), (39.387, 38.364), (39, 39)))
        self.add_line('sym-e29', (39, 39), (36, 44))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29')
