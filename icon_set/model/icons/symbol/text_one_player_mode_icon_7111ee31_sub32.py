"""Independent 32px profile of text-one-player-mode-icon-7111ee31.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '7111ee31-431e-46d9-8af7-0ae69eeb1699'
SOURCE_PATH = 'icon_set/dist/text32/text-one-player-mode-icon-7111ee31.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7111ee31-431e-46d9-8af7-0ae69eeb1699', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/1P (text)_7111ee31-431e-46d9-8af7-0ae69eeb1699.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-one-player-mode-icon-7111ee31',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-1', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = '2eceff290740685fde02bbe0cf6770e2a502df899ae09986de7207e3a35cf3f6'

class Drawing(TextSub32):
    icon_id = 'text-one-player-mode-icon-7111ee31-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 45
    text_ink_bounds = (0.0, 0.0, 45.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (23, 30), (23, 2))
        self.add_line('p1-r1-2', (23, 2), (33, 2))
        self.add_bezier('p1-r1-3', (33, 2), ((39, 2), (43, 6), (43, 9)))
        self.add_bezier('p1-r1-4', (43, 9), ((43, 13), (39, 17), (33, 17)))
        self.add_line('p1-r1-5', (33, 17), (23, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (9, 30), (9, 3))
        self.add_bezier('p2-r1-2', (9, 3), ((9, 2), (8, 2), (8, 2)))
        self.add_line('p2-r1-3', (8, 2), (2, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
        self.add_line('p3-r1-1', (2, 30), (15, 30))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
