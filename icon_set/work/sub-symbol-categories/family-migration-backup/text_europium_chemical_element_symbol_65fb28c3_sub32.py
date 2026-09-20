"""Independent 32px profile of text-europium-chemical-element-symbol-65fb28c3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '65fb28c3-f621-426e-ba5e-b1b75fdeab5c'
SOURCE_PATH = 'icon_set/dist/text32/text-europium-chemical-element-symbol-65fb28c3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('65fb28c3-f621-426e-ba5e-b1b75fdeab5c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/eu (text u)_65fb28c3-f621-426e-ba5e-b1b75fdeab5c.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-europium-chemical-element-symbol-65fb28c3',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-e-uppercase', 'letter-u')
REFERENCE_EXPORT_SHA256 = '2d17aeae95e09e803bdd82369cf20007f7e82ed9a32d2431bb4aefeceff0c295'

class Drawing(TextSub32):
    icon_id = 'text-europium-chemical-element-symbol-65fb28c3-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 33
    text_ink_bounds = (0.0, 0.0, 33.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (31, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (20, 8), (20, 16))
        self.add_bezier('p2-r1-2', (20, 16), ((20, 19), (23, 21), (26, 21)))
        self.add_bezier('p2-r1-3', (26, 21), ((28, 21), (31, 19), (31, 16)))
        self.add_line('p2-r1-4', (31, 16), (31, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (14, 2), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (2, 21))
        self.add_line('p3-r1-3', (2, 21), (14, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 12), (12, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
