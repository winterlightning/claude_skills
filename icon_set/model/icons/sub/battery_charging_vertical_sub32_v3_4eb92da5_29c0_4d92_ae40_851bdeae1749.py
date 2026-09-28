"""Independent 32px profile of battery-charging-vertical.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4eb92da5-29c0-4d92-ae40-851bdeae1749'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/lightning rectangle_4eb92da5-29c0-4d92-ae40-851bdeae1749.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4eb92da5-29c0-4d92-ae40-851bdeae1749', 'pictographic-primitives/symbol/lightning rectangle_4eb92da5-29c0-4d92-ae40-851bdeae1749.svg'),)
PROFILE_SOURCE_KEYS = ('solo/battery-charging-vertical',)
SOLO_SOURCE_ICON_IDS = ('battery-charging-vertical',)
REFERENCE_EXPORT_SHA256 = '0c8109e691174030648795152ecb7b76bf4a88561c03df1061f321f6c369f3c9'

class DrawingVariant3(Sub32):
    icon_id = 'battery-charging-vertical-sub32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Upright battery with raised terminal and a clear internal lightning bolt. Construction reference: battery-charging: open outline around the modifier."""
        self.add_line('left-bottom', (8, 30), (6, 30))
        self.add_arc('bl', (6, 30), (2, 26), radius_x=4)
        self.add_line('left', (2, 26), (2, 14))
        self.add_arc('tl', (2, 14), (6, 10), radius_x=4)
        self.add_polyline('terminal', (6, 10), (10, 10), (10, 2), (22, 2), (22, 10), (26, 10))
        self.add_arc('tr', (26, 10), (30, 14), radius_x=4)
        self.add_line('right', (30, 14), (30, 24))
        self.add_arc('br', (30, 24), (28, 26), radius_x=2)
        self.add_line('right-bottom', (28, 26), (28, 26))
        self.add_contour('left-frame', 'left-bottom', 'bl', 'left', 'tl')
        self.relate('connect', 'left-frame', 'terminal')
        self.add_contour('right-frame', 'tr', 'right', 'br', 'right-bottom')
        self.relate('connect', 'right-frame', 'terminal')
        self.add_polyline('bolt', (18, 16), (10, 24), (22, 24), (16, 30))

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
