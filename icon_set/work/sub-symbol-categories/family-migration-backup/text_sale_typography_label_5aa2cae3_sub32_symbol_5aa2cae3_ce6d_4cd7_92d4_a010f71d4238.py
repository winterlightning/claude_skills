# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-sale-typography-label-5aa2cae3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '5aa2cae3-ce6d-4cd7-92d4-a010f71d4238'
SOURCE_PATH = 'icon_set/dist/text32/text-sale-typography-label-5aa2cae3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5aa2cae3-ce6d-4cd7-92d4-a010f71d4238', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/sale (text)_5aa2cae3-ce6d-4cd7-92d4-a010f71d4238.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-sale-typography-label-5aa2cae3',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-a-uppercase', 'letter-l-uppercase', 'letter-e-uppercase')
REFERENCE_EXPORT_SHA256 = '3f210b9ff55bf06a6929a1b9caa6c5e2080923d708824f27a4c3e77b589fa155'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-sale-typography-label-5aa2cae3-sub32-symbol'
    variant_of = 'text-sale-typography-label-5aa2cae3-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-sale-typography-label-5aa2cae3-sub32'
    counterpart_icon_id = 'text-sale-typography-label-5aa2cae3-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 100
    text_ink_bounds = (0.0, 0.0, 100.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (98, 2), (81, 2))
        self.add_line('p1-r1-2', (81, 2), (81, 30))
        self.add_line('p1-r1-3', (81, 30), (98, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (81, 16), (95, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (57, 2), (57, 30))
        self.add_line('p3-r1-2', (57, 30), (73, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (28, 30), (38, 3))
        self.add_bezier('p4-r1-2', (38, 3), ((38, 2.3333333333333335), (38.333333333333336, 2), (39, 2)))
        self.add_bezier('p4-r1-3', (39, 2), ((39, 2), (39.333333333333336, 2.3333333333333335), (40, 3)))
        self.add_line('p4-r1-4', (40, 3), (49, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (32, 18), (45, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_bezier('p6-r1-1', (20, 6), ((19, 3), (15, 2), (12, 2)))
        self.add_bezier('p6-r1-2', (12, 2), ((8, 2), (4, 4), (3, 9)))
        self.add_bezier('p6-r1-3', (3, 9), ((3, 9), (3, 9), (3, 10)))
        self.add_bezier('p6-r1-4', (3, 10), ((3, 17), (20, 13), (20, 22)))
        self.add_bezier('p6-r1-5', (20, 22), ((20, 22), (20, 22), (20, 23)))
        self.add_bezier('p6-r1-6', (20, 23), ((20, 28), (16, 30), (11, 30)))
        self.add_bezier('p6-r1-7', (11, 30), ((7, 30), (4, 29), (2, 26)))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', 'p6-r1-6', 'p6-r1-7', closed=False)
