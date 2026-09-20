"""Independent 32px profile of shopping-cart-left-handle.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ddf04c55-ea1f-4ecd-932d-d90c57f04ad7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/shopping/cart_ddf04c55-ea1f-4ecd-932d-d90c57f04ad7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ddf04c55-ea1f-4ecd-932d-d90c57f04ad7', 'pictographic-primitives/shopping/cart_ddf04c55-ea1f-4ecd-932d-d90c57f04ad7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shopping-cart-left-handle',)
SOLO_SOURCE_ICON_IDS = ('shopping-cart-left-handle',)
REFERENCE_EXPORT_SHA256 = 'b120d56527394bc2eda1d4b5623ec3a12f293089d0909a90fd821a80ca0d84b2'

class DrawingVariant2(Sub32):
    icon_id = 'shopping-cart-left-handle-sub32-v2'
    variant_of = 'shopping-cart-left-handle-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Shopping cart with left handle, closed basket, lower hook and two round wheels. Construction reference: shopping-cart."""
        self.add_polyline('handle', (2, 2), (6, 2), (10, 18))
        self.add_line('top', (8, 10), (30, 10))
        self.add_bezier('basket-r', (30, 10), ((30, 16), (29, 18), (26, 18)))
        self.add_line('base', (26, 18), (10, 18))
        self.add_contour('basket', 'top', 'basket-r', 'base')
        self.relate('connect', 'basket', 'handle')
        self.add_bezier('hook', (10, 18), ((8, 20), (8, 22), (10, 24)))
        self.relate('connect', 'hook', 'basket')
        self.relate('connect', 'hook', 'handle')
        self.add_dot('wheel-l', (12, 30))
        self.add_dot('wheel-r', (26, 30))

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
