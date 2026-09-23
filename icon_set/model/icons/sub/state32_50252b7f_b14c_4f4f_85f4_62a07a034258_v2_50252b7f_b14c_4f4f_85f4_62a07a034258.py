"""Independent 32px profile of state32-50252b7f-b14c-4f4f-85f4-62a07a034258.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '50252b7f-b14c-4f4f-85f4-62a07a034258'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/three dots horizontal_50252b7f-b14c-4f4f-85f4-62a07a034258.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('50252b7f-b14c-4f4f-85f4-62a07a034258', 'pictographic-primitives/state/three dots horizontal_50252b7f-b14c-4f4f-85f4-62a07a034258.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-dots-horizontal',)
SOLO_SOURCE_ICON_IDS = ('three-dots-horizontal',)
REFERENCE_EXPORT_SHA256 = '212c70a81123cdf0115dc6ae81a137feafa69706bcd7632d34c80ef4281946eb'

class DrawingVariant2(Sub32):
    icon_id = 'state32-50252b7f-b14c-4f4f-85f4-62a07a034258-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded rectangular panel with exactly three equally spaced dots. Construction reference: none."""
        box(self, 'panel', 2, 4, 30, 28, 3)
        for i, x in enumerate((9, 16, 23)):
            self.add_dot(f'dot-{i}', (x, 16))

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
