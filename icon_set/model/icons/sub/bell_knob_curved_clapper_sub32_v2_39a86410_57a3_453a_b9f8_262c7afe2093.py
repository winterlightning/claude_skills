# Independent repair; parent preserved.
"""Independent 32px profile of bell-knob-curved-clapper.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '39a86410-57a3-453a-b9f8-262c7afe2093'
SOURCE_PATH = 'pictographic-primitives/symbol/ring_39a86410-57a3-453a-b9f8-262c7afe2093.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('39a86410-57a3-453a-b9f8-262c7afe2093', 'pictographic-primitives/symbol/ring_39a86410-57a3-453a-b9f8-262c7afe2093.svg'),)
PROFILE_SOURCE_KEYS = ('solo/bell-knob-curved-clapper',)
SOLO_SOURCE_ICON_IDS = ('bell-knob-curved-clapper',)
REFERENCE_EXPORT_SHA256 = 'c09581e29e7446aa593c50b6da69f5a0cfca5b93c9cb8eb176e35f8985b406c5'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'bell-knob-curved-clapper-sub32'
    icon_id = 'bell-knob-curved-clapper-sub32-v2'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_dot('knob', (16, 2))
        self.add_arc('dome', (8, 17), (24, 17), radius_x=8)
        self.add_line('right-wall', (24, 17), (24, 18))
        self.add_arc('right-flare', (24, 18), (28, 22), radius_x=4, sweep=False)
        self.add_line('hem', (28, 22), (4, 22))
        self.add_arc('left-flare', (4, 22), (8, 18), radius_x=4, sweep=False)
        self.add_line('left-wall', (8, 18), (8, 17))
        self.add_contour('bell', 'dome', 'right-wall', 'right-flare', 'hem', 'left-flare', 'left-wall', closed=True)
        self.add_arc('clapper', (13, 29), (19, 29), radius_x=3, radius_y=1, sweep=False)

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
REPAIR_PLAN = 'Bell with separate knob, tangent dome and mirrored flared hem, curved clapper.'
CONSTRUCTION_REFERENCE = 'bell'
