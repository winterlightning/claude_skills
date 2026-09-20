"""Independent 32px profile of text-css-web-styling-symbol-4e86ad2e.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '4e86ad2e-5a24-449c-8379-d7e832726bb6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-css-web-styling-symbol-4e86ad2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e86ad2e-5a24-449c-8379-d7e832726bb6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/CSS (text)_4e86ad2e-5a24-449c-8379-d7e832726bb6.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-css-web-styling-symbol-4e86ad2e',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'b19af96fc151c5083ee1937920decf50bbe98bc4011cc830f1829a0bc98dceb0'

class DrawingVariant2(TextSub32):
    icon_id = 'text-css-web-styling-symbol-4e86ad2e-sub32-v2'
    variant_of = 'text-css-web-styling-symbol-4e86ad2e-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 78
    text_ink_bounds = (0, 0, 77, 32)

    def build(self):
        """Shared typeface letter-c-uppercase, letter-s-uppercase, letter-s-uppercase; natural proportions, 32-unit ink height and integer fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_bezier('p1-r1-1', (19, 6), ((17, 3), (15, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((7, 2), (2, 8), (2, 16)))
        self.add_bezier('p1-r1-3', (2, 16), ((2, 24), (7, 30), (12, 30)))
        self.add_bezier('p1-r1-4', (12, 30), ((15, 30), (17, 29), (19, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (47, 6), ((46, 3), (42, 2), (39, 2)))
        self.add_bezier('p2-r1-2', (39, 2), ((35, 2), (31, 4), (30, 9)))
        self.add_bezier('p2-r1-3', (30, 9), ((30, 9), (30, 9), (30, 10)))
        self.add_bezier('p2-r1-4', (30, 10), ((30, 17), (47, 13), (47, 22)))
        self.add_bezier('p2-r1-5', (47, 22), ((47, 22), (47, 22), (47, 23)))
        self.add_bezier('p2-r1-6', (47, 23), ((47, 28), (43, 30), (38, 30)))
        self.add_bezier('p2-r1-7', (38, 30), ((34, 30), (31, 29), (29, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', 'p2-r1-5', 'p2-r1-6', 'p2-r1-7', closed=False)
        self.add_bezier('p3-r1-1', (75, 6), ((74, 3), (70, 2), (67, 2)))
        self.add_bezier('p3-r1-2', (67, 2), ((63, 2), (59, 4), (58, 9)))
        self.add_bezier('p3-r1-3', (58, 9), ((58, 9), (58, 9), (58, 10)))
        self.add_bezier('p3-r1-4', (58, 10), ((58, 17), (75, 13), (75, 22)))
        self.add_bezier('p3-r1-5', (75, 22), ((75, 22), (75, 22), (75, 23)))
        self.add_bezier('p3-r1-6', (75, 23), ((75, 28), (71, 30), (66, 30)))
        self.add_bezier('p3-r1-7', (66, 30), ((62, 30), (59, 29), (57, 26)))
        self.add_contour('path-3-1', 'p3-r1-1', 'p3-r1-2', 'p3-r1-3', 'p3-r1-4', 'p3-r1-5', 'p3-r1-6', 'p3-r1-7', closed=False)

def box(s, n, l, t, r, b, k=3):
    points = [(l + k, t), (r - k, t), (r, t + k), (r, b - k), (r - k, b), (l + k, b), (l, b - k), (l, t + k)]
    members = []
    for i, p in enumerate(points):
        q = points[(i + 1) % 8]
        name = f'{n}-{i}'
        if i % 2:
            s.add_arc(name, p, q, radius_x=k)
        else:
            s.add_line(name, p, q)
        members.append(name)
    s.add_contour(n, *members, closed=True)

def circle(s, n, cx, cy, r):
    s.add_arc(n + '-top', (cx - r, cy), (cx + r, cy), radius_x=r)
    s.add_arc(n + '-bottom', (cx + r, cy), (cx - r, cy), radius_x=r)
    s.add_contour(n, n + '-top', n + '-bottom', closed=True)
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-s-uppercase', 'letter-s-uppercase')
