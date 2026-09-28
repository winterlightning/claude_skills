"""Independent 32px profile of open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '14e0f209-1f73-4be1-9637-df2de37b666b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/holidays/hand_14e0f209-1f73-4be1-9637-df2de37b666b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('14e0f209-1f73-4be1-9637-df2de37b666b', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_14e0f209-1f73-4be1-9637-df2de37b666b.svg'), ('bc1a4fc0-cd35-423d-909c-bad3ddffd5c9', '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_bc1a4fc0-cd35-423d-909c-bad3ddffd5c9.svg'))
PROFILE_SOURCE_KEYS = ('solo/open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b', 'solo/open-palm-hand-bc1a4fc0-cd35-423d-909c-bad3ddffd5c9')
SOLO_SOURCE_ICON_IDS = ('open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b', 'open-palm-hand-bc1a4fc0-cd35-423d-909c-bad3ddffd5c9')
REFERENCE_EXPORT_SHA256 = '5d94efe90b12f2752213ae028698de92ef1533350fab01ddd1a3106fde411d38'

class DrawingVariant2(Sub32):
    icon_id = 'open-palm-hand-14e0f209-1f73-4be1-9637-df2de37b666b-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'holidays'
    categories = ('primitives', 'holidays')
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Open-palm hand gesture with four raised finger strokes and a separate thumb branch. Construction reference: human_ref/full_body_ref.png: simplified human gesture strokes."""
        self.add_line('outer-left', (6, 8), (6, 22))
        self.add_bezier('palm-left', (6, 22), ((6, 28), (12, 30), (18, 30)))
        self.add_bezier('palm-right', (18, 30), ((26, 30), (30, 26), (30, 22)))
        self.add_line('outer-right', (30, 22), (30, 10))
        self.add_contour('palm', 'outer-left', 'palm-left', 'palm-right', 'outer-right')
        self.add_line('finger-middle', (14, 2), (14, 18))
        self.add_line('finger-ring', (22, 4), (22, 18))
        self.add_line('thumb', (2, 20), (6, 22))
        self.relate('connect', 'thumb', 'palm')

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
