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

class DrawingVariant2(Sub32):
    icon_id = 'coins-sub32-v2'
    variant_of = 'coins-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'money'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two concentric coin circles and a short central vertical currency stroke. Construction reference: coins."""
        circle(self, 'frame', 16, 16, 14)
        pts = [(16, 9), (23, 16), (16, 23), (9, 16), (16, 9)]
        for i, (a, b) in enumerate(zip(pts, pts[1:])):
            self.add_arc(f'inner-{i}', a, b, radius_x=7)
        self.add_contour('inner', *[f'inner-{i}' for i in range(4)], closed=True)
        self.add_line('mark', (16, 15), (16, 17))

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
