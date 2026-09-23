"""Independent 32px profile of lgbt-heart.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '144220e1-741d-429f-9845-957359566973'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/lgbt heart_144220e1-741d-429f-9845-957359566973.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('144220e1-741d-429f-9845-957359566973', 'pictographic-primitives/symbol/lgbt heart_144220e1-741d-429f-9845-957359566973.svg'),)
PROFILE_SOURCE_KEYS = ('solo/lgbt-heart',)
SOLO_SOURCE_ICON_IDS = ('lgbt-heart',)
REFERENCE_EXPORT_SHA256 = '50f73b05417bfaade2793749f2bdeaf7563bfe4318472bff8f357c2e8c957fb8'

class DrawingVariant2(Sub32):
    icon_id = 'lgbt-heart-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Heart outline with two horizontal stripe divisions. Construction reference: none."""
        self.add_arc('lobe-l', (2, 7), (16, 7), radius_x=7, radius_y=5)
        self.add_arc('lobe-r', (16, 7), (30, 7), radius_x=7, radius_y=5)
        self.add_bezier('side-r', (30, 7), ((30, 16), (24, 24), (16, 30)))
        self.add_bezier('side-l', (16, 30), ((8, 24), (2, 16), (2, 7)))
        self.add_contour('heart', 'lobe-l', 'lobe-r', 'side-r', 'side-l', closed=True)
        self.add_line('stripe-1', (5, 15), (27, 15))
        self.add_line('stripe-2', (10, 23), (22, 23))
        self.relate('connect', 'stripe-1', 'heart')
        self.relate('connect', 'stripe-2', 'heart')

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
