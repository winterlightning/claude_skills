"""Independent 32px profile of text-number-ten-symbol-bb0be6c6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'bb0be6c6-3c34-4162-a998-bb5a6771d625'
SOURCE_PATH = 'icon_set/dist/text32/text-number-ten-symbol-bb0be6c6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bb0be6c6-3c34-4162-a998-bb5a6771d625', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/10 (text)_bb0be6c6-3c34-4162-a998-bb5a6771d625.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-ten-symbol-bb0be6c6',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-1', 'digit-0')
REFERENCE_EXPORT_SHA256 = '3312c101379b508d238a543e58a72f3542c13f61a61876328f54f1664eee4275'

























TYPEFACE_PROFILE = 'v2'
TEXT_TRACKING = 4

class Drawing(TextSub32):
    icon_id = 'text-number-ten-symbol-bb0be6c6-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    sizing_mode = 'text-source-native-v2'
    text_canvas_width = 44
    text_canvas_height = 20
    text_ink_bounds = (2.0, 0.0, 42.0, 20.0)

    def build(self):
        """Source-native uppercase composition for '10'; 4-unit letter spacing."""
        self.add_line('p1-r1-1', (10.4, 18), (10.4, 2.40859))
        self.add_bezier('p1-r1-2', (10.4, 2.40859), ((10.4, 2.18293), (10.2171, 2), (9.99141, 2)))
        self.add_line('p1-r1-3', (9.99141, 2), (4, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p1-r2-1', (4.85714, 18), (16, 18))
        self.add_contour('path-1-2', 'p1-r2-1', closed=False)
        self.add_line('p2-r1-1', (28, 2), (40, 2))
        self.add_line('p2-r1-2', (40, 2), (40, 18))
        self.add_line('p2-r1-3', (40, 18), (28, 18))
        self.add_line('p2-r1-4', (28, 18), (28, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
