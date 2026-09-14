"""Fast up (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. HRECT_L keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f61f1a6-7004-4899-8bf1-688257e3f936'
SOURCE_PATH = 'icons-json/arrows/fast up_1f61f1a6-7004-4899-8bf1-688257e3f936.json'
AUTHOR = 'json_to_solo'

class FastUp(Solo48):
    icon_id = 'fast-up'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('fast', 'up', 'arrows')

    def build(self):
        self.add_line('e0', (34, 12), (39, 8))
        self.add_line('e1', (44, 12), (39, 8))
        self.add_line('e2', (11, 39), (14, 38))
        self.add_line('e3', (4, 40), (7, 40))
        self.add_arc('e4', (19, 37), (39, 8), radius_x=31, sweep=False)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e4')
        self.add_contour('c2', 'e1')
        self.add_contour('c3', 'e2')
        self.add_contour('c4', 'e3')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
