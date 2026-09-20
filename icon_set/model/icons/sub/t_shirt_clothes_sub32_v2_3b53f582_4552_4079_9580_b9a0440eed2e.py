"""Independent 32px profile of t-shirt-clothes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3b53f582-4552-4079-9580-b9a0440eed2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/clothes/t shirt_3b53f582-4552-4079-9580-b9a0440eed2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3b53f582-4552-4079-9580-b9a0440eed2e', 'pictographic-primitives/clothes/t shirt_3b53f582-4552-4079-9580-b9a0440eed2e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/t-shirt-clothes',)
SOLO_SOURCE_ICON_IDS = ('t-shirt-clothes',)
REFERENCE_EXPORT_SHA256 = '5b4e5ac8c022667cf3ac40dbb4523522c7474644542029ebea9addbaf6dbce02'

class DrawingVariant2(Sub32):
    icon_id = 't-shirt-clothes-sub32-v2'
    variant_of = 't-shirt-clothes-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'clothes'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """T-shirt with angled sleeves, round neck, upright torso and flat hem. Construction reference: shirt."""
        points = ((11, 2), (2, 8), (6, 16), (10, 14), (10, 30), (22, 30), (22, 14), (26, 16), (30, 8), (21, 2))
        for i, (a, b) in enumerate(zip(points, points[1:])):
            self.add_line(f'edge-{i}', a, b)
        self.add_arc('neck', (21, 2), (11, 2), radius_x=5)
        self.add_contour('shirt', *[f'edge-{i}' for i in range(9)], 'neck', closed=True)

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
