"""Independent 32px profile of fork-spoon-crossed.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6305d089-5f4e-4d0d-8488-b6bf8ef99e4d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/spoon and fork_6305d089-5f4e-4d0d-8488-b6bf8ef99e4d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6305d089-5f4e-4d0d-8488-b6bf8ef99e4d', 'pictographic-primitives/symbol/spoon and fork_6305d089-5f4e-4d0d-8488-b6bf8ef99e4d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fork-spoon-crossed',)
SOLO_SOURCE_ICON_IDS = ('fork-spoon-crossed',)
REFERENCE_EXPORT_SHA256 = '2cbd63fe3602bc94254dadb0413e42262156d6210aef458e617a00c036f6dcb9'

class DrawingVariant2(Sub32):
    icon_id = 'fork-spoon-crossed-sub32-v2'
    variant_of = 'fork-spoon-crossed-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Crossed two-tine fork and round spoon with clear handles. Construction reference: utensils-crossed: crossed handles and rounded bowl."""
        self.add_polyline('fork', (2, 6), (8, 12), (14, 6), (8, 2))
        self.add_line('fork-handle', (8, 12), (26, 30))
        self.relate('connect', 'fork-handle', 'fork')
        circle(self, 'spoon', 25, 7, 5)
        self.add_line('spoon-handle', (22, 11), (10, 29))
        self.relate('connect', 'spoon-handle', 'spoon')
        self.relate('connect', 'spoon-handle', 'fork-handle')

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
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
