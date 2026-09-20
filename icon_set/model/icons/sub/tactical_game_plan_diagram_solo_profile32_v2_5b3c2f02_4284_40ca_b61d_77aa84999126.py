"""Independent 32px profile of tactical-game-plan-diagram-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5b3c2f02-4284-40ca-b61d-77aa84999126'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/strategy_5b3c2f02-4284-40ca-b61d-77aa84999126.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5b3c2f02-4284-40ca-b61d-77aa84999126', 'pictographic-primitives/state/strategy_5b3c2f02-4284-40ca-b61d-77aa84999126.svg'),)
PROFILE_SOURCE_KEYS = ('solo/tactical-game-plan-diagram-solo',)
SOLO_SOURCE_ICON_IDS = ('tactical-game-plan-diagram-solo',)
REFERENCE_EXPORT_SHA256 = '1a5497fa2fa112ad7d6880e943ae2a16cc938a1d74da0f85a82980c0a11374c8'

class DrawingVariant2(Sub32):
    icon_id = 'tactical-game-plan-diagram-solo-profile32-v2'
    variant_of = 'tactical-game-plan-diagram-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tactical diagram retaining both X marks, the circle and curved upward arrow. Construction reference: shared typeface / geometric source construction."""
        circle(self, 'start', 7, 25, 5)
        for name, x, y, r in [('upper', 7, 6, 3), ('lower', 27, 27, 3)]:
            self.add_line(name + '-a', (x - r, y - r), (x + r, y + r))
            self.add_line(name + '-b', (x - r, y + r), (x + r, y - r))
            self.relate('connect', name + '-a', name + '-b')
        self.add_bezier('route', (7, 20), ((7, 14), (24, 20), (24, 12)))
        self.add_line('up', (24, 12), (24, 2))
        self.add_contour('arrow', 'route', 'up')
        self.relate('connect', 'arrow', 'start')
        self.add_polyline('tip', (18, 8), (24, 2), (30, 8))
        self.relate('connect', 'tip', 'arrow')

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
