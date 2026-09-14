"""Round (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09113b60-330a-48f7-bd5a-2a66b63402bc'
SOURCE_PATH = 'icons-json/arrows/round_09113b60-330a-48f7-bd5a-2a66b63402bc.json'
AUTHOR = 'json_to_solo'

class RoundArrows(Solo48):
    icon_id = 'round-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('round', 'arrows')

    def build(self):
        self.add_line('e0', (13, 33), (10, 31))
        self.add_line('e1', (10, 31), (8, 31))
        self.add_line('e2', (6, 36), (8, 31))
        self.add_arc('e3-1', (7, 24), (24, 6), radius_x=18)
        self.add_arc('e3-2', (24, 6), (42, 24), radius_x=18)
        self.add_line('e3-3', (42, 24), (41, 30))
        self.add_arc('e3-4', (41, 30), (25, 42), radius_x=17)
        self.add_arc('e3-5', (25, 42), (8, 31), radius_x=19)
        self.add_contour('c0', 'e3-1', 'e3-2', 'e3-3', 'e3-4', 'e3-5')
        self.add_contour('c1', 'e0', 'e1')
        self.add_contour('c2', 'e2')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
