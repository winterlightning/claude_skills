"""Independent 32px profile of text-underlined-capital-letter-i-6faddbc4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '6faddbc4-023e-4d07-ba7b-b1826b2349e7'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-capital-letter-i-6faddbc4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6faddbc4-023e-4d07-ba7b-b1826b2349e7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/i (text u)_6faddbc4-023e-4d07-ba7b-b1826b2349e7.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-capital-letter-i-6faddbc4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-i-uppercase',)
REFERENCE_EXPORT_SHA256 = 'c535313ec7399b40fadbc4160b8d60e6dbc62c7cb70758f008236b6612879ad4'

class Drawing(TextSub32):
    icon_id = 'text-underlined-capital-letter-i-6faddbc4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 10
    text_ink_bounds = (0.0, 0.0, 10.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (8, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 2), (8, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (5, 2), (5, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (8, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
