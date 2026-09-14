"""Cog 1 (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3c5d9e7b-b736-46fd-9cd0-c46678889d84'
SOURCE_PATH = 'icons-json/interface-essential/cog 1_3c5d9e7b-b736-46fd-9cd0-c46678889d84.json'
AUTHOR = 'json_to_solo'

class Cog1InterfaceEssential(Solo48):
    icon_id = 'cog-1-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'interface-essential')

    def build(self):
        self.add_line('sym-e0', (6, 24), (6, 25))
        self.add_arc('sym-e1', (6, 25), (8, 27), radius_x=2, sweep=False)
        self.add_line('sym-e2', (8, 27), (11, 29))
        self.add_line('sym-e3', (11, 29), (10, 35))
        self.add_line('sym-e4', (10, 35), (13, 38))
        self.add_arc('sym-e5', (13, 38), (15, 37), radius_x=3, sweep=False)
        self.add_line('sym-e6', (15, 37), (19, 37))
        self.add_line('sym-e7-1', (19, 37), (21, 41))
        self.add_arc('sym-e7-2', (21, 41), (23, 42), radius_x=3)
        self.add_line('sym-e8', (23, 42), (24, 42))
        self.add_arc('sym-e9', (24, 42), (25, 42), radius_x=33)
        self.add_arc('sym-e10-1', (25, 42), (27, 41), radius_x=3)
        self.add_line('sym-e10-2', (27, 41), (29, 37))
        self.add_line('sym-e11', (29, 37), (33, 37))
        self.add_arc('sym-e12', (33, 37), (35, 38), radius_x=3, sweep=False)
        self.add_line('sym-e13', (35, 38), (38, 35))
        self.add_line('sym-e14', (38, 35), (37, 29))
        self.add_line('sym-e15', (37, 29), (40, 27))
        self.add_arc('sym-e16', (40, 27), (42, 25), radius_x=2, sweep=False)
        self.add_line('sym-e17', (42, 25), (42, 24))
        self.add_line('sym-e18', (42, 24), (42, 23))
        self.add_arc('sym-e19', (42, 23), (40, 21), radius_x=2, sweep=False)
        self.add_line('sym-e20', (40, 21), (37, 19))
        self.add_line('sym-e21', (37, 19), (38, 13))
        self.add_line('sym-e22', (38, 13), (35, 10))
        self.add_arc('sym-e23', (35, 10), (33, 11), radius_x=3, sweep=False)
        self.add_line('sym-e24', (33, 11), (29, 11))
        self.add_line('sym-e25-1', (29, 11), (27, 7))
        self.add_line('sym-e25-2', (27, 7), (25, 6))
        self.add_arc('sym-e26', (25, 6), (24, 6), radius_x=33)
        self.add_line('sym-e27', (24, 6), (23, 6))
        self.add_line('sym-e28-1', (23, 6), (21, 7))
        self.add_line('sym-e28-2', (21, 7), (19, 11))
        self.add_line('sym-e29', (19, 11), (15, 11))
        self.add_arc('sym-e30', (15, 11), (13, 10), radius_x=3, sweep=False)
        self.add_line('sym-e31', (13, 10), (10, 13))
        self.add_line('sym-e32', (10, 13), (11, 19))
        self.add_line('sym-e33', (11, 19), (8, 21))
        self.add_arc('sym-e34', (8, 21), (6, 23), radius_x=2, sweep=False)
        self.add_line('sym-e35', (6, 23), (6, 24))
        self.add_contour('sym-c0', 'sym-e0', 'sym-e1', 'sym-e2', 'sym-e3', 'sym-e4', 'sym-e5', 'sym-e6', 'sym-e7-1', 'sym-e7-2', 'sym-e8', 'sym-e9', 'sym-e10-1', 'sym-e10-2', 'sym-e11', 'sym-e12', 'sym-e13', 'sym-e14', 'sym-e15', 'sym-e16', 'sym-e17', 'sym-e18', 'sym-e19', 'sym-e20', 'sym-e21', 'sym-e22', 'sym-e23', 'sym-e24', 'sym-e25-1', 'sym-e25-2', 'sym-e26', 'sym-e27', 'sym-e28-1', 'sym-e28-2', 'sym-e29', 'sym-e30', 'sym-e31', 'sym-e32', 'sym-e33', 'sym-e34', 'sym-e35', closed=True)
