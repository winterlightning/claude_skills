"""Independent 32px profile of hand-pointing-at-3d-cube-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ec7d49e5-85a7-4bad-943c-fff9ce408048'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/hand point cube_ec7d49e5-85a7-4bad-943c-fff9ce408048.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ec7d49e5-85a7-4bad-943c-fff9ce408048', 'pictographic-primitives/state/hand point cube_ec7d49e5-85a7-4bad-943c-fff9ce408048.svg'),)
PROFILE_SOURCE_KEYS = ('solo/hand-pointing-at-3d-cube-solo',)
SOLO_SOURCE_ICON_IDS = ('hand-pointing-at-3d-cube-solo',)
REFERENCE_EXPORT_SHA256 = '0e04905611e451ab5d0a6d6e41b7eb57acab6019ea75f93e8c669e6cca7cf905'

class DrawingVariant2(Sub32):
    icon_id = 'hand-pointing-at-3d-cube-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Perspective cube above a small upward-pointing hand. Construction reference: box and human_ref/full_body_ref.png: geometric cube and simplified gesture."""
        self.add_polyline('cube-top', (12, 7), (21, 2), (30, 7), (21, 12), (12, 7))
        self.add_polyline('cube-front', (21, 12), (21, 23), (30, 18), (30, 7))
        self.relate('connect', 'cube-front', 'cube-top')
        self.add_line('cube-open-edge', (12, 7), (12, 15))
        self.relate('connect', 'cube-open-edge', 'cube-top')
        self.add_polyline('hand', (4, 20), (4, 28), (10, 28), (10, 30))
        self.add_line('thumb', (2, 26), (4, 28))
        self.relate('connect', 'thumb', 'hand')

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
