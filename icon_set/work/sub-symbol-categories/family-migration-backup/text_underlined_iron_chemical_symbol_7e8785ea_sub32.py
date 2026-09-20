"""Independent 32px profile of text-underlined-iron-chemical-symbol-7e8785ea.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '7e8785ea-6365-46e1-b990-86ec3b98e585'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-iron-chemical-symbol-7e8785ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7e8785ea-6365-46e1-b990-86ec3b98e585', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fe (text u)_7e8785ea-6365-46e1-b990-86ec3b98e585.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-iron-chemical-symbol-7e8785ea',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-f-uppercase', 'letter-e')
REFERENCE_EXPORT_SHA256 = 'c190e616807baafde2d59c6763608ae7c55793124deddbaf6b5d58f643485540'

class Drawing(TextSub32):
    icon_id = 'text-underlined-iron-chemical-symbol-7e8785ea-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 36
    text_ink_bounds = (0.0, 0.0, 36.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (34, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_bezier('p2-r1-1', (34, 15), ((34, 11), (31, 8), (27, 8)))
        self.add_bezier('p2-r1-2', (27, 8), ((23, 8), (20, 11), (20, 15)))
        self.add_bezier('p2-r1-3', (20, 15), ((20, 18), (23, 21), (27, 21)))
        self.add_bezier('p2-r1-4', (27, 21), ((29, 21), (32, 20), (33, 18)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (20, 15), (34, 15))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
        self.add_line('p4-r1-1', (14, 2), (2, 2))
        self.add_line('p4-r1-2', (2, 2), (2, 21))
        self.add_contour('path-4-1', 'p4-r1-1', 'p4-r1-2', closed=False)
        self.add_line('p5-r1-1', (2, 12), (12, 12))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-1')
        self.relate("connect", 'p2-r1-2', 'p3-r1-1')
        self.relate("connect", 'p2-r1-3', 'p3-r1-1')
