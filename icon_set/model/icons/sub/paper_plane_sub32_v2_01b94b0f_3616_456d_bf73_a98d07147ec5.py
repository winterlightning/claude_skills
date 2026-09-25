"""Independent 32px profile of paper-plane.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '01b94b0f-3616-456d-bf73-a98d07147ec5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/paper plane_01b94b0f-3616-456d-bf73-a98d07147ec5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('01b94b0f-3616-456d-bf73-a98d07147ec5', 'pictographic-primitives/symbol/paper plane_01b94b0f-3616-456d-bf73-a98d07147ec5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/paper-plane',)
SOLO_SOURCE_ICON_IDS = ('paper-plane',)
REFERENCE_EXPORT_SHA256 = '173aaab2d36f786be99715d94ce571dad58f55691f819f722e4c0194659f7848'

class DrawingVariant2(Sub32):
    icon_id = 'paper-plane-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Paper plane with pointed upper-right nose, lower folded tail and internal fold ending inside. Construction reference: send."""
        self.add_polyline('plane', (2, 15), (30, 2), (23, 28), (15, 23), (11, 30), (10, 20), closed=True)
        self.add_line('fold', (10, 20), (18, 15))
        self.relate('connect', 'fold', 'plane')

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
