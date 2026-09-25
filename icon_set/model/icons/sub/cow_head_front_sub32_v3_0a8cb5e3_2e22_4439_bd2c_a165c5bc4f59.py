"""Independent 32px profile of cow-head-front.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/bull head_0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59', 'pictographic-primitives/symbol/bull head_0a8cb5e3-2e22-4439-bd2c-a165c5bc4f59.svg'),)
PROFILE_SOURCE_KEYS = ('solo/cow-head-front',)
SOLO_SOURCE_ICON_IDS = ('cow-head-front',)
REFERENCE_EXPORT_SHA256 = '41004d51be8811ac90edff7215b79923799d47b45a94f525f5eb86efb036ea77'

class DrawingVariant3(Sub32):
    icon_id = 'cow-head-front-sub32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Long cow face with rounded chin, two open side ears and two upward curved horns. Construction reference: none."""
        self.add_bezier('forehead', (11, 8), ((14, 6), (18, 6), (21, 8)))
        self.add_line('face-r', (21, 8), (21, 25))
        self.add_bezier('jaw-r', (21, 25), ((21, 28), (20, 30), (16, 30)))
        self.add_bezier('jaw-l', (16, 30), ((12, 30), (11, 28), (11, 25)))
        self.add_line('face-l', (11, 25), (11, 8))
        self.add_contour('face', 'forehead', 'face-r', 'jaw-r', 'jaw-l', 'face-l', closed=True)
        self.add_bezier('horn-l', (11, 8), ((8, 8), (6, 5), (6, 2)))
        self.add_bezier('horn-r', (21, 8), ((24, 8), (26, 5), (26, 2)))
        self.add_polyline('ear-l', (11, 8), (2, 16), (11, 22))
        self.add_polyline('ear-r', (21, 8), (30, 16), (21, 22))
        for p in ('horn-l', 'horn-r', 'ear-l', 'ear-r'):
            self.relate('connect', p, 'face')
        self.relate('connect', 'horn-l', 'ear-l')
        self.relate('connect', 'horn-r', 'ear-r')

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
