"""Soap (symbol), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4'
SOURCE_PATH = 'icons-json/symbol/soap_4ee9ecc8-c1c5-4fbd-86bf-4c3aaf9a18f4.json'
AUTHOR = 'json_to_solo'

class Soap(Solo48):
    icon_id = 'soap'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('soap', 'symbol')

    def build(self):
        self.add_arc('sym-e0', (4, 22), (9, 25), radius_x=78)
        self.add_arc('sym-e1', (9, 25), (21, 28), radius_x=24, sweep=False)
        self.add_line('sym-e2', (21, 28), (24, 28))
        self.add_line('sym-e3', (24, 28), (27, 28))
        self.add_arc('sym-e4', (27, 28), (39, 25), radius_x=24, sweep=False)
        self.add_arc('sym-e5', (39, 25), (44, 22), radius_x=78)
        self.add_line('sym-e6', (44, 22), (44, 29))
        self.add_arc('sym-e7', (44, 29), (44, 30), radius_x=32, sweep=False)
        self.add_arc('sym-e8', (44, 30), (41, 36), radius_x=9)
        self.add_arc('sym-e9', (41, 36), (29, 40), radius_x=20)
        self.add_arc('sym-e10', (29, 40), (28, 40), radius_x=29, sweep=False)
        self.add_line('sym-e11', (28, 40), (27, 40))
        self.add_line('sym-e12', (27, 40), (24, 40))
        self.add_line('sym-e13', (24, 40), (21, 40))
        self.add_line('sym-e14', (21, 40), (20, 40))
        self.add_line('sym-e15', (20, 40), (19, 40))
        self.add_arc('sym-e16', (19, 40), (7, 36), radius_x=20)
        self.add_arc('sym-e17', (7, 36), (4, 30), radius_x=9)
        self.add_line('sym-e18', (4, 30), (4, 29))
        self.add_line('sym-e19', (4, 29), (4, 22))
        self.add_line('sym-e20', (4, 22), (4, 17))
        self.add_line('sym-e21', (4, 17), (4, 16))
        self.add_arc('sym-e22', (4, 16), (5, 13), radius_x=9, sweep=False)
        self.add_arc('sym-e23', (5, 13), (15, 8), radius_x=14)
        self.add_line('sym-e24', (15, 8), (17, 8))
        self.add_line('sym-e25', (17, 8), (24, 8))
        self.add_line('sym-e26', (24, 8), (31, 8))
        self.add_line('sym-e27', (31, 8), (33, 8))
        self.add_arc('sym-e28', (33, 8), (43, 13), radius_x=14)
        self.add_line('sym-e29', (43, 13), (44, 16))
        self.add_line('sym-e30', (44, 16), (44, 17))
        self.add_line('sym-e31', (44, 17), (44, 22))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e29', 'sym-e30', 'sym-e31')
