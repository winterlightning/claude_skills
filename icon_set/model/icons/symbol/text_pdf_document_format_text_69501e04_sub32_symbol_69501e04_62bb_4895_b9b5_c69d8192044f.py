"""Independent 32px profile of text-pdf-document-format-text-69501e04.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '69501e04-62bb-4895-b9b5-c69d8192044f'
SOURCE_PATH = 'icon_set/dist/text32/text-pdf-document-format-text-69501e04.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('69501e04-62bb-4895-b9b5-c69d8192044f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/pdf (text)_69501e04-62bb-4895-b9b5-c69d8192044f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-pdf-document-format-text-69501e04',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-d-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = 'f79ca80d7a63e876bf27be1f7cfd42e276d37af53ecd2418b29a1f5e1d9b309e'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-pdf-document-format-text-69501e04-sub32-symbol'
    related_origin_icon_id = 'text-pdf-document-format-text-69501e04-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-pdf-document-format-text-69501e04-sub32'
    counterpart_icon_id = 'text-pdf-document-format-text-69501e04-sub32'
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
        self.add_line('p3-r1-1', (29, 2), (37, 2))
        self.add_bezier('p3-r1-2', (37, 2), ((45, 2), (49, 9), (49, 16)))
        self.add_bezier('p3-r1-3', (49, 16), ((49, 23), (45, 30), (37, 30)))
        self.add_line('p3-r1-4', (37, 30), (29, 30))
        self.add_line('p3-r1-5', (29, 30), (29, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_line('p4-r1-1', (2, 30), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (12, 2))
        self.add_bezier('p4-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p4-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p4-r1-5', (12, 17), (2, 17))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
