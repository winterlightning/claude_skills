# Independent repair; parent preserved.
"""Independent 32px profile of battery.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9ad9cd5c-98cd-452e-ad18-784b9bd66c4d'
SOURCE_PATH = 'pictographic-primitives/photography/battery_9ad9cd5c-98cd-452e-ad18-784b9bd66c4d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9ad9cd5c-98cd-452e-ad18-784b9bd66c4d', 'pictographic-primitives/photography/battery_9ad9cd5c-98cd-452e-ad18-784b9bd66c4d.svg'), ('d0244858-b455-4673-842d-844f0c652966', 'pictographic-primitives/photography/battery_d0244858-b455-4673-842d-844f0c652966.svg'))
PROFILE_SOURCE_KEYS = ('solo/battery', 'solo/empty-upright-battery')
SOLO_SOURCE_ICON_IDS = ('battery', 'empty-upright-battery')
REFERENCE_EXPORT_SHA256 = '4695269714d782ca4e93e5345b16c88649e8e9bd14b055fe8cae0f66ec910ea6'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'battery-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'photography'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        box(self, 'body', 4, 10, 28, 30, 2)
        self.add_line('terminal-left', (10, 10), (10, 5))
        self.add_arc('terminal-tl', (10, 5), (13, 2), radius_x=3)
        self.add_line('terminal-top', (13, 2), (19, 2))
        self.add_arc('terminal-tr', (19, 2), (22, 5), radius_x=3)
        self.add_line('terminal-right', (22, 5), (22, 10))
        self.add_contour('terminal', 'terminal-left', 'terminal-tl', 'terminal-top', 'terminal-tr', 'terminal-right')
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
REPAIR_PLAN = 'Battery body and rounded attached terminal with full-size opening.'
CONSTRUCTION_REFERENCE = 'battery'
