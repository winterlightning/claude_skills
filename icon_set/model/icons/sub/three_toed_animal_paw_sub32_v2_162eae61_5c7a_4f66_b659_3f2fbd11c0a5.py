"""Independent 32px profile of three-toed-animal-paw.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '162eae61-5c7a-4f66-b659-3f2fbd11c0a5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_162eae61-5c7a-4f66-b659-3f2fbd11c0a5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('162eae61-5c7a-4f66-b659-3f2fbd11c0a5', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/paw print_162eae61-5c7a-4f66-b659-3f2fbd11c0a5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-toed-animal-paw',)
SOLO_SOURCE_ICON_IDS = ('three-toed-animal-paw',)
REFERENCE_EXPORT_SHA256 = '97e14db0f190787388dc6913bc426cf24f0f12f95de4197689b028c24eabf262'

class DrawingVariant2(Sub32):
    icon_id = 'three-toed-animal-paw-sub32-v2'
    variant_of = 'three-toed-animal-paw-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three oval toe loops and rounded paw pad; preserve count and open loops. Construction reference: paw-print."""
        for n, x, y in [('left', 5, 12), ('middle', 16, 6), ('right', 27, 12)]:
            self.add_arc(n + '-top', (x - 3, y), (x + 3, y), radius_x=3, radius_y=4)
            self.add_arc(n + '-bottom', (x + 3, y), (x - 3, y), radius_x=3, radius_y=4)
            self.add_contour(n, n + '-top', n + '-bottom', closed=True)
        self.add_bezier('pad-top-l', (8, 25), ((11, 23), (11, 19), (16, 19)))
        self.add_bezier('pad-top-r', (16, 19), ((21, 19), (21, 23), (24, 25)))
        self.add_bezier('pad-right', (24, 25), ((28, 30), (22, 30), (16, 30)))
        self.add_bezier('pad-left', (16, 30), ((10, 30), (4, 30), (8, 25)))
        self.add_contour('pad', 'pad-top-l', 'pad-top-r', 'pad-right', 'pad-left', closed=True)

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
