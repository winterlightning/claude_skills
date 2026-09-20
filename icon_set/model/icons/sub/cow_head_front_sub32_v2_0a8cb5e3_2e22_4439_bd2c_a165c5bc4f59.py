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

class DrawingVariant2(Sub32):
    icon_id = 'cow-head-front-sub32-v2'
    variant_of = 'cow-head-front-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbols/standalone'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Long cow face, two side ears and two upward-curved horns; no added eyes. Construction reference: none."""
        self.add_bezier('forehead', (8, 9), ((12, 7), (20, 7), (24, 9)))
        self.add_line('right-face', (24, 9), (22, 26))
        self.add_arc('jaw-r', (22, 26), (18, 30), radius_x=4)
        self.add_line('chin', (18, 30), (14, 30))
        self.add_arc('jaw-l', (14, 30), (10, 26), radius_x=4)
        self.add_line('left-face', (10, 26), (8, 9))
        self.add_contour('face', 'forehead', 'right-face', 'jaw-r', 'chin', 'jaw-l', 'left-face', closed=True)
        self.add_bezier('horn-l', (8, 9), ((5, 8), (3, 6), (3, 2)))
        self.add_bezier('horn-r', (24, 9), ((27, 8), (29, 6), (29, 2)))
        self.add_polyline('ear-l', (8, 9), (2, 18), (9, 20))
        self.add_polyline('ear-r', (24, 9), (30, 18), (23, 20))
        for n in ['horn-l', 'horn-r', 'ear-l', 'ear-r']:
            self.relate('connect', n, 'face')
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
