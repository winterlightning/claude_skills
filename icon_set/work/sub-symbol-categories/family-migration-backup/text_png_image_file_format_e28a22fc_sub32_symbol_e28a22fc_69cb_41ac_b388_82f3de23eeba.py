# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-png-image-file-format-e28a22fc.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'e28a22fc-69cb-41ac-b388-82f3de23eeba'
SOURCE_PATH = 'icon_set/dist/text32/text-png-image-file-format-e28a22fc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e28a22fc-69cb-41ac-b388-82f3de23eeba', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/png (text)_e28a22fc-69cb-41ac-b388-82f3de23eeba.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-png-image-file-format-e28a22fc',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-n-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = '3d506da12246d656a5554125edf7bd2c32c13c8af879b7a837fa023fb3a1abcf'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-png-image-file-format-e28a22fc-sub32-symbol'
    variant_of = 'text-png-image-file-format-e28a22fc-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-png-image-file-format-e28a22fc-sub32'
    counterpart_icon_id = 'text-png-image-file-format-e28a22fc-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 80
    text_ink_bounds = (0.0, 0.0, 80.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (75, 6), ((73, 4), (71, 2), (68, 2)))
        self.add_bezier('p1-r1-2', (68, 2), ((63, 2), (57, 9), (57, 17)))
        self.add_bezier('p1-r1-3', (57, 17), ((57, 18), (58, 20), (58, 21)))
        self.add_bezier('p1-r1-4', (58, 21), ((60, 27), (63, 29), (67, 29)))
        self.add_bezier('p1-r1-5', (67, 29), ((72, 29), (78, 24), (78, 16)))
        self.add_line('p1-r1-6', (78, 16), (70, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (29, 30), (29, 2))
        self.add_line('p2-r1-2', (29, 2), (50, 30))
        self.add_line('p2-r1-3', (50, 30), (50, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (12, 2))
        self.add_bezier('p3-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('p3-r1-4', (21, 9), ((21, 13), (18, 17), (12, 17)))
        self.add_line('p3-r1-5', (12, 17), (2, 17))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
