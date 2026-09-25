# Independent repair; parent preserved.
"""Independent 32px profile of checklist.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ee9d1910-a200-4e57-8b40-f41cdef29366'
SOURCE_PATH = 'pictographic-primitives/work/checklist_ee9d1910-a200-4e57-8b40-f41cdef29366.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ee9d1910-a200-4e57-8b40-f41cdef29366', 'pictographic-primitives/work/checklist_ee9d1910-a200-4e57-8b40-f41cdef29366.svg'),)
PROFILE_SOURCE_KEYS = ('solo/checklist',)
SOLO_SOURCE_ICON_IDS = ('checklist',)
REFERENCE_EXPORT_SHA256 = 'dc72fbb8823e2d0e1538bca01930fd065ef1f24ec231f0533a07201b6321506b'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'checklist-sub32-v2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'work'
    categories = ('work', 'primitives')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        box(self, 'page', 2, 2, 30, 30, 2)
        for i, y in enumerate((11, 21)):
            self.add_polyline(f'check-{i}', (9, y), (11, y + 2), (15, y - 2))
            self.add_line(f'line-{i}', (22, y + 1), (23, y + 1))

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
REPAIR_PLAN = 'Document with two checkmarks and two horizontal lines, uniform row spacing.'
CONSTRUCTION_REFERENCE = 'list-checks'
