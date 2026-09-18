"""Independent 32px profile of text-two-player-mode-symbol-fae72b07.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'fae72b07-c1a6-4e50-8a37-203afbd51530'
SOURCE_PATH = 'icon_set/dist/text32/text-two-player-mode-symbol-fae72b07.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fae72b07-c1a6-4e50-8a37-203afbd51530', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/2P (text)_fae72b07-c1a6-4e50-8a37-203afbd51530.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-two-player-mode-symbol-fae72b07',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-2', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = 'ad5fdb7f2bd808ded0c9b8e36aebc11574aa128950b580f5393802ca1506cf05'

class Drawing(TextSub32):
    icon_id = 'text-two-player-mode-symbol-fae72b07-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (29, 30), (29, 2))
        self.add_line('p1-r1-2', (29, 2), (39, 2))
        self.add_bezier('p1-r1-3', (39, 2), ((46, 2), (49, 6), (49, 9)))
        self.add_bezier('p1-r1-4', (49, 9), ((49, 13), (46, 17), (39, 17)))
        self.add_line('p1-r1-5', (39, 17), (29, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (2, 2), (16, 2))
        self.add_bezier('p2-r1-2', (16, 2), ((19, 2), (21, 5), (21, 8)))
        self.add_bezier('p2-r1-3', (21, 8), ((21, 9), (21, 11), (19, 12)))
        self.add_line('p2-r1-4', (19, 12), (6, 21))
        self.add_bezier('p2-r1-5', (6, 21), ((3, 23), (2, 25), (2, 28)))
        self.add_line('p2-r1-6', (2, 28), (2, 29))
        self.add_bezier('p2-r1-7', (2, 29), ((2, 29), (3, 30), (3, 30)))
        self.add_line('p2-r1-8', (3, 30), (22, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
