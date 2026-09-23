"""Independent 32px profile of cube.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '802601c0-689d-481d-86cd-d13aceeaf9a1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/cube_802601c0-689d-481d-86cd-d13aceeaf9a1.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('802601c0-689d-481d-86cd-d13aceeaf9a1', 'pictographic-primitives/symbol/cube_802601c0-689d-481d-86cd-d13aceeaf9a1.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cube',)
SOLO_SOURCE_ICON_IDS = ('cube',)
REFERENCE_EXPORT_SHA256 = 'f611f6378bc2d5b73eb4eb1f7aaac8312a3ca19eedfc0e3077d2e4015c86f227'

class DrawingVariant2(Sub32):
    icon_id = 'cube-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Perspective cube with three faces; one common central node. Construction reference: box."""
        self.add_polyline('outline', (16, 2), (30, 9), (30, 23), (16, 30), (2, 23), (2, 9), closed=True)
        self.add_polyline('upper-edges', (2, 9), (16, 16), (30, 9))
        self.add_line('front-edge', (16, 16), (16, 30))
        self.relate('connect', 'outline', 'upper-edges')
        self.relate('connect', 'outline', 'front-edge')
        self.relate('connect', 'upper-edges', 'front-edge')

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
