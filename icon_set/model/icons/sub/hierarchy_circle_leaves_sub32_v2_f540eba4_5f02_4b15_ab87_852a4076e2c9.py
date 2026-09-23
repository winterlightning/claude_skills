"""Independent 32px profile of hierarchy-circle-leaves.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f540eba4-5f02-4b15-ab87-852a4076e2c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/programing/hierarchy_f540eba4-5f02-4b15-ab87-852a4076e2c9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f540eba4-5f02-4b15-ab87-852a4076e2c9', 'pictographic-primitives/programing/hierarchy_f540eba4-5f02-4b15-ab87-852a4076e2c9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hierarchy-circle-leaves',)
SOLO_SOURCE_ICON_IDS = ('hierarchy-circle-leaves',)
REFERENCE_EXPORT_SHA256 = '422d84c25ff1bd4c6142b6667dbf3634fef2ece6d3334d62e375e856b66df33a'

class DrawingVariant2(Sub32):
    icon_id = 'hierarchy-circle-leaves-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/programming'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """One square root, central stem, branch and two truly circular leaves. Construction reference: network."""
        box(self, 'root', 12, 2, 20, 10, 1)
        self.add_line('stem', (16, 10), (16, 18))
        self.relate('connect', 'stem', 'root')
        self.add_polyline('branch', (5, 24), (5, 18), (27, 18), (27, 24))
        self.relate('connect', 'branch', 'stem')
        for x in (5, 27):
            circle(self, f'leaf-{x}', x, 27, 3)
            self.relate('connect', f'leaf-{x}', 'branch')

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
