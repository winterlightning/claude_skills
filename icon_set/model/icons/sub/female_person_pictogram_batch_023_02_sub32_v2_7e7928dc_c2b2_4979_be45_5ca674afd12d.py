"""Independent 32px profile of female-person-pictogram-batch-023-02.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7e7928dc-c2b2-4979-be45-5ca674afd12d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7e7928dc-c2b2-4979-be45-5ca674afd12d', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/full body women_7e7928dc-c2b2-4979-be45-5ca674afd12d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/female-person-pictogram-batch-023-02',)
SOLO_SOURCE_ICON_IDS = ('female-person-pictogram-batch-023-02',)
REFERENCE_EXPORT_SHA256 = '0cb5eafdb20fa971dfcf916cd41d1d1dc4fe8b02ff8bb49de5d0d802608a02f6'

class DrawingVariant2(Sub32):
    icon_id = 'female-person-pictogram-batch-023-02-sub32-v2'
    variant_of = 'female-person-pictogram-batch-023-02-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular detached head above rounded shoulders, flared dress and inset lower body. Construction reference: human_ref/full_body_ref.png."""
        circle(self, 'head', 16, 6, 4)
        self.add_line('shoulder-top', (12, 18), (20, 18))
        self.add_bezier('shoulder-right', (20, 18), ((23, 18), (23, 20), (24, 22)))
        points = ((24, 22), (28, 26), (21, 26), (20, 30), (12, 30), (11, 26), (4, 26), (8, 22))
        for i, (a, b) in enumerate(zip(points, points[1:])):
            self.add_line(f'dress-{i}', a, b)
        self.add_bezier('shoulder-left', (8, 22), ((9, 20), (9, 18), (12, 18)))
        self.add_contour('body', 'shoulder-top', 'shoulder-right', *[f'dress-{i}' for i in range(7)], 'shoulder-left', closed=True)

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
