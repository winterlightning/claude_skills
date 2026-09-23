"""Independent 32px profile of fork-and-knife.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'b66fd641-5f5f-41b7-acfe-644485d3c82d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('b66fd641-5f5f-41b7-acfe-644485d3c82d', 'pictographic-primitives/symbol/fork and knife_b66fd641-5f5f-41b7-acfe-644485d3c82d.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fork-and-knife',)
SOLO_SOURCE_ICON_IDS = ('fork-and-knife',)
REFERENCE_EXPORT_SHA256 = '0e3c5c399b5f2ffcfea4b2559f8efaddc39b23d60f0d07af3ea3404d9a17f070'

class DrawingVariant2(Sub32):
    icon_id = 'fork-and-knife-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Fork with two clear tines beside a closed curved knife blade. Construction reference: utensils: broad bowl and open blade counter."""
        self.add_line('fork-left', (2, 2), (2, 14))
        self.add_arc('fork-bowl', (2, 14), (10, 14), radius_x=4, sweep=False)
        self.add_line('fork-right', (10, 14), (10, 2))
        self.add_contour('fork', 'fork-left', 'fork-bowl', 'fork-right')
        self.add_line('fork-stem', (6, 18), (6, 30))
        self.relate('connect', 'fork-stem', 'fork')
        self.add_line('knife-stem', (22, 2), (22, 30))
        self.add_bezier('knife-curve', (22, 2), ((30, 4), (30, 10), (30, 20)))
        self.add_line('knife-base', (30, 20), (22, 20))
        self.add_contour('blade', 'knife-curve', 'knife-base')
        self.relate('connect', 'blade', 'knife-stem')

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
