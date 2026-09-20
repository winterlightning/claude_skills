# Independent repair; parent preserved.
"""Independent 32px profile of bicycle-reference-25-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ba2c7c5d-7b19-4251-8651-f1619fdbdc5e'
SOURCE_PATH = 'pictographic-primitives/other/bike_ba2c7c5d-7b19-4251-8651-f1619fdbdc5e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ba2c7c5d-7b19-4251-8651-f1619fdbdc5e', 'pictographic-primitives/other/bike_ba2c7c5d-7b19-4251-8651-f1619fdbdc5e.svg'), ('e918e425-b0c9-444c-bdb5-9884044e4703', 'pictographic-primitives/other/bike_e918e425-b0c9-444c-bdb5-9884044e4703.svg'), ('3bd744bc-3a24-4a8e-92f3-02a013f3d4f0', 'pictographic-primitives/other/bike_3bd744bc-3a24-4a8e-92f3-02a013f3d4f0.svg'))
PROFILE_SOURCE_KEYS = ('solo/bicycle-reference-25-solo', 'solo/bicycle-reference-165-solo', 'solo/bicycle-reference-184-solo')
SOLO_SOURCE_ICON_IDS = ('bicycle-reference-25-solo', 'bicycle-reference-165-solo', 'bicycle-reference-184-solo')
REFERENCE_EXPORT_SHA256 = '715c83355c6af1534edaeebc5e3f7c45ec47d099c947d3457999f263cffb24c0'

class DrawingVariant2(Sub32):
    icon_id = 'bicycle-reference-25-sub32-v2'
    variant_of = 'bicycle-reference-25-sub32'
    variant_label = 'Centerline and source fidelity repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        for x in (6, 26):
            circle(self, f'wheel-{x}', x, 24, 4)
        self.add_polyline('frame', (6, 24), (12, 12), (20, 12), (16, 24), (6, 24))
        self.add_line('crank', (12, 12), (16, 24))
        self.add_polyline('fork', (26, 24), (22, 4), (19, 4))
        self.add_line('seatpost', (12, 12), (12, 6))
        self.add_line('seat', (9, 6), (15, 6))
        self.relate('connect', 'frame', 'crank')
        self.relate('connect', 'frame', 'seatpost')
        self.relate('connect', 'seatpost', 'seat')
        self.relate('connect', 'frame', 'fork')
        self.relate('connect', 'frame', 'wheel-6')
        self.relate('connect', 'fork', 'wheel-26')

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
REPAIR_PLAN = 'Bicycle with two equal wheels, triangular frame, saddle and raised handlebar.'
CONSTRUCTION_REFERENCE = 'none'
