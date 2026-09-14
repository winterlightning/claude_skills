"""Target (war), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d7f6568-79d6-46e9-9ac8-8b13a1982cb3'
SOURCE_PATH = 'icons-json/war/target_2d7f6568-79d6-46e9-9ac8-8b13a1982cb3.json'
AUTHOR = 'json_to_solo'

class Target2d7f6568(Solo48):
    icon_id = 'target-2d7f6568'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('target', 'war')

    def build(self):
        self.add_line('e0', (24, 13), (24, 6))
        self.add_line('e1', (35, 24), (42, 24))
        self.add_line('e2', (24, 35), (24, 42))
        self.add_line('e3', (9, 24), (13, 24))
        self.add_line('e4', (6, 24), (9, 24))
        self.add_arc('e5-top', (9, 24), (39, 24), radius_x=15)
        self.add_arc('e5-bottom', (39, 24), (9, 24), radius_x=15)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c3', 'c4')
        self.relate('connect', 'c3', 'e5')
        self.relate('connect', 'c4', 'e5')
