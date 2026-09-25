"""Independent 32px profile of state32-229ee448-4dc8-470b-ac1f-fbbfcd586284.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '229ee448-4dc8-470b-ac1f-fbbfcd586284'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/needles two_229ee448-4dc8-470b-ac1f-fbbfcd586284.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('229ee448-4dc8-470b-ac1f-fbbfcd586284', 'pictographic-primitives/state/needles two_229ee448-4dc8-470b-ac1f-fbbfcd586284.svg'),)
PROFILE_SOURCE_KEYS = ('solo/needles-two',)
SOLO_SOURCE_ICON_IDS = ('needles-two',)
REFERENCE_EXPORT_SHA256 = 'd7e736475021d90c7a08f4300c715f916cdc99d07032fb12ba47cfae866ab62c'

class DrawingVariant2(Sub32):
    icon_id = 'state32-229ee448-4dc8-470b-ac1f-fbbfcd586284-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Two round-ended circuit terminals: upper diagonal lead and lower horizontal lead. Construction reference: none."""
        circle(self, 'upper-node', 14, 8, 4)
        circle(self, 'lower-node', 26, 24, 4)
        self.add_line('upper-wire', (2, 18), (11, 11))
        self.relate('connect', 'upper-wire', 'upper-node')
        self.add_line('lower-wire', (2, 24), (22, 24))
        self.relate('connect', 'lower-wire', 'lower-node')

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
