"""Independent 32px profile of text-underlined-nd-text-icon-c5a8d04e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'c5a8d04e-8e99-497e-8fad-2ddcfcd03cdf'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-nd-text-icon-c5a8d04e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c5a8d04e-8e99-497e-8fad-2ddcfcd03cdf', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/nd (text u)_c5a8d04e-8e99-497e-8fad-2ddcfcd03cdf.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-nd-text-icon-c5a8d04e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-d')
REFERENCE_EXPORT_SHA256 = '93fe0337b7d1db08375dd5eb96b79ec8d3343856282f680f869e85b6d8c2b2a6'

class Drawing(TextSub32):
    icon_id = 'text-underlined-nd-text-icon-c5a8d04e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 37
    text_ink_bounds = (0.0, 0.0, 37.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (35, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (35, 18), ((34, 20), (32, 21), (29, 21)))
        self.add_bezier('p2-r1-2', (29, 21), ((25, 21), (22, 18), (22, 15)))
        self.add_bezier('p2-r1-3', (22, 15), ((22, 11), (25, 8), (29, 8)))
        self.add_bezier('p2-r1-4', (29, 8), ((31, 8), (33, 9), (35, 11)))
        self.add_bezier('p2-r1-5', (35, 11), ((35, 11), (35, 11), (35, 12)))
        self.add_line('p2-r1-6', (35, 12), (35, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (35, 12), (35, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (16, 21))
        self.add_line('p4-r1-3', (16, 21), (16, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
