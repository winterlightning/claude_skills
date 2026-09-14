"""Sand (state), converted from the icons-json construction graph by json_to_solo --mode bezier. HRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '039d6076-f6f0-4285-9273-7fe0e43d2b2e'
SOURCE_PATH = 'icons-json/state/sand_039d6076-f6f0-4285-9273-7fe0e43d2b2e.json'
AUTHOR = 'json_to_solo'

class SandState(Solo48):
    icon_id = 'sand-state'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'state'
    aliases = ()
    keywords = ('sand', 'state')

    def build(self):
        self.add_line('e0', (4, 40), (23, 8))
        self.add_line('e1', (25, 8), (44, 40))
        self.add_bezier('e2', (23, 8), ((23.173, 8), (23.427, 8), (23.6, 8)), ((23.8, 8), (24.027, 8), (24.227, 8)), ((24.455, 8), (24.773, 8), (25, 8)))
        self.add_bezier('e3', (16, 40), ((15.7, 40), (15.3, 40), (15, 40)))
        self.add_bezier('e4', (24, 27), ((23.7, 27), (23.3, 27), (23, 27)))
        self.add_bezier('e5', (32, 38), ((31.7, 38), (31.3, 38), (31, 38)))
        self.add_contour('c0', 'e0', 'e2', 'e1')
        self.add_contour('c1', 'e3')
        self.add_contour('c2', 'e4')
        self.add_contour('c3', 'e5')
