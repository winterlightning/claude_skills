# Independent repair; parent preserved.
"""Independent 32px profile of bug-beetle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64'
SOURCE_PATH = 'pictographic-primitives/symbol/piece_9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64', 'pictographic-primitives/symbol/piece_9b6a0dc9-fcf3-46a0-9bdd-9491b1f0dd64.svg'), ('9a3ccf45-79d9-442e-9bbb-bf6598cc98bf', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bug_9a3ccf45-79d9-442e-9bbb-bf6598cc98bf.svg'))
PROFILE_SOURCE_KEYS = ('solo/bug-beetle',)
SOLO_SOURCE_ICON_IDS = ('bug-beetle',)
REFERENCE_EXPORT_SHA256 = 'f8b19500a7958cb097600733a4c60115200d7536dfdd043e56be6366d6b34045'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'bug-beetle-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('head-left', (7, 12), ((7, 9), (8, 8), (11, 5)))
        self.add_bezier('head-top-left', (11, 5), ((12, 4), (14, 4), (16, 4)))
        self.add_bezier('head-top-right', (16, 4), ((18, 4), (20, 4), (21, 5)))
        self.add_bezier('head-right', (21, 5), ((24, 8), (25, 9), (25, 12)))
        self.add_line('head-base', (25, 12), (7, 12))
        self.add_contour('head', 'head-left', 'head-top-left', 'head-top-right', 'head-right', 'head-base', closed=True)
        self.add_line('right', (25, 12), (25, 21))
        self.add_arc('bottom', (25, 21), (7, 21), radius_x=9)
        self.add_line('left', (7, 21), (7, 12))
        self.add_contour('body', 'right', 'bottom', 'left')
        self.relate('connect', 'head', 'body')
        for side in (-1, 1):
            x = 16 + 9 * side
            outer = 16 + 14 * side
            self.add_polyline(f'upper-leg-{side}', (x, 14), (outer - 2 * side, 14), (outer, 10))
            self.add_polyline(f'lower-leg-{side}', (x, 21), (outer - 2 * side, 24), (outer, 28))
            self.relate('connect', 'body', f'upper-leg-{side}')
            self.relate('connect', 'body', f'lower-leg-{side}')
            self.add_line(f'antenna-{side}', (16 + 5 * side, 5), (16 + 9 * side, 2))
            self.relate('connect', 'head', f'antenna-{side}')

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
REPAIR_PLAN = 'Restore original four lateral legs, two antennae, domed head and rounded body.'
CONSTRUCTION_REFERENCE = 'bug'
