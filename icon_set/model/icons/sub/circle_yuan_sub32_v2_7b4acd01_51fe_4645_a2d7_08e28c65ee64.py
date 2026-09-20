"""Independent 32px profile of circle-yuan.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '7b4acd01-51fe-4645-a2d7-08e28c65ee64'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/circle yuan_7b4acd01-51fe-4645-a2d7-08e28c65ee64.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('7b4acd01-51fe-4645-a2d7-08e28c65ee64', 'pictographic-primitives/state/circle yuan_7b4acd01-51fe-4645-a2d7-08e28c65ee64.svg'),)
PROFILE_SOURCE_KEYS = ('solo/circle-yuan',)
SOLO_SOURCE_ICON_IDS = ('circle-yuan',)
REFERENCE_EXPORT_SHA256 = '6f730681cf4a400fb4e2cfe7243963dc2f6918907414e6e77477dacef8dd11b6'

class DrawingVariant2(Sub32):
    icon_id = 'circle-yuan-sub32-v2'
    variant_of = 'circle-yuan-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Circular yuan badge with the shared one-bar yuan. Construction reference: shared typeface."""
        circle(self, 'frame', 16, 16, 14)
        self.add_line('char9-p1-r1-1', (11, 10), (16, 16))
        self.add_line('char9-p1-r1-2', (16, 16), (21, 10))
        self.add_contour('char9-path-1-1', 'char9-p1-r1-1', 'char9-p1-r1-2', closed=False)
        self.add_line('char9-p2-r1-1', (16, 16), (16, 22))
        self.add_contour('char9-path-2-1', 'char9-p2-r1-1', closed=False)
        self.add_line('char9-p3-r1-1', (12, 19), (20, 19))
        self.add_contour('char9-path-3-1', 'char9-p3-r1-1', closed=False)
        self.relate('connect', 'char9-p1-r1-1', 'char9-p2-r1-1')
        self.relate('connect', 'char9-p1-r1-2', 'char9-p2-r1-1')
        self.relate('connect', 'char9-path-2-1', 'char9-path-1-1')
        self.relate('connect', 'char9-path-3-1', 'char9-path-2-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-yuan-one-bar',)
