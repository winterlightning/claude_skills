"""Independent 32px profile of molecule-science.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '14f11930-2628-4025-a231-22735ffc293e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/science/molecule_14f11930-2628-4025-a231-22735ffc293e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14f11930-2628-4025-a231-22735ffc293e', 'pictographic-primitives/science/molecule_14f11930-2628-4025-a231-22735ffc293e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/molecule-science',)
SOLO_SOURCE_ICON_IDS = ('molecule-science',)
REFERENCE_EXPORT_SHA256 = '27efd11e433eb03658a32f52951937d48201b522b13d943e64ac4c53203d8112'

class DrawingVariant2(Sub32):
    icon_id = 'molecule-science-sub32-v2'
    variant_of = 'molecule-science-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'science'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three circular molecule nodes joined as a triangle; remove invented fourth central node. Construction reference: none."""
        for n, x, y in [('top', 16, 6), ('left', 6, 26), ('right', 26, 26)]:
            circle(self, n, x, y, 4)
        self.add_line('bond-l', (13, 9), (8, 22))
        self.add_line('bond-r', (19, 9), (24, 22))
        self.add_line('bond-base', (10, 26), (22, 26))
        for a, b in [('bond-l', 'top'), ('bond-l', 'left'), ('bond-r', 'top'), ('bond-r', 'right'), ('bond-base', 'left'), ('bond-base', 'right')]:
            self.relate('connect', a, b)

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
