# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-psd-file-format-type-f7c89911.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'f7c89911-684e-406a-a7a8-cc975c0bd5d5'
SOURCE_PATH = 'icon_set/dist/text32/text-psd-file-format-type-f7c89911.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f7c89911-684e-406a-a7a8-cc975c0bd5d5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/psd (text)_f7c89911-684e-406a-a7a8-cc975c0bd5d5.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-psd-file-format-type-f7c89911',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-s-uppercase', 'letter-d-uppercase')
REFERENCE_EXPORT_SHA256 = 'e0e06c1ece2245c6ddca002b3cd6dc713bc07bf06a8444996dbefb6190721eee'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-psd-file-format-type-f7c89911-sub32-symbol'
    variant_of = 'text-psd-file-format-type-f7c89911-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-psd-file-format-type-f7c89911-sub32'
    counterpart_icon_id = 'text-psd-file-format-type-f7c89911-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 77
    text_ink_bounds = (0.0, 0.0, 77.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (56, 2), (63, 2))
        self.add_bezier('p1-r1-2', (63, 2), ((71, 2), (75, 9), (75, 16)))
        self.add_bezier('p1-r1-3', (75, 16), ((75, 23), (71, 30), (63, 30)))
        self.add_line('p1-r1-4', (63, 30), (56, 30))
        self.add_line('p1-r1-5', (56, 30), (56, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_bezier('p2-r1-1', (47, 6), ((46, 3), (43, 2), (39, 2)))
        self.add_bezier('p2-r1-2', (39, 2), ((35, 2), (31, 4), (30, 9)))
        self.add_bezier('p2-r1-3', (30, 9), ((30, 9), (30, 9), (30, 10)))
        self.add_bezier('p2-r1-4', (30, 10), ((30, 17), (47, 13), (48, 22)))
        self.add_bezier('p2-r1-5', (48, 22), ((48, 22), (48, 22), (48, 23)))
        self.add_bezier('p2-r1-6', (48, 23), ((48, 28), (43, 30), (38, 30)))
        self.add_bezier('p2-r1-7', (38, 30), ((35, 30), (31, 29), (29, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (12, 2))
        self.add_bezier('p3-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p3-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p3-r1-5', (12, 17), (2, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
