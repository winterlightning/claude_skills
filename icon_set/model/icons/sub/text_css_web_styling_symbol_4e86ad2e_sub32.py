"""Independent 32px profile of text-css-web-styling-symbol-4e86ad2e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32

SOURCE_ICON_ID = '4e86ad2e-5a24-449c-8379-d7e832726bb6'
SOURCE_PATH = 'icon_set/dist/text32/text-css-web-styling-symbol-4e86ad2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e86ad2e-5a24-449c-8379-d7e832726bb6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/CSS (text)_4e86ad2e-5a24-449c-8379-d7e832726bb6.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-css-web-styling-symbol-4e86ad2e',)
SOLO_SOURCE_ICON_IDS = ()
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-s-uppercase', 'letter-s-uppercase')
REFERENCE_EXPORT_SHA256 = 'b19af96fc151c5083ee1937920decf50bbe98bc4011cc830f1829a0bc98dceb0'

class Drawing(TextSub32):
    icon_id = 'text-css-web-styling-symbol-4e86ad2e-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    text_canvas_width = 74
    text_ink_bounds = (0.001457877762348403, 0.0, 74.0, 32.0)

    def build(self):
        self.add_bezier('p1-r1-1', (71, 6), ((70, 3), (67, 2), (63, 2)))
        self.add_bezier('p1-r1-2', (63, 2), ((59, 2), (55, 4), (54, 9)))
        self.add_bezier('p1-r1-3', (54, 9), ((54, 9), (54, 9), (54, 10)))
        self.add_bezier('p1-r1-4', (54, 10), ((54, 17), (71, 13), (72, 22)))
        self.add_bezier('p1-r1-5', (72, 22), ((72, 22), (72, 22), (72, 23)))
        self.add_bezier('p1-r1-6', (72, 23), ((72, 28), (67, 30), (62, 30)))
        self.add_bezier('p1-r1-7', (62, 30), ((59, 30), (55, 29), (53, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', 'p1-r1-6', 'p1-r1-7', closed=False)
        self.add_bezier('p2-r1-1', (45, 6), ((44, 3), (40, 2), (37, 2)))
        self.add_bezier('p2-r1-2', (37, 2), ((33, 2), (29, 4), (28, 9)))
        self.add_bezier('p2-r1-3', (28, 9), ((28, 9), (28, 9), (28, 10)))
        self.add_bezier('p2-r1-4', (28, 10), ((28, 17), (45, 13), (45, 22)))
        self.add_bezier('p2-r1-5', (45, 22), ((46, 22), (46, 22), (46, 23)))
        self.add_bezier('p2-r1-6', (46, 23), ((46, 28), (41, 30), (36, 30)))
        self.add_bezier('p2-r1-7', (36, 30), ((32, 30), (29, 29), (27, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_arc('p3-r1-1', (19, 6), (19, 26), radius_x=10, radius_y=14, large_arc=True, sweep=False)
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
