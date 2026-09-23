"""Independent 32px profile of shop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/shopping/shop_0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca', 'pictographic-primitives/shopping/shop_0f2a4c7f-e2ba-49a8-9de9-86dd5ecb7dca.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shop',)
SOLO_SOURCE_ICON_IDS = ('shop',)
REFERENCE_EXPORT_SHA256 = '0f32fc330b5c8b5a33166cb8d011feeba756f88f76d45438a1ce7929b2922ad7'

class DrawingVariant2(Sub32):
    icon_id = 'shop-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Store front under tapered awning with FOUR scallops, as in the source. Construction reference: store."""
        self.add_polyline('roof', (2, 12), (6, 4), (26, 4), (30, 12))
        for i in range(4):
            self.add_arc(f'scallop-{i}', (30 - 7 * i, 12), (23 - 7 * i, 12), radius_x=4)
        self.add_contour('scallops', *[f'scallop-{i}' for i in range(4)])
        self.relate('connect', 'roof', 'scallops')
        self.add_polyline('front', (4, 13), (4, 28), (28, 28), (28, 13))
        self.relate('connect', 'front', 'scallops')

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
