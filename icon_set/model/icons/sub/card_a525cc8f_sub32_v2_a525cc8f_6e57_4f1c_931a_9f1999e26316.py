# Independent repair; parent preserved.
"""Independent 32px profile of card-a525cc8f.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a525cc8f-6e57-4f1c-931a-9f1999e26316'
SOURCE_PATH = 'pictographic-primitives/business/card_a525cc8f-6e57-4f1c-931a-9f1999e26316.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a525cc8f-6e57-4f1c-931a-9f1999e26316', 'pictographic-primitives/business/card_a525cc8f-6e57-4f1c-931a-9f1999e26316.svg'),)
PROFILE_SOURCE_KEYS = ('solo/card-a525cc8f',)
SOLO_SOURCE_ICON_IDS = ('card-a525cc8f',)
REFERENCE_EXPORT_SHA256 = '83cf2dfd353fa8a2169657a02a78af2808d74426525de8da3605902600dab092'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'card-a525cc8f-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'business'
    categories = ('primitives', 'business')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        box(self, 'card', 2, 4, 30, 28, 3)
        self.add_line('mark', (20, 20), (22, 20))

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
REPAIR_PLAN = 'Rounded card with original short horizontal mark.'
CONSTRUCTION_REFERENCE = 'laptop'
