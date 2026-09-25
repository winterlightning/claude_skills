"""Independent 32px profile of charging-battery-104-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f8b6ea0a-273a-4932-a93b-52454f7fd328'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/dist/gallery/combination-originals/f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f8b6ea0a-273a-4932-a93b-52454f7fd328', 'icon_set/dist/gallery/combination-originals/f8b6ea0a-273a-4932-a93b-52454f7fd328.svg'),)
PROFILE_SOURCE_KEYS = ('solo/charging-battery-104-solo',)
SOLO_SOURCE_ICON_IDS = ('charging-battery-104-solo',)
REFERENCE_EXPORT_SHA256 = 'bce7e3dc67e2bbf7ede8ce6ed99985ce7ae0e0bf332ad8f331136f953845b2fe'

class DrawingVariant2(Sub32):
    icon_id = 'charging-battery-104-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Side-terminal battery with a clear lightning mark. Construction reference: battery-charging: open modifier clearance."""

        class Rotated:

            def add_line(_, n, a, b):
                return self.add_line(n, (32 - a[1], a[0]), (32 - b[1], b[0]))

            def add_arc(_, n, a, b, **kw):
                rx = kw.pop('radius_x')
                ry = kw.pop('radius_y', rx)
                return self.add_arc(n, (32 - a[1], a[0]), (32 - b[1], b[0]), radius_x=ry, radius_y=rx, **kw)

            def add_polyline(_, n, *pts):
                return self.add_polyline(n, *[(32 - y, x) for x, y in pts])

            def __getattr__(_, n):
                return getattr(self, n)
        r = Rotated()
        r.add_line('left-bottom', (8, 30), (6, 30))
        r.add_arc('bl', (6, 30), (2, 26), radius_x=4)
        r.add_line('left', (2, 26), (2, 14))
        r.add_arc('tl', (2, 14), (6, 10), radius_x=4)
        r.add_polyline('terminal', (6, 10), (10, 10), (10, 2), (22, 2), (22, 10), (26, 10))
        r.add_arc('tr', (26, 10), (30, 14), radius_x=4)
        r.add_line('right', (30, 14), (30, 24))
        r.add_arc('br', (30, 24), (28, 26), radius_x=2)
        r.add_line('right-bottom', (28, 26), (28, 26))
        r.add_contour('left-frame', 'left-bottom', 'bl', 'left', 'tl')
        r.relate('connect', 'left-frame', 'terminal')
        r.add_contour('right-frame', 'tr', 'right', 'br', 'right-bottom')
        r.relate('connect', 'right-frame', 'terminal')
        r.add_polyline('bolt', (18, 16), (10, 24), (22, 24), (16, 30))

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
