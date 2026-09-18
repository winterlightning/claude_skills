"""Independent 32px profile of text-android-package-application-label-23d4a745.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '23d4a745-8534-4293-82d5-27b5b5626af4'
SOURCE_PATH = 'icon_set/dist/text32/text-android-package-application-label-23d4a745.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('23d4a745-8534-4293-82d5-27b5b5626af4', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/APK (text)_23d4a745-8534-4293-82d5-27b5b5626af4.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-android-package-application-label-23d4a745',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-p-uppercase', 'letter-k-uppercase')
REFERENCE_EXPORT_SHA256 = '96525b4bd98c628a880223d119e34f102f3b9dbe54ecb32e902f20ffe0eb43d7'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-android-package-application-label-23d4a745-sub32-symbol'
    related_origin_icon_id = 'text-android-package-application-label-23d4a745-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-android-package-application-label-23d4a745-sub32'
    counterpart_icon_id = 'text-android-package-application-label-23d4a745-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 79
    text_ink_bounds = (0.0, 0.0, 79.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (58, 2), (58, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (77, 2), (58, 17))
        self.add_line('p2-r1-2', (58, 17), (77, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (31, 30), (31, 2))
        self.add_line('p3-r1-2', (31, 2), (41, 2))
        self.add_bezier('p3-r1-3', (41, 2), ((47, 2), (50, 6), (50, 9)))
        self.add_bezier('p3-r1-4', (50, 9), ((50, 13), (47, 17), (41, 17)))
        self.add_line('p3-r1-5', (41, 17), (31, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (2, 30), (11, 3))
        self.add_bezier('p4-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p4-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p4-r1-4', (14, 3), (23, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (6, 18), (19, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
