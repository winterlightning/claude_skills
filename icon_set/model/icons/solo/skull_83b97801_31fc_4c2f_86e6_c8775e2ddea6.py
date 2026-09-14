"""Skull (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83b97801-31fc-4c2f-86e6-c8775e2ddea6'
SOURCE_PATH = 'icons-json/interface-essential/skull_83b97801-31fc-4c2f-86e6-c8775e2ddea6.json'
AUTHOR = 'json_to_solo'

class SkullInterfaceEssential(Solo48):
    icon_id = 'skull-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (24, 34), (24, 42))
        self.add_line('sym-e1', (24, 42), (19, 42))
        self.add_line('sym-e3', (19, 42), (18, 42))
        self.add_line('sym-e4', (18, 42), (17, 42))
        self.add_line('sym-e5', (17, 42), (16, 42))
        self.add_arc('sym-e6-1', (16, 42), (13, 39), radius_x=4)
        self.add_arc('sym-e6-2', (13, 39), (12, 33), radius_x=14, sweep=False)
        self.add_line('sym-e7', (12, 33), (8, 30))
        self.add_line('sym-e8', (8, 30), (6, 24))
        self.add_arc('sym-e9', (6, 24), (6, 23), radius_x=1, sweep=False)
        self.add_line('sym-e10', (6, 23), (6, 22))
        self.add_arc('sym-e11', (6, 22), (7, 19), radius_x=15)
        self.add_arc('sym-e12', (7, 19), (18, 7), radius_x=16)
        self.add_arc('sym-e13', (18, 7), (23, 6), radius_x=16)
        self.add_arc('sym-e15', (23, 6), (24, 6), radius_x=1, sweep=False)
        self.add_arc('sym-e16', (24, 6), (25, 6), radius_x=1, sweep=False)
        self.add_line('sym-e18', (25, 6), (30, 7))
        self.add_arc('sym-e19', (30, 7), (41, 19), radius_x=16)
        self.add_line('sym-e20', (41, 19), (42, 22))
        self.add_line('sym-e21', (42, 22), (42, 23))
        self.add_arc('sym-e22', (42, 23), (42, 24), radius_x=1, sweep=False)
        self.add_line('sym-e23', (42, 24), (40, 30))
        self.add_line('sym-e24', (40, 30), (36, 33))
        self.add_arc('sym-e25-1', (36, 33), (35, 39), radius_x=14, sweep=False)
        self.add_arc('sym-e25-2', (35, 39), (32, 42), radius_x=3)
        self.add_line('sym-e26', (32, 42), (31, 42))
        self.add_arc('sym-e27', (31, 42), (30, 42), radius_x=32, sweep=False)
        self.add_arc('sym-e28', (30, 42), (29, 42), radius_x=31, sweep=False)
        self.add_line('sym-e30', (29, 42), (24, 42))
        self.add_arc('sym-e31', (16, 24), (16, 23), radius_x=25)
        self.add_arc('sym-e32', (32, 24), (32, 23), radius_x=25)
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6-1', 'sym-e6-2', 'sym-e7', 'sym-e8', 'sym-e9', 'sym-e10', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e15', 'sym-e16', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25-1', 'sym-e25-2', 'sym-e26', 'sym-e27', 'sym-e28', 'sym-e30')
        self.add_contour('sym-c1', 'sym-e31')
        self.add_contour('sym-c2', 'sym-e32')
