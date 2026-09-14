"""Keyboard arrow bottom (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '921d7bfe-d6be-588f-ad4e-a75efb840443'
SOURCE_PATH = 'icons-json/arrows/keyboard arrow bottom_921d7bfe-d6be-588f-ad4e-a75efb840443.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowBottomArrows(Solo48):
    icon_id = 'keyboard-arrow-bottom-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'bottom', 'arrows')

    def build(self):
        self.add_line('e0', (30, 44), (21, 35))
        self.add_line('e1', (40, 35), (31, 44))
        self.add_line('e2', (31, 44), (31, 14))
        self.add_line('e3', (8, 15), (8, 23))
        self.add_bezier('e4', (31, 14), ((31, 9.973), (29.42, 6.964), (25.38, 5.091)), ((24.04, 4.464), (22.41, 4.018), (20.88, 4.018)), ((20.8, 4.009), (20.72, 4.009), (20.64, 4)), ((20.639, 4), (20.638, 4), (20.636, 4)), ((20.558, 4), (20.479, 4.009), (20.4, 4.009)), ((15.01, 4.009), (10.35, 7.718), (8.65, 12.2)), ((8.34, 13.045), (8, 14.1), (8, 15)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4', 'e3')
