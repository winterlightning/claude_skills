"""Independent 32px profile of circles-three-trefoil.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '35f09f7d-689b-4b3c-944a-4e852904bb48'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/three circles_35f09f7d-689b-4b3c-944a-4e852904bb48.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('35f09f7d-689b-4b3c-944a-4e852904bb48', 'pictographic-primitives/symbol/three circles_35f09f7d-689b-4b3c-944a-4e852904bb48.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circles-three-trefoil',)
SOLO_SOURCE_ICON_IDS = ('circles-three-trefoil',)
REFERENCE_EXPORT_SHA256 = '9dfca71b04c9158a59f2cd57ae4fb855ac7a8074d06ab21738e1722f604ad89a'

class DrawingVariant2(Sub32):
    icon_id = 'circles-three-trefoil-sub32-v2'
    variant_of = 'circles-three-trefoil-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three equal open circles in a triangular cluster. Construction reference: circle: equal radii and shared triangular layout."""
        for name, x, y in [('top', 16, 7), ('left', 7, 25), ('right', 25, 25)]:
            circle(self, name, x, y, 5)

def box(s, n, l, t, r, b, k=3):
    if k == 0:
        s.add_polyline(n, (l, t), (r, t), (r, b), (l, b), (l, t))
        return
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
