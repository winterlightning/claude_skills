"""Independent 32px profile of minimalist-pig-face-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '2878cc5b-7eb0-476d-b3f7-1ad79cba16a4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/pig_2878cc5b-7eb0-476d-b3f7-1ad79cba16a4.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('2878cc5b-7eb0-476d-b3f7-1ad79cba16a4', 'pictographic-primitives/state/pig_2878cc5b-7eb0-476d-b3f7-1ad79cba16a4.svg'),)
PROFILE_SOURCE_KEYS = ('solo/minimalist-pig-face-solo',)
SOLO_SOURCE_ICON_IDS = ('minimalist-pig-face-solo',)
REFERENCE_EXPORT_SHA256 = 'beeafe89b51ab7fabf5e06d610366fe3135b83c447034f4159cab89317bee5b2'

class DrawingVariant2(Sub32):
    icon_id = 'minimalist-pig-face-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    categories = ('primitives-generate', 'state')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Pig face with two rounded ears, broad curved cheeks, two short eyes and open oval snout. Construction reference: none."""
        self.add_bezier('ear-l-top', (9, 5), ((7, 2), (3, 2), (2, 2)))
        self.add_bezier('ear-l-side', (2, 2), ((2, 9), (3, 10), (4, 11)))
        self.add_bezier('cheek-l', (4, 11), ((1, 23), (5, 30), (16, 30)))
        self.add_bezier('cheek-r', (16, 30), ((27, 30), (31, 23), (28, 11)))
        self.add_bezier('ear-r-side', (28, 11), ((29, 10), (30, 9), (30, 2)))
        self.add_bezier('ear-r-top', (30, 2), ((29, 2), (25, 2), (23, 5)))
        self.add_bezier('forehead', (23, 5), ((19, 4), (13, 4), (9, 5)))
        self.add_contour('face', 'ear-l-top', 'ear-l-side', 'cheek-l', 'cheek-r', 'ear-r-side', 'ear-r-top', 'forehead', closed=True)
        self.add_arc('snout-top', (11, 20), (21, 20), radius_x=5, radius_y=3)
        self.add_arc('snout-bottom', (21, 20), (11, 20), radius_x=5, radius_y=3)
        self.add_contour('snout', 'snout-top', 'snout-bottom', closed=True)
        self.add_dot('eye-l', (11, 11))
        self.add_dot('eye-r', (21, 11))

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
