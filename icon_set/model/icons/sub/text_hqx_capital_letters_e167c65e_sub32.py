"""Independent 32px profile of text-hqx-capital-letters-e167c65e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'e167c65e-bbc2-4b60-8391-90d28768985a'
SOURCE_PATH = 'icon_set/dist/text32/text-hqx-capital-letters-e167c65e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e167c65e-bbc2-4b60-8391-90d28768985a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/hqx (text)_e167c65e-bbc2-4b60-8391-90d28768985a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-hqx-capital-letters-e167c65e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-q-uppercase', 'letter-x-uppercase')
REFERENCE_EXPORT_SHA256 = '066abee6e2d2cd152f7e8db11cc440b3738931a507876cc140a93b1489f650bc'

class Drawing(TextSub32):
    icon_id = 'text-hqx-capital-letters-e167c65e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 75
    text_ink_bounds = (0.0, 0.0, 75.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (55, 2), (73, 27))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (73, 2), (55, 27))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (28, 15), (46, 15), radius_x=9, radius_y=13, large_arc=True, sweep=True)
        self.add_arc('p3-r1-2', (46, 15), (28, 15), radius_x=9, radius_y=13, large_arc=True, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (40, 21), (47, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (2, 27))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (20, 2), (20, 27))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
        self.add_line('p7-r1-1', (2, 15), (20, 15))
        self.add_contour('path-7-1', 'p7-r1-1', closed=False)
