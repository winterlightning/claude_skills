# Independent repair; parent preserved.
"""Independent 32px profile of battery-1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd59453b3-a555-48ec-9434-865bcda7a62f'
SOURCE_PATH = 'pictographic-primitives/state/battery 1_d59453b3-a555-48ec-9434-865bcda7a62f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d59453b3-a555-48ec-9434-865bcda7a62f', 'pictographic-primitives/state/battery 1_d59453b3-a555-48ec-9434-865bcda7a62f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/battery-1',)
SOLO_SOURCE_ICON_IDS = ('battery-1',)
REFERENCE_EXPORT_SHA256 = '8c49772019cd8e86f290bd424f27d1e5902d44ffb25614032fdb4c8aca97db89'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'battery-1-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        box(self, 'body', 2, 4, 22, 28, 3)
        self.add_polyline('terminal', (22, 10), (30, 10), (30, 22), (22, 22))
        self.relate('connect', 'body', 'terminal')

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
REPAIR_PLAN = 'Battery shell with attached eight-unit-wide terminal.'
CONSTRUCTION_REFERENCE = 'battery'
