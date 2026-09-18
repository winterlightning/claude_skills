"""Independent 32px profile of text-adobe-indesign-document-file-f5ea5b1f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'f5ea5b1f-a0c0-4aab-b396-16942d8b27ce'
SOURCE_PATH = 'icon_set/dist/text32/text-adobe-indesign-document-file-f5ea5b1f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f5ea5b1f-a0c0-4aab-b396-16942d8b27ce', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/indd (text)_f5ea5b1f-a0c0-4aab-b396-16942d8b27ce.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-adobe-indesign-document-file-f5ea5b1f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-i-uppercase', 'letter-n-uppercase', 'letter-d-uppercase', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = '0ca1b4a0da39e8dc6429562113bd3b4d61d82e7a7c5a550d0c3f80e3bce97dec'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-adobe-indesign-document-file-f5ea5b1f-sub32-symbol'
    related_origin_icon_id = 'text-adobe-indesign-document-file-f5ea5b1f-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-adobe-indesign-document-file-f5ea5b1f-sub32'
    counterpart_icon_id = 'text-adobe-indesign-document-file-f5ea5b1f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 96
    text_ink_bounds = (0.0, 0.0, 96.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (75, 2), (82, 2))
        self.add_bezier('p1-r1-2', (82, 2), ((90, 2), (94, 9), (94, 16)))
        self.add_bezier('p1-r1-3', (94, 16), ((94, 23), (90, 30), (82, 30)))
        self.add_line('p1-r1-4', (82, 30), (75, 30))
        self.add_line('p1-r1-5', (75, 30), (75, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (47, 2), (55, 2))
        self.add_bezier('p2-r1-2', (55, 2), ((63, 2), (67, 9), (67, 16)))
        self.add_bezier('p2-r1-3', (67, 16), ((67, 23), (63, 30), (55, 30)))
        self.add_line('p2-r1-4', (55, 30), (47, 30))
        self.add_line('p2-r1-5', (47, 30), (47, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (19, 30), (19, 2))
        self.add_line('p3-r1-2', (19, 2), (39, 30))
        self.add_line('p3-r1-3', (39, 30), (39, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 2), (11, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (7, 2), (7, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 30), (11, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
