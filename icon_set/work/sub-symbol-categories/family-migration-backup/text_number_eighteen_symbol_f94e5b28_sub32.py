"""Independent 32px profile of text-number-eighteen-symbol-f94e5b28.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'f94e5b28-e5d6-46cd-9ee7-d30b6487f824'
SOURCE_PATH = 'icon_set/dist/text32/text-number-eighteen-symbol-f94e5b28.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f94e5b28-e5d6-46cd-9ee7-d30b6487f824', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/18_f94e5b28-e5d6-46cd-9ee7-d30b6487f824.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-eighteen-symbol-f94e5b28',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-1', 'digit-8')
REFERENCE_EXPORT_SHA256 = '80718a9ff4ddce09574d4ee856d5e0c16ca1d4ceb5fc0bc3393a1eeeb3ad1d59'

class Drawing(TextSub32):
    icon_id = 'text-number-eighteen-symbol-f94e5b28-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 44
    text_ink_bounds = (0.0, 0.0, 44.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (24, 9), ((24, 5), (27, 2), (31, 2)))
        self.add_line('p1-r1-2', (31, 2), (35, 2))
        self.add_bezier('p1-r1-3', (35, 2), ((38, 2), (41, 5), (41, 9)))
        self.add_bezier('p1-r1-4', (41, 9), ((41, 12), (38, 15), (35, 15)))
        self.add_line('p1-r1-5', (35, 15), (31, 15))
        self.add_bezier('p1-r1-6', (31, 15), ((27, 15), (24, 12), (24, 9)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', closed=False)
        self.add_bezier('p2-r1-1', (23, 23), ((23, 19), (26, 15), (30, 15)))
        self.add_line('p2-r1-2', (30, 15), (35, 15))
        self.add_bezier('p2-r1-3', (35, 15), ((39, 15), (42, 19), (42, 23)))
        self.add_bezier('p2-r1-4', (42, 23), ((42, 27), (39, 30), (35, 30)))
        self.add_line('p2-r1-5', (35, 30), (30, 30))
        self.add_bezier('p2-r1-6', (30, 30), ((26, 30), (23, 27), (23, 23)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (9, 30), (9, 3))
        self.add_bezier('p3-r1-2', (9, 3), ((9, 2), (8, 2), (8, 2)))
        self.add_line('p3-r1-3', (8, 2), (2, 2))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 30), (15, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate("connect", 'p1-r1-4', 'p2-r1-2')
        self.relate("connect", 'p1-r1-4', 'p2-r1-3')
        self.relate("connect", 'p1-r1-5', 'p2-r1-2')
        self.relate("connect", 'p1-r1-5', 'p2-r1-3')
