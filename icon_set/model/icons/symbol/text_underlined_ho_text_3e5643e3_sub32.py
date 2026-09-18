"""Independent 32px profile of text-underlined-ho-text-3e5643e3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '3e5643e3-1aed-4c98-8075-d06df0b03f59'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-ho-text-3e5643e3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3e5643e3-1aed-4c98-8075-d06df0b03f59', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ho (text u)_3e5643e3-1aed-4c98-8075-d06df0b03f59.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-ho-text-3e5643e3',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-o')
REFERENCE_EXPORT_SHA256 = '81e9404553518e296d85327a1b9272dfe1d58c6346f138f3cb94dac36aa02364'

class Drawing(TextSub32):
    icon_id = 'text-underlined-ho-text-3e5643e3-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 38
    text_ink_bounds = (0.0, 0.0, 38.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (36, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (29, 21), ((33, 21), (36, 18), (36, 15)))
        self.add_bezier('p2-r1-2', (36, 15), ((36, 11), (33, 8), (29, 8)))
        self.add_bezier('p2-r1-3', (29, 8), ((25, 8), (22, 11), (22, 15)))
        self.add_bezier('p2-r1-4', (22, 15), ((22, 18), (25, 21), (29, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 2), (2, 21))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (16, 2), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 12), (16, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
