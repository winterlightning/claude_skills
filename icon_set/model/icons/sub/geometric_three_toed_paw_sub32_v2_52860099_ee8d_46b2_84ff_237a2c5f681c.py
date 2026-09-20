"""Independent 32px profile of geometric-three-toed-paw.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '52860099-ee8d-46b2-84ff-237a2c5f681c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_52860099-ee8d-46b2-84ff-237a2c5f681c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('52860099-ee8d-46b2-84ff-237a2c5f681c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_52860099-ee8d-46b2-84ff-237a2c5f681c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/geometric-three-toed-paw',)
SOLO_SOURCE_ICON_IDS = ('geometric-three-toed-paw',)
REFERENCE_EXPORT_SHA256 = '39b268cd29b8fe180b12d9648e587752d662b0b77bb4626884bab91668a81a4f'

class DrawingVariant2(Sub32):
    icon_id = 'geometric-three-toed-paw-sub32-v2'
    variant_of = 'geometric-three-toed-paw-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three circular toes around a triangular paw pad. Construction reference: paw-print."""
        for name, x, y in [('top', 16, 6), ('left', 6, 16), ('right', 26, 16)]:
            circle(self, name, x, y, 4)
        self.add_polyline('pad', (6, 30), (16, 21), (26, 30), closed=True)

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
