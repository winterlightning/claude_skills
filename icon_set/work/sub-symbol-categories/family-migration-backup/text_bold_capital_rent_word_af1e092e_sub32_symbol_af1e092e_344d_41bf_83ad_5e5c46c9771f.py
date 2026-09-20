# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-bold-capital-rent-word-af1e092e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'af1e092e-344d-41bf-83ad-5e5c46c9771f'
SOURCE_PATH = 'icon_set/dist/text32/text-bold-capital-rent-word-af1e092e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('af1e092e-344d-41bf-83ad-5e5c46c9771f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/rent (text)_af1e092e-344d-41bf-83ad-5e5c46c9771f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-bold-capital-rent-word-af1e092e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-e-uppercase', 'letter-n-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = 'a776338cf963f1ac32fbd09b047366a6766912726a4ee592afc28af03240f7ec'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-bold-capital-rent-word-af1e092e-sub32-symbol'
    variant_of = 'text-bold-capital-rent-word-af1e092e-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-bold-capital-rent-word-af1e092e-sub32'
    counterpart_icon_id = 'text-bold-capital-rent-word-af1e092e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 107
    text_ink_bounds = (0.0, 0.0, 107.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (83, 2), (105, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (94, 2), (94, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (55, 30), (55, 2))
        self.add_line('p3-r1-2', (55, 2), (75, 30))
        self.add_line('p3-r1-3', (75, 30), (75, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (47, 2), (30, 2))
        self.add_line('p4-r1-2', (30, 2), (30, 30))
        self.add_line('p4-r1-3', (30, 30), (47, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (30, 16), (44, 16))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 30), (2, 2))
        self.add_line('p6-r1-2', (2, 2), (12, 2))
        self.add_bezier('p6-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p6-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p6-r1-5', (12, 17), (2, 17))
        self.add_contour('path-6-1', 'p6-r1-1', 'p6-r1-2', 'p6-r1-3', 'p6-r1-4', 'p6-r1-5', closed=False)
        self.add_line('p7-r1-1', (12, 17), (22, 30))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
        self.relate('connect', 'p6-r1-4', 'p7-r1-1')
        self.relate('connect', 'p6-r1-5', 'p7-r1-1')
