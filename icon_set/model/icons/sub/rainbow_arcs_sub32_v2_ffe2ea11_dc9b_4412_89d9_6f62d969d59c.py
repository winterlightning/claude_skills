"""Independent 32px profile of rainbow-arcs.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ffe2ea11-dc9b-4412-89d9-6f62d969d59c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/rainbow_ffe2ea11-dc9b-4412-89d9-6f62d969d59c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ffe2ea11-dc9b-4412-89d9-6f62d969d59c', 'pictographic-primitives/symbol/rainbow_ffe2ea11-dc9b-4412-89d9-6f62d969d59c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rainbow-arcs',)
SOLO_SOURCE_ICON_IDS = ('rainbow-arcs',)
REFERENCE_EXPORT_SHA256 = 'dcdb5a295e2a9ffe1d326ffeb613ed7bba7e24a93b9b05789dcfeed462075113'

class DrawingVariant2(Sub32):
    icon_id = 'rainbow-arcs-sub32-v2'
    variant_of = 'rainbow-arcs-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three concentric open rainbow semicircles, all retaining open undersides. Small-size treatment: Reduced three rainbow bands to two clear open arcs. Construction reference: rainbow: shared center and three arc radii."""
        self.add_arc('outer', (2, 22), (30, 22), radius_x=14, radius_y=12)
        self.add_arc('inner', (10, 22), (22, 22), radius_x=6, radius_y=5)

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
