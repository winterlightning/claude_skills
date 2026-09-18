"""Independent 32px profile of text-numero-sign-symbol-cfeaabc9.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'cfeaabc9-292f-4f2a-9d4c-21b0e7485cec'
SOURCE_PATH = 'icon_set/dist/text32/text-numero-sign-symbol-cfeaabc9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cfeaabc9-292f-4f2a-9d4c-21b0e7485cec', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/no (text u)_cfeaabc9-292f-4f2a-9d4c-21b0e7485cec.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-numero-sign-symbol-cfeaabc9',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-o')
REFERENCE_EXPORT_SHA256 = 'abd13da981d75d9f5f713b789445a868f23969a2515acce0e86fa050bb2eb49a'

class Drawing(TextSub32):
    icon_id = 'text-numero-sign-symbol-cfeaabc9-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 51
    text_ink_bounds = (0.0, 0.0, 51.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (40, 30), ((45, 30), (49, 26), (49, 20)))
        self.add_bezier('p1-r1-2', (49, 20), ((49, 15), (45, 11), (40, 11)))
        self.add_bezier('p1-r1-3', (40, 11), ((34, 11), (30, 15), (30, 20)))
        self.add_bezier('p1-r1-4', (30, 20), ((30, 26), (34, 30), (40, 30)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 30), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (22, 30))
        self.add_line('p2-r1-3', (22, 30), (22, 2))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', closed=False)
