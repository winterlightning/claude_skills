"""Independent 32px profile of text-closed-captions-icon-90913ece.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '90913ece-3e45-4b69-b088-eabf18ccdedd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-closed-captions-icon-90913ece.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('90913ece-3e45-4b69-b088-eabf18ccdedd', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/CC (text)_90913ece-3e45-4b69-b088-eabf18ccdedd.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-closed-captions-icon-90913ece',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'd5c06a774548f8e70b46e2a2c7ff4919f2a93cfb8ff8f020c692bb5da22fc2ae'

TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-c-uppercase')
























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant2(TextSub32):
    icon_id = 'text-closed-captions-icon-90913ece-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 42.000000000000014, 20.0)

    def build(self):
        """Source-native uppercase composition for 'CC'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (16, 2.6879), ((14.9406, 2.24575), (13.7674, 2), (12.533, 2)))
        self.add_bezier('p1-r1-2', (12.533, 2), ((7.82037, 2), (4, 5.58172), (4, 10)))
        self.add_bezier('p1-r1-3', (4, 10), ((4, 14.4183), (7.82037, 18), (12.533, 18)))
        self.add_bezier('p1-r1-4', (12.533, 18), ((13.7674, 18), (14.9406, 17.7543), (16, 17.3121)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (40, 2.6879), ((38.9406, 2.24575), (37.7674, 2), (36.533, 2)))
        self.add_bezier('p2-r1-2', (36.533, 2), ((31.82037, 2), (28, 5.58172), (28, 10)))
        self.add_bezier('p2-r1-3', (28, 10), ((28, 14.4183), (31.82037, 18), (36.533, 18)))
        self.add_bezier('p2-r1-4', (36.533, 18), ((37.7674, 18), (38.9406, 17.7543), (40, 17.3121)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
