"""Independent 32px profile of horse-head-symbol.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '9fa5c4e8-5509-4115-889b-fb3874cf4d30'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/horse head_9fa5c4e8-5509-4115-889b-fb3874cf4d30.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9fa5c4e8-5509-4115-889b-fb3874cf4d30', 'pictographic-primitives/symbol/horse head_9fa5c4e8-5509-4115-889b-fb3874cf4d30.svg'),)
PROFILE_SOURCE_KEYS = ('solo/horse-head-symbol',)
SOLO_SOURCE_ICON_IDS = ('horse-head-symbol',)
REFERENCE_EXPORT_SHA256 = '9830f4531c1a5eb2f9d41b627ac8e8f9751a2fbcf73d9a6087a3673909682c40'

class DrawingVariant2(Sub32):
    icon_id = 'horse-head-symbol-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Right-facing horse head with pointed ear, projecting muzzle, curved neck and flat base. Construction reference: none."""
        self.add_bezier('back', (4, 30), ((4, 12), (6, 6), (16, 5)))
        self.add_line('ear-a', (16, 5), (18, 2))
        self.add_line('ear-b', (18, 2), (19, 7))
        self.add_line('face', (19, 7), (28, 13))
        self.add_line('nose', (28, 13), (26, 18))
        self.add_bezier('muzzle', (26, 18), ((24, 20), (21, 17), (17, 16)))
        self.add_bezier('neck', (17, 16), ((16, 21), (19, 27), (22, 30)))
        self.add_line('base', (22, 30), (4, 30))
        self.add_contour('horse', 'back', 'ear-a', 'ear-b', 'face', 'nose', 'muzzle', 'neck', 'base', closed=True)

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
