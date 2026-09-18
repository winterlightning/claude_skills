"""Independent 32px profile of text-underlined-letters-rg-a2b4d767.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = 'a2b4d767-50d6-4c69-95ff-892bd71f2785'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-letters-rg-a2b4d767.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a2b4d767-50d6-4c69-95ff-892bd71f2785', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/rg (text u)_a2b4d767-50d6-4c69-95ff-892bd71f2785.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-letters-rg-a2b4d767',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-r-uppercase', 'letter-g')
REFERENCE_EXPORT_SHA256 = 'ebec2baeaeefbab2d9c618d20667bed3128e570b330bfe205544eea55ddf84aa'

class Drawing(TextSub32):
    icon_id = 'text-underlined-letters-rg-a2b4d767-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 34
    text_ink_bounds = (0.0, 0.0, 34.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (32, 15), (32, 10))
        self.add_bezier('p1-r1-2', (32, 10), ((32, 10), (32, 10), (32, 9)))
        self.add_bezier('p1-r1-3', (32, 9), ((31, 8), (29, 7), (27, 7)))
        self.add_bezier('p1-r1-4', (27, 7), ((24, 7), (21, 9), (21, 13)))
        self.add_bezier('p1-r1-5', (21, 13), ((21, 16), (24, 18), (27, 18)))
        self.add_bezier('p1-r1-6', (27, 18), ((29, 18), (31, 17), (32, 15)))
        self.add_line('p1-r1-7', (32, 15), (32, 19))
        self.add_bezier('p1-r1-8', (32, 19), ((32, 22), (29, 24), (26, 24)))
        self.add_line('p1-r1-9', (26, 24), (26, 24))
        self.add_bezier('p1-r1-10', (26, 24), ((24, 24), (22, 23), (22, 21)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', 'p1-r1-8', 'p1-r1-9', 'p1-r1-10', closed=False)
        self.add_line('p2-r1-1', (2, 18), (2, 2))
        self.add_line('p2-r1-2', (2, 2), (8, 2))
        self.add_bezier('p2-r1-3', (8, 2), ((11, 2), (13, 4), (13, 6)))
        self.add_bezier('p2-r1-4', (13, 6), ((13, 8), (11, 11), (8, 11)))
        self.add_line('p2-r1-5', (8, 11), (2, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', closed=False)
        self.add_line('p3-r1-1', (8, 11), (14, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 30), (32, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.relate('connect', 'p2-r1-4', 'p3-r1-1')
        self.relate('connect', 'p2-r1-5', 'p3-r1-1')
