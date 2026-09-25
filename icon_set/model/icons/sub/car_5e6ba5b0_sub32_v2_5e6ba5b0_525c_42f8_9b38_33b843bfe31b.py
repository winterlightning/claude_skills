# Independent repair; parent preserved.
"""Independent 32px profile of car-5e6ba5b0.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5e6ba5b0-525c-42f8-9b38-33b843bfe31b'
SOURCE_PATH = 'pictographic-primitives/transportation/car_5e6ba5b0-525c-42f8-9b38-33b843bfe31b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5e6ba5b0-525c-42f8-9b38-33b843bfe31b', 'pictographic-primitives/transportation/car_5e6ba5b0-525c-42f8-9b38-33b843bfe31b.svg'), ('796e3289-99b8-4ef8-bce0-4e8fa2bfefc8', 'pictographic-primitives/transportation/car_796e3289-99b8-4ef8-bce0-4e8fa2bfefc8.svg'), ('eaa7f06c-57de-4d21-aaa7-d89d24b33193', 'pictographic-primitives/transportation/car_eaa7f06c-57de-4d21-aaa7-d89d24b33193.svg'), ('edd4874e-4e76-4ead-a51d-24426b253623', 'pictographic-primitives/transportation/car_edd4874e-4e76-4ead-a51d-24426b253623.svg'))
PROFILE_SOURCE_KEYS = ('solo/car-5e6ba5b0', 'solo/car-796e3289', 'solo/car-eaa7f06c', 'solo/car-edd4874e')
SOLO_SOURCE_ICON_IDS = ('car-5e6ba5b0', 'car-796e3289', 'car-eaa7f06c', 'car-edd4874e')
REFERENCE_EXPORT_SHA256 = '74c0ff8439a2ad60f72d38cffa5d6783aeb36217329f66101bd7a6a604bc8cf1'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'car-5e6ba5b0-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'transportation'
    categories = ('transportation', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('roof-left', (8, 13), ((10, 9), (10, 4), (14, 4)))
        self.add_line('roof-top', (14, 4), (18, 4))
        self.add_bezier('roof-right', (18, 4), ((22, 4), (22, 9), (24, 13)))
        self.add_contour('roof', 'roof-left', 'roof-top', 'roof-right')
        self.add_bezier('rear', (5, 24), ((2, 24), (2, 21), (2, 19)))
        self.add_arc('rear-top', (2, 19), (8, 13), radius_x=6)
        self.add_line('hood', (8, 13), (24, 13))
        self.add_arc('front-top', (24, 13), (30, 19), radius_x=6)
        self.add_bezier('front', (30, 19), ((30, 21), (30, 24), (27, 24)))
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
REPAIR_PLAN = 'Side car with source roof, smooth body and two equal round wheels.'
CONSTRUCTION_REFERENCE = 'car'
