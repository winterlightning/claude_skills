"""Target (war), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ff85295-bc70-4db2-bf5d-2efaa7b0cead'
SOURCE_PATH = 'icons-json/war/target_3ff85295-bc70-4db2-bf5d-2efaa7b0cead.json'
AUTHOR = 'json_to_solo'

class Target3ff85295(Solo48):
    icon_id = 'target-3ff85295'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('target', 'war')

    def build(self):
        self.add_line('e0', (24, 6), (24, 8))
        self.add_line('e1', (40, 24), (42, 24))
        self.add_line('e2', (24, 42), (24, 40))
        self.add_line('e3', (6, 24), (8, 24))
        self.add_arc('e4-top', (8, 24), (40, 24), radius_x=16)
        self.add_arc('e4-bottom', (40, 24), (8, 24), radius_x=16)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
