# Independent repair; parent preserved.
"""Independent 32px profile of balaclava-mask-batch-025-12.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '484cb3fb-0065-4ca7-ac5f-156d807d114c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('484cb3fb-0065-4ca7-ac5f-156d807d114c', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/criminal_484cb3fb-0065-4ca7-ac5f-156d807d114c.svg'),)
PROFILE_SOURCE_KEYS = ('solo/balaclava-mask-batch-025-12',)
SOLO_SOURCE_ICON_IDS = ('balaclava-mask-batch-025-12',)
REFERENCE_EXPORT_SHA256 = 'c4e86c80d7111839b06cbdba703750f8525d496d58afabdac997f2e29302f882'

class DrawingVariant2(Sub32):
    icon_id = 'balaclava-mask-batch-025-12-sub32-v2'
    variant_of = 'balaclava-mask-batch-025-12-sub32'
    variant_label = 'Centerline and source fidelity repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_bezier('top-left', (2, 17), ((2, 8), (7, 2), (16, 2)))
        self.add_bezier('top-right', (16, 2), ((25, 2), (30, 8), (30, 17)))
        self.add_bezier('right', (30, 17), ((30, 23), (27, 25), (26, 26)))
        self.add_polyline('hem-right', (26, 26), (28, 30), (4, 30), (6, 26))
        self.add_bezier('left', (6, 26), ((5, 25), (2, 23), (2, 17)))
        self.add_contour('top', 'top-left', 'top-right', 'right')
        self.relate('connect', 'top', 'hem-right')
        self.relate('connect', 'left', 'hem-right')
        self.relate('connect', 'left', 'top')
        self.add_bezier('eye-a', (16, 16), ((10, 7), (6, 11), (8, 17)))
        self.add_bezier('eye-b', (8, 17), ((10, 22), (13, 19), (16, 16)))
        self.add_bezier('eye-c', (16, 16), ((22, 7), (26, 11), (24, 17)))
        self.add_bezier('eye-d', (24, 17), ((22, 22), (19, 19), (16, 16)))
        self.add_contour('eyes', 'eye-a', 'eye-b', 'eye-c', 'eye-d', closed=True)

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
REPAIR_PLAN = 'Balaclava outline and two crossing loop eye opening; all source parts retained.'
CONSTRUCTION_REFERENCE = 'none'
