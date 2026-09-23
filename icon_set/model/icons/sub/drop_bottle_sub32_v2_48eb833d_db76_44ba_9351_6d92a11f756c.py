"""Independent 32px profile of drop-bottle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '48eb833d-db76-44ba-9351-6d92a11f756c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/drop bottle_48eb833d-db76-44ba-9351-6d92a11f756c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('48eb833d-db76-44ba-9351-6d92a11f756c', 'pictographic-primitives/symbol/drop bottle_48eb833d-db76-44ba-9351-6d92a11f756c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/drop-bottle',)
SOLO_SOURCE_ICON_IDS = ('drop-bottle',)
REFERENCE_EXPORT_SHA256 = 'd8dbcc733c8c0f8aa0944a5bcb2205ad7b927eafd7af1202d73a348c48b36f96'

class DrawingVariant2(Sub32):
    icon_id = 'drop-bottle-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Drop bottle with rounded nozzle, sloping shoulder and distinct lower body seam. Construction reference: none."""
        self.add_arc('tip', (12, 6), (20, 6), radius_x=4)
        self.add_bezier('neck-r', (20, 6), ((20, 10), (25, 10), (25, 16)))
        self.add_line('seam', (25, 16), (7, 16))
        self.add_bezier('neck-l', (7, 16), ((7, 10), (12, 10), (12, 6)))
        self.add_contour('neck', 'tip', 'neck-r', 'seam', 'neck-l', closed=True)
        self.add_bezier('body-r', (25, 16), ((28, 17), (28, 18), (28, 21)))
        self.add_line('right', (28, 21), (28, 26))
        self.add_arc('br', (28, 26), (24, 30), radius_x=4)
        self.add_line('base', (24, 30), (8, 30))
        self.add_arc('bl', (8, 30), (4, 26), radius_x=4)
        self.add_line('left', (4, 26), (4, 21))
        self.add_bezier('body-l', (4, 21), ((4, 18), (4, 17), (7, 16)))
        self.add_contour('body', 'body-r', 'right', 'br', 'base', 'bl', 'left', 'body-l')
        self.relate('connect', 'body', 'neck')

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
