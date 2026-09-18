"""Independent 32px profile of text-avi-video-file-format-2d337092.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '2d337092-378f-4348-8ecb-887c43d4dcb8'
SOURCE_PATH = 'icon_set/dist/text32/text-avi-video-file-format-2d337092.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2d337092-378f-4348-8ecb-887c43d4dcb8', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/avi (text)_2d337092-378f-4348-8ecb-887c43d4dcb8.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-avi-video-file-format-2d337092',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-v-uppercase', 'letter-i-uppercase')
REFERENCE_EXPORT_SHA256 = '315540e15e7a351d0a8e073337e0b38675189abb2a94f17b5e5215e95adfabd9'

class Drawing(TextSub32):
    icon_id = 'text-avi-video-file-format-2d337092-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 71
    text_ink_bounds = (0.0, 0.0, 71.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (60, 2), (69, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (64, 2), (64, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (60, 30), (69, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (31, 2), (40, 28))
        self.add_bezier('p4-r1-2', (40, 28), ((40.666666666666664, 29.333333333333332), (41, 30), (41, 30)))
        self.add_bezier('p4-r1-3', (41, 30), ((41.666666666666664, 30), (42.333333333333336, 29.333333333333332), (43, 28)))
        self.add_line('p4-r1-4', (43, 28), (52, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (2, 30), (11, 3))
        self.add_bezier('p5-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p5-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p5-r1-4', (14, 3), (23, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_line('p6-r1-1', (6, 18), (19, 18))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
