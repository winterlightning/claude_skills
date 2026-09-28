# Independent repair; parent preserved.
"""Independent 32px profile of bed.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '300dd66a-1ed3-4055-80d4-1d8fabe4b3ef'
SOURCE_PATH = 'pictographic-primitives/state/bed_300dd66a-1ed3-4055-80d4-1d8fabe4b3ef.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('300dd66a-1ed3-4055-80d4-1d8fabe4b3ef', 'pictographic-primitives/state/bed_300dd66a-1ed3-4055-80d4-1d8fabe4b3ef.svg'), ('95113cf8-8d4a-42f4-be40-9ff828544b7a', 'pictographic-primitives/symbol/bed_95113cf8-8d4a-42f4-be40-9ff828544b7a.svg'))
PROFILE_SOURCE_KEYS = ('solo/bed', 'solo/bed-symbol')
SOLO_SOURCE_ICON_IDS = ('bed', 'bed-symbol')
REFERENCE_EXPORT_SHA256 = '1367e16a7aaa6416e25a2ce6c9f814eda55b163a7f4fe47ac1ebdb65b9f80b42'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'bed-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('headpost', (2, 4), (2, 28))
        self.add_line('footpost', (30, 16), (30, 28))
        self.add_line('mattress-top', (2, 16), (30, 16))
        self.add_line('mattress-bottom', (2, 24), (30, 24))
        for rail in ('mattress-top', 'mattress-bottom'):
            for post in ('headpost', 'footpost'):
                self.relate('connect', rail, post)

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
REPAIR_PLAN = 'Bed posts and two mattress rails; eight-unit rail spacing.'
CONSTRUCTION_REFERENCE = 'bed'
