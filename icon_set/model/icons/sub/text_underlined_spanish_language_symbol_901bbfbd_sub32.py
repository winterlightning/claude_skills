"""Independent 32px profile of text-underlined-spanish-language-symbol-901bbfbd.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '901bbfbd-f392-4578-9592-ae246d76df6f'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-spanish-language-symbol-901bbfbd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('901bbfbd-f392-4578-9592-ae246d76df6f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/es (text u)_901bbfbd-f392-4578-9592-ae246d76df6f.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-spanish-language-symbol-901bbfbd',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-e-uppercase', 'letter-s')
REFERENCE_EXPORT_SHA256 = '6abc5108f0084f1ff460b9bf2941703eab18d18395c2fd230fd9e35387a5f127'

class Drawing(TextSub32):
    icon_id = 'text-underlined-spanish-language-symbol-901bbfbd-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 31
    text_ink_bounds = (0.0, 0.0, 31.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (29, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (29, 10), ((29, 10), (29, 8), (25, 8)))
        self.add_bezier('p2-r1-2', (25, 8), ((22, 8), (21, 10), (21, 11)))
        self.add_bezier('p2-r1-3', (21, 11), ((21, 12), (21, 13), (23, 14)))
        self.add_bezier('p2-r1-4', (23, 14), ((26, 15), (26, 15), (28, 16)))
        self.add_bezier('p2-r1-5', (28, 16), ((29, 16), (29, 17), (29, 18)))
        self.add_bezier('p2-r1-6', (29, 18), ((29, 19), (28, 21), (25, 21)))
        self.add_bezier('p2-r1-7', (25, 21), ((20, 21), (20, 19), (20, 19)))
        self.add_bezier('p2-r1-8', (20, 19), ((20, 19), (20, 19), (20, 19)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', 'p2-r1-8', closed=False)
        self.add_line('p3-r1-1', (14, 2), (2, 2))
        self.add_line('p3-r1-2', (2, 2), (2, 21))
        self.add_line('p3-r1-3', (2, 21), (14, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', closed=False)
        self.add_line('p4-r1-1', (2, 12), (12, 12))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
