"""Text rotations horizontal (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b7e3142-f35a-43c6-9dd1-3b10bd5b4e47'
SOURCE_PATH = 'icons-json/interface-essential/text rotations horizontal_7b7e3142-f35a-43c6-9dd1-3b10bd5b4e47.json'
AUTHOR = 'json_to_solo'

class TextRotationsHorizontalInterfaceEssential(Solo48):
    icon_id = 'text-rotations-horizontal-interface-essential'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'rotations', 'horizontal', 'interface-essential')

    def build(self):
        self.add_line('e0', (14, 26), (17, 19))
        self.add_line('e1', (29, 26), (27, 19))
        self.add_line('e2', (17, 19), (27, 19))
        self.add_line('e3', (17, 19), (20, 10))
        self.add_line('e4', (23, 10), (27, 19))
        self.add_line('e5', (38, 28), (44, 34))
        self.add_line('e6', (4, 34), (44, 34))
        self.add_line('e7', (39, 40), (44, 34))
        self.add_arc('e8-1', (20, 10), (22, 8), radius_x=13, sweep=False)
        self.add_line('e8-2', (22, 8), (23, 10))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e8-1', 'e8-2', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6')
        self.add_contour('c6', 'e7')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
