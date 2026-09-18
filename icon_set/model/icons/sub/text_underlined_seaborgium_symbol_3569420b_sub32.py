"""Independent 32px profile of text-underlined-seaborgium-symbol-3569420b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '3569420b-b180-4388-8019-22de44d27527'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-seaborgium-symbol-3569420b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3569420b-b180-4388-8019-22de44d27527', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/sg (text u)_3569420b-b180-4388-8019-22de44d27527.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-seaborgium-symbol-3569420b',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-s-uppercase', 'letter-g')
REFERENCE_EXPORT_SHA256 = '1872de7942b484e73da6461708f90c4c7c8e940255e754ab0e3a15142c59baef'

class Drawing(TextSub32):
    icon_id = 'text-underlined-seaborgium-symbol-3569420b-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 28
    text_ink_bounds = (0.0, 0.0, 28.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (26, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (26, 14), (26, 9))
        self.add_bezier('p2-r1-2', (26, 9), ((26, 9), (26, 9), (26, 8)))
        self.add_bezier('p2-r1-3', (26, 8), ((25, 7), (24, 6), (22, 6)))
        self.add_bezier('p2-r1-4', (22, 6), ((20, 6), (17, 9), (17, 11)))
        self.add_bezier('p2-r1-5', (17, 11), ((17, 14), (20, 16), (22, 16)))
        self.add_bezier('p2-r1-6', (22, 16), ((24, 16), (26, 15), (26, 14)))
        self.add_line('p2-r1-7', (26, 14), (26, 17))
        self.add_bezier('p2-r1-8', (26, 17), ((26, 19), (24, 21), (22, 21)))
        self.add_line('p2-r1-9', (22, 21), (21, 21))
        self.add_bezier('p2-r1-10', (21, 21), ((20, 21), (18, 20), (18, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', 'p2-r1-9', 'p2-r1-10', closed=False)
        self.add_bezier('p3-r1-1', (11, 4), ((10, 3), (9, 2), (7, 2)))
        self.add_bezier('p3-r1-2', (7, 2), ((5, 2), (3, 3), (2, 5)))
        self.add_bezier('p3-r1-3', (2, 5), ((2, 6), (2, 6), (2, 6)))
        self.add_bezier('p3-r1-4', (2, 6), ((2, 10), (11, 8), (11, 12)))
        self.add_bezier('p3-r1-5', (11, 12), ((11, 12), (11, 12), (11, 12)))
        self.add_bezier('p3-r1-6', (11, 12), ((11, 15), (9, 16), (7, 16)))
        self.add_bezier('p3-r1-7', (7, 16), ((5, 16), (3, 15), (2, 14)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)
