"""Independent 32px profile of text-sentence-case-underline-text-e8cbbf5a.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e8cbbf5a-0ea4-44b3-8f38-77598d857116'
SOURCE_PATH = 'icon_set/dist/text32/text-sentence-case-underline-text-e8cbbf5a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e8cbbf5a-0ea4-44b3-8f38-77598d857116', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/sc (text u)_e8cbbf5a-0ea4-44b3-8f38-77598d857116.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-sentence-case-underline-text-e8cbbf5a',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-c')
REFERENCE_EXPORT_SHA256 = '447b9911fbe903b4b808b13cf8109391f70c8dd685d0a376d5685b4ed91600d7'

class Drawing(TextSub32):
    icon_id = 'text-sentence-case-underline-text-e8cbbf5a-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 36
    text_ink_bounds = (0.0, 0.0, 36.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (34, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (33, 11), ((32, 9), (30, 8), (28, 8)))
        self.add_bezier('p2-r1-2', (28, 8), ((24, 8), (21, 11), (21, 15)))
        self.add_bezier('p2-r1-3', (21, 15), ((21, 18), (24, 21), (28, 21)))
        self.add_bezier('p2-r1-4', (28, 21), ((30, 21), (32, 20), (34, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (14, 5), ((13, 3), (11, 2), (9, 2)))
        self.add_bezier('p3-r1-2', (9, 2), ((6, 2), (3, 3), (3, 7)))
        self.add_bezier('p3-r1-3', (3, 7), ((2, 7), (2, 7), (2, 7)))
        self.add_bezier('p3-r1-4', (2, 7), ((2, 12), (14, 10), (15, 16)))
        self.add_bezier('p3-r1-5', (15, 16), ((15, 16), (15, 16), (15, 16)))
        self.add_bezier('p3-r1-6', (15, 16), ((15, 20), (11, 21), (8, 21)))
        self.add_bezier('p3-r1-7', (8, 21), ((6, 21), (3, 20), (2, 18)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
