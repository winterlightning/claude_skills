"""Independent 32px profile of text-zero-grams-weight-measurement-5e6242e4.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '5e6242e4-4ccf-4be2-b9b7-c4e89bae22c3'
SOURCE_PATH = 'icon_set/dist/text32/text-zero-grams-weight-measurement-5e6242e4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e6242e4-4ccf-4be2-b9b7-c4e89bae22c3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/og (text u)_5e6242e4-4ccf-4be2-b9b7-c4e89bae22c3.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-zero-grams-weight-measurement-5e6242e4',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-0', 'letter-g')
REFERENCE_EXPORT_SHA256 = '4278292739df7e07007fd8491985f697aeb54447931db9894d053f7806a19cc3'

class Drawing(TextSub32):
    icon_id = 'text-zero-grams-weight-measurement-5e6242e4-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 38
    text_ink_bounds = (0.0, 0.0, 38.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (36, 19), (36, 12))
        self.add_bezier('p1-r1-2', (36, 12), ((36, 12), (36, 12), (36, 11)))
        self.add_bezier('p1-r1-3', (36, 11), ((35, 10), (33, 8), (30, 8)))
        self.add_bezier('p1-r1-4', (30, 8), ((26, 8), (23, 12), (23, 15)))
        self.add_bezier('p1-r1-5', (23, 15), ((23, 19), (26, 23), (30, 23)))
        self.add_bezier('p1-r1-6', (30, 23), ((33, 23), (35, 21), (36, 19)))
        self.add_line('p1-r1-7', (36, 19), (36, 23))
        self.add_bezier('p1-r1-8', (36, 23), ((36, 27), (33, 30), (30, 30)))
        self.add_line('p1-r1-9', (30, 30), (29, 30))
        self.add_bezier('p1-r1-10', (29, 30), ((26, 30), (24, 29), (24, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_arc('p2-r1-1', (2, 8), (16, 8), radius_x=7, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (16, 8), (16, 17))
        self.add_arc('p2-r1-3', (16, 17), (2, 17), radius_x=7, radius_y=6, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (2, 17), (2, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
