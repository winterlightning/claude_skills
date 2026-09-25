"""Independent 32px profile of users-two-overlap.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/two persons_45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7', 'pictographic-primitives/symbol/two persons_45a7c221-ee5e-4f5f-9d50-3b2bfc2ef6e7.svg'),)
PROFILE_SOURCE_KEYS = ('solo/users-two-overlap',)
SOLO_SOURCE_ICON_IDS = ('users-two-overlap',)
REFERENCE_EXPORT_SHA256 = '6cb9bfc0e94a523cb8e8699ac8ae9c422a582350f343bb074f9cda8dba52c6a4'

class DrawingVariant2(Sub32):
    icon_id = 'users-two-overlap-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    categories = ('symbol', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Overlapping two-person bust: smaller left head and shoulders behind larger right person. Construction reference: human_ref/user.svg."""
        circle(self, 'back-head', 7, 10, 3)
        circle(self, 'front-head', 22, 7, 5)
        self.add_arc('front-l', (12, 30), (22, 20), radius_x=10)
        self.add_bezier('front-r', (22, 20), ((27, 20), (30, 24), (30, 30)))
        self.add_contour('front', 'front-l', 'front-r')
        self.add_bezier('back-l', (2, 30), ((2, 24), (3, 21), (7, 21)))
        self.add_bezier('back-r', (7, 21), ((10, 21), (12, 23), (14, 24)))
        self.add_contour('back', 'back-l', 'back-r')
        self.relate('connect', 'back', 'front')

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
