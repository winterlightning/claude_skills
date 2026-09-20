"""Independent 32px profile of minus-bold.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'a6b4ed56-3a81-4fe8-ab46-c2e8af425eff'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/minus bold_a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a6b4ed56-3a81-4fe8-ab46-c2e8af425eff', 'pictographic-primitives/state/minus bold_a6b4ed56-3a81-4fe8-ab46-c2e8af425eff.svg'),)
PROFILE_SOURCE_KEYS = ('solo/minus-bold',)
SOLO_SOURCE_ICON_IDS = ('minus-bold',)
REFERENCE_EXPORT_SHA256 = '7b8f3082619ce5237a6e1d44ab69665d9a1569915821bd0df89c59cd4e651d44'

class DrawingVariant2(Sub32):
    icon_id = 'minus-bold-sub32-v2'
    variant_of = 'minus-bold-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_S
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Wide closed rounded rectangular minus outline. Construction reference: minus."""
        box(self, 'minus', 2, 10, 30, 22, 3)

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
