# Independent repair; parent preserved.
"""Independent 32px profile of battery-charging-vertical.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4eb92da5-29c0-4d92-ae40-851bdeae1749'
SOURCE_PATH = 'pictographic-primitives/symbol/lightning rectangle_4eb92da5-29c0-4d92-ae40-851bdeae1749.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4eb92da5-29c0-4d92-ae40-851bdeae1749', 'pictographic-primitives/symbol/lightning rectangle_4eb92da5-29c0-4d92-ae40-851bdeae1749.svg'),)
PROFILE_SOURCE_KEYS = ('solo/battery-charging-vertical',)
SOLO_SOURCE_ICON_IDS = ('battery-charging-vertical',)
REFERENCE_EXPORT_SHA256 = '0c8109e691174030648795152ecb7b76bf4a88561c03df1061f321f6c369f3c9'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'battery-charging-vertical-sub32'
    icon_id = 'battery-charging-vertical-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        box(self, 'body', 4, 10, 28, 30, 3)
        self.add_polyline('terminal', (10, 10), (10, 2), (22, 2), (22, 10))
        self.relate('connect', 'body', 'terminal')
        self.add_polyline('charge', (18, 17), (13, 21), (19, 21), (14, 23))

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
REPAIR_PLAN = 'Battery shell, attached terminal and open lightning bolt.'
CONSTRUCTION_REFERENCE = 'battery-charging'
