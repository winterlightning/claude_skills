# Independent repair; parent preserved.
"""Independent 32px profile of airplane-other.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4a625cc1-8989-433b-89db-ddf1b6a98ffe'
SOURCE_PATH = 'pictographic-primitives/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4a625cc1-8989-433b-89db-ddf1b6a98ffe', 'pictographic-primitives/other/airplane_4a625cc1-8989-433b-89db-ddf1b6a98ffe.svg'),)
PROFILE_SOURCE_KEYS = ('solo/airplane-other',)
SOLO_SOURCE_ICON_IDS = ('airplane-other',)
REFERENCE_EXPORT_SHA256 = '71fea4c7397e16d0129ef815a68871c7c07a8e6f98d58b1d3e6ee8094214d97e'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'airplane-other-sub32'
    icon_id = 'airplane-other-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'other'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('left', (2, 23), (5, 20), (10, 21), (16, 15), (9, 9), (12, 7), (21, 12), (24, 6))
        self.add_bezier('nose-top', (24, 6), ((25, 4), (26, 4), (27, 4)))
        self.add_arc('nose', (27, 4), (30, 7), radius_x=3)
        self.add_bezier('nose-bottom', (30, 7), ((30, 9), (29, 10), (27, 12)))
        self.add_line('fuselage', (27, 12), (13, 26))
        self.add_bezier('tail-start', (13, 26), ((12, 27), (11, 28), (9, 28)))
        self.add_bezier('tail', (9, 28), ((7, 28), (6, 27), (5, 26)))
        self.add_line('tail-end', (5, 26), (2, 23))
        self.add_contour('front', 'nose-top', 'nose', 'nose-bottom', 'fuselage', 'tail-start', 'tail', 'tail-end')
        self.relate('connect', 'left', 'front')

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
REPAIR_PLAN = 'Diagonal airplane with original orientation, wing and tail.'
CONSTRUCTION_REFERENCE = 'plane'
