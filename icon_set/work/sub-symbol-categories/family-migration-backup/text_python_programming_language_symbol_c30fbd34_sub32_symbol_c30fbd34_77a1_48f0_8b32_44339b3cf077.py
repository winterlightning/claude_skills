# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-python-programming-language-symbol-c30fbd34.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'c30fbd34-77a1-48f0-8b32-44339b3cf077'
SOURCE_PATH = 'icon_set/dist/text32/text-python-programming-language-symbol-c30fbd34.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c30fbd34-77a1-48f0-8b32-44339b3cf077', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/py (text)_c30fbd34-77a1-48f0-8b32-44339b3cf077.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-python-programming-language-symbol-c30fbd34',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-y-uppercase')
REFERENCE_EXPORT_SHA256 = '46b038a7620e8eec77cc922303680f75fcc6c5ccca95039434e99f813f2014e0'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-python-programming-language-symbol-c30fbd34-sub32-symbol'
    variant_of = 'text-python-programming-language-symbol-c30fbd34-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-python-programming-language-symbol-c30fbd34-sub32'
    counterpart_icon_id = 'text-python-programming-language-symbol-c30fbd34-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 53
    text_ink_bounds = (0.0, 0.0, 53.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 2), (40, 17))
        self.add_line('p1-r1-2', (40, 17), (51, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (40, 17), (40, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (12, 2))
        self.add_bezier('p3-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p3-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p3-r1-5', (12, 17), (2, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
