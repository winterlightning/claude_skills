"""Independent 32px profile of geometric-shapes-in-rounded-square-batch-006-02.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '610733a3-dfd5-42df-9651-d396d039493b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/shapes_610733a3-dfd5-42df-9651-d396d039493b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('610733a3-dfd5-42df-9651-d396d039493b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/design/shapes_610733a3-dfd5-42df-9651-d396d039493b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/geometric-shapes-in-rounded-square-batch-006-02',)
SOLO_SOURCE_ICON_IDS = ('geometric-shapes-in-rounded-square-batch-006-02',)
REFERENCE_EXPORT_SHA256 = 'd38ff80d7fc9183b47c7ff0c0ba2e766d259eed2a5f1a6bfa3e53affb9940c45'

class DrawingVariant2(Sub32):
    icon_id = 'geometric-shapes-in-rounded-square-batch-006-02-sub32-v2'
    variant_of = 'geometric-shapes-in-rounded-square-batch-006-02-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/batch-006'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Separate circle, square and triangle. Construction reference: shapes: three distinct geometric forms."""
        circle(self, 'circle', 9, 8, 6)
        box(self, 'square', 2, 22, 10, 30, 0)
        self.add_polyline('triangle', (18, 30), (24, 18), (30, 30), (18, 30))

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
