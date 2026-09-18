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

class Drawing(TextSub32):
    icon_id = 'text-executable-file-format-symbol-f31ac6f8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 74
    text_ink_bounds = (0.0, 0.0, 74.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (72, 2), (55, 2))
        self.add_line('p1-r1-2', (55, 2), (55, 30))
        self.add_line('p1-r1-3', (55, 30), (72, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (55, 16), (69, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27, 2), (47, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (47, 2), (27, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (19, 2), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (2, 30))
        self.add_line('p5-r1-3', (2, 30), (19, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.add_line('p6-r1-1', (2, 16), (16, 16))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
