# Independent container symbol; edit separately from linked side sub-icon.
"""Independent 32px profile of text-xls-spreadsheet-file-format-537c3e64.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '537c3e64-2125-4115-80ac-862f539aecc8'
SOURCE_PATH = 'icon_set/dist/text32/text-xls-spreadsheet-file-format-537c3e64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('537c3e64-2125-4115-80ac-862f539aecc8', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/xls (text)_537c3e64-2125-4115-80ac-862f539aecc8.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-xls-spreadsheet-file-format-537c3e64',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-x-uppercase', 'letter-l-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = '6c33c74233526c8f6e9b72d866a79817b3966836a1816d79632e6f2f1effe7ad'

class DrawingContainerSymbol(TextSub32):
    icon_id = 'text-xls-spreadsheet-file-format-537c3e64-sub32-symbol'
    variant_of = 'text-xls-spreadsheet-file-format-537c3e64-sub32'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/text-xls-spreadsheet-file-format-537c3e64-sub32'
    counterpart_icon_id = 'text-xls-spreadsheet-file-format-537c3e64-sub32'
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
        self.add_line('p2-r1-1', (30, 2), (30, 30))
        self.add_line('p2-r1-2', (30, 30), (46, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_line('p3-r1-1', (2, 2), (22, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (22, 2), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
