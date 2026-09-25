# Independent repair; parent preserved.
"""Independent 32px profile of broken-chain-link-reference-batch-019-12.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7fcc14bd-bf5e-41f1-97bb-f6b06da48c98'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/disconnect_7fcc14bd-bf5e-41f1-97bb-f6b06da48c98.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7fcc14bd-bf5e-41f1-97bb-f6b06da48c98', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/disconnect_7fcc14bd-bf5e-41f1-97bb-f6b06da48c98.svg'),)
PROFILE_SOURCE_KEYS = ('solo/broken-chain-link-reference-batch-019-12',)
SOLO_SOURCE_ICON_IDS = ('broken-chain-link-reference-batch-019-12',)
REFERENCE_EXPORT_SHA256 = '3fa6d2713325b3262e53c246fd830b88d9224a1235cf27990b29cff86b44fecf'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'broken-chain-link-reference-batch-019-12-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('symbol', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('lower-left', (11, 15), (4, 22))
        self.add_bezier('lower-end-a', (4, 22), ((2, 24), (2, 26), (4, 28)))
        self.add_bezier('lower-end-b', (4, 28), ((5, 29), (6, 30), (7, 30)))
        self.add_bezier('lower-end-c', (7, 30), ((8, 30), (9, 29), (10, 28)))
        self.add_line('lower-right', (10, 28), (16, 22))
        self.add_contour('lower', 'lower-left', 'lower-end-a', 'lower-end-b', 'lower-end-c', 'lower-right')
        self.add_line('upper-left', (17, 10), (23, 4))
        self.add_bezier('upper-end-a', (23, 4), ((25, 2), (27, 2), (29, 4)))
        self.add_bezier('upper-end-b', (29, 4), ((30, 5), (30, 6), (30, 7)))
        self.add_bezier('upper-end-c', (30, 7), ((30, 8), (30, 9), (29, 10)))
        self.add_line('upper-right', (29, 10), (22, 17))
        self.add_contour('upper', 'upper-left', 'upper-end-a', 'upper-end-b', 'upper-end-c', 'upper-right')
        self.add_line('break-diagonal', (3, 4), (5, 6))
        self.add_line('break-left', (2, 12), (5, 12))
        self.add_line('break-top', (11, 2), (11, 5))

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
REPAIR_PLAN = 'Two open rounded chain links and all three break rays.'
CONSTRUCTION_REFERENCE = 'unlink'
