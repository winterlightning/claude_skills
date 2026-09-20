"""Independent 32px profile of coins.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5cabb173-08d9-478c-9912-5357cbf2ed85'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/money/coins_5cabb173-08d9-478c-9912-5357cbf2ed85.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5cabb173-08d9-478c-9912-5357cbf2ed85', 'pictographic-primitives/money/coins_5cabb173-08d9-478c-9912-5357cbf2ed85.svg'),)
PROFILE_SOURCE_KEYS = ('solo/coins',)
SOLO_SOURCE_ICON_IDS = ('coins',)
REFERENCE_EXPORT_SHA256 = 'e854f337b3c543c33ad1270a1e8e9c07bc89b4d44151b16c98832b1db2691547'

class DrawingVariant3(Sub32):
    icon_id = 'coins-sub32-v3'
    variant_of = 'coins-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two concentric coin outlines. Construction reference: circle: consistent circular centerlines."""
        circle(self, 'outer', 16, 16, 14)
        circle(self, 'inner', 16, 16, 7)

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
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
