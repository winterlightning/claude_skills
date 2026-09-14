"""Warp arc lower (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0a4f4267-7d21-5808-b7a6-444116b80104'
SOURCE_PATH = 'icons-json/design/warp arc lower_0a4f4267-7d21-5808-b7a6-444116b80104.json'
AUTHOR = 'json_to_solo'

class WarpArcLowerDesign(Solo48):
    icon_id = 'warp-arc-lower-design'
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
        self.add_bezier('e3', (42, 25), ((42, 26.456), (41.493, 27.927), (41.018, 29.294)), ((38.588, 36.322), (31.985, 42), (24.319, 42)), ((24.317, 42), (24.315, 42), (24.313, 42)), ((24.184, 42), (24.055, 42), (23.926, 42)), ((23.73, 42), (23.534, 41.984), (23.337, 41.984)), ((14.116, 41.984), (6.016, 33.033), (6.016, 23.984)), ((6.016, 23.787), (6, 23.583), (6, 23.386)), ((6, 23.313), (6, 23.065), (6, 23)))
        self.add_contour('c0', 'e0', 'e1', 'e2', 'e3', closed=True)
