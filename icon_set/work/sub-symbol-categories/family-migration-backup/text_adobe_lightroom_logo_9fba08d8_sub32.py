"""Independent 32px profile of text-adobe-lightroom-logo-9fba08d8.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '9fba08d8-0810-449a-bf1e-621cdbf51189'
SOURCE_PATH = 'icon_set/dist/text32/text-adobe-lightroom-logo-9fba08d8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9fba08d8-0810-449a-bf1e-621cdbf51189', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/lr (text u)_9fba08d8-0810-449a-bf1e-621cdbf51189.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-adobe-lightroom-logo-9fba08d8',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-l-uppercase', 'letter-r')
REFERENCE_EXPORT_SHA256 = '5d1b6ab12813401ec72bcc6398d7b0e8ab800991c4abec8cba1f23a515701892'

class Drawing(TextSub32):
    icon_id = 'text-adobe-lightroom-logo-9fba08d8-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 27
    text_ink_bounds = (0.0, 0.0, 27.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (25, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (20, 8), (20, 12))
        self.add_line('p2-r1-2', (20, 12), (20, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', closed=False)
        self.add_bezier('p3-r1-1', (20, 12), ((20, 10), (22, 8), (24, 8)))
        self.add_line('p3-r1-2', (24, 8), (25, 8))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 2), (2, 21))
        self.add_line('p4-r1-2', (2, 21), (13, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
