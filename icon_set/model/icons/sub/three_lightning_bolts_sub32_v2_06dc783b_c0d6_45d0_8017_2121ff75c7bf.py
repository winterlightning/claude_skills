"""Independent 32px profile of three-lightning-bolts-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '06dc783b-c0d6-45d0-8017-2121ff75c7bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/thunder heavy_06dc783b-c0d6-45d0-8017-2121ff75c7bf.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('06dc783b-c0d6-45d0-8017-2121ff75c7bf', 'pictographic-primitives/state/thunder heavy_06dc783b-c0d6-45d0-8017-2121ff75c7bf.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-lightning-bolts-solo',)
SOLO_SOURCE_ICON_IDS = ('three-lightning-bolts-solo',)
REFERENCE_EXPORT_SHA256 = '5dde48edd89c3fc235d34bb3eddd75ceb154bf98c751b8187c1dcc74ea221f44'

class DrawingVariant2(Sub32):
    icon_id = 'three-lightning-bolts-sub32-v2'
    variant_of = 'three-lightning-bolts-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three separate matching vertical lightning zigzags. Construction reference: zap."""
        for i, x in enumerate((2, 13, 25)):
            self.add_polyline(f'bolt-{i}', (x + 5, 4), (x, 16), (x + 5, 16), (x, 28))

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
