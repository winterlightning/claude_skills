"""Independent 32px profile of financial-dollar-sign-document-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '35820950-4e21-49b7-a67d-b15356efda77'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/dollar bill_35820950-4e21-49b7-a67d-b15356efda77.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('35820950-4e21-49b7-a67d-b15356efda77', 'pictographic-primitives/other/dollar bill_35820950-4e21-49b7-a67d-b15356efda77.svg'),)
PROFILE_SOURCE_KEYS = ('solo/financial-dollar-sign-document-solo',)
SOLO_SOURCE_ICON_IDS = ('financial-dollar-sign-document-solo',)
REFERENCE_EXPORT_SHA256 = '6d5b6d721f6bdede00fd4d9d02872bc8992658ea250d9fe293a9c8809019ba41'

class DrawingVariant3(Sub32):
    icon_id = 'financial-dollar-sign-document-solo-profile32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('state', 'other', 'primitives-generate')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Clipped-corner dollar document retaining the earlier light-dollar appearance. Construction reference: source composition; shared small-size character construction."""
        self.add_polyline('page', (2, 2), (20, 2), (30, 12), (30, 30), (2, 30), (2, 2))
        from icon_set.typeface.sub32 import draw_dollar
        draw_dollar(self, 14, 2)

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
TYPEFACE_GLYPH_IDS = ('symbol-dollar',)

TYPEFACE_PROFILE_VARIANTS = ('symbol-dollar-compact32',)
