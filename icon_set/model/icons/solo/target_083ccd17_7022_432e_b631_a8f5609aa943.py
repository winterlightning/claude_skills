"""Target (war), converted from the icons-json construction graph by json_to_solo --mode fit. CIRCLE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '083ccd17-7022-432e-b631-a8f5609aa943'
SOURCE_PATH = 'icons-json/war/target_083ccd17-7022-432e-b631-a8f5609aa943.json'
AUTHOR = 'json_to_solo'

class Target(Solo48):
    icon_id = 'target-083ccd17'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('target', 'war')

    def build(self):
        self.add_line('e0', (24, 4), (24, 7))
        self.add_line('e1', (41, 24), (44, 24))
        self.add_line('e2', (24, 44), (24, 41))
        self.add_line('e3', (4, 24), (7, 24))
        self.add_arc('e4-top', (4, 24), (44, 24), radius_x=20)
        self.add_arc('e4-bottom', (44, 24), (4, 24), radius_x=20)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.relate('connect', 'c0', 'e4')
        self.relate('connect', 'c1', 'e4')
        self.relate('connect', 'c2', 'e4')
        self.relate('connect', 'c3', 'e4')
