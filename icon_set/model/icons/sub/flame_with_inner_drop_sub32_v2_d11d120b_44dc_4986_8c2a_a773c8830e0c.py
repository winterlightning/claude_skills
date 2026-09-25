"""Independent 32px profile of flame-with-inner-drop.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd11d120b-44dc-4986-8c2a-a773c8830e0c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/fire/flame_d11d120b-44dc-4986-8c2a-a773c8830e0c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d11d120b-44dc-4986-8c2a-a773c8830e0c', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/flame_d11d120b-44dc-4986-8c2a-a773c8830e0c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/flame-with-inner-drop',)
SOLO_SOURCE_ICON_IDS = ('flame-with-inner-drop',)
REFERENCE_EXPORT_SHA256 = '6480a8274acccf6a7f1325e9837658e0827c5d5b5d6b54a54acbb3a1bddf168a'

class DrawingVariant2(Sub32):
    icon_id = 'flame-with-inner-drop-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'fire'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Complete flame with right lick and lower inner drop; widen the outer body to keep the inner tip visibly separate. Construction reference: flame."""
        self.add_bezier('outer-lower-left', (12, 30), ((6, 28), (2, 24), (2, 20)))
        self.add_bezier('outer-upper-left', (2, 20), ((2, 13), (16, 10), (13, 2)))
        self.add_bezier('outer-top', (13, 2), ((21, 7), (23, 11), (21, 15)))
        self.add_bezier('lick-top', (21, 15), ((26, 14), (28, 12), (28, 9)))
        self.add_bezier('lick-right', (28, 9), ((29, 13), (30, 17), (30, 20)))
        self.add_bezier('outer-lower-right', (30, 20), ((30, 25), (24, 28), (20, 30)))
        self.add_contour('outer', 'outer-lower-left', 'outer-upper-left', 'outer-top', 'lick-top', 'lick-right', 'outer-lower-right')
        self.add_bezier('inner-left', (12, 30), ((7, 25), (10, 22), (15, 19)))
        self.add_bezier('inner-right', (15, 19), ((15, 24), (25, 24), (20, 30)))
        self.add_contour('inner', 'inner-left', 'inner-right')
        self.relate('connect', 'inner', 'outer')

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
