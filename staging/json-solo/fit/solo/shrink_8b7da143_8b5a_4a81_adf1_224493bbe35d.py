"""Shrink (interface-essential), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b7da143-8b5a-4a81-adf1-224493bbe35d'
SOURCE_PATH = 'icons-json/interface-essential/shrink_8b7da143-8b5a-4a81-adf1-224493bbe35d.json'
AUTHOR = 'json_to_solo'

class Shrink8b7da143(Solo48):
    icon_id = 'shrink-8b7da143'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('shrink', 'interface-essential')

    def build(self):
        self.add_line('e0', (42, 6), (27, 21))
        self.add_line('e1', (27, 9), (27, 21))
        self.add_line('e2', (39, 21), (27, 21))
        self.add_line('e3', (12, 26), (22, 26))
        self.add_line('e4', (6, 42), (22, 26))
        self.add_line('e5', (22, 36), (22, 26))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.relate('connect', 'c0', 'c1')
        self.relate('connect', 'c0', 'c2')
        self.relate('connect', 'c1', 'c2')
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c4', 'c5')
