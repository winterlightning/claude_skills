"""Independent 32px profile of monitor-with-dollar-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a113d58d-e6b9-465b-a63a-51b045031b0b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/monitor dollar sign_a113d58d-e6b9-465b-a63a-51b045031b0b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a113d58d-e6b9-465b-a63a-51b045031b0b', 'pictographic-primitives/symbol/monitor dollar sign_a113d58d-e6b9-465b-a63a-51b045031b0b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/monitor-with-dollar-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('monitor-with-dollar-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '9ba5df7fdc87988260ad6ce87b3597e491efb20dcfef355330b225846ed0fa97'

class DrawingVariant2(Sub32):
    icon_id = 'monitor-with-dollar-symbol-solo-profile32-v2'
    variant_of = 'monitor-with-dollar-symbol-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/finance'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Financial monitor with stand and shared dollar sign. Construction reference: shared typeface and original frame."""
        box(self, 'screen', 2, 2, 30, 22, 2)
        self.add_line('stand', (16, 22), (16, 30))
        self.relate('connect', 'stand', 'screen')
        self.add_line('foot', (10, 30), (22, 30))
        self.relate('connect', 'foot', 'stand')
        self.add_bezier('char33-p1-r1-1', (20, 11), ((20, 10), (18, 10), (16, 10)))
        self.add_bezier('char33-p1-r1-2', (16, 10), ((14, 10), (12, 11), (12, 13)))
        self.add_bezier('char33-p1-r1-3', (12, 13), ((12, 13), (12, 13), (12, 13)))
        self.add_bezier('char33-p1-r1-4', (12, 13), ((12, 17), (20, 15), (20, 19)))
        self.add_bezier('char33-p1-r1-5', (20, 19), ((20, 19), (20, 19), (20, 19)))
        self.add_bezier('char33-p1-r1-6', (20, 19), ((20, 22), (18, 23), (16, 23)))
        self.add_bezier('char33-p1-r1-7', (16, 23), ((14, 23), (12, 22), (12, 21)))
        self.add_contour('char33-path-1-1', 'char33-p1-r1-1', 'char33-p1-r1-2', 'char33-p1-r1-3', 'char33-p1-r1-4', 'char33-p1-r1-5', 'char33-p1-r1-6', 'char33-p1-r1-7', closed=False)
        self.add_line('char33-p2-r1-1', (16, 8), (16, 24))
        self.add_contour('char33-path-2-1', 'char33-p2-r1-1', closed=False)
        self.relate('connect', 'char33-path-2-1', 'char33-path-1-1')

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
TYPEFACE_GLYPH_IDS = ('symbol-dollar',)
