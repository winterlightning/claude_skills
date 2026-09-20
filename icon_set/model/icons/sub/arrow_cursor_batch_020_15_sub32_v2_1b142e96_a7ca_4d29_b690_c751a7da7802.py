# Independent repair; parent preserved.
"""Independent 32px profile of arrow-cursor-batch-020-15.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1b142e96-a7ca-4d29-b690-c751a7da7802'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cursor left 2_1b142e96-a7ca-4d29-b690-c751a7da7802.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b142e96-a7ca-4d29-b690-c751a7da7802', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/cursor left 2_1b142e96-a7ca-4d29-b690-c751a7da7802.svg'),)
PROFILE_SOURCE_KEYS = ('solo/arrow-cursor-batch-020-15',)
SOLO_SOURCE_ICON_IDS = ('arrow-cursor-batch-020-15',)
REFERENCE_EXPORT_SHA256 = '7aba1b24d85456c2b09ab7b5dcea534f1ab71d99c2828dcbfaccaf2a2d903495'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    variant_of = 'arrow-cursor-batch-020-15-sub32'
    icon_id = 'arrow-cursor-batch-020-15-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_polyline('cursor', (2, 2), (30, 10), (21, 15), (30, 24), (24, 30), (15, 21), (10, 30), closed=True)

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
REPAIR_PLAN = 'Cursor outline with widened diagonal tail; direction and all corners retained.'
CONSTRUCTION_REFERENCE = 'mouse-pointer-2'
