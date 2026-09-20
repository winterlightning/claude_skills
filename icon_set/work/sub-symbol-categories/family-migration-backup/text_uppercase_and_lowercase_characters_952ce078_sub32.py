"""Independent 32px profile of text-uppercase-and-lowercase-characters-952ce078.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '952ce078-e06e-414f-9bfc-1d0ec3a9e267'
SOURCE_PATH = 'icon_set/dist/text32/text-uppercase-and-lowercase-characters-952ce078.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('952ce078-e06e-414f-9bfc-1d0ec3a9e267', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/An_952ce078-e06e-414f-9bfc-1d0ec3a9e267.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-uppercase-and-lowercase-characters-952ce078',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-a-uppercase', 'letter-n')
REFERENCE_EXPORT_SHA256 = 'a61c68444e8adf3a4a9a0b7e0bbc75dffa1bf6138947b68d5533c084dd828bd8'

class Drawing(TextSub32):
    icon_id = 'text-uppercase-and-lowercase-characters-952ce078-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 48
    text_ink_bounds = (0.0, 0.0, 48.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (46, 30), (46, 18))
        self.add_bezier('p1-r1-2', (46, 18), ((46, 14), (43, 11), (38, 11)))
        self.add_bezier('p1-r1-3', (38, 11), ((34, 11), (31, 14), (31, 18)))
        self.add_line('p1-r1-4', (31, 18), (31, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_line('p2-r1-1', (2, 30), (11, 3))
        self.add_bezier('p2-r1-2', (11, 3), ((11.666666666666666, 2.3333333333333335), (12, 2), (12, 2)))
        self.add_bezier('p2-r1-3', (12, 2), ((12.666666666666666, 2), (13.333333333333334, 2.3333333333333335), (14, 3)))
        self.add_line('p2-r1-4', (14, 3), (23, 30))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (6, 18), (19, 18))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
