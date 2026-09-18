"""Independent 32px profile of text-maximum-value-label-4b12edd2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '4b12edd2-eaa6-4637-8b66-5e60cd53e0ed'
SOURCE_PATH = 'icon_set/dist/text32/text-maximum-value-label-4b12edd2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4b12edd2-eaa6-4637-8b66-5e60cd53e0ed', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/max (text)_4b12edd2-eaa6-4637-8b66-5e60cd53e0ed.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-maximum-value-label-4b12edd2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-a-uppercase', 'letter-x-uppercase')
REFERENCE_EXPORT_SHA256 = 'f84f23d7a9eac6f0a95824594f43bd73ae9f85000f5fab747681dde6a55f3647'

class Drawing(TextSub32):
    icon_id = 'text-maximum-value-label-4b12edd2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 87
    text_ink_bounds = (0.0, 0.0, 87.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (65, 2), (85, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (85, 2), (65, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (36, 30), (46, 3))
        self.add_bezier('p3-r1-2', (46, 3), ((46, 2.3333333333333335), (46.333333333333336, 2), (47, 2)))
        self.add_bezier('p3-r1-3', (47, 2), ((47, 2), (47.333333333333336, 2.3333333333333335), (48, 3)))
        self.add_line('p3-r1-4', (48, 3), (57, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (40, 18), (53, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (15, 20))
        self.add_line('p5-r1-3', (15, 20), (28, 2))
        self.add_line('p5-r1-4', (28, 2), (28, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
