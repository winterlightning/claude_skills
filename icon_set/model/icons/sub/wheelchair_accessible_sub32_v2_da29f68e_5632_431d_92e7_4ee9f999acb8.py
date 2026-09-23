"""Independent 32px profile of wheelchair-accessible.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'da29f68e-5632-431d-92e7-4ee9f999acb8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/wheelchair_da29f68e-5632-431d-92e7-4ee9f999acb8.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('da29f68e-5632-431d-92e7-4ee9f999acb8', 'pictographic-primitives/symbol/wheelchair_da29f68e-5632-431d-92e7-4ee9f999acb8.svg'),)
PROFILE_SOURCE_KEYS = ('solo/wheelchair-accessible',)
SOLO_SOURCE_ICON_IDS = ('wheelchair-accessible',)
REFERENCE_EXPORT_SHA256 = '628c4b176c82ac2974b34469f9b2489870b6ccc915ab01b84fda940c9fb63018'

class DrawingVariant2(Sub32):
    icon_id = 'wheelchair-accessible-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/symbols'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Wheelchair user with round attached head, upright torso, armrest, bent leg and foot beside an open curved wheel. Construction reference: human_ref/full_body_ref.png."""
        circle(self, 'head', 12, 5, 3)
        self.add_polyline('body', (12, 8), (12, 22), (22, 22), (28, 28), (30, 28))
        self.relate('connect', 'body', 'head')
        self.add_line('arm', (12, 14), (20, 14))
        self.relate('connect', 'arm', 'body')
        self.add_bezier('wheel-top', (5, 17), ((3, 19), (2, 20), (2, 23)))
        self.add_bezier('wheel-base', (2, 23), ((2, 27), (5, 30), (10, 30)))
        self.add_bezier('wheel-end', (10, 30), ((13, 30), (16, 30), (18, 29)))
        self.add_contour('wheel', 'wheel-top', 'wheel-base', 'wheel-end')

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
