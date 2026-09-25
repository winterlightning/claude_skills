"""Independent 32px profile of stethoscope.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd302c6d8-a92a-4d28-bbf2-86fef555f93f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/stethoscope_d302c6d8-a92a-4d28-bbf2-86fef555f93f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d302c6d8-a92a-4d28-bbf2-86fef555f93f', 'pictographic-primitives/symbol/stethoscope_d302c6d8-a92a-4d28-bbf2-86fef555f93f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/stethoscope',)
SOLO_SOURCE_ICON_IDS = ('stethoscope',)
REFERENCE_EXPORT_SHA256 = '41b12e62b7ad988e90811b3e82a5d0ebf1efa864f1509281bbf4b90cfed740d0'

class DrawingVariant2(Sub32):
    icon_id = 'stethoscope-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Stethoscope with two earpieces, round U yoke, curved tube and circular chestpiece. Construction reference: stethoscope."""
        self.add_polyline('left', (6, 2), (2, 4), (2, 13))
        self.add_arc('yoke', (2, 13), (16, 13), radius_x=7, sweep=False)
        self.add_polyline('right', (16, 13), (16, 4), (12, 2))
        self.relate('connect', 'left', 'yoke')
        self.relate('connect', 'right', 'yoke')
        self.add_line('tube-l', (9, 20), (9, 21))
        self.add_arc('tube-bottom', (9, 21), (27, 21), radius_x=9, sweep=False)
        self.add_line('tube-r', (27, 21), (27, 11))
        self.add_contour('tube', 'tube-l', 'tube-bottom', 'tube-r')
        self.relate('connect', 'tube', 'yoke')
        circle(self, 'chest', 27, 8, 3)
        self.relate('connect', 'tube', 'chest')

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
