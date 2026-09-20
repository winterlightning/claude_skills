# Independent repair; parent preserved.
"""Independent 32px profile of batch-01-laptop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0eca8bb8-75fe-4501-aa58-53ce337798cc'
SOURCE_PATH = 'pictographic-primitives/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0eca8bb8-75fe-4501-aa58-53ce337798cc', 'pictographic-primitives/computers/batch-01/laptop_0eca8bb8-75fe-4501-aa58-53ce337798cc.svg'),)
PROFILE_SOURCE_KEYS = ('solo/batch-01-laptop',)
SOLO_SOURCE_ICON_IDS = ('batch-01-laptop',)
REFERENCE_EXPORT_SHA256 = '7a8d541adbc07580400536eb9000ec61fff450b9862a40b2700ca972491e9215'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'batch-01-laptop-sub32'
    icon_id = 'batch-01-laptop-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'computers'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('left', (4, 20), (4, 7))
        self.add_arc('tl', (4, 7), (7, 4), radius_x=3)
        self.add_line('top', (7, 4), (25, 4))
        self.add_arc('tr', (25, 4), (28, 7), radius_x=3)
        self.add_line('right', (28, 7), (28, 20))
        self.add_line('bottom', (28, 20), (4, 20))
        self.add_contour('screen', 'left', 'tl', 'top', 'tr', 'right', 'bottom', closed=True)
        self.add_polyline('base', (4, 20), (2, 28), (30, 28), (28, 20))
        self.relate('connect', 'screen', 'base')

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
REPAIR_PLAN = 'Laptop screen and base, eight-unit centerline separation at base.'
CONSTRUCTION_REFERENCE = 'laptop'
