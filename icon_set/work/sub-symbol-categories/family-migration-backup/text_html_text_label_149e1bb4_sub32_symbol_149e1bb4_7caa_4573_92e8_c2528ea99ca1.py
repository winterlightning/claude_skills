# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-html-text-label-149e1bb4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '149e1bb4-7caa-4573-92e8-c2528ea99ca1'
SOURCE_PATH = 'icon_set/dist/text32/text-html-text-label-149e1bb4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('149e1bb4-7caa-4573-92e8-c2528ea99ca1', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/html (text)_149e1bb4-7caa-4573-92e8-c2528ea99ca1.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-html-text-label-149e1bb4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-t-uppercase', 'letter-m-uppercase', 'letter-l-uppercase')
REFERENCE_EXPORT_SHA256 = 'd477a4a303d3b7100be7fbe03fe31251250ddd398c07604e20ed3d5fc8ec735b'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-html-text-label-149e1bb4-sub32-symbol'
    variant_of = 'text-html-text-label-149e1bb4-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-html-text-label-149e1bb4-sub32'
    counterpart_icon_id = 'text-html-text-label-149e1bb4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 112
    text_ink_bounds = (0.0, 0.0, 112.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (94, 2), (94, 30))
        self.add_line('p1-r1-2', (94, 30), (110, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (60, 30), (60, 2))
        self.add_line('p2-r1-2', (60, 2), (73, 20))
        self.add_line('p2-r1-3', (73, 20), (86, 2))
        self.add_line('p2-r1-4', (86, 2), (86, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (30, 2), (52, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (41, 2), (41, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (2, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (22, 2), (22, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (2, 16), (22, 16))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
