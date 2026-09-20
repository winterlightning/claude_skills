"""Independent 32px profile of text-closed-captions-icon-90913ece.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '90913ece-3e45-4b69-b088-eabf18ccdedd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/text32/text-closed-captions-icon-90913ece.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('90913ece-3e45-4b69-b088-eabf18ccdedd', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/text/CC (text)_90913ece-3e45-4b69-b088-eabf18ccdedd.svg'),)
PROFILE_SOURCE_KEYS = ('text/text-closed-captions-icon-90913ece',)
SOLO_SOURCE_ICON_IDS = ()
REFERENCE_EXPORT_SHA256 = 'd5c06a774548f8e70b46e2a2c7ff4919f2a93cfb8ff8f020c692bb5da22fc2ae'

class DrawingVariant2(TextSub32):
    icon_id = 'text-closed-captions-icon-90913ece-sub32-v2'
    variant_of = 'text-closed-captions-icon-90913ece-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 48
    text_ink_bounds = (0, 0, 47, 32)

    def build(self):
        """Shared typeface letter-c-uppercase, letter-c-uppercase; natural proportions, 32-unit ink height and grid-fitted layout. Construction reference: icon_set/typeface/glyphs.json."""
        self.add_bezier('p1-r1-1', (19, 6), ((17, 3), (15, 2), (12, 2)))
        self.add_bezier('p1-r1-2', (12, 2), ((7, 2), (2, 8), (2, 16)))
        self.add_bezier('p1-r1-3', (2, 16), ((2, 24), (7, 30), (12, 30)))
        self.add_bezier('p1-r1-4', (12, 30), ((15, 30), (17, 29), (19, 26)))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', closed=False)
        self.add_bezier('p2-r1-1', (45, 6), ((43, 3), (41, 2), (38, 2)))
        self.add_bezier('p2-r1-2', (38, 2), ((33, 2), (28, 8), (28, 16)))
        self.add_bezier('p2-r1-3', (28, 16), ((28, 24), (33, 30), (38, 30)))
        self.add_bezier('p2-r1-4', (38, 30), ((41, 30), (43, 29), (45, 26)))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)

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
TYPEFACE_GLYPH_IDS = ('letter-c-uppercase', 'letter-c-uppercase')
