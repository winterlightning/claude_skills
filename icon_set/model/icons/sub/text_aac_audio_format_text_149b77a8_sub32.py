"""Independent 32px profile of text-aac-audio-format-text-149b77a8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '149b77a8-c99e-4921-be5c-930e9b10c61b'
SOURCE_PATH = 'icon_set/dist/text32/text-aac-audio-format-text-149b77a8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('149b77a8-c99e-4921-be5c-930e9b10c61b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/acc (text)_149b77a8-c99e-4921-be5c-930e9b10c61b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-aac-audio-format-text-149b77a8',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-a-uppercase', 'letter-c-uppercase')
REFERENCE_EXPORT_SHA256 = '5f83298b2b9a9115a4f5a4d97d61792d4634c8ee29e9e59bdafc5956630e624b'































TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-aac-audio-format-text-149b77a8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 68
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 66.0, 20.0)

    def build(self):
        """Source-native uppercase composition for 'AAC'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 18), ((4, 18), (5.26667, 2), (10.1333, 2)))
        self.add_bezier('p1-r1-2', (10.1333, 2), ((15, 2), (16, 18), (16, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (4.49782, 13.9921), (15.5709, 14.0032))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_bezier('p2-r1-1', (28, 18), ((28, 18), (29.26667, 2), (34.1333, 2)))
        self.add_bezier('p2-r1-2', (34.1333, 2), ((39, 2), (40, 18), (40, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p2-r2-1', (28.49782, 13.9921), (39.5709, 14.0032))
        self.add_contour('path-2-2', 'p2-r2-1', closed=False)
        self.add_bezier('p3-r1-1', (64, 2.6879), ((62.9406, 2.24575), (61.7674, 2), (60.533, 2)))
        self.add_bezier('p3-r1-2', (60.533, 2), ((55.82037, 2), (52, 5.58172), (52, 10)))
        self.add_bezier('p3-r1-3', (52, 10), ((52, 14.4183), (55.82037, 18), (60.533, 18)))
        self.add_bezier('p3-r1-4', (60.533, 18), ((61.7674, 18), (62.9406, 17.7543), (64, 17.3121)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
