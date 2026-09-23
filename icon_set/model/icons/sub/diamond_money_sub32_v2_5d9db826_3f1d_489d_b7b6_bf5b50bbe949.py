"""Independent 32px profile of diamond-money.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5d9db826-3f1d-489d-b7b6-bf5b50bbe949'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/diamond_5d9db826-3f1d-489d-b7b6-bf5b50bbe949.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5d9db826-3f1d-489d-b7b6-bf5b50bbe949', 'pictographic-primitives/money/diamond_5d9db826-3f1d-489d-b7b6-bf5b50bbe949.svg'),)
PROFILE_SOURCE_KEYS = ('solo/diamond-money',)
SOLO_SOURCE_ICON_IDS = ('diamond-money',)
REFERENCE_EXPORT_SHA256 = '2a0c5306cbdd87ab938391e3c8e1d687d04e1fed025b6426bc4ed454a87a9ae0'

class DrawingVariant2(Sub32):
    icon_id = 'diamond-money-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Diamond outline with one horizontal and one vertical facet divider, as in original. Construction reference: gem."""
        self.add_polyline('diamond', (8, 4), (24, 4), (30, 12), (16, 28), (2, 12), closed=True)
        self.add_line('crossbar', (2, 12), (30, 12))
        self.add_line('center', (16, 4), (16, 28))
        self.relate('connect', 'crossbar', 'diamond')
        self.relate('connect', 'center', 'diamond')
        self.relate('connect', 'center', 'crossbar')

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
