"""Independent 32px profile of prescription-px.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '75d310c2-6d65-443d-b092-89dae29f9457'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/prescription px_75d310c2-6d65-443d-b092-89dae29f9457.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('75d310c2-6d65-443d-b092-89dae29f9457', 'pictographic-primitives/health/prescription px_75d310c2-6d65-443d-b092-89dae29f9457.svg'),)
PROFILE_SOURCE_KEYS = ('solo/prescription-px',)
SOLO_SOURCE_ICON_IDS = ('prescription-px',)
REFERENCE_EXPORT_SHA256 = 'bc4bb7535cfbc24db8f065e65ca4baffab987de25ff769d0bb1fcc5995da839f'

class DrawingVariant2(TextSub32):
    icon_id = 'prescription-px-sub32-v2'
    variant_of = 'prescription-px-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 27
    text_ink_bounds = (0, 0, 27, 32)

    def build(self):
        """Shared glyphs symbol-prescription at 32px ink height and natural width. Construction reference: shared typeface / geometric source construction."""
        self.add_line('g0-p1-r1-1', (2, 29), (2, 2))
        self.add_line('g0-p1-r1-2', (2, 2), (12, 2))
        self.add_bezier('g0-p1-r1-3', (12, 2), ((18, 2), (21, 6), (21, 9)))
        self.add_bezier('g0-p1-r1-4', (21, 9), ((21, 13), (18, 16), (12, 16)))
        self.add_line('g0-p1-r1-5', (12, 16), (2, 16))
        self.add_contour('g0-path-1-1', 'g0-p1-r1-1', 'g0-p1-r1-2', 'g0-p1-r1-3', 'g0-p1-r1-4', 'g0-p1-r1-5', closed=False)
        self.add_line('g0-p2-r1-1', (12, 16), (25, 29))
        self.add_contour('g0-path-2-1', 'g0-p2-r1-1', closed=False)
        self.add_line('g0-p3-r1-1', (25, 17), (11, 30))
        self.add_contour('g0-path-3-1', 'g0-p3-r1-1', closed=False)
        self.relate('connect', 'g0-p1-r1-4', 'g0-p2-r1-1')
        self.relate('connect', 'g0-p1-r1-5', 'g0-p2-r1-1')
        self.relate('connect', 'g0-path-2-1', 'g0-path-1-1')
        self.relate('connect', 'g0-path-3-1', 'g0-path-2-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-prescription',)
