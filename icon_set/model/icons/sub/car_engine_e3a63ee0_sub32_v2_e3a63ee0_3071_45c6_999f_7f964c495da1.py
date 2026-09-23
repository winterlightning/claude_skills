# Independent repair; parent preserved.
"""Independent 32px profile of car-engine-e3a63ee0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e3a63ee0-3071-45c6-999f-7f964c495da1'
SOURCE_PATH = 'pictographic-primitives/transportation/car engine_e3a63ee0-3071-45c6-999f-7f964c495da1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e3a63ee0-3071-45c6-999f-7f964c495da1', 'pictographic-primitives/transportation/car engine_e3a63ee0-3071-45c6-999f-7f964c495da1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-engine-e3a63ee0',)
SOLO_SOURCE_ICON_IDS = ('car-engine-e3a63ee0',)
REFERENCE_EXPORT_SHA256 = 'dfac30424efb30f536d2f35ae82f55be693c5f26c5dc6c4936eaaf572dfc9203'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'car-engine-e3a63ee0-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('body', (2, 16), (10, 16), (10, 12), (22, 12), (26, 18), (30, 18), (30, 28), (15, 28), (10, 24), (2, 24))
        self.add_line('end', (2, 12), (2, 28))
        self.add_line('stem', (16, 4), (16, 12))
        self.add_line('cap', (11, 4), (21, 4))
        self.relate('connect', 'body', 'end')
        self.relate('connect', 'body', 'stem')
        self.relate('connect', 'stem', 'cap')

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
REPAIR_PLAN = 'Engine outline, top stem and cap, left shaft and end marker.'
CONSTRUCTION_REFERENCE = 'car'
