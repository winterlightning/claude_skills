"""Independent 32px profile of text-underlined-nb-symbol-bd2eab8d.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = 'bd2eab8d-8295-4dde-8483-1d280094910a'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-nb-symbol-bd2eab8d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bd2eab8d-8295-4dde-8483-1d280094910a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/nb (text u)_bd2eab8d-8295-4dde-8483-1d280094910a.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-nb-symbol-bd2eab8d',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-n-uppercase', 'letter-b')
REFERENCE_EXPORT_SHA256 = 'a6a5bec119e0ec875001873db08b22725e37b656c575bbb2387d76e3e4709ddc'

class Drawing(TextSub32):
    icon_id = 'text-underlined-nb-symbol-bd2eab8d-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 37
    text_ink_bounds = (0.0, 0.0, 37.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (35, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (22, 18), ((24, 20), (26, 21), (28, 21)))
        self.add_bezier('p2-r1-2', (28, 21), ((32, 21), (35, 18), (35, 15)))
        self.add_bezier('p2-r1-3', (35, 15), ((35, 11), (32, 8), (28, 8)))
        self.add_bezier('p2-r1-4', (28, 8), ((26, 8), (24, 9), (23, 11)))
        self.add_bezier('p2-r1-5', (23, 11), ((23, 11), (22, 11), (22, 12)))
        self.add_line('p2-r1-6', (22, 12), (22, 18))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', closed=False)
        self.add_line('p3-r1-1', (22, 12), (22, 2))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (2, 21), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (16, 21))
        self.add_line('p4-r1-3', (16, 21), (16, 2))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', 'p4-r1-3', closed=False)
        self.relate("connect", 'p2-r1-5', 'p3-r1-1')
        self.relate("connect", 'p2-r1-6', 'p3-r1-1')
