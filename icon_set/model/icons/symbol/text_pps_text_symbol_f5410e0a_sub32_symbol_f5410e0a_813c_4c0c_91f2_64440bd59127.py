"""Independent 32px profile of text-pps-text-symbol-f5410e0a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'f5410e0a-813c-4c0c-91f2-64440bd59127'
SOURCE_PATH = 'icon_set/dist/text32/text-pps-text-symbol-f5410e0a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f5410e0a-813c-4c0c-91f2-64440bd59127', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/pps (text)_f5410e0a-813c-4c0c-91f2-64440bd59127.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-pps-text-symbol-f5410e0a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-p-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = 'de8936a3c872801ceec7f79ca62bb0f6c00d172a0b158bca090098b604e153e8'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-pps-text-symbol-f5410e0a-sub32-symbol'
    related_origin_icon_id = 'text-pps-text-symbol-f5410e0a-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-pps-text-symbol-f5410e0a-sub32'
    counterpart_icon_id = 'text-pps-text-symbol-f5410e0a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 77
    text_ink_bounds = (0.0, 0.0, 77.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (74, 6), ((73, 3), (70, 2), (66, 2)))
        self.add_bezier('p1-r1-2', (66, 2), ((62, 2), (58, 4), (57, 9)))
        self.add_bezier('p1-r1-3', (57, 9), ((57, 9), (57, 9), (57, 10)))
        self.add_bezier('p1-r1-4', (57, 10), ((57, 17), (74, 13), (75, 22)))
        self.add_bezier('p1-r1-5', (75, 22), ((75, 22), (75, 22), (75, 23)))
        self.add_bezier('p1-r1-6', (75, 23), ((75, 28), (70, 30), (66, 30)))
        self.add_bezier('p1-r1-7', (66, 30), ((62, 30), (58, 29), (57, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_line('p2-r1-1', (29, 30), (29, 2))
        self.add_line('p2-r1-2', (29, 2), (39, 2))
        self.add_bezier('p2-r1-3', (39, 2), ((46, 2), (49, 6), (49, 9)))
        self.add_bezier('p2-r1-4', (49, 9), ((49, 13), (46, 17), (39, 17)))
        self.add_line('p2-r1-5', (39, 17), (29, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (12, 2))
        self.add_bezier('p3-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p3-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p3-r1-5', (12, 17), (2, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
