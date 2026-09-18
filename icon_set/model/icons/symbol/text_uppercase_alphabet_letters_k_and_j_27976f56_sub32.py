"""Independent 32px profile of text-uppercase-alphabet-letters-k-and-j-27976f56.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '27976f56-4e44-4d51-a265-66e6164f5a42'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-alphabet-letters-k-and-j-27976f56.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('27976f56-4e44-4d51-a265-66e6164f5a42', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/KJ (text)_27976f56-4e44-4d51-a265-66e6164f5a42.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-alphabet-letters-k-and-j-27976f56',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-k-uppercase', 'letter-j-uppercase')
REFERENCE_EXPORT_SHA256 = '856e5e883713418802b74cb97e814002474a10e196a6d5de1ed890149df6544a'

class Drawing(TextSub32):
    icon_id = 'text-uppercase-alphabet-letters-k-and-j-27976f56-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 47
    text_ink_bounds = (0.0, 0.0, 47.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (34, 2), (45, 2))
        self.add_line('p1-r1-2', (45, 2), (45, 21))
        self.add_bezier('p1-r1-3', (45, 21), ((45, 27), (41, 30), (37, 30)))
        self.add_bezier('p1-r1-4', (37, 30), ((33, 30), (30, 28), (29, 24)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 2), (2, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (21, 2), (2, 17))
        self.add_line('p3-r1-2', (2, 17), (21, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
