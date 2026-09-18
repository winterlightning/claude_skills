"""Independent 32px profile of text-fat-text-symbol-dded3d36.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'dded3d36-d09a-4abe-8e46-8acd6d60897d'
SOURCE_PATH = 'icon_set/dist/text32/text-fat-text-symbol-dded3d36.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('dded3d36-d09a-4abe-8e46-8acd6d60897d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/fat (text)_dded3d36-d09a-4abe-8e46-8acd6d60897d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-fat-text-symbol-dded3d36',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-a-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = '6d3069324b3b8a2e260c9cdf4111f97faefb3b4b4a72b2f6b3afc7d2eb0234ec'

class Drawing(TextSub32):
    icon_id = 'text-fat-text-symbol-dded3d36-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 79
    text_ink_bounds = (0.0, 0.0, 79.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (56, 2), (77, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (67, 2), (67, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (27, 30), (36, 3))
        self.add_bezier('p3-r1-2', (36, 3), ((36.666666666666664, 2.3333333333333335), (37, 2), (37, 2)))
        self.add_bezier('p3-r1-3', (37, 2), ((37.666666666666664, 2), (38.333333333333336, 2.3333333333333335), (39, 3)))
        self.add_line('p3-r1-4', (39, 3), (48, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (31, 18), (44, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (19, 2), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (2, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', closed=False)
        self.add_line('p6-r1-1', (2, 16), (16, 16))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
