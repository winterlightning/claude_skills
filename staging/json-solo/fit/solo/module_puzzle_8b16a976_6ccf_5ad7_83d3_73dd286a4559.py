"""Module puzzle (programing), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b16a976-6ccf-5ad7-83d3-73dd286a4559'
SOURCE_PATH = 'icons-json/programing/module puzzle_8b16a976-6ccf-5ad7-83d3-73dd286a4559.json'
AUTHOR = 'json_to_solo'

class ModulePuzzlePrograming(Solo48):
    icon_id = 'module-puzzle-programing'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('module', 'puzzle', 'programing')

    def build(self):
        self.add_line('e0', (21, 13), (11, 13))
        self.add_line('e1', (8, 17), (8, 25))
        self.add_line('e2', (8, 31), (8, 42))
        self.add_line('e3', (11, 44), (21, 44))
        self.add_line('e4', (27, 44), (38, 44))
        self.add_line('e5', (40, 42), (40, 16))
        self.add_line('e6', (37, 13), (27, 13))
        self.add_arc('e7-1', (27, 13), (24, 4), radius_x=5, sweep=False)
        self.add_arc('e7-2', (24, 4), (21, 13), radius_x=5, sweep=False)
        self.add_arc('e8-1', (11, 13), (8, 16), radius_x=3, sweep=False)
        self.add_line('e8-2', (8, 16), (8, 17))
        self.add_arc('e9', (8, 25), (8, 31), radius_x=5, large_arc=True)
        self.add_arc('e10', (8, 42), (11, 44), radius_x=4, sweep=False)
        self.add_arc('e11-1', (21, 44), (20, 38), radius_x=7)
        self.add_arc('e11-2', (20, 38), (25, 35), radius_x=4)
        self.add_arc('e11-3', (25, 35), (27, 44), radius_x=5)
        self.add_arc('e12', (38, 44), (40, 42), radius_x=2, sweep=False)
        self.add_arc('e13', (40, 16), (37, 13), radius_x=3, sweep=False)
        self.add_contour('c0', 'e7-1', 'e7-2', 'e0', 'e8-1', 'e8-2', 'e1', 'e9', 'e2', 'e10', 'e3', 'e11-1', 'e11-2', 'e11-3', 'e4', 'e12', 'e5', 'e13', 'e6', closed=True)
