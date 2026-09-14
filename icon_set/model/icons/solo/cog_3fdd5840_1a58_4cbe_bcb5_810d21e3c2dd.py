"""Cog (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fdd5840-1a58-4cbe-bcb5-810d21e3c2dd'
SOURCE_PATH = 'icons-json/interface-essential/cog_3fdd5840-1a58-4cbe-bcb5-810d21e3c2dd.json'
AUTHOR = 'gpt-6'

class CogInterfaceEssential(Solo48):
    icon_id = 'cog-interface-essential'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'interface-essential')

    def build(self):
        self.add_line('e0', (6, 31), (10, 36))
        self.add_line('e1', (10, 36), (15, 35))
        self.add_line('e2', (15, 35), (19, 36))
        self.add_line('e3', (19, 36), (21, 42))
        self.add_line('e4', (21, 42), (27, 42))
        self.add_line('e5', (27, 42), (29, 36))
        self.add_line('e6', (29, 36), (33, 35))
        self.add_line('e7', (33, 35), (38, 36))
        self.add_line('e8', (38, 36), (42, 31))
        self.add_line('e9', (42, 31), (38, 26))
        self.add_line('e10', (38, 26), (38, 22))
        self.add_line('e11', (38, 22), (42, 17))
        self.add_line('e12', (42, 17), (38, 12))
        self.add_line('e13', (38, 12), (32, 13))
        self.add_line('e14', (32, 13), (29, 12))
        self.add_line('e15', (29, 12), (27, 6))
        self.add_line('e16', (27, 6), (21, 6))
        self.add_line('e17', (21, 6), (19, 12))
        self.add_line('e18', (19, 12), (15, 13))
        self.add_line('e19', (15, 13), (10, 12))
        self.add_line('e20', (10, 12), (6, 17))
        self.add_line('e21', (6, 17), (10, 22))
        self.add_arc('e22-top', (20, 24), (28, 24), radius_x=4)
        self.add_arc('e22-bottom', (28, 24), (20, 24), radius_x=4)
        self.add_line('e23-1', (10, 22), (10, 26))
        self.add_line('e23-2', (10, 26), (6, 31))
        self.add_contour('c0', 'e23-1', 'e23-2', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19', 'e20', 'e21', closed=True)
        self.add_contour('e22', 'e22-top', 'e22-bottom', closed=True)
