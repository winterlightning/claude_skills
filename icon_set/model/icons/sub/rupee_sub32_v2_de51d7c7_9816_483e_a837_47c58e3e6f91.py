"""Independent 32px profile of rupee.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = 'de51d7c7-9816-483e-a837-47c58e3e6f91'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/rupee_de51d7c7-9816-483e-a837-47c58e3e6f91.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('de51d7c7-9816-483e-a837-47c58e3e6f91', 'pictographic-primitives/money/rupee_de51d7c7-9816-483e-a837-47c58e3e6f91.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rupee',)
SOLO_SOURCE_ICON_IDS = ('rupee',)
REFERENCE_EXPORT_SHA256 = 'd536f4e4b92b12d08bb5b92748218d185264fe9015b95befd0da3660c8abd9fc'

class DrawingVariant2(TextSub32):
    icon_id = 'rupee-sub32-v2'
    variant_of = 'rupee-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 28
    text_ink_bounds = (0, 0, 27, 32)

    def build(self):
        """Shared glyphs symbol-rupee at 32px ink height and natural width. Construction reference: shared typeface / geometric source construction."""
        self.add_line('g0-p1-r1-1', (2, 2), (25, 2))
        self.add_contour('g0-path-1-1', 'g0-p1-r1-1', closed=False)
        self.add_line('g0-p2-r1-1', (2, 12), (25, 12))
        self.add_contour('g0-path-2-1', 'g0-p2-r1-1', closed=False)
        self.add_bezier('g0-p3-r1-1', (17, 2), ((17, 15), (15, 20), (2, 20)))
        self.add_line('g0-p3-r1-2', (2, 20), (22, 30))
        self.add_contour('g0-path-3-1', 'g0-p3-r1-1', 'g0-p3-r1-2', closed=False)
        self.relate('connect', 'g0-path-3-1', 'g0-path-1-1')
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
TYPEFACE_GLYPH_IDS = ('symbol-rupee',)
