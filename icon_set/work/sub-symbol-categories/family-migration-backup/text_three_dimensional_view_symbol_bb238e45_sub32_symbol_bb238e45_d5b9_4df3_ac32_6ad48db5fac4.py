# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-three-dimensional-view-symbol-bb238e45.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'bb238e45-d5b9-4df3-ac32-6ad48db5fac4'
SOURCE_PATH = 'icon_set/dist/text32/text-three-dimensional-view-symbol-bb238e45.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bb238e45-d5b9-4df3-ac32-6ad48db5fac4', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/3D (text)_bb238e45-d5b9-4df3-ac32-6ad48db5fac4.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-three-dimensional-view-symbol-bb238e45',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-3', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '40e8a4930e92c1d413291e7a7cb884f62578d05c6fd4b2d051fa3442839186e4'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-three-dimensional-view-symbol-bb238e45-sub32-symbol'
    variant_of = 'text-three-dimensional-view-symbol-bb238e45-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-three-dimensional-view-symbol-bb238e45-sub32'
    counterpart_icon_id = 'text-three-dimensional-view-symbol-bb238e45-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 49
    text_ink_bounds = (0.0, 0.0, 49.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (28, 2), (36, 2))
        self.add_bezier('p1-r1-2', (36, 2), ((44, 2), (47, 9), (47, 16)))
        self.add_bezier('p1-r1-3', (47, 16), ((47, 23), (44, 30), (36, 30)))
        self.add_line('p1-r1-4', (36, 30), (28, 30))
        self.add_line('p1-r1-5', (28, 30), (28, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 2), (13, 2))
        self.add_bezier('p2-r1-2', (13, 2), ((17, 2), (20, 5), (20, 9)))
        self.add_bezier('p2-r1-3', (20, 9), ((20, 13), (17, 16), (13, 16)))
        self.add_line('p2-r1-4', (13, 16), (9, 16))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (10, 16), (13, 16))
        self.add_bezier('p3-r1-2', (13, 16), ((17, 16), (20, 19), (20, 23)))
        self.add_bezier('p3-r1-3', (20, 23), ((20, 27), (17, 30), (13, 30)))
        self.add_line('p3-r1-4', (13, 30), (2, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.relate('connect', 'p2-r1-3', 'p3-r1-1')
        self.relate('connect', 'p2-r1-3', 'p3-r1-2')
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
        self.relate('connect', 'p2-r1-4', 'p3-r1-2')
