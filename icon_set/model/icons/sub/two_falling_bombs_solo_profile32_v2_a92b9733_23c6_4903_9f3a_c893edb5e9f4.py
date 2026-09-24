"""Independent 32px profile of two-falling-bombs-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a92b9733-23c6-4903-9f3a-c893edb5e9f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/bombs_a92b9733-23c6-4903-9f3a-c893edb5e9f4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a92b9733-23c6-4903-9f3a-c893edb5e9f4', 'pictographic-primitives/state/bombs_a92b9733-23c6-4903-9f3a-c893edb5e9f4.svg'), ('c44044e2-1060-423d-b9c2-c927d9bf1777', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/bombs_c44044e2-1060-423d-b9c2-c927d9bf1777.svg'))
PROFILE_SOURCE_KEYS = ('solo/two-falling-bombs-solo',)
SOLO_SOURCE_ICON_IDS = ('two-falling-bombs-solo',)
REFERENCE_EXPORT_SHA256 = '541331099ccfba43b09640cdf3f213721080150ea2b320abe3b5a2af4a61cb6c'

class DrawingVariant2(Sub32):
    icon_id = 'two-falling-bombs-solo-profile32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two staggered falling bombs, each with an elongated rounded body and complete notched chevron tail. Construction reference: none."""
        for name, x, y in [('left', 2, 2), ('right', 22, 8)]:
            box(self, name + '-body', x, y + 10, x + 8, y + 22, 4)
            self.add_polyline(name + '-tail', (x, y), (x + 4, y + 3), (x + 8, y), (x + 8, y + 8), (x + 4, y + 10), (x, y + 8), closed=True)
            self.relate('connect', name + '-tail', name + '-body')

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
