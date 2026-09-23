"""Independent 32px profile of text-executable-file-format-symbol-f31ac6f8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f31ac6f8-97b2-46d9-96fe-178982007df7'
SOURCE_PATH = 'icon_set/dist/text32/text-executable-file-format-symbol-f31ac6f8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f31ac6f8-97b2-46d9-96fe-178982007df7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/exe (text)_f31ac6f8-97b2-46d9-96fe-178982007df7.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-executable-file-format-symbol-f31ac6f8',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-e-uppercase', 'letter-x-uppercase', 'letter-e-uppercase')
REFERENCE_EXPORT_SHA256 = '9ba1f55cdecbea4b8c41d8856842c0904430e492ba8ef0f87ca505be2afad46b'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-executable-file-format-symbol-f31ac6f8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (1.9999999999999982, 0.0, 66.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'EXE'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (16, 17.9999), (4.26183, 18))
        self.add_bezier('p1-r1-2', (4.26183, 18), ((4.11723, 18), (4, 17.8828), (4, 17.7382)))
        self.add_line('p1-r1-3', (4, 17.7382), (4, 9.98924))
        self.add_line('p1-r1-4', (4, 9.98924), (4, 2.01314))
        self.add_line('p1-r1-5', (4, 2.01314), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (12.4, 10), (4, 10))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27, 2.00003), (41, 17.9909))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27.02295, 18), (40.9638, 2.04587))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (64, 17.9999), (52.26183, 18))
        self.add_bezier('p5-r1-2', (52.26183, 18), ((52.11723, 18), (52, 17.8828), (52, 17.7382)))
        self.add_line('p5-r1-3', (52, 17.7382), (52, 9.98924))
        self.add_line('p5-r1-4', (52, 9.98924), (52, 2.01314))
        self.add_line('p5-r1-5', (52, 2.01314), (64, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
        self.add_line('p6-r1-1', (60.4, 10), (52, 10))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
