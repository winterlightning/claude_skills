# Independent repair; parent preserved.
"""Independent 32px profile of biometric-fingerprint.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '18f6118d-0b0a-4a7b-89e0-52ba5abbcb54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fingerprint_18f6118d-0b0a-4a7b-89e0-52ba5abbcb54.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('18f6118d-0b0a-4a7b-89e0-52ba5abbcb54', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/fingerprint_18f6118d-0b0a-4a7b-89e0-52ba5abbcb54.svg'),)
PROFILE_SOURCE_KEYS = ('solo/biometric-fingerprint',)
SOLO_SOURCE_ICON_IDS = ('biometric-fingerprint',)
REFERENCE_EXPORT_SHA256 = 'fd061383d4724e84344b7d1a07e4103e71c657c50ff4965ed041db3987e1c4aa'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'biometric-fingerprint-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('outer-left', (2, 22), (2, 16))
        self.add_arc('outer-top', (2, 16), (30, 16), radius_x=14)
        self.add_line('outer-right', (30, 16), (30, 22))
        self.add_contour('outer', 'outer-left', 'outer-top', 'outer-right')
        self.add_bezier('middle-left', (7, 27), ((10, 26), (10, 20), (10, 16)))
        self.add_arc('middle-top', (10, 16), (22, 16), radius_x=6)
        self.add_line('middle-right', (22, 16), (22, 23))
        self.add_bezier('middle-end', (22, 23), ((22, 26), (24, 29), (26, 30)))
        self.add_contour('middle', 'middle-left', 'middle-top', 'middle-right', 'middle-end')
        self.add_bezier('inner', (16, 24), ((16, 26), (15, 29), (13, 30)))

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
REPAIR_PLAN = 'Three fingerprint ridges with expanded spacing and smooth tangent transitions.'
CONSTRUCTION_REFERENCE = 'fingerprint'
