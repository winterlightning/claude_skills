"""Independent 32px profile of text-zip-file-archive-text-d2b9b22c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'd2b9b22c-4c35-4d77-b2fd-13360e555011'
SOURCE_PATH = 'icon_set/dist/text32/text-zip-file-archive-text-d2b9b22c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d2b9b22c-4c35-4d77-b2fd-13360e555011', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/zip (text)_d2b9b22c-4c35-4d77-b2fd-13360e555011.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-zip-file-archive-text-d2b9b22c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-z-uppercase', 'letter-i-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = '74410472cfb86341d8fe90d6c976728276cbae1e03b425311271910d16827dc8'

class Drawing(TextSub32):
    icon_id = 'text-zip-file-archive-text-d2b9b22c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 66
    text_ink_bounds = (0.0, 0.0, 66.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (44, 30), (44, 2))
        self.add_line('p1-r1-2', (44, 2), (54, 2))
        self.add_bezier('p1-r1-3', (54, 2), ((61, 2), (64, 6), (64, 9)))
        self.add_bezier('p1-r1-4', (64, 9), ((64, 13), (61, 17), (54, 17)))
        self.add_line('p1-r1-5', (54, 17), (44, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (27, 2), (37, 2))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (32, 2), (32, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (27, 30), (37, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (18, 2))
        self.add_bezier('p5-r1-2', (18, 2), ((18.666666666666668, 2), (19, 2.3333333333333335), (19, 3)))
        self.add_bezier('p5-r1-3', (19, 3), ((19, 3), (19, 3.3333333333333335), (19, 4)))
        self.add_line('p5-r1-4', (19, 4), (3, 28))
        self.add_bezier('p5-r1-5', (3, 28), ((2.3333333333333335, 28.666666666666668), (2, 29), (2, 29)))
        self.add_bezier('p5-r1-6', (2, 29), ((2, 29.666666666666668), (2.3333333333333335, 30), (3, 30)))
        self.add_line('p5-r1-7', (3, 30), (19, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', 'p5-r1-7', closed=False)
