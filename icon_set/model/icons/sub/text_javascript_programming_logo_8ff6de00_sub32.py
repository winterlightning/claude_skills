"""Independent 32px profile of text-javascript-programming-logo-8ff6de00.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '8ff6de00-b727-4281-bda7-6deac32a7fb0'
SOURCE_PATH = 'icon_set/dist/text32/text-javascript-programming-logo-8ff6de00.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8ff6de00-b727-4281-bda7-6deac32a7fb0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/js (text)_8ff6de00-b727-4281-bda7-6deac32a7fb0.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-javascript-programming-logo-8ff6de00',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-j-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '5e0ecd4c3d314804827a566eddad5c2fd44e61ec535a2c7befd7c361e2261e4c'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-javascript-programming-logo-8ff6de00-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 42.00000753985241, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for 'JS'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 13.4286), ((4, 16.5714), (6.68629, 18), (10, 18)))
        self.add_bezier('p1-r1-2', (10, 18), ((13.3137, 18), (16, 16.5714), (16, 13.6918)))
        self.add_line('p1-r1-3', (16, 13.6918), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (39.9314, 2), (32.77906, 2))
        self.add_bezier('p2-r1-2', (32.77906, 2), ((27.70172, 2), (26.21029, 7.42857), (30.98284, 9.42857)))
        self.add_line('p2-r1-3', (30.98284, 9.42857), (37.4623, 11.608))
        self.add_bezier('p2-r1-4', (37.4623, 11.608), ((41.7211, 13.4286), (40.2526, 18), (35.7787, 18)))
        self.add_line('p2-r1-5', (35.7787, 18), (28, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
