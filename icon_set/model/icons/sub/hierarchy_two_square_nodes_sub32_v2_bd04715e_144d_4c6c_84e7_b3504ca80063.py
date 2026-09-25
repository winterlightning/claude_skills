"""Independent 32px profile of hierarchy-two-square-nodes.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'bd04715e-144d-4c6c-84e7-b3504ca80063'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/programing/hierarchy_bd04715e-144d-4c6c-84e7-b3504ca80063.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('bd04715e-144d-4c6c-84e7-b3504ca80063', 'pictographic-primitives/programing/hierarchy_bd04715e-144d-4c6c-84e7-b3504ca80063.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hierarchy-two-square-nodes',)
SOLO_SOURCE_ICON_IDS = ('hierarchy-two-square-nodes',)
REFERENCE_EXPORT_SHA256 = 'aef39f16091aa56e8e083fb4c5fda10865b79c2467ffdd9c7b10c0340367cc80'

class DrawingVariant2(Sub32):
    icon_id = 'hierarchy-two-square-nodes-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'programing'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Square root node, connected branching stem and two square child nodes. Small-size treatment: Simplified the stepped branch routing to two direct links, retaining all three square nodes. Construction reference: network: connected node hierarchy."""
        box(self, 'root', 12, 2, 20, 10, 0)
        box(self, 'left', 2, 22, 10, 30, 0)
        box(self, 'right', 22, 22, 30, 30, 0)
        for name, x in [('left', 6), ('right', 26)]:
            self.add_line(name + '-link', (16, 10), (x, 22))
            self.relate('connect', name + '-link', 'root')
            self.relate('connect', name + '-link', name)
        self.relate('connect', 'left-link', 'right-link')

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
