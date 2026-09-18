"""Independent 32px profile of text-number-seventy-2792944b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '2792944b-1f57-4c58-8e3b-19150be318d8'
SOURCE_PATH = 'icon_set/dist/text32/text-number-seventy-2792944b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2792944b-1f57-4c58-8e3b-19150be318d8', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/70 (text)_2792944b-1f57-4c58-8e3b-19150be318d8.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-number-seventy-2792944b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('digit-7', 'digit-0')
REFERENCE_EXPORT_SHA256 = '0720cd8b1d191059d09f408e79aa4b83ae074d4996173846deecea4c7abce095'

class Drawing(TextSub32):
    icon_id = 'text-number-seventy-2792944b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 50
    text_ink_bounds = (0.0, 0.0, 50.0, 32.0)

    def build(self):
        self.add_arc('p1-r1-1', (29, 10), (48, 10), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-2', (48, 10), (48, 22))
        self.add_arc('p1-r1-3', (48, 22), (29, 22), radius_x=10, radius_y=8, large_arc=False, sweep=True)
        self.add_line('p1-r1-4', (29, 22), (29, 10))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 2), (20, 2))
        self.add_bezier('p2-r1-2', (20, 2), ((21, 2), (21, 2), (21, 3)))
        self.add_bezier('p2-r1-3', (21, 3), ((21, 3), (21, 3), (21, 3)))
        self.add_line('p2-r1-4', (21, 3), (8, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
