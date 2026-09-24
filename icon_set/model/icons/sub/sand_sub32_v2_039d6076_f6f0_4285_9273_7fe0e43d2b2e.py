"""Independent 32px profile of sand.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '039d6076-f6f0-4285-9273-7fe0e43d2b2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/sand_039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('039d6076-f6f0-4285-9273-7fe0e43d2b2e', 'pictographic-primitives/state/sand_039d6076-f6f0-4285-9273-7fe0e43d2b2e.svg'),)
PROFILE_SOURCE_KEYS = ('solo/sand',)
SOLO_SOURCE_ICON_IDS = ('sand',)
REFERENCE_EXPORT_SHA256 = 'db243ce3cbb6059099dbd79c7244b776ccc3c7a24a2cc1c936775dbfbda8dbfc'

class DrawingVariant2(Sub32):
    icon_id = 'sand-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Open triangular sand mound with three separate dots inside. Construction reference: mountain."""
        self.add_polyline('mound', (2, 28), (16, 4), (30, 28))
        for i, p in enumerate(((11, 26), (21, 26), (16, 18))):
            self.add_dot(f'grain-{i}', p)

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
