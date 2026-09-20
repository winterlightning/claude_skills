"""Independent 32px profile of baby-head.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '454b702c-a035-5fa0-a3ec-ac065587fca8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('454b702c-a035-5fa0-a3ec-ac065587fca8', 'pictographic-primitives/babies/baby_454b702c-a035-5fa0-a3ec-ac065587fca8.svg'), ('5393b57b-1ff9-4e16-b855-128e09e91ba7', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/baby face_5393b57b-1ff9-4e16-b855-128e09e91ba7.svg'))
PROFILE_SOURCE_KEYS = ('solo/baby-head',)
SOLO_SOURCE_ICON_IDS = ('baby-head',)
REFERENCE_EXPORT_SHA256 = 'c68e2a7d40d4e7ea30956ae407215e1929527232a33f01a28390ff1f6647ba72'

class DrawingVariant3(Sub32):
    icon_id = 'baby-head-sub32-v3'
    variant_of = 'baby-head-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'babies'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Baby with round head, hair tuft, two ears, shoulders and diagonal swaddle. Construction reference: human_ref/user.svg: round head and exact detached head gap."""
        circle(self, 'head', 16, 8, 4)
        for n, a, b in [('hair', (16, 2), (16, 4)), ('ear-left', (10, 8), (12, 8)), ('ear-right', (20, 8), (22, 8))]:
            self.add_line(n, a, b)
            self.relate('connect', n, 'head')
        self.add_bezier('body-left', (2, 30), ((2, 25), (9, 20), (16, 20)))
        self.add_bezier('body-right-a', (16, 20), ((21, 20), (24, 22), (26, 25)))
        self.add_bezier('body-right-b', (26, 25), ((28, 27), (29, 29), (30, 30)))
        self.add_contour('body', 'body-left', 'body-right-a', 'body-right-b')
        self.add_line('wrap', (10, 30), (26, 25))
        self.relate('connect', 'wrap', 'body')

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
