"""Independent 32px profile of thermometer-mercury.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b9550739-2fcc-4d3f-b1da-62a62d9213f5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/thermometer_b9550739-2fcc-4d3f-b1da-62a62d9213f5.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b9550739-2fcc-4d3f-b1da-62a62d9213f5', 'pictographic-primitives/symbol/thermometer_b9550739-2fcc-4d3f-b1da-62a62d9213f5.svg'),)
PROFILE_SOURCE_KEYS = ('solo/thermometer-mercury',)
SOLO_SOURCE_ICON_IDS = ('thermometer-mercury',)
REFERENCE_EXPORT_SHA256 = '9433a09109e9f1cdfb74828e8676ad88c428493c5035e679adb41688fd4eefa9'

class DrawingVariant2(Sub32):
    icon_id = 'thermometer-mercury-sub32-v2'
    variant_of = 'thermometer-mercury-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded thermometer shell, vertical mercury line and detached bulb dot. Construction reference: thermometer."""
        self.add_arc('cap', (8, 10), (24, 10), radius_x=8)
        self.add_line('neck-r', (24, 10), (24, 19))
        self.add_bezier('bulb-r', (24, 19), ((28, 19), (28, 21), (28, 23)))
        self.add_arc('bulb-bottom', (28, 23), (4, 23), radius_x=12, radius_y=7)
        self.add_bezier('bulb-l', (4, 23), ((4, 21), (4, 19), (8, 19)))
        self.add_line('neck-l', (8, 19), (8, 10))
        self.add_contour('shell', 'cap', 'neck-r', 'bulb-r', 'bulb-bottom', 'bulb-l', 'neck-l', closed=True)
        self.add_line('mercury', (16, 9), (16, 16))
        self.add_dot('bulb', (16, 23))

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
