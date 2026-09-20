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

class DrawingVariant2(Sub32):
    icon_id = 'measurement-marker-draft-batch-024-15-sub32-v2'
    variant_of = 'measurement-marker-draft-batch-024-15-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two rounded measurement jaws, short middle guide and right lower vertical with end tick. Construction reference: none."""
        self.add_line('top', (6, 2), (30, 2))
        self.add_arc('top-round', (6, 10), (6, 2), radius_x=4)
        self.add_polyline('top-jaw', (6, 10), (10, 10), (14, 2))
        self.relate('connect', 'top-jaw', 'top-round')
        self.relate('connect', 'top-jaw', 'top')
        self.relate('connect', 'top-round', 'top')
        self.add_line('middle', (20, 16), (30, 16))
        self.add_polyline('bottom-jaw', (6, 20), (10, 20), (14, 28))
        self.add_arc('bottom-round', (6, 28), (6, 20), radius_x=4)
        self.add_polyline('bottom', (6, 28), (30, 28), (30, 30), (29, 30))
        for a, b in [('bottom-jaw', 'bottom-round'), ('bottom-jaw', 'bottom'), ('bottom-round', 'bottom')]:
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
