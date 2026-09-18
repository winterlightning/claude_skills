"""Independent 32px profile of text-mov-video-file-format-a126e323.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'a126e323-d53b-4fec-a13c-409a222a15c7'
SOURCE_PATH = 'icon_set/dist/text32/text-mov-video-file-format-a126e323.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a126e323-d53b-4fec-a13c-409a222a15c7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/mov (text)_a126e323-d53b-4fec-a13c-409a222a15c7.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-mov-video-file-format-a126e323',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-m-uppercase', 'letter-o-uppercase', 'letter-v-uppercase')
REFERENCE_EXPORT_SHA256 = 'a6ff874c9a98595bedb02bf7e02a0a3ed48ae89a09af9d19a1995732fd07dfcf'

class Drawing(TextSub32):
    icon_id = 'text-mov-video-file-format-a126e323-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 88
    text_ink_bounds = (0.0, 0.0, 88.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (64, 2), (73, 28))
        self.add_bezier('p1-r1-2', (73, 28), ((73.66666666666667, 29.333333333333332), (74.33333333333333, 30), (75, 30)))
        self.add_bezier('p1-r1-3', (75, 30), ((75.66666666666667, 30), (76, 29.333333333333332), (76, 28)))
        self.add_line('p1-r1-4', (76, 28), (86, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (36, 16), ((36, 8), (41, 2), (46, 2)))
        self.add_bezier('p2-r1-2', (46, 2), ((52, 2), (57, 8), (57, 16)))
        self.add_bezier('p2-r1-3', (57, 16), ((57, 24), (52, 30), (46, 30)))
        self.add_bezier('p2-r1-4', (46, 30), ((41, 30), (36, 24), (36, 16)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (2, 30), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (15, 20))
        self.add_line('p3-r1-3', (15, 20), (28, 2))
        self.add_line('p3-r1-4', (28, 2), (28, 30))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', closed=False)
