"""Independent 32px profile of kips.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._text_base import TextSub32
SOURCE_ICON_ID = '53a2b4a3-1baf-47dc-a7f6-5760e32d3d59'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/kips_53a2b4a3-1baf-47dc-a7f6-5760e32d3d59.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('53a2b4a3-1baf-47dc-a7f6-5760e32d3d59', 'pictographic-primitives/money/kips_53a2b4a3-1baf-47dc-a7f6-5760e32d3d59.svg'),)
PROFILE_SOURCE_KEYS = ('solo/kips',)
SOLO_SOURCE_ICON_IDS = ('kips',)
REFERENCE_EXPORT_SHA256 = '82cb25dba3107a4eb4ff98100e292dc7d27f165f3e51479e119c93d7391716e9'

class DrawingVariant2(TextSub32):
    icon_id = 'kips-sub32-v2'
    variant_of = 'kips-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS
    text_canvas_width = 35
    text_ink_bounds = (0, 0, 35, 32)

    def build(self):
        """Shared glyphs symbol-kip at 32px ink height and natural width. Construction reference: shared typeface / geometric source construction."""
        self.add_line('g0-p1-r1-1', (8, 2), (8, 30))
        self.add_contour('g0-path-1-1', 'g0-p1-r1-1', closed=False)
        self.add_line('g0-p2-r1-1', (28, 2), (8, 17))
        self.add_line('g0-p2-r1-2', (8, 17), (28, 30))
        self.add_contour('g0-path-2-1', 'g0-p2-r1-1', 'g0-p2-r1-2', closed=False)
        self.add_line('g0-p3-r1-1', (2, 17), (33, 17))
        self.add_contour('g0-path-3-1', 'g0-p3-r1-1', closed=False)
        self.relate('connect', 'g0-path-2-1', 'g0-path-1-1')
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
TYPEFACE_GLYPH_IDS = ('symbol-kip',)
