"""Independent 32px profile of text-four-way-bold-text-71e83a5c.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '71e83a5c-ca8f-4fc3-96ff-5a4ac5b09283'
SOURCE_PATH = 'icon_set/dist/text32/text-four-way-bold-text-71e83a5c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('71e83a5c-ca8f-4fc3-96ff-5a4ac5b09283', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/4 way_71e83a5c-ca8f-4fc3-96ff-5a4ac5b09283.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-four-way-bold-text-71e83a5c',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-4', 'letter-w-uppercase', 'letter-a-uppercase', 'letter-y-uppercase')
REFERENCE_EXPORT_SHA256 = '2574c601c4520feabf02a2f79dd8436caf92e4acacb99fc78a919189f73788e1'

class Drawing(TextSub32):
    icon_id = 'text-four-way-bold-text-71e83a5c-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 134
    text_ink_bounds = (0.0, 0.0, 134.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (110, 2), (121, 17))
        self.add_line('p1-r1-2', (121, 17), (132, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (121, 17), (121, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (82, 30), (91, 3))
        self.add_bezier('p3-r1-2', (91, 3), ((91, 2.3333333333333335), (91.33333333333333, 2), (92, 2)))
        self.add_bezier('p3-r1-3', (92, 2), ((92.66666666666667, 2), (93, 2.3333333333333335), (93, 3)))
        self.add_line('p3-r1-4', (93, 3), (102, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (86, 18), (98, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (44, 2), (50, 28))
        self.add_bezier('p5-r1-2', (50, 28), ((50.666666666666664, 29.333333333333332), (51, 30), (51, 30)))
        self.add_bezier('p5-r1-3', (51, 30), ((51, 30), (51.333333333333336, 29.333333333333332), (52, 28)))
        self.add_line('p5-r1-4', (52, 28), (58, 4))
        self.add_bezier('p5-r1-5', (58, 4), ((58, 3.3333333333333335), (58.333333333333336, 3), (59, 3)))
        self.add_bezier('p5-r1-6', (59, 3), ((59, 3), (59.333333333333336, 3.3333333333333335), (60, 4)))
        self.add_line('p5-r1-7', (60, 4), (66, 28))
        self.add_bezier('p5-r1-8', (66, 28), ((66, 29.333333333333332), (66.33333333333333, 30), (67, 30)))
        self.add_bezier('p5-r1-9', (67, 30), ((67, 30), (67, 29.333333333333332), (67, 28)))
        self.add_line('p5-r1-10', (67, 28), (74, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', 'p5-r1-6', 'p5-r1-7', 'p5-r1-8', 'p5-r1-9', 'p5-r1-10', closed=False)
        self.add_line('p6-r1-1', (2, 2), (2, 20))
        self.add_bezier('p6-r1-2', (2, 20), ((2, 20), (2, 20), (3, 20)))
        self.add_line('p6-r1-3', (3, 20), (26, 20))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', closed=False)
        self.add_line('p7-r1-1', (21, 2), (21, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p1-r1-1', 'p2-r1-1')
        self.relate('connect', 'p1-r1-2', 'p2-r1-1')
