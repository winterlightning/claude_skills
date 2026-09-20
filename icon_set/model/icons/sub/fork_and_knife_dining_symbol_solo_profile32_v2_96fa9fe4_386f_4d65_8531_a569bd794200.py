"""Independent 32px profile of fork-and-knife-dining-symbol-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '96fa9fe4-386f-4d65-8531-a569bd794200'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('96fa9fe4-386f-4d65-8531-a569bd794200', 'pictographic-primitives/state/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'),)
PROFILE_SOURCE_KEYS = ('solo/fork-and-knife-dining-symbol-solo',)
SOLO_SOURCE_ICON_IDS = ('fork-and-knife-dining-symbol-solo',)
REFERENCE_EXPORT_SHA256 = '49724c00817f2a191a568b756b87affadf10176d432cf5172660d50da0d24c68'

class DrawingVariant2(Sub32):
    icon_id = 'fork-and-knife-dining-symbol-solo-profile32-v2'
    variant_of = 'fork-and-knife-dining-symbol-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
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
