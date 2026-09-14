"""Strategy split (arrows), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8a64710-b7eb-5217-beec-39744ce7d77c'
SOURCE_PATH = 'icons-json/arrows/strategy split_c8a64710-b7eb-5217-beec-39744ce7d77c.json'
AUTHOR = 'json_to_solo'

class StrategySplitArrows(Solo48):
    icon_id = 'strategy-split-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('strategy', 'split', 'arrows')

    def build(self):
        self.add_line('e0', (24, 13), (24, 36))
        self.add_line('e1', (24, 42), (24, 37))
        self.add_line('e2', (42, 21), (35, 19))
        self.add_line('e3', (35, 19), (37, 27))
        self.add_line('e4', (37, 27), (42, 21))
        self.add_line('e5', (13, 19), (6, 21))
        self.add_line('e6', (6, 21), (11, 27))
        self.add_line('e7', (11, 27), (13, 19))
        self.add_line('e8', (19, 13), (28, 13))
        self.add_line('e9', (28, 13), (24, 6))
        self.add_line('e10', (24, 6), (19, 13))
        self.add_arc('e11', (24, 36), (35, 22), radius_x=18)
        self.add_arc('e12', (24, 37), (13, 22), radius_x=18, sweep=False)
        self.add_contour('c0', 'e11')
        self.add_contour('c1', 'e0')
        self.add_contour('c2', 'e1', 'e12')
        self.add_contour('c3', 'e2', 'e3', 'e4', closed=True)
        self.add_contour('c4', 'e5', 'e6', 'e7', closed=True)
        self.add_contour('c5', 'e8', 'e9', 'e10', closed=True)
        self.relate('connect', 'c0', 'c3')
        self.relate('connect', 'c1', 'c5')
        self.relate('connect', 'c1', 'c0')
        self.relate('connect', 'c2', 'c4')
