"""Independent 32px profile of first-aid-medical-case.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1f12e0e9-892e-4d3d-ab45-7a2a22a30f92'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/medical kit_1f12e0e9-892e-4d3d-ab45-7a2a22a30f92.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1f12e0e9-892e-4d3d-ab45-7a2a22a30f92', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/medical kit_1f12e0e9-892e-4d3d-ab45-7a2a22a30f92.svg'), ('41bb0b4b-dc69-42d5-bf22-17d0a68fea2b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/medical kit 1_41bb0b4b-dc69-42d5-bf22-17d0a68fea2b.svg'))
PROFILE_SOURCE_KEYS = ('solo/first-aid-medical-case', 'solo/emergency-medical-first-aid-kit')
SOLO_SOURCE_ICON_IDS = ('first-aid-medical-case', 'emergency-medical-first-aid-kit')
REFERENCE_EXPORT_SHA256 = '52c1a511ad3015b76444f7acd543b8d84e05538e9e6297433748b71165d087ce'

class DrawingVariant2(Sub32):
    icon_id = 'first-aid-medical-case-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded medical case, open U handle and central plus. Construction reference: briefcase-medical."""
        box(self, 'case', 2, 10, 30, 30, 3)
        self.add_polyline('handle', (9, 10), (9, 2), (23, 2), (23, 10))
        self.relate('connect', 'handle', 'case')
        self.add_line('cross-h', (11, 20), (21, 20))
        self.add_line('cross-v', (16, 17), (16, 23))
        self.relate('connect', 'cross-h', 'cross-v')

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
