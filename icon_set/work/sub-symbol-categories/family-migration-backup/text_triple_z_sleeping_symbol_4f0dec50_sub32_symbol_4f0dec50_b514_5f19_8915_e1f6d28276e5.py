# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-triple-z-sleeping-symbol-4f0dec50.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '4f0dec50-b514-5f19-8915-e1f6d28276e5'
SOURCE_PATH = 'icon_set/dist/text32/text-triple-z-sleeping-symbol-4f0dec50.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4f0dec50-b514-5f19-8915-e1f6d28276e5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/sleep zzz_4f0dec50-b514-5f19-8915-e1f6d28276e5.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-triple-z-sleeping-symbol-4f0dec50',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-z-uppercase', 'letter-z-uppercase', 'letter-z-uppercase')
REFERENCE_EXPORT_SHA256 = 'df25efcbefcedc6b907e08266422a638f3ab7cca6ccbd77c46a5f3a5442427b2'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-triple-z-sleeping-symbol-4f0dec50-sub32-symbol'
    variant_of = 'text-triple-z-sleeping-symbol-4f0dec50-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-triple-z-sleeping-symbol-4f0dec50-sub32'
    counterpart_icon_id = 'text-triple-z-sleeping-symbol-4f0dec50-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 99
    text_ink_bounds = (0.0, 0.0, 98.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (79, 2), (95, 2))
        self.add_bezier('p1-r1-2', (95, 2), ((95.66666666666667, 2), (96, 2.3333333333333335), (96, 3)))
        self.add_bezier('p1-r1-3', (96, 3), ((96, 3), (96, 3.3333333333333335), (96, 4)))
        self.add_line('p1-r1-4', (96, 4), (79, 28))
        self.add_bezier('p1-r1-5', (79, 28), ((79, 28.666666666666668), (79, 29), (79, 29)))
        self.add_bezier('p1-r1-6', (79, 29), ((79, 29.666666666666668), (79.33333333333333, 30), (80, 30)))
        self.add_line('p1-r1-7', (80, 30), (96, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (41, 2), (57, 2))
        self.add_bezier('p2-r1-2', (57, 2), ((57.666666666666664, 2), (58, 2.3333333333333335), (58, 3)))
        self.add_bezier('p2-r1-3', (58, 3), ((58, 3), (57.666666666666664, 3.3333333333333335), (57, 4)))
        self.add_line('p2-r1-4', (57, 4), (41, 28))
        self.add_bezier('p2-r1-5', (41, 28), ((40.333333333333336, 28.666666666666668), (40, 29), (40, 29)))
        self.add_bezier('p2-r1-6', (40, 29), ((40, 29.666666666666668), (40.333333333333336, 30), (41, 30)))
        self.add_line('p2-r1-7', (41, 30), (58, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (2, 2), (18, 2))
        self.add_bezier('p3-r1-2', (18, 2), ((18.666666666666668, 2), (19, 2.3333333333333335), (19, 3)))
        self.add_bezier('p3-r1-3', (19, 3), ((19, 3), (19, 3.3333333333333335), (19, 4)))
        self.add_line('p3-r1-4', (19, 4), (2, 28))
        self.add_bezier('p3-r1-5', (2, 28), ((2, 28.666666666666668), (2, 29), (2, 29)))
        self.add_bezier('p3-r1-6', (2, 29), ((2, 29.666666666666668), (2.3333333333333335, 30), (3, 30)))
        self.add_line('p3-r1-7', (3, 30), (19, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
