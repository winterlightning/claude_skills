"""Keyboard arrow top (arrows), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9ac4fae5-c371-5faf-8ca1-01fe89c4d4ce'
SOURCE_PATH = 'icons-json/arrows/keyboard arrow top_9ac4fae5-c371-5faf-8ca1-01fe89c4d4ce.json'
AUTHOR = 'json_to_solo'

class KeyboardArrowTopArrows(Solo48):
    icon_id = 'keyboard-arrow-top-arrows'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('keyboard', 'arrow', 'top', 'arrows')

    def build(self):
        self.add_line('e0', (18, 4), (27, 13))
        self.add_line('e1', (8, 13), (17, 4))
        self.add_line('e2', (17, 4), (17, 34))
        self.add_line('e3', (40, 33), (40, 25))
        self.add_bezier('e4', (17, 34), ((17, 38.027), (18.58, 41.036), (22.62, 42.909)), ((23.96, 43.536), (25.59, 43.982), (27.12, 43.982)), ((27.2, 43.991), (27.28, 43.991), (27.36, 44)), ((27.361, 44), (27.362, 44), (27.364, 44)), ((27.442, 44), (27.521, 43.991), (27.6, 43.991)), ((32.99, 43.991), (37.65, 40.282), (39.35, 35.8)), ((39.66, 34.955), (40, 33.9), (40, 33)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1', 'e2', 'e4', 'e3')
