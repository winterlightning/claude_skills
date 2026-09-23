"""Independent 32px profile of text-css-web-styling-symbol-4e86ad2e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '4e86ad2e-5a24-449c-8379-d7e832726bb6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-css-web-styling-symbol-4e86ad2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e86ad2e-5a24-449c-8379-d7e832726bb6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/CSS (text)_4e86ad2e-5a24-449c-8379-d7e832726bb6.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-css-web-styling-symbol-4e86ad2e',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'b19af96fc151c5083ee1937920decf50bbe98bc4011cc830f1829a0bc98dceb0'

TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-s-uppercase', 'letter-s-uppercase')
























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant2(TextSub32):
    icon_id = 'text-css-web-styling-symbol-4e86ad2e-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 66.0000075398524, 20.000000000000004)

    def build(self):
        """Source-native uppercase composition for 'CSS'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (16, 2.6879), ((14.9406, 2.24575), (13.7674, 2), (12.533, 2)))
        self.add_bezier('p1-r1-2', (12.533, 2), ((7.82037, 2), (4, 5.58172), (4, 10)))
        self.add_bezier('p1-r1-3', (4, 10), ((4, 14.4183), (7.82037, 18), (12.533, 18)))
        self.add_bezier('p1-r1-4', (12.533, 18), ((13.7674, 18), (14.9406, 17.7543), (16, 17.3121)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (39.9314, 2), (32.77906, 2))
        self.add_bezier('p2-r1-2', (32.77906, 2), ((27.70172, 2), (26.21029, 7.42857), (30.98284, 9.42857)))
        self.add_line('p2-r1-3', (30.98284, 9.42857), (37.4623, 11.608))
        self.add_bezier('p2-r1-4', (37.4623, 11.608), ((41.7211, 13.4286), (40.2526, 18), (35.7787, 18)))
        self.add_line('p2-r1-5', (35.7787, 18), (28, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (63.9314, 2), (56.77906, 2))
        self.add_bezier('p3-r1-2', (56.77906, 2), ((51.70172, 2), (50.21029, 7.42857), (54.98284, 9.42857)))
        self.add_line('p3-r1-3', (54.98284, 9.42857), (61.4623, 11.608))
        self.add_bezier('p3-r1-4', (61.4623, 11.608), ((65.7211, 13.4286), (64.2526, 18), (59.7787, 18)))
        self.add_line('p3-r1-5', (59.7787, 18), (52, 18))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
