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

class DrawingVariant4(Sub32):
    icon_id = 'baby-head-sub32-v4'
    variant_of = 'baby-head-sub32-v3'
    variant_label = 'User review correction; preserve earlier variants'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'babies'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('head-right', (28, 8), ((29, 10), (30, 13), (30, 16)))
        self.add_arc('head-br', (30, 16), (16, 30), radius_x=14)
        self.add_arc('head-bl', (16, 30), (2, 16), radius_x=14)
        self.add_arc('head-tl', (2, 16), (16, 2), radius_x=14)
        self.add_bezier('curl', (16, 2), ((22, 2), (24, 8), (18, 8)))
        self.add_contour('head', 'head-right', 'head-br', 'head-bl', 'head-tl', 'curl')
        self.add_line('eye-left', (10, 16), (10, 16))
        self.add_line('eye-right', (22, 16), (22, 16))
        self.add_bezier('smile', (12, 22), ((14, 24), (18, 24), (20, 22)))

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
