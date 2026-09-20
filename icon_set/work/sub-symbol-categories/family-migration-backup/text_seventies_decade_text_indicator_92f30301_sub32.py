"""Independent 32px profile of text-seventies-decade-text-indicator-92f30301.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '92f30301-60e6-432a-beb0-2009f2ff2b40'
SOURCE_PATH = 'icon_set/dist/text32/text-seventies-decade-text-indicator-92f30301.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('92f30301-60e6-432a-beb0-2009f2ff2b40', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/70s_92f30301-60e6-432a-beb0-2009f2ff2b40.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-seventies-decade-text-indicator-92f30301',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-7', 'digit-0', 'letter-s')
REFERENCE_EXPORT_SHA256 = 'd4cc65516389483024b50391b4000da4bd5a8b9ba678ab45fce6f79e68e5d961'

class Drawing(TextSub32):
    icon_id = 'text-seventies-decade-text-indicator-92f30301-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 71
    text_ink_bounds = (0.0, 0.0, 71.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (68, 13), ((68, 13), (68, 11), (63, 11)))
        self.add_bezier('p1-r1-2', (63, 11), ((59, 11), (56, 13), (56, 16)))
        self.add_bezier('p1-r1-3', (56, 16), ((56, 17), (57, 19), (59, 19)))
        self.add_bezier('p1-r1-4', (59, 19), ((65, 21), (64, 21), (67, 22)))
        self.add_bezier('p1-r1-5', (67, 22), ((68, 23), (69, 24), (69, 25)))
        self.add_bezier('p1-r1-6', (69, 25), ((69, 27), (67, 30), (63, 30)))
        self.add_bezier('p1-r1-7', (63, 30), ((56, 30), (56, 26), (56, 26)))
        self.add_bezier('p1-r1-8', (56, 26), ((56, 26), (56, 26), (56, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', closed=False)
        self.add_arc('p2-r1-1', (29, 10), (48, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-2', (48, 10), (48, 22))
        self.add_arc('p2-r1-3', (48, 22), (29, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p2-r1-4', (29, 22), (29, 10))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 2), (20, 2))
        self.add_bezier('p3-r1-2', (20, 2), ((21, 2), (21, 2), (21, 3)))
        self.add_bezier('p3-r1-3', (21, 3), ((21, 3), (21, 3), (21, 3)))
        self.add_line('p3-r1-4', (21, 3), (8, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
