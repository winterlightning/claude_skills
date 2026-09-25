"""Independent 32px profile of tulip-with-curved-leaves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3d724858-fd0e-4b7f-a29c-165c62b8e0f2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/nature/flower_3d724858-fd0e-4b7f-a29c-165c62b8e0f2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3d724858-fd0e-4b7f-a29c-165c62b8e0f2', 'pictographic-primitives/nature/flower_3d724858-fd0e-4b7f-a29c-165c62b8e0f2.svg'), ('3e0aa5f5-7bc6-4864-acd6-4434c86246fe', 'pictographic-primitives/nature/flower_3e0aa5f5-7bc6-4864-acd6-4434c86246fe.svg'))
PROFILE_SOURCE_KEYS = ('solo/tulip-with-curved-leaves', 'solo/tulip-with-curved-leaves-alternate')
SOLO_SOURCE_ICON_IDS = ('tulip-with-curved-leaves', 'tulip-with-curved-leaves-alternate')
REFERENCE_EXPORT_SHA256 = '4464cc32a8460746dc9d4f9a337855db876c96b747153fcec5d7c6e817cd92dc'

class DrawingVariant2(Sub32):
    icon_id = 'tulip-with-curved-leaves-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tulip with two pointed upper petals, curved cup, straight stem and two curved leaves. Construction reference: flower-2."""
        self.add_line('petal-l', (7, 2), (16, 8))
        self.add_line('petal-r', (16, 8), (25, 2))
        self.add_line('petal-side', (25, 2), (25, 11))
        self.add_arc('cup', (25, 11), (7, 11), radius_x=9)
        self.add_line('left', (7, 11), (7, 2))
        self.add_contour('flower', 'petal-l', 'petal-r', 'petal-side', 'cup', 'left', closed=True)
        self.add_line('stem', (16, 20), (16, 30))
        self.relate('connect', 'stem', 'flower')
        for name, end, c1, c2 in [('leaf-l', (4, 24), (14, 26), (8, 24)), ('leaf-r', (28, 24), (18, 26), (24, 24))]:
            self.add_bezier(name, (16, 30), (c1, c2, end))
            self.relate('connect', name, 'stem')
        self.relate('connect', 'leaf-l', 'leaf-r')

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
