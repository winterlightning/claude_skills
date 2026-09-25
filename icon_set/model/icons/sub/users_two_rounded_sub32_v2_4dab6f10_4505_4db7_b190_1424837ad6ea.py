"""Independent 32px profile of users-two-rounded.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4dab6f10-4505-4db7-b190-1424837ad6ea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/user group_4dab6f10-4505-4db7-b190-1424837ad6ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4dab6f10-4505-4db7-b190-1424837ad6ea', 'pictographic-primitives/symbol/user group_4dab6f10-4505-4db7-b190-1424837ad6ea.svg'),)
PROFILE_SOURCE_KEYS = ('solo/users-two-rounded',)
SOLO_SOURCE_ICON_IDS = ('users-two-rounded',)
REFERENCE_EXPORT_SHA256 = '36d09edd47734eec69c887cd9b7067181110f04121c8c35795f32a169570808d'

class DrawingVariant2(Sub32):
    icon_id = 'users-two-rounded-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two outlined circular heads above overlapping rounded shoulder busts with a common baseline. Construction reference: human_ref/user.svg."""
        circle(self, 'front-head', 9, 8, 4)
        circle(self, 'back-head', 23, 9, 3)
        self.add_line('front-l', (2, 28), (2, 27))
        self.add_arc('front-shoulders', (2, 27), (16, 27), radius_x=7)
        self.add_line('front-r', (16, 27), (16, 28))
        self.add_line('baseline', (16, 28), (2, 28))
        self.add_contour('front-body', 'front-l', 'front-shoulders', 'front-r', 'baseline', closed=True)
        self.add_arc('back-shoulders', (16, 27), (30, 27), radius_x=7)
        self.add_line('back-r', (30, 27), (30, 28))
        self.add_line('back-base', (30, 28), (16, 28))
        self.add_line('back-l', (16, 28), (16, 27))
        self.add_contour('back-body', 'back-shoulders', 'back-r', 'back-base', 'back-l', closed=True)
        self.relate('connect', 'front-body', 'back-body')

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
