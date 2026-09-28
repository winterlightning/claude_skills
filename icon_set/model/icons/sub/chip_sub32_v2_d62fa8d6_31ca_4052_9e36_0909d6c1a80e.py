"""Independent 32px profile of chip.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'd62fa8d6-31ca-4052-9e36-0909d6c1a80e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/chip_d62fa8d6-31ca-4052-9e36-0909d6c1a80e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d62fa8d6-31ca-4052-9e36-0909d6c1a80e', 'pictographic-primitives/state/chip_d62fa8d6-31ca-4052-9e36-0909d6c1a80e.svg'), ('d0dd0f52-f552-4b31-8bb1-bed37c84eff0', 'pictographic-primitives/symbol/chip_d0dd0f52-f552-4b31-8bb1-bed37c84eff0.svg'))
PROFILE_SOURCE_KEYS = ('solo/chip', 'solo/chip-symbol')
SOLO_SOURCE_ICON_IDS = ('chip', 'chip-symbol')
REFERENCE_EXPORT_SHA256 = '412d4aec8a5078c4a220a81f21eed8d171a85595b8e3b17f79e9bc208e9488a9'

class DrawingVariant2(Sub32):
    icon_id = 'chip-sub32-v2'
    variant_of = 'chip-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded microchip body with exactly two straight pins on each of its four sides. Construction reference: cpu."""
        box(self, 'body', 6, 6, 26, 26, 3)
        for i, v in enumerate((11, 21)):
            for side, a, b in [('top', (v, 2), (v, 6)), ('bottom', (v, 26), (v, 30)), ('left', (2, v), (6, v)), ('right', (26, v), (30, v))]:
                name = f'{side}-{i}'
                self.add_line(name, a, b)
                self.relate('connect', name, 'body')

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
