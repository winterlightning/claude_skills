"""Independent 32px profile of man-head-shoulders-outline.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'fabe2871-28e2-4de0-93c6-579984309329'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/photography/man_fabe2871-28e2-4de0-93c6-579984309329.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('fabe2871-28e2-4de0-93c6-579984309329', 'pictographic-primitives/photography/man_fabe2871-28e2-4de0-93c6-579984309329.svg'),)
PROFILE_SOURCE_KEYS = ('solo/man-head-shoulders-outline',)
SOLO_SOURCE_ICON_IDS = ('man-head-shoulders-outline',)
REFERENCE_EXPORT_SHA256 = '49be0ec3d8f72c2837c6bd1eb5b01cf0c292408a493deb9f7778281fed18efe0'

class DrawingVariant2(Sub32):
    icon_id = 'man-head-shoulders-outline-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'photography'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Continuous man bust outline with rounded crown, two ears, circular jaw arcs, neck and shoulders. Construction reference: user."""
        self.add_bezier('shoulder-l', (2, 30), ((2, 25), (8, 24), (12, 22)))
        self.add_line('neck-l', (12, 22), (12, 18))
        self.add_arc('jaw-l', (12, 18), (9, 14), radius_x=7)
        self.add_arc('ear-l', (9, 14), (9, 10), radius_x=2)
        self.add_line('temple-l', (9, 10), (9, 9))
        self.add_arc('crown', (9, 9), (23, 9), radius_x=7)
        self.add_line('temple-r', (23, 9), (23, 10))
        self.add_arc('ear-r', (23, 10), (23, 14), radius_x=2)
        self.add_arc('jaw-r', (23, 14), (20, 18), radius_x=7)
        self.add_line('neck-r', (20, 18), (20, 22))
        self.add_bezier('shoulder-r', (20, 22), ((24, 24), (30, 25), (30, 30)))
        self.add_contour('bust', 'shoulder-l', 'neck-l', 'jaw-l', 'ear-l', 'temple-l', 'crown', 'temple-r', 'ear-r', 'jaw-r', 'neck-r', 'shoulder-r')

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
