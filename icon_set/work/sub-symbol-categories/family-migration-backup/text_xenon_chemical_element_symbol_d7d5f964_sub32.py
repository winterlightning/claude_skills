"""Independent 32px profile of text-xenon-chemical-element-symbol-d7d5f964.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'd7d5f964-0081-49e8-82d4-5a16cf05ca8d'
SOURCE_PATH = 'icon_set/dist/text32/text-xenon-chemical-element-symbol-d7d5f964.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d7d5f964-0081-49e8-82d4-5a16cf05ca8d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/xe (text u)_d7d5f964-0081-49e8-82d4-5a16cf05ca8d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-xenon-chemical-element-symbol-d7d5f964',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = '0bc6f3ef298f868e01f41c9108191e5459209202d3a0aa7f0cebaea030e4ce35'

class Drawing(TextSub32):
    icon_id = 'text-xenon-chemical-element-symbol-d7d5f964-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 38
    text_ink_bounds = (0.0, 0.0, 38.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (36, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (36, 15), ((36, 11), (33, 8), (29, 8)))
        self.add_bezier('p2-r1-2', (29, 8), ((25, 8), (22, 11), (22, 15)))
        self.add_bezier('p2-r1-3', (22, 15), ((22, 18), (25, 21), (29, 21)))
        self.add_bezier('p2-r1-4', (29, 21), ((32, 21), (34, 20), (35, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (22, 15), (36, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (16, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 2), (2, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
