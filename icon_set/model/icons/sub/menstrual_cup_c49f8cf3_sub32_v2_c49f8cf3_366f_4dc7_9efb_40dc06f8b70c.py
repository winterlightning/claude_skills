"""Independent 32px profile of menstrual-cup-c49f8cf3.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'c49f8cf3-366f-4dc7-9efb-40dc06f8b70c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/health/menstrual cup_c49f8cf3-366f-4dc7-9efb-40dc06f8b70c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c49f8cf3-366f-4dc7-9efb-40dc06f8b70c', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/menstrual cup_c49f8cf3-366f-4dc7-9efb-40dc06f8b70c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/menstrual-cup-c49f8cf3',)
SOLO_SOURCE_ICON_IDS = ('menstrual-cup-c49f8cf3',)
REFERENCE_EXPORT_SHA256 = '55424d86d9f1c23322099a7cc56667b45eb911bd6f3ac5d604311a8c5d5ea4f1'

class DrawingVariant2(Sub32):
    icon_id = 'menstrual-cup-c49f8cf3-sub32-v2'
    variant_of = 'menstrual-cup-c49f8cf3-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'health'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Menstrual cup with closed thick rim, tapered curved cup and rounded lower stem. Construction reference: none."""
        box(self, 'rim', 4, 2, 28, 10, 3)
        self.add_bezier('left', (7, 10), ((7, 17), (12, 20), (12, 24)))
        self.add_line('stem-l', (12, 24), (12, 26))
        self.add_arc('stem-base', (12, 26), (20, 26), radius_x=4, sweep=False)
        self.add_line('stem-r', (20, 26), (20, 24))
        self.add_bezier('right', (20, 24), ((20, 20), (25, 17), (25, 10)))
        self.add_contour('cup', 'left', 'stem-l', 'stem-base', 'stem-r', 'right')
        self.relate('connect', 'cup', 'rim')

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
