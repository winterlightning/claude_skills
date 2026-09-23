"""Independent 32px profile of text-txt-text-document-icon-15c48b39.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '15c48b39-7bf3-43b2-930a-e15900db4131'
SOURCE_PATH = 'icon_set/dist/text32/text-txt-text-document-icon-15c48b39.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('15c48b39-7bf3-43b2-930a-e15900db4131', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/txt (text)_15c48b39-7bf3-43b2-930a-e15900db4131.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-txt-text-document-icon-15c48b39',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-x-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = '158c64d4cc6a8adbbfb56c318e65b18ea2b04fc6fc9f67b1afdb9acba8fb394b'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-txt-text-document-icon-15c48b39-sub32'
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
        """Source-native uppercase composition for 'TXT'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (4, 2), (16, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (10, 18), (10.0064, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27, 2.00003), (41, 17.9909))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27.02295, 18), (40.9638, 2.04587))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (52, 2), (64, 2))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (58, 18), (58.0064, 2))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.relate("connect", 'path-1-1', 'path-2-1')
        self.relate("connect", 'path-3-1', 'path-4-1')
        self.relate("connect", 'path-5-1', 'path-6-1')
