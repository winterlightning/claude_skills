"""Warp shell upper (design), converted from the icons-json construction graph by json_to_solo --mode bezier. SQUARE keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '318570bf-d868-5293-9426-d9a1090f3879'
SOURCE_PATH = 'pictographic-primitives/design/warp shell upper_318570bf-d868-5293-9426-d9a1090f3879.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-retained-after-visual-review'

class WarpShellUpper(Solo48):
    icon_id = 'warp-shell-upper'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('warp', 'shell', 'upper', 'design')

    def build(self):
        self.add_line('e0', (31, 42), (31, 35))
        self.add_line('e1', (38, 26), (42, 26))
        self.add_line('e2', (17, 34), (17, 42))
        self.add_line('e3', (17, 42), (31, 42))
        self.add_bezier('e4', (31, 35), ((31, 31.719), (33.466, 29.015), (36.175, 27.322)), ((36.674, 27.003), (37.411, 26.115), (38, 26)))
        self.add_bezier('e5', (42, 26), ((42, 25.305), (41.992, 24.254), (41.992, 23.558)), ((41.992, 14.305), (33.884, 6.016), (24.573, 6.016)), ((24.393, 6.016), (24.213, 6), (24.041, 6)), ((24.038, 6), (24.035, 6), (24.032, 6)), ((23.839, 6), (23.653, 6.008), (23.468, 6.008)), ((14.075, 6.008), (6.008, 14.591), (6.008, 23.869)), ((6.008, 23.966), (6, 24.054), (6, 24.151)), ((6, 24.152), (6, 24.154), (6, 24.155)), ((6.008, 24.605), (6.025, 25.047), (6.033, 25.497)), ((6.041, 25.538), (6.875, 25.62), (6.957, 25.636)), ((8.005, 25.8), (9.101, 25.939), (10.075, 26.365)), ((12.84, 27.559), (14.992, 29.58), (16.129, 32.386)), ((16.293, 32.787), (17, 33.566), (17, 34)))
        self.add_contour('c0', 'e0', 'e4', 'e1', 'e5', 'e2', 'e3', closed=True)
