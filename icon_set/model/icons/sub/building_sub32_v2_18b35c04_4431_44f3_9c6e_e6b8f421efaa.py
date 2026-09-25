# Independent repair; parent preserved.
"""Independent 32px profile of building.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '18b35c04-4431-44f3-9c6e-e6b8f421efaa'
SOURCE_PATH = 'pictographic-primitives/building/building_18b35c04-4431-44f3-9c6e-e6b8f421efaa.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('18b35c04-4431-44f3-9c6e-e6b8f421efaa', 'pictographic-primitives/building/building_18b35c04-4431-44f3-9c6e-e6b8f421efaa.svg'),)
PROFILE_SOURCE_KEYS = ('solo/building',)
SOLO_SOURCE_ICON_IDS = ('building',)
REFERENCE_EXPORT_SHA256 = 'e1143185a448471579457b69cb9f93509d07b5f239f9784e1bc67b71e37d6e4f'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'building-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'building'
    categories = ('building', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('left', (8, 2), (8, 30))
        self.add_polyline('roof-wall', (8, 6), (28, 18), (28, 30))
        self.add_line('base', (4, 30), (28, 30))
        self.add_line('door', (18, 24), (18, 30))
        self.relate('connect', 'left', 'roof-wall')
        self.relate('connect', 'left', 'base')
        self.relate('connect', 'roof-wall', 'base')
        self.relate('connect', 'door', 'base')

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
REPAIR_PLAN = 'Sloping building and original short entrance marker; no invented box door.'
CONSTRUCTION_REFERENCE = 'building'
