"""Independent 32px profile of text-letters-o-and-c-symbol-83b28959.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '83b28959-2b38-492c-ac13-4b3442ce26af'
SOURCE_PATH = 'icon_set/dist/text32/text-letters-o-and-c-symbol-83b28959.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('83b28959-2b38-492c-ac13-4b3442ce26af', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/OC (text)_83b28959-2b38-492c-ac13-4b3442ce26af.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-letters-o-and-c-symbol-83b28959',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-o-uppercase', 'letter-c-uppercase')
REFERENCE_EXPORT_SHA256 = '6b488f3a896f6ae04cb3eae983ebb17e1bbb31208795e67ad9d991b68154def0'

class Drawing(TextSub32):
    icon_id = 'text-letters-o-and-c-symbol-83b28959-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 49
    text_ink_bounds = (0.0, 0.0, 49.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (47, 6), (47, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_arc('p2-r1-1', (2, 16), (22, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('p2-r1-2', (22, 16), (2, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
