# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-dat-file-format-icon-31feea69.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '31feea69-61c1-4251-bf45-f3338a7ae5c0'
SOURCE_PATH = 'icon_set/dist/text32/text-dat-file-format-icon-31feea69.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('31feea69-61c1-4251-bf45-f3338a7ae5c0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/dat (text)_31feea69-61c1-4251-bf45-f3338a7ae5c0.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-dat-file-format-icon-31feea69',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-a-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = 'd2c41fc36be82571c98ce3d364b9a9e1656ae0a6bfe993c92b7b3d6c833278ae'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-dat-file-format-icon-31feea69-sub32-symbol'
    variant_of = 'text-dat-file-format-icon-31feea69-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-dat-file-format-icon-31feea69-sub32'
    counterpart_icon_id = 'text-dat-file-format-icon-31feea69-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 82
    text_ink_bounds = (0.0, 0.0, 82.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (58, 2), (80, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (69, 2), (69, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (29, 30), (39, 3))
        self.add_bezier('p3-r1-2', (39, 3), ((39, 2.3333333333333335), (39.333333333333336, 2), (40, 2)))
        self.add_bezier('p3-r1-3', (40, 2), ((40, 2), (40.333333333333336, 2.3333333333333335), (41, 3)))
        self.add_line('p3-r1-4', (41, 3), (50, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (33, 18), (46, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (10, 2))
        self.add_bezier('p5-r1-2', (10, 2), ((18, 2), (21, 9), (21, 16)))
        self.add_bezier('p5-r1-3', (21, 16), ((21, 23), (18, 30), (10, 30)))
        self.add_line('p5-r1-4', (10, 30), (2, 30))
        self.add_line('p5-r1-5', (2, 30), (2, 2))
        self.add_contour('path-5-1', 'p5-r1-1', 'p5-r1-2', 'p5-r1-3', 'p5-r1-4', 'p5-r1-5', closed=False)
