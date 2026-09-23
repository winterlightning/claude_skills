"""Independent 32px profile of strategy-play.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'cf25f25b-0432-4d98-b894-c281bc60e8ea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/strategy_cf25f25b-0432-4d98-b894-c281bc60e8ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('cf25f25b-0432-4d98-b894-c281bc60e8ea', 'pictographic-primitives/symbol/strategy_cf25f25b-0432-4d98-b894-c281bc60e8ea.svg'),)
PROFILE_SOURCE_KEYS = ('solo/strategy-play',)
SOLO_SOURCE_ICON_IDS = ('strategy-play',)
REFERENCE_EXPORT_SHA256 = '12f2cddb08d6a6b936834fd64f3caf3b6e1043a25627b64dfe1fddcf92081101'

class DrawingVariant2(Sub32):
    icon_id = 'strategy-play-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two X marks, circular start node and curved rising arrow with head. Construction reference: route."""
        circle(self, 'start', 5, 27, 3)
        self.add_bezier('route-l', (5, 24), ((5, 16), (10, 16), (16, 16)))
        self.add_bezier('route-r', (16, 16), ((24, 16), (27, 12), (27, 2)))
        self.add_contour('route', 'route-l', 'route-r')
        self.relate('connect', 'start', 'route')
        self.add_polyline('arrow', (22, 7), (27, 2), (30, 7))
        self.relate('connect', 'arrow', 'route')
        for name, x, y in [('upper', 5, 5), ('lower', 26, 26)]:
            self.add_line(name + '-a', (x - 3, y - 3), (x + 3, y + 3))
            self.add_line(name + '-b', (x + 3, y - 3), (x - 3, y + 3))
            self.relate('connect', name + '-a', name + '-b')

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
