"""Independent 32px profile of text-eps-vector-file-format-006d9246.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '006d9246-2e6f-4b96-b509-805f33a778d2'
SOURCE_PATH = 'icon_set/dist/text32/text-eps-vector-file-format-006d9246.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('006d9246-2e6f-4b96-b509-805f33a778d2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/eps (text)_006d9246-2e6f-4b96-b509-805f33a778d2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-eps-vector-file-format-006d9246',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-e-uppercase', 'letter-p-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '84019554684cfc0c696d8b7af930da4cd014ee5ba7d28be8c56b28a7c0a8193b'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-eps-vector-file-format-006d9246-sub32-symbol'
    related_origin_icon_id = 'text-eps-vector-file-format-006d9246-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-eps-vector-file-format-006d9246-sub32'
    counterpart_icon_id = 'text-eps-vector-file-format-006d9246-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 75
    text_ink_bounds = (0.0, 0.0, 75.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (72, 6), ((71, 3), (68, 2), (64, 2)))
        self.add_bezier('p1-r1-2', (64, 2), ((60, 2), (56, 4), (55, 9)))
        self.add_bezier('p1-r1-3', (55, 9), ((55, 9), (55, 9), (55, 10)))
        self.add_bezier('p1-r1-4', (55, 10), ((55, 17), (72, 13), (73, 22)))
        self.add_bezier('p1-r1-5', (73, 22), ((73, 22), (73, 22), (73, 23)))
        self.add_bezier('p1-r1-6', (73, 23), ((73, 28), (68, 30), (63, 30)))
        self.add_bezier('p1-r1-7', (63, 30), ((60, 30), (56, 29), (54, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (27, 30), (27, 2))
        self.add_line('p2-r1-2', (27, 2), (37, 2))
        self.add_bezier('p2-r1-3', (37, 2), ((43, 2), (46, 6), (46, 9)))
        self.add_bezier('p2-r1-4', (46, 9), ((46, 13), (43, 17), (37, 17)))
        self.add_line('p2-r1-5', (37, 17), (27, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (19, 2), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (2, 30))
        self.add_line('p3-r1-3', (2, 30), (19, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 16), (16, 16))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
