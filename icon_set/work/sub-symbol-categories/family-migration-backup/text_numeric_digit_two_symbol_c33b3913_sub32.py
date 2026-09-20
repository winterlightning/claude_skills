"""Independent 32px profile of text-numeric-digit-two-symbol-c33b3913.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c33b3913-667e-4763-8536-f0c4f32f976e'
SOURCE_PATH = 'icon_set/dist/text32/text-numeric-digit-two-symbol-c33b3913.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c33b3913-667e-4763-8536-f0c4f32f976e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/2 (text)_c33b3913-667e-4763-8536-f0c4f32f976e.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-numeric-digit-two-symbol-c33b3913',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-2',)
REFERENCE_EXPORT_SHA256 = 'e78f852f1ae15f8c6650699f7d0eef0766393ee95b4564092c770af0e3519734'

class Drawing(TextSub32):
    icon_id = 'text-numeric-digit-two-symbol-c33b3913-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 24
    text_ink_bounds = (0.0, 0.0, 24.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 2), (16, 2))
        self.add_bezier('p1-r1-2', (16, 2), ((19, 2), (21, 5), (21, 8)))
        self.add_bezier('p1-r1-3', (21, 8), ((21, 9), (21, 11), (19, 12)))
        self.add_line('p1-r1-4', (19, 12), (6, 21))
        self.add_bezier('p1-r1-5', (6, 21), ((3, 23), (2, 25), (2, 28)))
        self.add_line('p1-r1-6', (2, 28), (2, 29))
        self.add_bezier('p1-r1-7', (2, 29), ((2, 29), (3, 30), (3, 30)))
        self.add_line('p1-r1-8', (3, 30), (22, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
