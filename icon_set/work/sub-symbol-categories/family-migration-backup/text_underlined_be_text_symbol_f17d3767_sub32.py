"""Independent 32px profile of text-underlined-be-text-symbol-f17d3767.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f17d3767-756e-40e4-a1d9-8b2fc618d58d'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-be-text-symbol-f17d3767.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f17d3767-756e-40e4-a1d9-8b2fc618d58d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/be (text u)_f17d3767-756e-40e4-a1d9-8b2fc618d58d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-be-text-symbol-f17d3767',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = 'f32fcc8170839de76aeaa98e62cbca1a16b3b0a6fa9a89be231f8b5f635d675b'

class Drawing(TextSub32):
    icon_id = 'text-underlined-be-text-symbol-f17d3767-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 37
    text_ink_bounds = (0.0, 0.0, 37.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (35, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (35, 15), ((35, 11), (32, 8), (28, 8)))
        self.add_bezier('p2-r1-2', (28, 8), ((24, 8), (21, 11), (21, 15)))
        self.add_bezier('p2-r1-3', (21, 15), ((21, 18), (24, 21), (28, 21)))
        self.add_bezier('p2-r1-4', (28, 21), ((30, 21), (33, 20), (34, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (21, 15), (35, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (8, 2))
        self.add_bezier('p4-r1-3', (8, 2), ((12, 2), (14, 4), (14, 7)))
        self.add_bezier('p4-r1-4', (14, 7), ((14, 9), (12, 12), (8, 12)))
        self.add_line('p4-r1-5', (8, 12), (2, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_bezier('p5-r1-1', (8, 12), ((13, 12), (15, 14), (15, 16)))
        self.add_bezier('p5-r1-2', (15, 16), ((15, 19), (13, 21), (8, 21)))
        self.add_line('p5-r1-3', (8, 21), (2, 21))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
        self.relate("connect", 'p4-r1-1', 'p5-r1-3')
        self.relate("connect", 'p4-r1-4', 'p5-r1-1')
        self.relate("connect", 'p4-r1-5', 'p5-r1-1')
