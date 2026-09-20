"""Independent 32px profile of oval-check.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/oval check_fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c', 'pictographic-primitives/state/oval check_fcc6c0e8-8b5a-41f9-8c32-ac8f4d74f39c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/oval-check',)
SOLO_SOURCE_ICON_IDS = ('oval-check',)
REFERENCE_EXPORT_SHA256 = 'd72e7226c9146f68419dc2c8df7694c6870102230ad408f644f26251cec497af'

class DrawingVariant2(Sub32):
    icon_id = 'oval-check-sub32-v2'
    variant_of = 'oval-check-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Horizontal oval frame and separate rising check mark. Construction reference: circle-check."""
        self.add_arc('top', (2, 16), (30, 16), radius_x=14, radius_y=12)
        self.add_arc('bottom', (30, 16), (2, 16), radius_x=14, radius_y=12)
        self.add_contour('oval', 'top', 'bottom', closed=True)
        self.add_polyline('check', (10, 16), (14, 20), (21, 12))

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
