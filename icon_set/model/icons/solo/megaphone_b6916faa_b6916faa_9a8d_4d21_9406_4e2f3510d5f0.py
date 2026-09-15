"""Megaphone (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b6916faa-9a8d-4d21-9406-4e2f3510d5f0'
SOURCE_PATH = 'icons-json/interface-essential/megaphone_b6916faa-9a8d-4d21-9406-4e2f3510d5f0.json'
AUTHOR = 'gpt-6'

class MegaphoneB6916faa(Solo48):
    icon_id = 'megaphone-b6916faa'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('megaphone', 'interface-essential')

    def build(self):
        self.add_line('e0', (18, 32), (22, 32))
        self.add_line('e1', (44, 33), (35, 8))
        self.add_line('e2', (35, 8), (31, 11))
        self.add_line('e3', (15, 21), (7, 24))
        self.add_line('e4', (12, 33), (18, 32))
        self.add_line('e5', (18, 32), (15, 21))
        self.add_line('e6', (18, 32), (23, 40))
        self.add_arc('e7', (22, 32), (44, 33), radius_x=54, radius_y=54, large_arc=False, sweep=True)
        self.add_arc('e8', (31, 11), (15, 21), radius_x=47, radius_y=47, large_arc=False, sweep=True)
        self.add_arc('e9-1', (7, 24), (4, 28), radius_x=5, radius_y=5, large_arc=False, sweep=False)
        self.add_arc('e9-2', (4, 28), (12, 33), radius_x=6, radius_y=6, large_arc=False, sweep=False)
        self.add_contour('c0', 'e0', 'e7', 'e1', 'e2', 'e8', 'e3', 'e9-1', 'e9-2', 'e4', closed=True)
        self.add_contour('c1', 'e5', closed=False)
        self.add_contour('c2', 'e6', closed=False)
        self.relate('connect', 'c1', 'c0')
