"""Independent 32px profile of single-tail-award-badge.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4e2ed51b-8309-4e10-861b-a51459770e84'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/rewards/badge_4e2ed51b-8309-4e10-861b-a51459770e84.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4e2ed51b-8309-4e10-861b-a51459770e84', 'pictographic-primitives/rewards/badge_4e2ed51b-8309-4e10-861b-a51459770e84.svg'),)
PROFILE_SOURCE_KEYS = ('solo/single-tail-award-badge',)
SOLO_SOURCE_ICON_IDS = ('single-tail-award-badge',)
REFERENCE_EXPORT_SHA256 = 'cfcb94ead085503027d1aa95c3ffb1e312499fc2f5d9f21ef717ca752e5bf81e'

class DrawingVariant2(Sub32):
    icon_id = 'single-tail-award-badge-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/award'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular medal with one long notched ribbon, both ribbon openings kept clear. Construction reference: award."""
        circle(self, 'medal', 16, 10, 8)
        self.add_polyline('ribbon', (10, 15), (10, 30), (16, 26), (22, 30), (22, 15))
        self.relate('connect', 'medal', 'ribbon')

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
