"""Independent 32px profile of text-capital-letter-a-37012d29.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '37012d29-357d-4e7a-9788-4fe102b86097'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-capital-letter-a-37012d29.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('37012d29-357d-4e7a-9788-4fe102b86097', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/a (text)_37012d29-357d-4e7a-9788-4fe102b86097.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-capital-letter-a-37012d29',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = '25cf18d5525249db4d9a534bc3a4c2b9ea361a1f824dc3d4b7245e14ba7d9ab6'

TYPEFACE_GLYPH_IDS = ('letter-a-uppercase',)
























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class DrawingVariant2(TextSub32):
    icon_id = 'text-capital-letter-a-37012d29-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 20
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 18.000000000000004, 20.0)

    def build(self):
        """Source-native uppercase composition for 'A'; 4-unit letter spacing."""
        self.add_bezier('p1-r1-1', (4, 18), ((4, 18), (5.26667, 2), (10.1333, 2)))
        self.add_bezier('p1-r1-2', (10.1333, 2), ((15, 2), (16, 18), (16, 18)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p1-r2-1', (4.49782, 13.9921), (15.5709, 14.0032))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
