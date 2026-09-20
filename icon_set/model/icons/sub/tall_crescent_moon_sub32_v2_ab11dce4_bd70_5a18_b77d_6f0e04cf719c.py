"""Independent 32px profile of tall-crescent-moon.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ab11dce4-bd70-5a18-b77d-6f0e04cf719c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/weather/night moon gibbous_ab11dce4-bd70-5a18-b77d-6f0e04cf719c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ab11dce4-bd70-5a18-b77d-6f0e04cf719c', 'pictographic-primitives/weather/night moon gibbous_ab11dce4-bd70-5a18-b77d-6f0e04cf719c.svg'), ('65e05ed7-b793-4969-b4cd-b8618a5b69d3', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/night_65e05ed7-b793-4969-b4cd-b8618a5b69d3.svg'))
PROFILE_SOURCE_KEYS = ('solo/tall-crescent-moon',)
SOLO_SOURCE_ICON_IDS = ('tall-crescent-moon',)
REFERENCE_EXPORT_SHA256 = 'd4bdd3bcaea9bac5ad527af69259d952a5d74b50ce11f4c85d865d3168e9ce51'

class DrawingVariant2(Sub32):
    icon_id = 'tall-crescent-moon-sub32-v2'
    variant_of = 'tall-crescent-moon-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/weather'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Tall crescent, smooth convex outer edge and concave inner edge meeting at both tips. Construction reference: moon."""
        self.add_bezier('outer-top', (28, 2), ((14, 2), (4, 8), (4, 16)))
        self.add_bezier('outer-bottom', (4, 16), ((4, 24), (14, 30), (28, 30)))
        self.add_bezier('inner-bottom', (28, 30), ((23, 26), (21, 21), (21, 16)))
        self.add_bezier('inner-top', (21, 16), ((21, 11), (23, 6), (28, 2)))
        self.add_contour('crescent', 'outer-top', 'outer-bottom', 'inner-bottom', 'inner-top', closed=True)

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
