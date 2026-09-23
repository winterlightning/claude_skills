"""Independent 32px profile of synchronize-refresh-arrow-a0553293.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a0553293-203d-4c9b-9583-f6ead215b9d7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/interface-essential/synchronize refresh arrow_a0553293-203d-4c9b-9583-f6ead215b9d7.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a0553293-203d-4c9b-9583-f6ead215b9d7', 'pictographic-primitives/interface-essential/synchronize refresh arrow_a0553293-203d-4c9b-9583-f6ead215b9d7.svg'), ('4d77908b-9f0a-416f-bab9-3143aecf95b6', 'pictographic-primitives/interface-essential/synchronize refresh arrow_4d77908b-9f0a-416f-bab9-3143aecf95b6.svg'))
PROFILE_SOURCE_KEYS = ('solo/synchronize-refresh-arrow-a0553293', 'solo/synchronize-refresh-arrow-interface-essential')
SOLO_SOURCE_ICON_IDS = ('synchronize-refresh-arrow-a0553293', 'synchronize-refresh-arrow-interface-essential')
REFERENCE_EXPORT_SHA256 = '9677eec079b466cfacf500d6b45a19cbff276d484544d1af04b88058fb82fcf6'

class DrawingVariant2(Sub32):
    icon_id = 'synchronize-refresh-arrow-a0553293-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Clockwise three-quarter return arc and downward arrowhead. Construction reference: rotate-cw."""
        self.add_arc('bottom-left', (14, 28), (2, 16), radius_x=12)
        self.add_arc('top', (2, 16), (26, 16), radius_x=12)
        self.add_contour('return', 'bottom-left', 'top')
        self.add_polyline('arrow', (21, 13), (26, 16), (30, 10))
        self.relate('connect', 'return', 'arrow')

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
