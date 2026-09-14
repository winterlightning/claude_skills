"""Blind (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5dce7e9a-2184-434a-9e94-71138d2b612d'
SOURCE_PATH = 'icons-json/interface-essential/blind_5dce7e9a-2184-434a-9e94-71138d2b612d.json'
AUTHOR = 'json_to_solo'

class BlindInterfaceEssential(Solo48):
    icon_id = 'blind-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('blind', 'interface-essential')

    def build(self):
        self.add_line('e0', (16, 38), (34, 12))
        self.add_line('e1', (16, 38), (19, 39))
        self.add_line('e2', (36, 13), (31, 10))
        self.add_line('e3-1', (19, 39), (24, 40))
        self.add_arc('e3-2', (24, 40), (44, 24), radius_x=25, sweep=False)
        self.add_arc('e3-3', (44, 24), (36, 13), radius_x=37, sweep=False)
        self.add_line('e4-1', (31, 10), (23, 8))
        self.add_arc('e4-2', (23, 8), (4, 24), radius_x=26, sweep=False)
        self.add_arc('e4-3', (4, 24), (16, 38), radius_x=33, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e3-1', 'e3-2', 'e3-3', 'e2', 'e4-1', 'e4-2', 'e4-3', closed=True)
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c1')
