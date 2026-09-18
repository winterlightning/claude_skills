"""Independent 32px profile of text-underlined-markdown-text-8f859757.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '8f859757-d9ba-4d92-8889-0e22b2a1aeb2'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-markdown-text-8f859757.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8f859757-d9ba-4d92-8889-0e22b2a1aeb2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/md (text u)_8f859757-d9ba-4d92-8889-0e22b2a1aeb2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-markdown-text-8f859757',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-d')
REFERENCE_EXPORT_SHA256 = '506fa5a742bb78704a1194aeba4bab0c80e4ea692637e51821cb974a7cde5c35'

class Drawing(TextSub32):
    icon_id = 'text-underlined-markdown-text-8f859757-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 41
    text_ink_bounds = (0.0, 0.0, 41.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (39, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (39, 18), ((38, 20), (36, 21), (33, 21)))
        self.add_bezier('p2-r1-2', (33, 21), ((30, 21), (27, 18), (27, 15)))
        self.add_bezier('p2-r1-3', (27, 15), ((27, 11), (30, 8), (33, 8)))
        self.add_bezier('p2-r1-4', (33, 8), ((36, 8), (38, 9), (39, 11)))
        self.add_bezier('p2-r1-5', (39, 11), ((39, 11), (39, 11), (39, 12)))
        self.add_line('p2-r1-6', (39, 12), (39, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (39, 12), (39, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (11, 14))
        self.add_line('p4-r1-3', (11, 14), (20, 2))
        self.add_line('p4-r1-4', (20, 2), (20, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
        self.relate('connect', 'p2-r1-6', 'p3-r1-1')
