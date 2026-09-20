"""Independent 32px profile of three-leaf-sprout.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f0327d2c-bb99-5e91-9ec2-af95814cf0fe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/nature/plant_f0327d2c-bb99-5e91-9ec2-af95814cf0fe.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f0327d2c-bb99-5e91-9ec2-af95814cf0fe', 'pictographic-primitives/nature/plant_f0327d2c-bb99-5e91-9ec2-af95814cf0fe.svg'), ('4a47df00-a455-41d9-84a4-6416eb861ee6', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/leaf_4a47df00-a455-41d9-84a4-6416eb861ee6.svg'))
PROFILE_SOURCE_KEYS = ('solo/three-leaf-sprout',)
SOLO_SOURCE_ICON_IDS = ('three-leaf-sprout',)
REFERENCE_EXPORT_SHA256 = 'bfc02d96844395296df394aab25c07ed978e4bd958a79482b856d9d39470a98a'

class DrawingVariant2(Sub32):
    icon_id = 'three-leaf-sprout-sub32-v2'
    variant_of = 'three-leaf-sprout-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'nature/batch-02'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three open pointed leaves: top leaf attached to upright stem, two separated side leaves, and ground line. Construction reference: none."""
        self.add_bezier('top-l', (16, 2), ((10, 7), (10, 10), (16, 14)))
        self.add_bezier('top-r', (16, 14), ((22, 10), (22, 7), (16, 2)))
        self.add_contour('top', 'top-l', 'top-r', closed=True)
        self.add_line('stem', (16, 14), (16, 30))
        self.relate('connect', 'stem', 'top')
        for name, a, b, c1, c2, c3, c4 in [('left', (2, 14), (10, 24), (2, 24), (2, 24), (10, 18), (7, 16)), ('right', (30, 14), (22, 24), (30, 24), (30, 24), (22, 18), (25, 16))]:
            self.add_bezier(name + '-a', a, (c1, c2, b))
            self.add_bezier(name + '-b', b, (c3, c4, a))
            self.add_contour(name, name + '-a', name + '-b', closed=True)
        self.add_line('ground', (8, 30), (24, 30))
        self.relate('connect', 'ground', 'stem')

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
