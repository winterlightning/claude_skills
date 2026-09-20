# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-dxf-file-format-symbol-ef7bb64f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'ef7bb64f-2ca6-4de8-80aa-37d95ecbe745'
SOURCE_PATH = 'icon_set/dist/text32/text-dxf-file-format-symbol-ef7bb64f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef7bb64f-2ca6-4de8-80aa-37d95ecbe745', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/dxf (text)_ef7bb64f-2ca6-4de8-80aa-37d95ecbe745.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-dxf-file-format-symbol-ef7bb64f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-x-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = '2645e115a3138228491aa650a5f1adc89dab9ef8c9887e264aa973b68e9626fa'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-dxf-file-format-symbol-ef7bb64f-sub32-symbol'
    variant_of = 'text-dxf-file-format-symbol-ef7bb64f-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-dxf-file-format-symbol-ef7bb64f-sub32'
    counterpart_icon_id = 'text-dxf-file-format-symbol-ef7bb64f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 76
    text_ink_bounds = (0.0, 0.0, 76.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (74, 2), (57, 2))
        self.add_line('p1-r1-2', (57, 2), (57, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (57, 16), (71, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (29, 2), (50, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (50, 2), (29, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (10, 2))
        self.add_bezier('p5-r1-2', (10, 2), ((18, 2), (21, 9), (21, 16)))
        self.add_bezier('p5-r1-3', (21, 16), ((21, 23), (18, 30), (10, 30)))
        self.add_line('p5-r1-4', (10, 30), (2, 30))
        self.add_line('p5-r1-5', (2, 30), (2, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
