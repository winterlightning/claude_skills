"""Independent 32px profile of side-text-77375878.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '77375878-6b26-4a4a-baa4-a1006faf1f47'
SOURCE_PATH = 'icon_set/dist/text32/side-text-77375878.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('77375878-6b26-4a4a-baa4-a1006faf1f47', 'icon_set/dist/gallery/combination-originals/77375878-6b26-4a4a-baa4-a1006faf1f47.svg'),)
PROFILE_SOURCE_KEYS = ('text/side-text-77375878',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-p-uppercase', 'letter-i-uppercase')
REFERENCE_EXPORT_SHA256 = '711f3a0082e0aac40074f7f1c4d6bee0c6b60c029cffe0525b42ac868caeb185'

class Drawing(TextSub32):
    icon_id = 'side-text-77375878-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 68
    text_ink_bounds = (0.0, 0.0, 68.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (57, 2), (66, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (61, 2), (61, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (57, 30), (66, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (30, 30), (30, 2))
        self.add_line('p4-r1-2', (30, 2), (40, 2))
        self.add_bezier('p4-r1-3', (40, 2), ((46, 2), (50, 6), (50, 9)))
        self.add_bezier('p4-r1-4', (50, 9), ((50, 13), (46, 17), (40, 17)))
        self.add_line('p4-r1-5', (40, 17), (30, 17))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.add_line('p5-r1-1', (2, 30), (11, 3))
        self.add_bezier('p5-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p5-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p5-r1-4', (14, 3), (23, 30))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', closed=False)
        self.add_line('p6-r1-1', (6, 18), (19, 18))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
