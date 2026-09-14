"""Target center (business), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39549a2c-f890-5365-b866-44d3f44ceb57'
SOURCE_PATH = 'icons-json/business/target center_39549a2c-f890-5365-b866-44d3f44ceb57.json'
AUTHOR = 'json_to_solo'

class TargetCenter(Solo48):
    icon_id = 'target-center'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    aliases = ()
    keywords = ('target', 'center', 'business')

    def build(self):
        self.add_line('e0', (42, 24), (30, 24))
        self.add_line('e1', (24, 30), (24, 42))
        self.add_line('e2', (18, 24), (6, 24))
        self.add_line('e3', (24, 18), (24, 6))
        self.add_arc('e4-top', (10, 24), (38, 24), radius_x=14)
        self.add_arc('e4-bottom', (38, 24), (10, 24), radius_x=14)
        self.add_arc('e5-top', (18, 24), (30, 24), radius_x=6)
        self.add_arc('e5-bottom', (30, 24), (18, 24), radius_x=6)
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3')
        self.add_contour('e4', 'e4-top', 'e4-bottom', closed=True)
        self.add_contour('e5', 'e5-top', 'e5-bottom', closed=True)
        self.relate('connect', 'c0', 'e5')
        self.relate('connect', 'c1', 'e5')
        self.relate('connect', 'c2', 'e5')
        self.relate('connect', 'c3', 'e5')
