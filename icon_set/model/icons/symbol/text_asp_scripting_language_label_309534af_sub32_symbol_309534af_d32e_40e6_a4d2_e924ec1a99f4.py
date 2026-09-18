"""Independent 32px profile of text-asp-scripting-language-label-309534af.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '309534af-d32e-40e6-a4d2-e924ec1a99f4'
SOURCE_PATH = 'icon_set/dist/text32/text-asp-scripting-language-label-309534af.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('309534af-d32e-40e6-a4d2-e924ec1a99f4', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/asp (text)_309534af-d32e-40e6-a4d2-e924ec1a99f4.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-asp-scripting-language-label-309534af',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-s-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = 'b17cea440ae74160482074bec8f5d188c19baa3e4359737374542116ae0061a6'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-asp-scripting-language-label-309534af-sub32-symbol'
    related_origin_icon_id = 'text-asp-scripting-language-label-309534af-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-asp-scripting-language-label-309534af-sub32'
    counterpart_icon_id = 'text-asp-scripting-language-label-309534af-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 78
    text_ink_bounds = (0.0, 0.0, 78.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (57, 30), (57, 2))
        self.add_line('p1-r1-2', (57, 2), (67, 2))
        self.add_bezier('p1-r1-3', (67, 2), ((73, 2), (76, 6), (76, 9)))
        self.add_bezier('p1-r1-4', (76, 9), ((76, 13), (73, 17), (67, 17)))
        self.add_line('p1-r1-5', (67, 17), (57, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (48, 6), ((47, 3), (44, 2), (41, 2)))
        self.add_bezier('p2-r1-2', (41, 2), ((37, 2), (32, 4), (31, 9)))
        self.add_bezier('p2-r1-3', (31, 9), ((31, 9), (31, 9), (31, 10)))
        self.add_bezier('p2-r1-4', (31, 10), ((31, 17), (48, 13), (49, 22)))
        self.add_bezier('p2-r1-5', (49, 22), ((49, 22), (49, 22), (49, 23)))
        self.add_bezier('p2-r1-6', (49, 23), ((49, 28), (45, 30), (40, 30)))
        self.add_bezier('p2-r1-7', (40, 30), ((36, 30), (32, 29), (31, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (2, 30), (11, 3))
        self.add_bezier('p3-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p3-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p3-r1-4', (14, 3), (23, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (6, 18), (19, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
