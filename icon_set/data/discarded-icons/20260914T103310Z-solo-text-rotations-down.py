"""Text rotations down (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed890308-8456-4c1f-9b2b-8be5a009a415'
SOURCE_PATH = 'icons-json/interface-essential/text rotations down_ed890308-8456-4c1f-9b2b-8be5a009a415.json'
AUTHOR = 'json_to_solo'

class TextRotationsDown(Solo48):
    icon_id = 'text-rotations-down'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'rotations', 'down', 'interface-essential')

    def build(self):
        self.add_line('e0', (27, 22), (30, 17))
        self.add_line('e1', (42, 22), (40, 17))
        self.add_line('e2', (30, 17), (40, 17))
        self.add_line('e3', (30, 17), (34, 7))
        self.add_line('e4', (35, 7), (40, 17))
        self.add_line('e5', (6, 15), (34, 42))
        self.add_line('e6', (26, 42), (32, 42))
        self.add_line('e7', (32, 42), (34, 42))
        self.add_line('e8', (34, 34), (34, 42))
        self.add_line('e9-1', (34, 7), (34, 6))
        self.add_arc('e9-2', (34, 6), (35, 7), radius_x=1)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e9-1', 'e9-2', 'e4')
        self.add_contour('c4', 'e5')
        self.add_contour('c5', 'e6', 'e7')
        self.add_contour('c6', 'e8')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c1', 'c3')
        self.relate('connect', 'c2', 'c3')
        self.relate('connect', 'c4', 'c5')
        self.relate('connect', 'c4', 'c6')
        self.relate('connect', 'c5', 'c6')
