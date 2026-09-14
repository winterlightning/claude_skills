"""Cog (interface-essential), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1e82d117-570c-41ee-9217-7031427f5fea'
SOURCE_PATH = 'icons-json/interface-essential/cog_1e82d117-570c-41ee-9217-7031427f5fea.json'
AUTHOR = 'json_to_solo'

class Cog1e82d117(Solo48):
    icon_id = 'cog-1e82d117'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('cog', 'interface-essential')

    def build(self):
        self.add_line('e0', (14, 40), (20, 42))
        self.add_line('e1', (20, 42), (22, 37))
        self.add_line('e2', (22, 37), (26, 37))
        self.add_line('e3', (26, 37), (28, 42))
        self.add_line('e4', (28, 42), (33, 40))
        self.add_line('e5', (33, 40), (33, 35))
        self.add_line('e6', (33, 35), (35, 32))
        self.add_line('e7', (35, 32), (40, 32))
        self.add_line('e8', (40, 32), (42, 26))
        self.add_line('e9', (42, 26), (38, 24))
        self.add_line('e10', (37, 20), (40, 15))
        self.add_line('e11', (40, 15), (37, 11))
        self.add_line('e12', (37, 11), (31, 13))
        self.add_line('e13', (31, 13), (28, 12))
        self.add_line('e14', (28, 12), (26, 6))
        self.add_line('e15', (26, 6), (22, 6))
        self.add_line('e16', (22, 6), (20, 10))
        self.add_line('e17', (19, 12), (17, 13))
        self.add_line('e18', (17, 13), (11, 11))
        self.add_line('e19', (11, 11), (8, 15))
        self.add_line('e20', (8, 15), (11, 20))
        self.add_line('e21', (8, 26), (6, 27))
        self.add_line('e22', (6, 27), (8, 32))
        self.add_line('e23', (8, 32), (13, 32))
        self.add_line('e24', (13, 32), (16, 35))
        self.add_line('e25', (16, 35), (14, 40))
        self.add_bezier('e26', (38, 24), ((37.149, 23.493), (37.065, 20.974), (37, 20)))
        self.add_bezier('e27', (20, 10), ((20, 10.049), (19.909, 10.189), (19.909, 10.238)), ((19.639, 10.737), (19.27, 11.501), (19, 12)))
        self.add_bezier('e28', (11, 20), ((10.853, 21.015), (10.705, 22.928), (10.222, 23.697)), ((9.87, 24.254), (8.532, 25.624), (8, 26)))
        self.add_bezier('e29', (13, 32), ((13.27, 32), (12.73, 32), (13, 32)))
        self.add_dot('e30', (24, 24))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e26', 'e10', 'e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e27', 'e17', 'e18', 'e19', 'e20', 'e28', 'e21', 'e22', 'e23', 'e29', 'e24', 'e25')
