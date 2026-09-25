"""Independent 32px profile of tilted-cctv-camera-facing-right.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7ab0b15b-d8bf-4b7c-a79c-022333fdde6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/protection/surveillance cctv_7ab0b15b-d8bf-4b7c-a79c-022333fdde6c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7ab0b15b-d8bf-4b7c-a79c-022333fdde6c', 'pictographic-primitives/protection/surveillance cctv_7ab0b15b-d8bf-4b7c-a79c-022333fdde6c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tilted-cctv-camera-facing-right',)
SOLO_SOURCE_ICON_IDS = ('tilted-cctv-camera-facing-right',)
REFERENCE_EXPORT_SHA256 = '8aff0258405f85a8d935136eb394e179a0d49f0e6525e6b038c023d54897b435'

class DrawingVariant2(Sub32):
    icon_id = 'tilted-cctv-camera-facing-right-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    categories = ('protection', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tilted camera housing, separate front mark and curved bracket. Construction reference: cctv."""
        self.add_polyline('housing', (7, 4), (25, 10), (21, 24), (3, 18), closed=True)
        self.add_line('front', (30, 15), (28, 24))
        self.add_line('bracket-top', (12, 21), (12, 24))
        self.add_arc('bracket-bend', (12, 24), (8, 28), radius_x=4)
        self.add_line('bracket-base', (8, 28), (2, 28))
        self.add_contour('bracket', 'bracket-top', 'bracket-bend', 'bracket-base')
        self.relate('connect', 'bracket', 'housing')

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
