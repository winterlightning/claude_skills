"""Independent 32px profile of text-underlined-letters-mc-f7ec73e6.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f7ec73e6-2bc7-4281-8e4b-5443f3b85159'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-mc-f7ec73e6.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f7ec73e6-2bc7-4281-8e4b-5443f3b85159', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mc (text u)_f7ec73e6-2bc7-4281-8e4b-5443f3b85159.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-mc-f7ec73e6',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-c')
REFERENCE_EXPORT_SHA256 = 'a8bfd8b28a0fbb0bf29eeae03ff9635d826d241d8276964e66280d3bee791100'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-mc-f7ec73e6-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 41
    text_ink_bounds = (0.0, 0.0, 41.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (39, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (39, 11), ((38, 9), (36, 8), (33, 8)))
        self.add_bezier('p2-r1-2', (33, 8), ((30, 8), (27, 11), (27, 15)))
        self.add_bezier('p2-r1-3', (27, 15), ((27, 18), (30, 21), (33, 21)))
        self.add_bezier('p2-r1-4', (33, 21), ((36, 21), (38, 20), (39, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (11, 14))
        self.add_line('p3-r1-3', (11, 14), (20, 2))
        self.add_line('p3-r1-4', (20, 2), (20, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
