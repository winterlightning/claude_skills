"""Independent 32px profile of text-seventy-five-number-symbol-96923c04.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '96923c04-af2b-4baa-b0f7-7fb4d30662f9'
SOURCE_PATH = 'icon_set/dist/text32/text-seventy-five-number-symbol-96923c04.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('96923c04-af2b-4baa-b0f7-7fb4d30662f9', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/75_96923c04-af2b-4baa-b0f7-7fb4d30662f9.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-seventy-five-number-symbol-96923c04',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-7', 'digit-5')
REFERENCE_EXPORT_SHA256 = '3a134d29cd5d4be413f454f80bde4821c8c88cb8aa77ba8fb9d67527b9ec20c4'

class Drawing(TextSub32):
    icon_id = 'text-seventy-five-number-symbol-96923c04-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 50
    text_ink_bounds = (0.0, 0.0, 50.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (46, 2), (30, 2))
        self.add_bezier('p1-r1-2', (30, 2), ((29, 2), (29, 2), (29, 3)))
        self.add_line('p1-r1-3', (29, 3), (29, 13))
        self.add_bezier('p1-r1-4', (29, 13), ((29, 13), (29, 14), (30, 14)))
        self.add_line('p1-r1-5', (30, 14), (40, 14))
        self.add_bezier('p1-r1-6', (40, 14), ((45, 14), (48, 18), (48, 22)))
        self.add_bezier('p1-r1-7', (48, 22), ((48, 24), (47, 26), (46, 28)))
        self.add_bezier('p1-r1-8', (46, 28), ((44, 29), (42, 30), (40, 30)))
        self.add_line('p1-r1-9', (40, 30), (30, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', closed=False)
        self.add_line('p2-r1-1', (2, 2), (20, 2))
        self.add_bezier('p2-r1-2', (20, 2), ((21, 2), (21, 2), (21, 3)))
        self.add_bezier('p2-r1-3', (21, 3), ((21, 3), (21, 3), (21, 3)))
        self.add_line('p2-r1-4', (21, 3), (8, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
