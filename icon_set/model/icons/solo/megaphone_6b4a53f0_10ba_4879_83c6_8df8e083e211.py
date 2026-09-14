"""Megaphone (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b4a53f0-10ba-4879-83c6-8df8e083e211'
SOURCE_PATH = 'icons-json/interface-essential/megaphone_6b4a53f0-10ba-4879-83c6-8df8e083e211.json'
AUTHOR = 'json_to_solo'

class Megaphone6b4a53f0(Solo48):
    icon_id = 'megaphone-6b4a53f0'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('megaphone', 'interface-essential')

    def build(self):
        self.add_line('e0', (21, 39), (19, 40))
        self.add_line('e1', (16, 38), (11, 32))
        self.add_line('e2', (16, 21), (19, 31))
        self.add_line('e3', (11, 32), (19, 31))
        self.add_line('e4', (16, 21), (20, 20))
        self.add_line('e5', (32, 12), (38, 8))
        self.add_line('e6', (38, 8), (44, 32))
        self.add_line('e7', (44, 32), (38, 30))
        self.add_line('e8', (25, 30), (19, 31))
        self.add_arc('e9', (19, 40), (16, 38), radius_x=4)
        self.add_arc('e10-1', (11, 32), (4, 28), radius_x=5)
        self.add_line('e10-2', (4, 28), (4, 27))
        self.add_arc('e10-3', (4, 27), (7, 23), radius_x=5)
        self.add_line('e10-4', (7, 23), (16, 21))
        self.add_arc('e11', (20, 20), (32, 12), radius_x=48, sweep=False)
        self.add_arc('e12', (38, 30), (25, 30), radius_x=41, sweep=False)
        self.add_contour('c0', 'e0', 'e9', 'e1')
        self.add_contour('c1', 'e2')
        self.add_contour('c2', 'e3')
        self.add_contour('c3', 'e10-1', 'e10-2', 'e10-3', 'e10-4', 'e4', 'e11', 'e5', 'e6', 'e7', 'e12', 'e8')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c3')
