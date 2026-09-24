"""Independent 32px profile of three-arrows-down.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4fe44175-fb41-4dbd-a349-bde8c4354a91'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/three arrows down_4fe44175-fb41-4dbd-a349-bde8c4354a91.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4fe44175-fb41-4dbd-a349-bde8c4354a91', 'pictographic-primitives/state/three arrows down_4fe44175-fb41-4dbd-a349-bde8c4354a91.svg'),)
PROFILE_SOURCE_KEYS = ('solo/three-arrows-down',)
SOLO_SOURCE_ICON_IDS = ('three-arrows-down',)
REFERENCE_EXPORT_SHA256 = 'a642aaee0d5b7509366d15c650f70e035204ba14d54e5e1cf992233277c23a7c'

class DrawingVariant2(Sub32):
    icon_id = 'three-arrows-down-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Three downward arrows, center arrow lower than the two matching outer arrows. Construction reference: arrow-down."""
        for name, x, y in [('left', 6, 2), ('right', 26, 2), ('middle', 16, 14)]:
            self.add_line(name + '-stem', (x, y), (x, y + 16))
            self.add_polyline(name + '-head', (x - 4, y + 12), (x, y + 16), (x + 4, y + 12))
            self.relate('connect', name + '-head', name + '-stem')

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
