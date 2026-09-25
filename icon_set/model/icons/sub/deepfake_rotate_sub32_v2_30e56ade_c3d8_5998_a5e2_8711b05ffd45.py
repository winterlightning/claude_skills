"""Independent 32px profile of deepfake-rotate.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '30e56ade-c3d8-5998-a5e2-8711b05ffd45'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/artificial-intelligence/deepfake rotate_30e56ade-c3d8-5998-a5e2-8711b05ffd45.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('30e56ade-c3d8-5998-a5e2-8711b05ffd45', 'pictographic-primitives/artificial-intelligence/deepfake rotate_30e56ade-c3d8-5998-a5e2-8711b05ffd45.svg'),)
PROFILE_SOURCE_KEYS = ('solo/deepfake-rotate',)
SOLO_SOURCE_ICON_IDS = ('deepfake-rotate',)
REFERENCE_EXPORT_SHA256 = '744a2a18a095297bca04c268ad53b850a868e36427cc4ccf87e4f939c79a79f6'

class DrawingVariant2(Sub32):
    icon_id = 'deepfake-rotate-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular rotation arrow with a break at upper right and curved diagonal internal sweep. Construction reference: rotate-cw."""
        self.add_bezier('outer-a', (18, 4), ((13, 4), (9, 6), (7, 9)))
        self.add_bezier('outer-upper-left', (7, 9), ((5, 12), (4, 14), (4, 17)))
        self.add_bezier('outer-b', (4, 17), ((4, 24), (9, 30), (16, 30)))
        self.add_bezier('outer-c', (16, 30), ((21, 30), (25, 27), (27, 23)))
        self.add_bezier('outer-lower-right', (27, 23), ((28, 21), (28, 19), (28, 17)))
        self.add_bezier('outer-d', (28, 17), ((28, 13), (26, 10), (24, 8)))
        self.add_contour('outer', 'outer-a', 'outer-upper-left', 'outer-b', 'outer-c', 'outer-lower-right', 'outer-d')
        self.add_polyline('arrow', (12, 2), (18, 4), (14, 8))
        self.relate('connect', 'arrow', 'outer')
        self.add_bezier('sweep', (7, 9), ((10, 17), (20, 23), (27, 23)))
        self.relate('connect', 'sweep', 'outer')

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
