"""Independent 32px profile of text-underlined-dy-text-2da2da3d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '2da2da3d-94f9-4835-b93e-c6f792dd33b0'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-dy-text-2da2da3d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2da2da3d-94f9-4835-b93e-c6f792dd33b0', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/dy (text u)_2da2da3d-94f9-4835-b93e-c6f792dd33b0.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-dy-text-2da2da3d',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-d-uppercase', 'letter-y')
REFERENCE_EXPORT_SHA256 = '501d5e04bc24fb384f3f418039cbcb17c020521ff4c74927e90fa403fcf6b766'

class Drawing(TextSub32):
    icon_id = 'text-underlined-dy-text-2da2da3d-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 31
    text_ink_bounds = (0.0, 0.0, 31.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (29, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (19, 7), ((19, 8), (23, 14), (24, 17)))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (29, 7), (24, 18))
        self.add_bezier('p3-r1-2', (24, 18), ((24, 18), (23, 20), (22, 20)))
        self.add_bezier('p3-r1-3', (22, 20), ((21, 21), (19, 21), (19, 21)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 2), (6, 2))
        self.add_bezier('p4-r1-2', (6, 2), ((11, 2), (13, 6), (13, 10)))
        self.add_bezier('p4-r1-3', (13, 10), ((13, 14), (11, 17), (6, 17)))
        self.add_line('p4-r1-4', (6, 17), (2, 17))
        self.add_line('p4-r1-5', (2, 17), (2, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', 'p4-r1-4', 'p4-r1-5', closed=False)
