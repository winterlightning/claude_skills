"""Independent 32px profile of concentric-circles.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '26e01ba9-21e7-4f28-81fc-dbb55673230c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/concentric circles_26e01ba9-21e7-4f28-81fc-dbb55673230c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('26e01ba9-21e7-4f28-81fc-dbb55673230c', 'pictographic-primitives/symbol/concentric circles_26e01ba9-21e7-4f28-81fc-dbb55673230c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/concentric-circles',)
SOLO_SOURCE_ICON_IDS = ('concentric-circles',)
REFERENCE_EXPORT_SHA256 = '47bdd3925984cab8e42192c0b6dd0c984af45fa0a80c625d4559e95cc18302a4'

class DrawingVariant2(Sub32):
    icon_id = 'concentric-circles-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two complete concentric circular outlines with open center. Construction reference: circle."""
        circle(self, 'frame', 16, 16, 14)
        circle(self, 'inner', 16, 16, 7)

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
