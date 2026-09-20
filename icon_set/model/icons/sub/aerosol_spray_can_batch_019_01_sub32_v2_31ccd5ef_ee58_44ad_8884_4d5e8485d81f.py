"""Independent 32px profile of aerosol-spray-can-batch-019-01.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '31ccd5ef-ee58-44ad-8884-4d5e8485d81f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/spray can_31ccd5ef-ee58-44ad-8884-4d5e8485d81f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('31ccd5ef-ee58-44ad-8884-4d5e8485d81f', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/spray can_31ccd5ef-ee58-44ad-8884-4d5e8485d81f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/aerosol-spray-can-batch-019-01',)
SOLO_SOURCE_ICON_IDS = ('aerosol-spray-can-batch-019-01',)
REFERENCE_EXPORT_SHA256 = '39fa470eb754bd0af248cc1a09283a709fb12819622e60a31985c19a26bc5fde'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'aerosol-spray-can-batch-019-01-sub32'
    icon_id = 'aerosol-spray-can-batch-019-01-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        box(self, 'can', 4, 12, 20, 30, 3)
        self.add_line('nozzle-left', (8, 12), (8, 4))
        self.add_arc('nozzle-tl', (8, 4), (10, 2), radius_x=2)
        self.add_line('nozzle-top', (10, 2), (14, 2))
        self.add_arc('nozzle-tr', (14, 2), (16, 4), radius_x=2)
        self.add_line('nozzle-right', (16, 4), (16, 12))
        self.add_contour('nozzle', 'nozzle-left', 'nozzle-tl', 'nozzle-top', 'nozzle-tr', 'nozzle-right')
        self.relate('connect', 'can', 'nozzle')
        self.add_line('spray-upper', (24, 5), (28, 2))
        self.add_line('spray-lower', (26, 12), (28, 14))

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
REPAIR_PLAN = 'Can, rounded actuator, two separate spray strokes. Restore diverging spray.'
CONSTRUCTION_REFERENCE = 'spray-can'
