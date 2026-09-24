"""Independent 32px profile of ring-sight-inner-ticks.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '61a1fffb-c03a-4331-bdb2-c4f0c937d918'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/war/target_61a1fffb-c03a-4331-bdb2-c4f0c937d918.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('61a1fffb-c03a-4331-bdb2-c4f0c937d918', 'pictographic-primitives/war/target_61a1fffb-c03a-4331-bdb2-c4f0c937d918.svg'),)
PROFILE_SOURCE_KEYS = ('solo/ring-sight-inner-ticks',)
SOLO_SOURCE_ICON_IDS = ('ring-sight-inner-ticks',)
REFERENCE_EXPORT_SHA256 = '7ecae7256fe5a5cbd99b00c67677a2b71bd5845fe8f1630835fe10f0ec7a0455'

class DrawingVariant3(Sub32):
    icon_id = 'ring-sight-inner-ticks-sub32-v3'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/war'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Outer circular sight, inner circular ring and four short attached cardinal ticks. Construction reference: crosshair."""
        circle(self, 'frame', 16, 16, 14)
        circle(self, 'inner', 16, 16, 5)
        for n, a, b in [('left', (11, 16), (9, 16)), ('right', (21, 16), (23, 16)), ('top', (16, 11), (16, 9)), ('base', (16, 21), (16, 23))]:
            self.add_line(n, a, b)
            self.relate('connect', n, 'inner')

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
