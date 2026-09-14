"""Target (war), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f6422635-c7a1-4188-8095-c06bed191a06'
SOURCE_PATH = 'icons-json/war/target_f6422635-c7a1-4188-8095-c06bed191a06.json'
AUTHOR = 'json_to_solo'

class Target(Solo48):
    icon_id = 'target'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('target', 'war')

    def build(self):
        self.add_line('e0', (24, 13), (24, 10))
        self.add_line('e1', (10, 24), (6, 24))
        self.add_line('e2', (35, 24), (38, 24))
        self.add_line('e3', (24, 35), (24, 38))
        self.add_line('e4', (13, 24), (10, 24))
        self.add_line('e5', (24, 38), (24, 42))
        self.add_line('e6', (24, 6), (24, 10))
        self.add_line('e7', (42, 24), (38, 24))
        self.add_arc('e8-top', (10, 24), (38, 24), radius_x=14)
        self.add_arc('e8-bottom', (38, 24), (10, 24), radius_x=14)
        self.add_dot('e9', (24, 24))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('c4', 'e4')
        self.add_contour('c5', 'e5')
        self.add_contour('c6', 'e6')
        self.add_contour('c7', 'e7')
        self.add_contour('e8', 'e8-top', 'e8-bottom', closed=True)
        self.relate('connect', 'c0', 'c6')
        self.relate('connect', 'c1', 'c4')
        self.relate('connect', 'c2', 'c7')
        self.relate('connect', 'c3', 'c5')
        self.relate('connect', 'c0', 'e8')
        self.relate('connect', 'c6', 'e8')
        self.relate('connect', 'c1', 'e8')
        self.relate('connect', 'c4', 'e8')
        self.relate('connect', 'c2', 'e8')
        self.relate('connect', 'c7', 'e8')
        self.relate('connect', 'c3', 'e8')
        self.relate('connect', 'c5', 'e8')
