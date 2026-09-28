"""Independent 32px profile of airplane-other.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4a625cc1-8989-433b-89db-ddf1b6a98ffe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4a625cc1-8989-433b-89db-ddf1b6a98ffe', 'pictographic-primitives/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airplane-other',)
SOLO_SOURCE_ICON_IDS = ('airplane-other',)
REFERENCE_EXPORT_SHA256 = '71fea4c7397e16d0129ef815a68871c7c07a8e6f98d58b1d3e6ee8094214d97e'

class DrawingVariant4(Sub32):
    icon_id = 'airplane-other-sub32-v4'
    variant_of = 'airplane-other-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Diagonal aircraft facing upper-right, rounded nose, broad swept wing and notched lower-left tail. Construction reference: plane: coherent rounded nose and diagonal outer silhouette."""
        points = ((2, 26), (5, 20), (10, 22), (16, 18), (2, 10), (10, 2), (22, 10), (26, 6))
        for i, (a, b) in enumerate(zip(points, points[1:])):
            self.add_line(f'edge-{i}', a, b)
        self.add_bezier('nose-top', (26, 6), ((28, 4), (30, 4), (30, 8)))
        self.add_bezier('nose-bottom', (30, 8), ((30, 12), (30, 14), (28, 16)))
        self.add_line('body-bottom', (28, 16), (14, 28))
        self.add_bezier('tail-bottom', (14, 28), ((13, 29), (13, 30), (12, 30)))
        self.add_bezier('tail-round', (12, 30), ((10, 30), (11, 29), (8, 28)))
        self.add_line('tail-close', (8, 28), (2, 26))
        self.add_contour('plane', *[f'edge-{i}' for i in range(7)], 'nose-top', 'nose-bottom', 'body-bottom', 'tail-bottom', 'tail-round', 'tail-close', closed=True)

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
