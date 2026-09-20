# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-php-programming-language-logo-272a7439.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '272a7439-f7fd-4eae-b038-1de7018bcbc1'
SOURCE_PATH = 'icon_set/dist/text32/text-php-programming-language-logo-272a7439.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('272a7439-f7fd-4eae-b038-1de7018bcbc1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/php (text)_272a7439-f7fd-4eae-b038-1de7018bcbc1.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-php-programming-language-logo-272a7439',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-h-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = 'fe9665d95e2417283d4432f4d60d105a00ca834e4d373ca62654af0f0a5d0158'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-php-programming-language-logo-272a7439-sub32-symbol'
    variant_of = 'text-php-programming-language-logo-272a7439-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-php-programming-language-logo-272a7439-sub32'
    counterpart_icon_id = 'text-php-programming-language-logo-272a7439-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 79
    text_ink_bounds = (0.0, 0.0, 79.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (57, 30), (57, 2))
        self.add_line('p1-r1-2', (57, 2), (67, 2))
        self.add_bezier('p1-r1-3', (67, 2), ((74, 2), (77, 6), (77, 9)))
        self.add_bezier('p1-r1-4', (77, 9), ((77, 13), (74, 17), (67, 17)))
        self.add_line('p1-r1-5', (67, 17), (57, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (29, 2), (29, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (50, 2), (50, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (29, 16), (50, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 30), (2, 2))
        self.add_line('p5-r1-2', (2, 2), (12, 2))
        self.add_bezier('p5-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p5-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p5-r1-5', (12, 17), (2, 17))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
