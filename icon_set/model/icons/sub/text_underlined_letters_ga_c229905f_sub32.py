"""Independent 32px profile of text-underlined-letters-ga-c229905f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c229905f-b32a-434c-b3d8-e60a3dab6312'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-ga-c229905f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c229905f-b32a-434c-b3d8-e60a3dab6312', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ga (text u)_c229905f-b32a-434c-b3d8-e60a3dab6312.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-ga-c229905f',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-g-uppercase', 'letter-a')
REFERENCE_EXPORT_SHA256 = '09c5d5c06cbb94ef6972e0e4dc6504bf38013d9de6f425105bbb2ee4583d086e'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-ga-c229905f-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 37
    text_ink_bounds = (0.0, 0.0, 37.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (35, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (35, 18), (35, 12))
        self.add_bezier('p2-r1-2', (35, 12), ((35, 11), (35, 11), (35, 11)))
        self.add_bezier('p2-r1-3', (35, 11), ((33, 9), (31, 8), (29, 8)))
        self.add_bezier('p2-r1-4', (29, 8), ((25, 8), (22, 11), (22, 15)))
        self.add_bezier('p2-r1-5', (22, 15), ((22, 18), (25, 21), (29, 21)))
        self.add_bezier('p2-r1-6', (29, 21), ((32, 21), (34, 20), (35, 18)))
        self.add_line('p2-r1-7', (35, 18), (35, 21))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_bezier('p3-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p3-r1-2', (9, 2), ((6, 2), (2, 7), (2, 12)))
        self.add_bezier('p3-r1-3', (2, 12), ((2, 13), (2, 14), (3, 15)))
        self.add_bezier('p3-r1-4', (3, 15), ((4, 19), (6, 21), (9, 21)))
        self.add_bezier('p3-r1-5', (9, 21), ((12, 21), (16, 17), (16, 12)))
        self.add_line('p3-r1-6', (16, 12), (11, 12))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
