"""Independent 32px profile of two-standing-people.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'da65a8df-c40a-4960-bff3-74262390682c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/users/multiple man_da65a8df-c40a-4960-bff3-74262390682c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('da65a8df-c40a-4960-bff3-74262390682c', 'pictographic-primitives/users/multiple man_da65a8df-c40a-4960-bff3-74262390682c.svg'), ('5e8b621f-4f10-4323-943d-1337196c6e73', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_5e8b621f-4f10-4323-943d-1337196c6e73.svg'))
PROFILE_SOURCE_KEYS = ('solo/two-standing-people',)
SOLO_SOURCE_ICON_IDS = ('two-standing-people',)
REFERENCE_EXPORT_SHA256 = 'cbfb479fbf96c0aac0266d16da300e7cd0c1ee99857f525854f0148da8cbde69'

class DrawingVariant3(Sub32):
    icon_id = 'two-standing-people-sub32-v3'
    variant_of = 'two-standing-people-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'people/groups'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two matching standing figures with circular heads, rounded shoulders and inset lower torsos. Construction reference: human_ref/full_body_ref.png."""
        for name, cx in [('left', 7), ('right', 25)]:
            circle(self, name + '-head', cx, 6, 4)
            self.add_arc(name + '-shoulders', (cx - 5, 22), (cx + 5, 22), radius_x=5, radius_y=4)
            points = ((cx + 5, 22), (cx + 5, 24), (cx + 4, 24), (cx + 4, 30), (cx - 4, 30), (cx - 4, 24), (cx - 5, 24), (cx - 5, 22))
            for i, (a, b) in enumerate(zip(points, points[1:])):
                self.add_line(name + f'-edge-{i}', a, b)
            self.add_contour(name + '-body', name + '-shoulders', *[name + f'-edge-{i}' for i in range(7)], closed=True)

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
