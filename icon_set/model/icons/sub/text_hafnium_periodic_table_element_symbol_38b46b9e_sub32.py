"""Independent 32px profile of text-hafnium-periodic-table-element-symbol-38b46b9e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '38b46b9e-f697-4b17-95a6-2b7297be8148'
SOURCE_PATH = 'icon_set/dist/text32/text-hafnium-periodic-table-element-symbol-38b46b9e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('38b46b9e-f697-4b17-95a6-2b7297be8148', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/hf (text u)_38b46b9e-f697-4b17-95a6-2b7297be8148.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-hafnium-periodic-table-element-symbol-38b46b9e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-f')
REFERENCE_EXPORT_SHA256 = 'd89945d1a9049272db369322ea2821f19bcd873e6304eec695af65d80c8f710a'

class Drawing(TextSub32):
    icon_id = 'text-hafnium-periodic-table-element-symbol-38b46b9e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 31
    text_ink_bounds = (0.0, 0.0, 31.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (29, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (25, 21), (25, 7))
        self.add_bezier('p2-r1-2', (25, 7), ((25, 5), (27, 3), (29, 3)))
        self.add_line('p2-r1-3', (29, 3), (29, 3))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (22, 8), (27, 8))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 2), (2, 21))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (16, 2), (16, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 12), (16, 12))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
