"""Independent 32px profile of text-underlined-monday-day-abbreviation-05f9d47b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSymbol32 as TextSub32
SOURCE_ICON_ID = '05f9d47b-81e8-4019-8920-57b1f9c4d96b'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-monday-day-abbreviation-05f9d47b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('05f9d47b-81e8-4019-8920-57b1f9c4d96b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/mo (text u)_05f9d47b-81e8-4019-8920-57b1f9c4d96b.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-monday-day-abbreviation-05f9d47b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-o')
REFERENCE_EXPORT_SHA256 = 'b6aaad61b7f9a6377ed556cd47e0d2d0e162d01a9498f2dcf9eecb6ea0495134'

class Drawing(TextSub32):
    icon_id = 'text-underlined-monday-day-abbreviation-05f9d47b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 42
    text_ink_bounds = (0.0, 0.0, 42.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (40, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (33, 21), ((37, 21), (40, 18), (40, 15)))
        self.add_bezier('p2-r1-2', (40, 15), ((40, 11), (37, 8), (33, 8)))
        self.add_bezier('p2-r1-3', (33, 8), ((30, 8), (27, 11), (27, 15)))
        self.add_bezier('p2-r1-4', (27, 15), ((27, 18), (30, 21), (33, 21)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 21), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (11, 14))
        self.add_line('p3-r1-3', (11, 14), (20, 2))
        self.add_line('p3-r1-4', (20, 2), (20, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
