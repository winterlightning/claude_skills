"""Independent 32px profile of text-hot-text-label-2c3cc802.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '2c3cc802-309e-469d-ad63-e80091958218'
SOURCE_PATH = 'icon_set/dist/text32/text-hot-text-label-2c3cc802.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2c3cc802-309e-469d-ad63-e80091958218', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/hot (text)_2c3cc802-309e-469d-ad63-e80091958218.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-hot-text-label-2c3cc802',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-h-uppercase', 'letter-o-uppercase', 'letter-t-uppercase')
REFERENCE_EXPORT_SHA256 = 'ecc6457567a1c266a44c0803596054d86541587ebee7b2418662f116397cfdad'

class Drawing(TextSub32):
    icon_id = 'text-hot-text-label-2c3cc802-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 82
    text_ink_bounds = (0.0, 0.0, 82.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (58, 2), (80, 2))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (69, 2), (69, 30))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_arc('p3-r1-1', (30, 16), (50, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_arc('p3-r1-2', (50, 16), (30, 16), radius_x=10, radius_y=14, large_arc=True, sweep=True)
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', closed=False)
        self.add_line('p4-r1-1', (2, 2), (2, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (22, 2), (22, 30))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (2, 16), (22, 16))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
