"""Independent 32px profile of make-up-brush.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'e16dd241-96b2-4b10-9b5a-ee1bb50491a2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/beauty/make up brush_e16dd241-96b2-4b10-9b5a-ee1bb50491a2.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e16dd241-96b2-4b10-9b5a-ee1bb50491a2', 'pictographic-primitives/beauty/make up brush_e16dd241-96b2-4b10-9b5a-ee1bb50491a2.svg'),)
PROFILE_SOURCE_KEYS = ('solo/make-up-brush',)
SOLO_SOURCE_ICON_IDS = ('make-up-brush',)
REFERENCE_EXPORT_SHA256 = '15b5e36562673a9e61b4b1b34483fb391015a4ffa272fc1542839c4c3c08da9b'

class DrawingVariant2(Sub32):
    icon_id = 'make-up-brush-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'beauty'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Makeup brush with domed bristles, single bristle stroke, ferrule and rounded handle. Construction reference: brush."""
        self.add_arc('bristles-top', (4, 8), (28, 8), radius_x=12, radius_y=6)
        self.add_polyline('bristles-sides', (28, 8), (22, 16), (10, 16), (4, 8))
        self.relate('connect', 'bristles-sides', 'bristles-top')
        self.add_line('bristle', (15, 9), (16, 16))
        self.relate('connect', 'bristle', 'bristles-sides')
        self.add_polyline('handle-r', (22, 16), (22, 20), (20, 23), (20, 26))
        self.add_arc('handle-bottom', (20, 26), (12, 26), radius_x=4)
        self.add_polyline('handle-l', (12, 26), (12, 23), (10, 20), (10, 16))
        self.relate('connect', 'handle-r', 'handle-bottom')
        self.relate('connect', 'handle-l', 'handle-bottom')
        self.relate('connect', 'handle-r', 'bristles-sides')
        self.relate('connect', 'handle-l', 'bristles-sides')

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
