# Independent repair; parent preserved.
"""Independent 32px profile of bus-front.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6be3bbdd-720f-407c-af2d-59983752017d'
SOURCE_PATH = 'pictographic-primitives/transportation/bus_6be3bbdd-720f-407c-af2d-59983752017d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6be3bbdd-720f-407c-af2d-59983752017d', 'pictographic-primitives/transportation/bus_6be3bbdd-720f-407c-af2d-59983752017d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bus-front',)
SOLO_SOURCE_ICON_IDS = ('bus-front',)
REFERENCE_EXPORT_SHA256 = 'a515514d2accbf20d8e88d0f111e037fe0a3fb605e3b5591d47aaba7df81e861'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'bus-front-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        box(self, 'body', 4, 2, 28, 26, 3)
        self.add_line('window', (4, 12), (28, 12))
        self.relate('connect', 'body', 'window')
        for x in (11, 21):
            self.add_dot(f'headlight-{x}', (x, 19))
            self.add_line(f'wheel-{x}', (x, 26), (x, 30))
            self.relate('connect', 'body', f'wheel-{x}')

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
REPAIR_PLAN = 'Front bus: rounded body, window rail, two headlights and two legs.'
CONSTRUCTION_REFERENCE = 'bus-front'
