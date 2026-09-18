"""Independent 32px profile of text-number-zero-digit-icon-e070fae7.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'e070fae7-149d-4c33-a2d6-4734b2d75e94'
SOURCE_PATH = 'icon_set/dist/text32/text-number-zero-digit-icon-e070fae7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e070fae7-149d-4c33-a2d6-4734b2d75e94', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/0 (text)_e070fae7-149d-4c33-a2d6-4734b2d75e94.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-zero-digit-icon-e070fae7',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-0',)
REFERENCE_EXPORT_SHA256 = '0e67d9d1dda6156e94709502b0f0e979a29e448a5eb034cdd7ba4d245e4a7dce'

class Drawing(TextSub32):
    icon_id = 'text-number-zero-digit-icon-e070fae7-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 23
    text_ink_bounds = (0.0, 0.0, 23.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (2, 10), ((2, 6), (6, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((17, 2), (21, 6), (21, 10)))
        self.add_line('p1-r1-3', (21, 10), (21, 22))
        self.add_bezier('p1-r1-4', (21, 22), ((21, 26), (17, 30), (12, 30)))
        self.add_bezier('p1-r1-5', (12, 30), ((6, 30), (2, 26), (2, 22)))
        self.add_line('p1-r1-6', (2, 22), (2, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
