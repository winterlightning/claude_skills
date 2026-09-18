"""Independent 32px profile of text-application-text-label-b583b017.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'b583b017-1004-447b-b65e-c7c25b920a81'
SOURCE_PATH = 'icon_set/dist/text32/text-application-text-label-b583b017.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b583b017-1004-447b-b65e-c7c25b920a81', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/app (text)_b583b017-1004-447b-b65e-c7c25b920a81.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-application-text-label-b583b017',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-p-uppercase', 'letter-p-uppercase')
REFERENCE_EXPORT_SHA256 = 'eda7f8181a186732e59cd28aec2dfea8f2cd57071d72e4b0d246dbc89146c579'

class Drawing(TextSub32):
    icon_id = 'text-application-text-label-b583b017-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 79
    text_ink_bounds = (0.0, 0.0, 79.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (58, 30), (58, 2))
        self.add_line('p1-r1-2', (58, 2), (68, 2))
        self.add_bezier('p1-r1-3', (68, 2), ((74, 2), (77, 6), (77, 9)))
        self.add_bezier('p1-r1-4', (77, 9), ((77, 13), (74, 17), (68, 17)))
        self.add_line('p1-r1-5', (68, 17), (58, 17))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (31, 30), (31, 2))
        self.add_line('p2-r1-2', (31, 2), (41, 2))
        self.add_bezier('p2-r1-3', (41, 2), ((47, 2), (50, 6), (50, 9)))
        self.add_bezier('p2-r1-4', (50, 9), ((50, 13), (47, 17), (41, 17)))
        self.add_line('p2-r1-5', (41, 17), (31, 17))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (2, 30), (11, 3))
        self.add_bezier('p3-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p3-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p3-r1-4', (14, 3), (23, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (6, 18), (19, 18))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
