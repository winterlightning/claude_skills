"""Independent 32px profile of text-svg-file-format-a5e635a2.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'a5e635a2-0920-48ba-9eea-82070fddd821'
SOURCE_PATH = 'icon_set/dist/text32/text-svg-file-format-a5e635a2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a5e635a2-0920-48ba-9eea-82070fddd821', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/svg (text)_a5e635a2-0920-48ba-9eea-82070fddd821.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-svg-file-format-a5e635a2',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-v-uppercase', 'letter-g-uppercase')
REFERENCE_EXPORT_SHA256 = 'f1bb94f357763ace7bcdbe94200623c2015c83fcadb116bb76879ee6a55981e4'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-svg-file-format-a5e635a2-sub32-symbol'
    related_origin_icon_id = 'text-svg-file-format-a5e635a2-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-svg-file-format-a5e635a2-sub32'
    counterpart_icon_id = 'text-svg-file-format-a5e635a2-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 80
    text_ink_bounds = (0.0, 0.0, 80.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (75, 6), ((73, 4), (70, 2), (68, 2)))
        self.add_bezier('p1-r1-2', (68, 2), ((63, 2), (57, 9), (57, 17)))
        self.add_bezier('p1-r1-3', (57, 17), ((57, 18), (58, 20), (58, 21)))
        self.add_bezier('p1-r1-4', (58, 21), ((60, 27), (63, 29), (67, 29)))
        self.add_bezier('p1-r1-5', (67, 29), ((72, 29), (78, 24), (78, 16)))
        self.add_line('p1-r1-6', (78, 16), (70, 16))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_line('p2-r1-1', (28, 2), (37, 28))
        self.add_bezier('p2-r1-2', (37, 28), ((37.666666666666664, 29.333333333333332), (38.333333333333336, 30), (39, 30)))
        self.add_bezier('p2-r1-3', (39, 30), ((39.666666666666664, 30), (40, 29.333333333333332), (40, 28)))
        self.add_line('p2-r1-4', (40, 28), (49, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (20, 6), ((19, 3), (15, 2), (12, 2)))
        self.add_bezier('p3-r1-2', (12, 2), ((8, 2), (4, 4), (3, 9)))
        self.add_bezier('p3-r1-3', (3, 9), ((3, 9), (3, 9), (3, 10)))
        self.add_bezier('p3-r1-4', (3, 10), ((3, 17), (20, 13), (20, 22)))
        self.add_bezier('p3-r1-5', (20, 22), ((20, 22), (20, 22), (20, 23)))
        self.add_bezier('p3-r1-6', (20, 23), ((20, 28), (16, 30), (11, 30)))
        self.add_bezier('p3-r1-7', (11, 30), ((7, 30), (4, 29), (2, 26)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
