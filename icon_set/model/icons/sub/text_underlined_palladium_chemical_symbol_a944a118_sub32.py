"""Independent 32px profile of text-underlined-palladium-chemical-symbol-a944a118.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a944a118-8d0a-43d9-a913-9b94c9eb2ad4'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-palladium-chemical-symbol-a944a118.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a944a118-8d0a-43d9-a913-9b94c9eb2ad4', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/pd (text u)_a944a118-8d0a-43d9-a913-9b94c9eb2ad4.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-palladium-chemical-symbol-a944a118',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-p-uppercase', 'letter-d')
REFERENCE_EXPORT_SHA256 = 'e18ee634554c0b0e389d9a63096f99ce73e9a73acdd9c0b1ea72a4cca2fd1bc8'

class Drawing(TextSub32):
    icon_id = 'text-underlined-palladium-chemical-symbol-a944a118-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 36
    text_ink_bounds = (0.0, 0.0, 36.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (34, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (34, 18), ((33, 20), (31, 21), (29, 21)))
        self.add_bezier('p2-r1-2', (29, 21), ((25, 21), (22, 18), (22, 15)))
        self.add_bezier('p2-r1-3', (22, 15), ((22, 11), (25, 8), (29, 8)))
        self.add_bezier('p2-r1-4', (29, 8), ((31, 8), (33, 9), (34, 11)))
        self.add_bezier('p2-r1-5', (34, 11), ((34, 11), (34, 11), (34, 12)))
        self.add_line('p2-r1-6', (34, 12), (34, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (34, 12), (34, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (9, 2))
        self.add_bezier('p4-r1-3', (9, 2), ((13, 2), (15, 5), (15, 7)))
        self.add_bezier('p4-r1-4', (15, 7), ((15, 10), (13, 12), (9, 12)))
        self.add_line('p4-r1-5', (9, 12), (2, 12))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
