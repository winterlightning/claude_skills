"""Independent 32px profile of helmet-d5b67122.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd5b67122-8eaa-475e-8ad0-0d51c15807ab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/protection/helmet_d5b67122-8eaa-475e-8ad0-0d51c15807ab.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d5b67122-8eaa-475e-8ad0-0d51c15807ab', 'pictographic-primitives/protection/helmet_d5b67122-8eaa-475e-8ad0-0d51c15807ab.svg'),)
PROFILE_SOURCE_KEYS = ('solo/helmet-d5b67122',)
SOLO_SOURCE_ICON_IDS = ('helmet-d5b67122',)
REFERENCE_EXPORT_SHA256 = 'ef4d35f716e8a78bb97617de1e25b23dfcccdaf0dc8bb4d25604baef4e643336'

class DrawingVariant2(Sub32):
    icon_id = 'helmet-d5b67122-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Hard-hat paired elliptical dome shoulders, open central ridge and brim. Construction reference: hard-hat."""
        self.add_line('brim', (2, 28), (30, 28))
        self.add_arc('left-dome', (4, 28), (12, 10), radius_x=8, radius_y=18)
        self.add_arc('right-dome', (20, 10), (28, 28), radius_x=8, radius_y=18)
        self.add_polyline('ridge', (12, 14), (12, 4), (20, 4), (20, 14))
        for a, b in [('brim', 'left-dome'), ('brim', 'right-dome'), ('ridge', 'left-dome'), ('ridge', 'right-dome')]:
            self.relate('connect', a, b)

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
