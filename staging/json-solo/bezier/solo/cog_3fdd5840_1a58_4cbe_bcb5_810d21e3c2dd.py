"""Cog (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3fdd5840-1a58-4cbe-bcb5-810d21e3c2dd'
SOURCE_PATH = 'icons-json/interface-essential/cog_3fdd5840-1a58-4cbe-bcb5-810d21e3c2dd.json'
AUTHOR = 'json_to_solo'

class Cog3fdd5840(Solo48):
    icon_id = 'cog-3fdd5840'
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
        self.add_arc('e22-top', (18, 24), (30, 24), radius_x=6)
        self.add_arc('e22-bottom', (30, 24), (18, 24), radius_x=6)
        self.add_bezier('e23', (10, 22), ((9.943, 22.63), (9.927, 22.822), (9.911, 23.46)), ((9.895, 24.139), (10.205, 25.546), (10.042, 26.119)), ((9.903, 26.61), (6.769, 29.936), (6, 31)))
        self.add_bezier('e24', (6, 17), ((6, 17.27), (6, 16.73), (6, 17)))
        self.add_contour('c0', 'e23', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19', 'e20', 'e24', 'e21', closed=True)
        self.add_contour('e22', 'e22-top', 'e22-bottom', closed=True)
