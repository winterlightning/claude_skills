"""Independent 32px profile of managed-service-search.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f247c571-ece0-4e14-ab87-79542cc147ad'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/business/managed service search_f247c571-ece0-4e14-ab87-79542cc147ad.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f247c571-ece0-4e14-ab87-79542cc147ad', 'pictographic-primitives/business/managed service search_f247c571-ece0-4e14-ab87-79542cc147ad.svg'),)
PROFILE_SOURCE_KEYS = ('solo/managed-service-search',)
SOLO_SOURCE_ICON_IDS = ('managed-service-search',)
REFERENCE_EXPORT_SHA256 = '656440a3f26cdafe16d3d8195de80e8a5e75427797efdd258be0621b11e7783f'

class DrawingVariant2(Sub32):
    icon_id = 'managed-service-search-sub32-v2'
    variant_of = 'managed-service-search-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular search lens with lower-right handle and connected activity pulse. Construction reference: search-activity (local reference unavailable)."""
        circle(self, 'lens', 15, 15, 13)
        self.add_line('handle', (24, 24), (30, 30))
        self.relate('connect', 'handle', 'lens')
        self.add_polyline('pulse', (2, 15), (8, 15), (10, 19), (14, 9), (18, 21), (20, 13), (21, 13))
        self.relate('connect', 'pulse', 'lens')

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
