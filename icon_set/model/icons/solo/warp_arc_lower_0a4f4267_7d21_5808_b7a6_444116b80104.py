"""Warp arc lower (design), converted from the icons-json construction graph by json_to_solo --mode fit. SQUARE keyshape; curves fitted to integer lines and arcs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a4f4267-7d21-5808-b7a6-444116b80104'
SOURCE_PATH = 'icons-json/design/warp arc lower_0a4f4267-7d21-5808-b7a6-444116b80104.json'
AUTHOR = 'json_to_solo'

class WarpArcLower(Solo48):
    icon_id = 'warp-arc-lower'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'arc', 'lower', 'design')

    def build(self):
        self.add_line('e0', (6, 23), (6, 6))
        self.add_line('e1', (6, 6), (42, 6))
        self.add_line('e2', (42, 6), (42, 25))
        self.add_arc('e3-1', (42, 25), (24, 42), radius_x=19)
        self.add_line('e3-2', (24, 42), (18, 41))
        self.add_arc('e3-3', (18, 41), (8, 32), radius_x=20)
        self.add_line('e3-4', (8, 32), (6, 23))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3-1', 'e3-2', 'e3-3', 'e3-4', closed=True)
