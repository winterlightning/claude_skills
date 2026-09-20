"""Independent 32px profile of house-b6632e92.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b6632e92-d138-462e-a017-77d5e5b870dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/house_b6632e92-d138-462e-a017-77d5e5b870dd.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b6632e92-d138-462e-a017-77d5e5b870dd', 'pictographic-primitives/interface-essential/house_b6632e92-d138-462e-a017-77d5e5b870dd.svg'),)
PROFILE_SOURCE_KEYS = ('solo/house-b6632e92',)
SOLO_SOURCE_ICON_IDS = ('house-b6632e92',)
REFERENCE_EXPORT_SHA256 = '6a73c41cd7d09f798690ebf6158c62280ab6d0b8aa8a67a50ea84ab3b895176c'

class DrawingVariant2(Sub32):
    icon_id = 'house-b6632e92-sub32-v2'
    variant_of = 'house-b6632e92-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """House roof with two overhangs, square body and short horizontal interior mark. Construction reference: house."""
        self.add_polyline('roof', (2, 16), (16, 2), (30, 16))
        self.add_polyline('body', (6, 12), (6, 30), (26, 30), (26, 12))
        self.relate('connect', 'roof', 'body')
        self.add_line('mark', (12, 22), (20, 22))

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
