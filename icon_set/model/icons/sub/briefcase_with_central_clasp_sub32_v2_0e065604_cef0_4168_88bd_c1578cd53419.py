"""Independent 32px profile of briefcase-with-central-clasp.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0e065604-cef0-4168-88bd-c1578cd53419'
SOURCE_PATH = 'pictographic-primitives/business/briefcase_0e065604-cef0-4168-88bd-c1578cd53419.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0e065604-cef0-4168-88bd-c1578cd53419', 'pictographic-primitives/business/briefcase_0e065604-cef0-4168-88bd-c1578cd53419.svg'),)
PROFILE_SOURCE_KEYS = ('solo/briefcase-with-central-clasp',)
SOLO_SOURCE_ICON_IDS = ('briefcase-with-central-clasp',)
REFERENCE_EXPORT_SHA256 = 'd22103870bbebc47ceeb0e8dc746602a8bc24fcd12e56a87f31953e4f9eca500'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'briefcase-with-central-clasp-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'business'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        box(self, 'body', 2, 10, 30, 30, 3)
        self.add_line('handle-left', (10, 10), (10, 5))
        self.add_arc('handle-tl', (10, 5), (13, 2), radius_x=3)
        self.add_line('handle-top', (13, 2), (19, 2))
        self.add_arc('handle-tr', (19, 2), (22, 5), radius_x=3)
        self.add_line('handle-right', (22, 5), (22, 10))
        self.add_contour('handle', 'handle-left', 'handle-tl', 'handle-top', 'handle-tr', 'handle-right')
        self.add_line('flap', (2, 18), (30, 18))
        self.add_line('clasp', (16, 18), (16, 23))
        self.relate('connect', 'body', 'handle')
        self.relate('connect', 'body', 'flap')
        self.relate('connect', 'flap', 'clasp')

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
REPAIR_PLAN = 'Briefcase, rounded handle, flap seam and central clasp; retain all parts.'
CONSTRUCTION_REFERENCE = 'briefcase-business'
