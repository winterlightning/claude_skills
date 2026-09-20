# Independent repair; parent preserved.
"""Independent 32px profile of airplane-horizontal.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0e73af01-7338-412e-b76b-79b5b693ad46'
SOURCE_PATH = 'pictographic-primitives/symbol/plane horizontal_0e73af01-7338-412e-b76b-79b5b693ad46.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0e73af01-7338-412e-b76b-79b5b693ad46', 'pictographic-primitives/symbol/plane horizontal_0e73af01-7338-412e-b76b-79b5b693ad46.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airplane-horizontal',)
SOLO_SOURCE_ICON_IDS = ('airplane-horizontal',)
REFERENCE_EXPORT_SHA256 = '1ced619c9f7ceac5ee7827e4a839b108a5f50ff8d495a43abca8958dbf401f3c'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'airplane-horizontal-sub32'
    icon_id = 'airplane-horizontal-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('upper', (2, 10), (8, 12), (12, 12), (9, 4), (15, 4), (22, 12), (26, 12))
        self.add_arc('nose', (26, 12), (26, 20), radius_x=4)
        self.add_polyline('lower', (26, 20), (22, 20), (15, 28), (9, 28), (12, 20), (8, 20), (2, 22), (5, 16), (2, 10))
        self.relate('connect', 'upper', 'nose')
        self.relate('connect', 'lower', 'nose')
        self.relate('connect', 'upper', 'lower')

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
REPAIR_PLAN = 'One airplane outline, two mirrored wings, tail and rounded nose.'
CONSTRUCTION_REFERENCE = 'plane'
