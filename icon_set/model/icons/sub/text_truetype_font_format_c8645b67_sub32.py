"""Independent 32px profile of text-truetype-font-format-c8645b67.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'c8645b67-a98b-429c-9c1d-33100a9270ba'
SOURCE_PATH = 'icon_set/dist/text32/text-truetype-font-format-c8645b67.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c8645b67-a98b-429c-9c1d-33100a9270ba', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/ttf (text)_c8645b67-a98b-429c-9c1d-33100a9270ba.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-truetype-font-format-c8645b67',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-t-uppercase', 'letter-f-uppercase')
REFERENCE_EXPORT_SHA256 = '164d3b85c3e0939f6430517ef559cacf7a1cd80585019ee25f498d6340383f52'

class Drawing(TextSub32):
    icon_id = 'text-truetype-font-format-c8645b67-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 80
    text_ink_bounds = (0.0, 0.0, 80.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (78, 2), (61, 2))
        self.add_line('p1-r1-2', (61, 2), (61, 30))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', closed=False)
        self.add_line('p2-r1-1', (61, 16), (75, 16))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (32, 2), (53, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (43, 2), (43, 30))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (2, 2), (24, 2))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.add_line('p6-r1-1', (13, 2), (13, 30))
        self.add_contour('path-6-1', 'p6-r1-1', closed=False)
