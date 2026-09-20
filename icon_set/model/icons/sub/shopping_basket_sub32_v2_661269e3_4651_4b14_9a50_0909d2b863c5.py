"""Independent 32px profile of shopping-basket.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '661269e3-4651-4b14-9a50-0909d2b863c5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/shopping/shopping basket_661269e3-4651-4b14-9a50-0909d2b863c5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('661269e3-4651-4b14-9a50-0909d2b863c5', 'pictographic-primitives/shopping/shopping basket_661269e3-4651-4b14-9a50-0909d2b863c5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shopping-basket',)
SOLO_SOURCE_ICON_IDS = ('shopping-basket',)
REFERENCE_EXPORT_SHA256 = 'c83f38101b2d8df7cbe47d2c0e91da7b5dbc125e0ddfe9ce1eafc012de998c04'

class DrawingVariant2(Sub32):
    icon_id = 'shopping-basket-sub32-v2'
    variant_of = 'shopping-basket-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tapered basket, two detached upward handle arms and two short slanted slots. Construction reference: shopping-basket."""
        self.add_line('rim', (2, 12), (30, 12))
        self.add_line('right', (30, 12), (25, 26))
        self.add_bezier('br', (25, 26), ((25, 28), (23, 28), (22, 28)))
        self.add_line('base', (22, 28), (10, 28))
        self.add_bezier('bl', (10, 28), ((9, 28), (7, 28), (7, 26)))
        self.add_line('left', (7, 26), (2, 12))
        self.add_contour('basket', 'rim', 'right', 'br', 'base', 'bl', 'left', closed=True)
        for n, a, b in [('left-handle', (6, 12), (10, 4)), ('right-handle', (26, 12), (22, 4))]:
            self.add_line(n, a, b)
            self.relate('connect', n, 'basket')
        self.add_line('slot-l', (12, 19), (13, 21))
        self.add_line('slot-r', (20, 19), (19, 21))

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
