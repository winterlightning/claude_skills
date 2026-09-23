"""Independent 32px profile of car-side.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '695aca30-f091-42f4-b8c1-dabb9d4a8a44'
SOURCE_PATH = 'pictographic-primitives/symbol/car side_695aca30-f091-42f4-b8c1-dabb9d4a8a44.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('695aca30-f091-42f4-b8c1-dabb9d4a8a44', 'pictographic-primitives/symbol/car side_695aca30-f091-42f4-b8c1-dabb9d4a8a44.svg'),)
PROFILE_SOURCE_KEYS = ('solo/car-side',)
SOLO_SOURCE_ICON_IDS = ('car-side',)
REFERENCE_EXPORT_SHA256 = 'a6c8e1a0946edf245160fc0b9b9cf12938d7fe1e9444e4116177a28c42ae379e'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'car-side-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('roof-lower-left', (7, 13), (10, 7))
        self.add_bezier('roof-left', (10, 7), ((11, 5), (12, 4), (14, 4)))
        self.add_line('roof-top', (14, 4), (18, 4))
        self.add_bezier('roof-right', (18, 4), ((20, 4), (21, 5), (22, 7)))
        self.add_line('roof-lower-right', (22, 7), (25, 13))
        self.add_contour('roof', 'roof-lower-left', 'roof-left', 'roof-top', 'roof-right', 'roof-lower-right')
        self.add_bezier('rear', (5, 24), ((2, 24), (2, 21), (2, 18)))
        self.add_arc('rear-top', (2, 18), (7, 13), radius_x=5)
        self.add_line('hood', (7, 13), (25, 13))
        self.add_arc('front-top', (25, 13), (30, 18), radius_x=5)
        self.add_bezier('front', (30, 18), ((30, 21), (30, 24), (27, 24)))
        self.add_contour('body', 'rear', 'rear-top', 'hood', 'front-top', 'front')
        for cx in (9, 23):
            circle(self, f'wheel-{cx}', cx, 24, 4)
            self.relate('connect', 'body', f'wheel-{cx}')
        self.add_line('chassis', (13, 24), (19, 24))
        self.relate('connect', 'chassis', 'wheel-9')
        self.relate('connect', 'chassis', 'wheel-23')
        self.relate('connect', 'roof', 'body')

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
REPAIR_PLAN = 'Side car with smooth roof and two proper circular wheels; source counts retained.'
CONSTRUCTION_REFERENCE = 'car'
