"""Independent 32px profile of text-java-programming-language-text-3679e6b1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '3679e6b1-f8a5-4ea0-a14d-1131e2498789'
SOURCE_PATH = 'icon_set/dist/text32/text-java-programming-language-text-3679e6b1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3679e6b1-f8a5-4ea0-a14d-1131e2498789', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/JAVA (text)_3679e6b1-f8a5-4ea0-a14d-1131e2498789.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-java-programming-language-text-3679e6b1',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-j-uppercase', 'letter-a-uppercase', 'letter-v-uppercase', 'letter-a-uppercase')
REFERENCE_EXPORT_SHA256 = '79b055ac2e81d22579484c87557f4156ac8e39c57082d315ea91d9c2e8f4caa3'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-java-programming-language-text-3679e6b1-sub32-symbol'
    related_origin_icon_id = 'text-java-programming-language-text-3679e6b1-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-java-programming-language-text-3679e6b1-sub32'
    counterpart_icon_id = 'text-java-programming-language-text-3679e6b1-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 106
    text_ink_bounds = (0.0, 0.0, 106.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (83, 30), (93, 3))
        self.add_bezier('p1-r1-2', (93, 3), ((93, 2.3333333333333335), (93.33333333333333, 2), (94, 2)))
        self.add_bezier('p1-r1-3', (94, 2), ((94, 2), (94.33333333333333, 2.3333333333333335), (95, 3)))
        self.add_line('p1-r1-4', (95, 3), (104, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (87, 18), (100, 18))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (54, 2), (63, 28))
        self.add_bezier('p3-r1-2', (63, 28), ((63.666666666666664, 29.333333333333332), (64.33333333333333, 30), (65, 30)))
        self.add_bezier('p3-r1-3', (65, 30), ((65.66666666666667, 30), (66, 29.333333333333332), (66, 28)))
        self.add_line('p3-r1-4', (66, 28), (76, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (26, 30), (35, 3))
        self.add_bezier('p4-r1-2', (35, 3), ((35, 2.3333333333333335), (35.333333333333336, 2), (36, 2)))
        self.add_bezier('p4-r1-3', (36, 2), ((36.666666666666664, 2), (37, 2.3333333333333335), (37, 3)))
        self.add_line('p4-r1-4', (37, 3), (46, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', closed=False)
        self.add_line('p5-r1-1', (30, 18), (42, 18))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (6, 2), (18, 2))
        self.add_line('p6-r1-2', (18, 2), (18, 21))
        self.add_bezier('p6-r1-3', (18, 21), ((18, 27), (14, 30), (9, 30)))
        self.add_bezier('p6-r1-4', (9, 30), ((6, 30), (3, 28), (2, 24)))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', closed=False)
