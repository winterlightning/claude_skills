# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-bmp-file-format-def3f5b4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'def3f5b4-965a-491a-aafa-f539a425bff2'
SOURCE_PATH = 'icon_set/dist/text32/text-bmp-file-format-def3f5b4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('def3f5b4-965a-491a-aafa-f539a425bff2', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/bmp (text)_def3f5b4-965a-491a-aafa-f539a425bff2.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-bmp-file-format-def3f5b4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-b-uppercase', 'letter-m-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = '8e3a0a6d9bc6888008de710a5622c9b40425c934c396e05d862dbe85cbcbcf7e'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-bmp-file-format-def3f5b4-sub32-symbol'
    variant_of = 'text-bmp-file-format-def3f5b4-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-bmp-file-format-def3f5b4-sub32'
    counterpart_icon_id = 'text-bmp-file-format-def3f5b4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 84
    text_ink_bounds = (0.0, 0.0, 84.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (63, 30), (63, 2))
        self.add_line('p1-r1-2', (63, 2), (73, 2))
        self.add_bezier('p1-r1-3', (73, 2), ((79, 2), (82, 6), (82, 9)))
        self.add_bezier('p1-r1-4', (82, 9), ((82, 13), (79, 17), (73, 17)))
        self.add_line('p1-r1-5', (73, 17), (63, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (29, 30), (29, 2))
        self.add_line('p2-r1-2', (29, 2), (42, 20))
        self.add_line('p2-r1-3', (42, 20), (55, 2))
        self.add_line('p2-r1-4', (55, 2), (55, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (11, 2))
        self.add_bezier('p3-r1-3', (11, 2), ((17, 2), (20, 6), (20, 9)))
        self.add_bezier('p3-r1-4', (20, 9), ((20, 12), (17, 16), (11, 16)))
        self.add_line('p3-r1-5', (11, 16), (2, 16))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
        self.add_bezier('p4-r1-1', (11, 16), ((18, 16), (21, 20), (21, 23)))
        self.add_bezier('p4-r1-2', (21, 23), ((21, 26), (18, 30), (11, 30)))
        self.add_line('p4-r1-3', (11, 30), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate('connect', 'p3-r1-1', 'p4-r1-3')
        self.relate('connect', 'p3-r1-4', 'p4-r1-1')
        self.relate('connect', 'p3-r1-5', 'p4-r1-1')
