"""Independent 32px profile of person-with-center-parted-hair.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '194e0c8a-520e-4ab3-9a3e-2d1ab17a737a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/avatars/woman_194e0c8a-520e-4ab3-9a3e-2d1ab17a737a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('194e0c8a-520e-4ab3-9a3e-2d1ab17a737a', 'pictographic-primitives/avatars/woman_194e0c8a-520e-4ab3-9a3e-2d1ab17a737a.svg'),)
PROFILE_SOURCE_KEYS = ('solo/person-with-center-parted-hair',)
SOLO_SOURCE_ICON_IDS = ('person-with-center-parted-hair',)
REFERENCE_EXPORT_SHA256 = '289e8424138ee365ea9675a60bced483833aa53253ef39ca5fab2d919caa37bc'

class DrawingVariant2(Sub32):
    icon_id = 'person-with-center-parted-hair-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'avatars'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Portrait with a center-parted hair silhouette, circular jaw and open shoulders. Construction reference: human_ref/user.svg: circular jaw and four-unit detached gap."""
        self.add_bezier('hair-l', (9, 9), ((9, 5), (9, 2), (12, 2)))
        self.add_bezier('part-l', (12, 2), ((14, 2), (16, 3), (16, 5)))
        self.add_bezier('part-r', (16, 5), ((16, 3), (18, 2), (20, 2)))
        self.add_bezier('hair-r', (20, 2), ((23, 2), (23, 5), (23, 9)))
        self.add_arc('jaw', (23, 9), (9, 9), radius_x=7)
        self.add_contour('head', 'hair-l', 'part-l', 'part-r', 'hair-r', 'jaw', closed=True)
        self.add_bezier('shoulder-l', (4, 30), ((4, 27), (10, 24), (16, 24)))
        self.add_bezier('shoulder-r', (16, 24), ((22, 24), (28, 27), (28, 30)))
        self.add_contour('body', 'shoulder-l', 'shoulder-r')

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
