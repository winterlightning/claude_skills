"""Independent 32px profile of text-error-404-page-not-found-cc453cf4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'cc453cf4-5e60-4a0a-8f2d-420bd0906ce0'
SOURCE_PATH = 'icon_set/dist/text32/text-error-404-page-not-found-cc453cf4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cc453cf4-5e60-4a0a-8f2d-420bd0906ce0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/404 (text)_cc453cf4-5e60-4a0a-8f2d-420bd0906ce0.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-error-404-page-not-found-cc453cf4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-4', 'digit-0', 'digit-4')
REFERENCE_EXPORT_SHA256 = 'a0be8419f866008f0a91085026a93458a3b7f22f21e461c6b46af475b73d5d97'

class Drawing(TextSub32):
    icon_id = 'text-error-404-page-not-found-cc453cf4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 86
    text_ink_bounds = (0.0, 0.0, 86.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (61, 2), (61, 20))
        self.add_bezier('p1-r1-2', (61, 20), ((61, 20), (61, 20), (62, 20)))
        self.add_line('p1-r1-3', (62, 20), (84, 20))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', closed=False)
        self.add_line('p2-r1-1', (79, 2), (79, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (33, 10), (53, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p3-r1-2', (53, 10), (53, 22))
        self.add_arc('p3-r1-3', (53, 22), (33, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p3-r1-4', (33, 22), (33, 10))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
        self.add_line('p4-r1-1', (2, 2), (2, 20))
        self.add_bezier('p4-r1-2', (2, 20), ((2, 20), (2, 20), (3, 20)))
        self.add_line('p4-r1-3', (3, 20), (26, 20))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.add_line('p5-r1-1', (21, 2), (21, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
