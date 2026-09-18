"""Independent 32px profile of text-nickel-chemical-element-symbol-bf43754a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'bf43754a-32e4-4cbd-be65-839a04327737'
SOURCE_PATH = 'icon_set/dist/text32/text-nickel-chemical-element-symbol-bf43754a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bf43754a-32e4-4cbd-be65-839a04327737', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ni (text u)_bf43754a-32e4-4cbd-be65-839a04327737.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-nickel-chemical-element-symbol-bf43754a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-i')
REFERENCE_EXPORT_SHA256 = 'caa997c9b4b1aa5e12b1c673bd2946419e98c51c648d60ed262ba8345c44b236'

class Drawing(TextSub32):
    icon_id = 'text-nickel-chemical-element-symbol-bf43754a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 24
    text_ink_bounds = (0.0, 0.0, 24.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (22, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 2), (22, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (22, 8), (22, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (16, 21))
        self.add_line('p4-r1-3', (16, 21), (16, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
