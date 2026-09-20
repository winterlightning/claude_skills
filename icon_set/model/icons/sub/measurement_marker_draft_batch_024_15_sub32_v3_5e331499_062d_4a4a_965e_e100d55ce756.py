"""Independent 32px profile of measurement-marker-draft-batch-024-15.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5e331499-062d-4a4a-965e-e100d55ce756'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e331499-062d-4a4a-965e-e100d55ce756', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/measurement markers_5e331499-062d-4a4a-965e-e100d55ce756.svg'),)
PROFILE_SOURCE_KEYS = ('solo/measurement-marker-draft-batch-024-15',)
SOLO_SOURCE_ICON_IDS = ('measurement-marker-draft-batch-024-15',)
REFERENCE_EXPORT_SHA256 = '87c7e406c9b43dd8ea797baabb748d1eb350ef001b0658e1a16b8ee683f20445'

class DrawingVariant3(Sub32):
    icon_id = 'measurement-marker-draft-batch-024-15-sub32-v3'
    variant_of = 'measurement-marker-draft-batch-024-15-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two rounded measurement jaws, separate middle guide and lower-right vertical extension. Construction reference: none."""
        self.add_line('top', (6, 2), (30, 2))
        self.add_arc('top-round', (6, 10), (6, 2), radius_x=4)
        self.add_polyline('top-jaw', (6, 10), (10, 10), (14, 2))
        for a, b in [('top', 'top-round'), ('top', 'top-jaw'), ('top-round', 'top-jaw')]:
            self.relate('connect', a, b)
        self.add_line('guide', (22, 18), (30, 18))
        self.add_arc('bottom-round', (6, 26), (6, 18), radius_x=4)
        self.add_polyline('bottom-jaw', (6, 18), (10, 18), (14, 26))
        self.add_polyline('bottom', (6, 26), (30, 26), (30, 30))
        for a, b in [('bottom', 'bottom-round'), ('bottom', 'bottom-jaw'), ('bottom-round', 'bottom-jaw')]:
            self.relate('connect', a, b)

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
