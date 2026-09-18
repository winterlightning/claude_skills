"""Independent 32px profile of text-plutonium-chemical-element-symbol-e41d9405.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e41d9405-ab74-46da-af5a-21bfd17b16e3'
SOURCE_PATH = 'icon_set/dist/text32/text-plutonium-chemical-element-symbol-e41d9405.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e41d9405-ab74-46da-af5a-21bfd17b16e3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/pu (text u)_e41d9405-ab74-46da-af5a-21bfd17b16e3.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-plutonium-chemical-element-symbol-e41d9405',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-u')
REFERENCE_EXPORT_SHA256 = 'cdff2e108696c15aa9ca241b69f06a8bf0946b64ad478214d42899e292551a83'

class Drawing(TextSub32):
    icon_id = 'text-plutonium-chemical-element-symbol-e41d9405-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 34
    text_ink_bounds = (0.0, 0.0, 34.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (32, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (22, 8), (22, 16))
        self.add_bezier('p2-r1-2', (22, 16), ((22, 19), (24, 21), (27, 21)))
        self.add_bezier('p2-r1-3', (27, 21), ((30, 21), (32, 19), (32, 16)))
        self.add_line('p2-r1-4', (32, 16), (32, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (9, 2))
        self.add_bezier('p3-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p3-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p3-r1-5', (9, 12), (2, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', closed=False)
