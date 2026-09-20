"""Independent 32px profile of vintage-movie-camera-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e27f92c4-11f6-4c62-91f1-78b562213eb2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/video_e27f92c4-11f6-4c62-91f1-78b562213eb2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e27f92c4-11f6-4c62-91f1-78b562213eb2', 'pictographic-primitives/state/video_e27f92c4-11f6-4c62-91f1-78b562213eb2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/vintage-movie-camera-solo',)
SOLO_SOURCE_ICON_IDS = ('vintage-movie-camera-solo',)
REFERENCE_EXPORT_SHA256 = '68e2a0a36089dd99416d90054cef68f6915ee4d4ca7bae94e8cbda4866843754'

class DrawingVariant2(Sub32):
    icon_id = 'vintage-movie-camera-sub32-v2'
    variant_of = 'vintage-movie-camera-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Vintage film camera with broad round left reel attached to the roof, smaller separate right reel, rounded body and flared lens. Construction reference: film / video."""
        self.add_bezier('reel-l', (5, 15), ((2, 13), (2, 11), (2, 9)))
        self.add_arc('reel-top', (2, 9), (16, 9), radius_x=7)
        self.add_bezier('reel-r', (16, 9), ((16, 12), (15, 14), (13, 15)))
        self.add_contour('large-reel', 'reel-l', 'reel-top', 'reel-r')
        circle(self, 'small-reel', 26, 8, 3)
        box(self, 'body', 2, 15, 22, 30, 3)
        self.relate('connect', 'body', 'large-reel')
        self.add_polyline('lens', (22, 20), (30, 17), (30, 27), (22, 24))
        self.relate('connect', 'lens', 'body')

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
