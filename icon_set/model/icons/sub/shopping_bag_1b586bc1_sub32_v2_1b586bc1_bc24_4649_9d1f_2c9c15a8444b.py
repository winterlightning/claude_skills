"""Independent 32px profile of shopping-bag-1b586bc1.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '1b586bc1-bc24-4649-9d1f-2c9c15a8444b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1b586bc1-bc24-4649-9d1f-2c9c15a8444b', 'pictographic-primitives/shopping/shopping bag_1b586bc1-bc24-4649-9d1f-2c9c15a8444b.svg'), ('80985b68-e4c6-544f-91e4-19b090803024', 'pictographic-primitives/accessories/batch-07/bag carry_80985b68-e4c6-544f-91e4-19b090803024.svg'), ('a00cf782-226f-44d9-baca-8f8157db6f9a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/battery 2_a00cf782-226f-44d9-baca-8f8157db6f9a.svg'))
PROFILE_SOURCE_KEYS = ('solo/shopping-bag-1b586bc1', 'solo/shopping-bag-with-arched-handle')
SOLO_SOURCE_ICON_IDS = ('shopping-bag-1b586bc1', 'shopping-bag-with-arched-handle')
REFERENCE_EXPORT_SHA256 = '41a9f5f19bf82a9f429195d6eecc9bad2dab7033f694408c10e732d5f483fa58'

class DrawingVariant2(Sub32):
    icon_id = 'shopping-bag-1b586bc1-sub32-v2'
    variant_of = 'shopping-bag-1b586bc1-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'shopping'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded trapezoid shopping bag and arched handle extending below rim. Construction reference: shopping-bag."""
        self.add_line('top', (5, 12), (27, 12))
        self.add_bezier('right', (27, 12), ((28, 16), (30, 23), (30, 26)))
        self.add_arc('br', (30, 26), (26, 30), radius_x=4)
        self.add_line('base', (26, 30), (6, 30))
        self.add_arc('bl', (6, 30), (2, 26), radius_x=4)
        self.add_bezier('left', (2, 26), ((2, 23), (4, 16), (5, 12)))
        self.add_contour('bag', 'top', 'right', 'br', 'base', 'bl', 'left', closed=True)
        self.add_line('handle-l', (11, 16), (11, 7))
        self.add_arc('handle-top', (11, 7), (21, 7), radius_x=5)
        self.add_line('handle-r', (21, 7), (21, 16))
        self.add_contour('handle', 'handle-l', 'handle-top', 'handle-r')
        self.relate('connect', 'handle', 'bag')

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
