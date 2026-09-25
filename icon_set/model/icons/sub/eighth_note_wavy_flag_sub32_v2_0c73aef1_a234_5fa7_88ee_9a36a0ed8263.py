"""Independent 32px profile of eighth-note-wavy-flag.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '0c73aef1-a234-5fa7-88ee-9a36a0ed8263'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/music/music note_0c73aef1-a234-5fa7-88ee-9a36a0ed8263.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('0c73aef1-a234-5fa7-88ee-9a36a0ed8263', 'pictographic-primitives/music/music note_0c73aef1-a234-5fa7-88ee-9a36a0ed8263.svg'),)
PROFILE_SOURCE_KEYS = ('solo/eighth-note-wavy-flag',)
SOLO_SOURCE_ICON_IDS = ('eighth-note-wavy-flag',)
REFERENCE_EXPORT_SHA256 = 'f72f78d8bcbe0c60b91ef44863877b687f05c79fbd301134ecc2e2268aa2f113'

class DrawingVariant2(Sub32):
    icon_id = 'eighth-note-wavy-flag-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'music'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Eighth note with tilted oval head, straight stem and flowing single flag. Construction reference: music-2."""
        self.add_bezier('head-tl', (4, 25), ((4, 22), (8, 20), (11, 20)))
        self.add_bezier('head-tr', (11, 20), ((14, 20), (16, 21), (16, 24)))
        self.add_bezier('head-br', (16, 24), ((16, 27), (12, 30), (9, 30)))
        self.add_bezier('head-bl', (9, 30), ((6, 30), (4, 28), (4, 25)))
        self.add_contour('head', 'head-tl', 'head-tr', 'head-br', 'head-bl', closed=True)
        self.add_line('stem', (16, 24), (16, 2))
        self.relate('connect', 'stem', 'head')
        self.add_bezier('flag-top', (16, 2), ((18, 7), (28, 8), (28, 12)))
        self.add_bezier('flag-tip', (28, 12), ((28, 15), (25, 17), (25, 19)))
        self.add_contour('flag', 'flag-top', 'flag-tip')
        self.relate('connect', 'flag', 'stem')

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
