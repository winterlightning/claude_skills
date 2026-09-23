"""Independent 32px profile of shield-3bbd3635.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '3bbd3635-ed19-4db8-953f-adcc7ed97b05'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/protection/shield_3bbd3635-ed19-4db8-953f-adcc7ed97b05.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('3bbd3635-ed19-4db8-953f-adcc7ed97b05', 'pictographic-primitives/protection/shield_3bbd3635-ed19-4db8-953f-adcc7ed97b05.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shield-3bbd3635',)
SOLO_SOURCE_ICON_IDS = ('shield-3bbd3635',)
REFERENCE_EXPORT_SHA256 = '1af47d7d7b1c4ee049f475dfdc90039a4955a204e45826475e5df167bf55fb5a'

class DrawingVariant2(Sub32):
    icon_id = 'shield-3bbd3635-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'protection'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Shield with central crown, two dipped shoulders, curved pointed base and horizontal divider. Construction reference: shield."""
        self.add_line('tip-l', (16, 2), (10, 6))
        self.add_bezier('dip-l', (10, 6), ((8, 7), (6, 6), (4, 5)))
        self.add_line('left', (4, 5), (4, 15))
        self.add_bezier('base-l', (4, 15), ((4, 22), (9, 27), (16, 30)))
        self.add_bezier('base-r', (16, 30), ((23, 27), (28, 22), (28, 15)))
        self.add_line('right', (28, 15), (28, 5))
        self.add_bezier('dip-r', (28, 5), ((26, 6), (24, 7), (22, 6)))
        self.add_line('tip-r', (22, 6), (16, 2))
        self.add_contour('shield', 'tip-l', 'dip-l', 'left', 'base-l', 'base-r', 'right', 'dip-r', 'tip-r', closed=True)
        self.add_line('divider', (4, 14), (28, 14))
        self.relate('connect', 'divider', 'shield')

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
