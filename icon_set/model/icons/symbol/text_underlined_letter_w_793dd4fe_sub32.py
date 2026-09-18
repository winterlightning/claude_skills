"""Independent 32px profile of text-underlined-letter-w-793dd4fe.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '793dd4fe-ce02-4596-b689-c68a21e6544d'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letter-w-793dd4fe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('793dd4fe-ce02-4596-b689-c68a21e6544d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/w (text u)_793dd4fe-ce02-4596-b689-c68a21e6544d.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letter-w-793dd4fe',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-w-uppercase',)
REFERENCE_EXPORT_SHA256 = 'fe15a9567d276b7767f83116a7892dc8c5f8e5e1d0f5b040eb6614ec224e5462'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letter-w-793dd4fe-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 24
    text_ink_bounds = (0.0, 0.0, 24.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (22, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (2, 2), (6, 20))
        self.add_bezier('p2-r1-2', (6, 20), ((6.666666666666667, 20.666666666666668), (7, 21), (7, 21)))
        self.add_bezier('p2-r1-3', (7, 21), ((7, 21), (7, 20.666666666666668), (7, 20)))
        self.add_line('p2-r1-4', (7, 20), (12, 4))
        self.add_bezier('p2-r1-5', (12, 4), ((12, 3.3333333333333335), (12, 3), (12, 3)))
        self.add_bezier('p2-r1-6', (12, 3), ((12, 3), (12.333333333333334, 3.3333333333333335), (13, 4)))
        self.add_line('p2-r1-7', (13, 4), (17, 20))
        self.add_bezier('p2-r1-8', (17, 20), ((17, 20.666666666666668), (17, 21), (17, 21)))
        self.add_bezier('p2-r1-9', (17, 21), ((17.666666666666668, 21), (18, 20.666666666666668), (18, 20)))
        self.add_line('p2-r1-10', (18, 20), (22, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
