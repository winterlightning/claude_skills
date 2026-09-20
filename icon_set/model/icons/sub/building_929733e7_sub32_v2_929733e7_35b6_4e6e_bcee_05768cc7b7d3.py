# Independent repair; parent preserved.
"""Independent 32px profile of building-929733e7.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '929733e7-35b6-4e6e-bcee-05768cc7b7d3'
SOURCE_PATH = 'pictographic-primitives/building/building_929733e7-35b6-4e6e-bcee-05768cc7b7d3.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('929733e7-35b6-4e6e-bcee-05768cc7b7d3', 'pictographic-primitives/building/building_929733e7-35b6-4e6e-bcee-05768cc7b7d3.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building-929733e7',)
SOLO_SOURCE_ICON_IDS = ('building-929733e7',)
REFERENCE_EXPORT_SHA256 = '7ca30296605e6290a01732226625a81724b195cdd0e173964f9cd4bcec01fdd1'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'building-929733e7-sub32'
    icon_id = 'building-929733e7-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'building'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('back', (6, 30), (6, 2), (19, 2), (19, 10))
        self.add_polyline('front', (14, 30), (14, 10), (28, 10), (28, 30))
        self.add_line('ground', (4, 30), (28, 30))
        self.add_line('window', (21, 18), (22, 18))
        self.relate('connect', 'back', 'front')
        self.relate('connect', 'back', 'ground')
        self.relate('connect', 'front', 'ground')

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
REPAIR_PLAN = 'Two overlapping buildings, baseline and short window dash.'
CONSTRUCTION_REFERENCE = 'building'
