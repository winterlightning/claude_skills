"""Independent 32px profile of liras.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '986af714-6fb8-449a-ad31-d5271f278137'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/liras_986af714-6fb8-449a-ad31-d5271f278137.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('986af714-6fb8-449a-ad31-d5271f278137', 'pictographic-primitives/money/liras_986af714-6fb8-449a-ad31-d5271f278137.svg'),)
PROFILE_SOURCE_KEYS = ('solo/liras',)
SOLO_SOURCE_ICON_IDS = ('liras',)
REFERENCE_EXPORT_SHA256 = 'e40bd69750f4eb3147f9a383eb2bc20ab3339d4b8dabc691afe542e24fafce2a'

class DrawingVariant2(TextSub32):
    icon_id = 'liras-sub32-v2'
    variant_of = 'liras-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 27
    text_ink_bounds = (0, 0, 27, 32)

    def build(self):
        """Shared glyphs symbol-lira-two-bar at 32px ink height and natural width. Construction reference: shared typeface / geometric source construction."""
        self.add_bezier('g0-p1-r1-1', (23, 7), ((23, 4), (19, 2), (15, 2)))
        self.add_bezier('g0-p1-r1-2', (15, 2), ((11, 2), (7, 4), (7, 9)))
        self.add_line('g0-p1-r1-3', (7, 9), (7, 21))
        self.add_bezier('g0-p1-r1-4', (7, 21), ((7, 26), (5, 30), (2, 30)))
        self.add_line('g0-p1-r1-5', (2, 30), (25, 30))
        self.add_contour('g0-path-1-1', 'g0-p1-r1-1', 'g0-p1-r1-2', 'g0-p1-r1-3', 'g0-p1-r1-4', 'g0-p1-r1-5', closed=False)
        self.add_line('g0-p2-r1-1', (2, 12), (17, 12))
        self.add_contour('g0-path-2-1', 'g0-p2-r1-1', closed=False)
        self.add_line('g0-p3-r1-1', (2, 21), (17, 21))
        self.add_contour('g0-path-3-1', 'g0-p3-r1-1', closed=False)
        self.relate('connect', 'g0-path-2-1', 'g0-path-1-1')
        self.relate('connect', 'g0-path-3-1', 'g0-path-1-1')

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
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
TYPEFACE_GLYPH_IDS = ('symbol-lira-two-bar',)
