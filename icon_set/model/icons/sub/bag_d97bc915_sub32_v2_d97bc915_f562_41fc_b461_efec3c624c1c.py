"""Independent 32px profile of bag-d97bc915.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd97bc915-f562-41fc-b461-efec3c624c1c'
SOURCE_PATH = 'pictographic-primitives/shopping/bag_d97bc915-f562-41fc-b461-efec3c624c1c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d97bc915-f562-41fc-b461-efec3c624c1c', 'pictographic-primitives/shopping/bag_d97bc915-f562-41fc-b461-efec3c624c1c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bag-d97bc915',)
SOLO_SOURCE_ICON_IDS = ('bag-d97bc915',)
REFERENCE_EXPORT_SHA256 = '9006fe3a8677e5d01079cf7b1059cd6582231ad99323db8936cdfcfc74dd8bff'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'bag-d97bc915-sub32'
    icon_id = 'bag-d97bc915-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('bag', (4, 12), (28, 12), (30, 30), (2, 30), closed=True)
        self.add_line('handle-left', (11, 16), (11, 7))
        self.add_arc('handle-top', (11, 7), (21, 7), radius_x=5)
        self.add_line('handle-right', (21, 7), (21, 16))
        self.add_contour('handle', 'handle-left', 'handle-top', 'handle-right')
        self.relate('connect', 'bag', 'handle')

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
REPAIR_PLAN = 'Source trapezoid shopping bag with rounded handle; remove invented side panel.'
CONSTRUCTION_REFERENCE = 'shopping-bag'
