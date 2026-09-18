"""Independent 32px profile of text-copper-chemical-symbol-underlined-d2287aae.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'd2287aae-54a7-4e4c-9033-5df0a68ec4c5'
SOURCE_PATH = 'icon_set/dist/text32/text-copper-chemical-symbol-underlined-d2287aae.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d2287aae-54a7-4e4c-9033-5df0a68ec4c5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/cu (text u)_d2287aae-54a7-4e4c-9033-5df0a68ec4c5.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-copper-chemical-symbol-underlined-d2287aae',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-u')
REFERENCE_EXPORT_SHA256 = '3268619828811d252186298e95971a6f1231cc0b5ab550fc7c4a26f5bd8924e0'

class Drawing(TextSub32):
    icon_id = 'text-copper-chemical-symbol-underlined-d2287aae-sub32'
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
        self.add_bezier('p2-r1-3', (26, 21), ((29, 21), (31, 19), (31, 16)))
        self.add_line('p2-r1-4', (31, 16), (31, 8))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_bezier('p3-r1-1', (14, 5), ((12, 3), (11, 2), (9, 2)))
        self.add_bezier('p3-r1-2', (9, 2), ((6, 2), (2, 6), (2, 12)))
        self.add_bezier('p3-r1-3', (2, 12), ((2, 17), (6, 21), (9, 21)))
        self.add_bezier('p3-r1-4', (9, 21), ((11, 21), (12, 20), (14, 18)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
