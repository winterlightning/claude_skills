"""Independent 32px profile of text-underlined-tm-symbol-45736507.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '45736507-40a8-4c9f-b6d6-8fab6aac23ed'
SOURCE_PATH = 'icon_set/dist/text32/text-underlined-tm-symbol-45736507.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('45736507-40a8-4c9f-b6d6-8fab6aac23ed', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/tm (text u)_45736507-40a8-4c9f-b6d6-8fab6aac23ed.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-underlined-tm-symbol-45736507',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-t-uppercase', 'letter-m')
REFERENCE_EXPORT_SHA256 = '436e87caa3a7ade8dc6dc489d063c08aa969bbbe638b3fa6033ddbba8d05d55a'

class Drawing(TextSub32):
    icon_id = 'text-underlined-tm-symbol-45736507-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 45
    text_ink_bounds = (0.0, 0.0, 45.0, 32.0)

    def build(self):
        self.add_line('p1-r1-1', (2, 30), (43, 30))
        self.add_contour('path-1-1', 'p1-r1-1', closed=False)
        self.add_line('p2-r1-1', (33, 13), (33, 21))
        self.add_contour('path-2-1', 'p2-r1-1', closed=False)
        self.add_line('p3-r1-1', (24, 21), (24, 13))
        self.add_bezier('p3-r1-2', (24, 13), ((24, 10), (26, 8), (28, 8)))
        self.add_bezier('p3-r1-3', (28, 8), ((31, 8), (33, 10), (33, 13)))
        self.add_bezier('p3-r1-4', (33, 13), ((33, 10), (35, 8), (38, 8)))
        self.add_bezier('p3-r1-5', (38, 8), ((40, 8), (43, 10), (43, 13)))
        self.add_line('p3-r1-6', (43, 13), (43, 21))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', closed=False)
        self.add_line('p4-r1-1', (2, 2), (17, 2))
        self.add_contour('path-4-1', 'p4-r1-1', closed=False)
        self.add_line('p5-r1-1', (9, 2), (9, 21))
        self.add_contour('path-5-1', 'p5-r1-1', closed=False)
        self.relate("connect", 'p2-r1-1', 'p3-r1-3')
        self.relate("connect", 'p2-r1-1', 'p3-r1-4')
