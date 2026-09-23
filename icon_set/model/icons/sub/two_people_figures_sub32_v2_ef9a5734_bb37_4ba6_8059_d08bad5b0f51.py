"""Independent 32px profile of two-people-figures.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ef9a5734-bb37-4ba6-8059-d08bad5b0f51'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/couple_ef9a5734-bb37-4ba6-8059-d08bad5b0f51.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ef9a5734-bb37-4ba6-8059-d08bad5b0f51', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/couple_ef9a5734-bb37-4ba6-8059-d08bad5b0f51.svg'), ('bacf1dca-6143-4371-a879-10b3112e2203', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/two persons_bacf1dca-6143-4371-a879-10b3112e2203.svg'))
PROFILE_SOURCE_KEYS = ('solo/two-people-figures', 'solo/two-person-user-group')
SOLO_SOURCE_ICON_IDS = ('two-people-figures', 'two-person-user-group')
REFERENCE_EXPORT_SHA256 = '920bc3d7d7d9c7f6d2eb3d4c71201a2257f490ab8dc99438fdd9063da4d4c306'

class DrawingVariant2(Sub32):
    icon_id = 'two-people-figures-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/container-components'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two staggered circular heads above separate open shoulder curves, left figure higher. Construction reference: human_ref/user.svg."""
        circle(self, 'head-l', 9, 6, 4)
        circle(self, 'head-r', 23, 10, 4)
        self.add_line('side-l', (2, 30), (2, 25))
        self.add_arc('shoulder-l', (2, 25), (9, 18), radius_x=7)
        self.add_bezier('back-tip', (9, 18), ((11, 18), (12, 18), (13, 19)))
        self.add_contour('back', 'side-l', 'shoulder-l', 'back-tip')
        self.add_line('front-l', (16, 30), (16, 29))
        self.add_arc('front-top', (16, 29), (30, 29), radius_x=7)
        self.add_line('front-r', (30, 29), (30, 30))
        self.add_contour('front', 'front-l', 'front-top', 'front-r')

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
