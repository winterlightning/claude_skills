"""Independent 32px profile of bicycle-reference-25-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ba2c7c5d-7b19-4251-8651-f1619fdbdc5e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/bike_ba2c7c5d-7b19-4251-8651-f1619fdbdc5e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ba2c7c5d-7b19-4251-8651-f1619fdbdc5e', 'pictographic-primitives/other/bike_ba2c7c5d-7b19-4251-8651-f1619fdbdc5e.svg'), ('e918e425-b0c9-444c-bdb5-9884044e4703', 'pictographic-primitives/other/bike_e918e425-b0c9-444c-bdb5-9884044e4703.svg'), ('3bd744bc-3a24-4a8e-92f3-02a013f3d4f0', 'pictographic-primitives/other/bike_3bd744bc-3a24-4a8e-92f3-02a013f3d4f0.svg'))
PROFILE_SOURCE_KEYS = ('solo/bicycle-reference-25-solo', 'solo/bicycle-reference-165-solo', 'solo/bicycle-reference-184-solo')
SOLO_SOURCE_ICON_IDS = ('bicycle-reference-25-solo', 'bicycle-reference-165-solo', 'bicycle-reference-184-solo')
REFERENCE_EXPORT_SHA256 = '715c83355c6af1534edaeebc5e3f7c45ec47d099c947d3457999f263cffb24c0'

class DrawingVariant2(Sub32):
    icon_id = 'bicycle-reference-25-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Bicycle with two open tyres, raised saddle, handlebar and connecting frame. Construction reference: bike: circular wheels and external frame joins."""
        circle(self, 'rear', 7, 25, 5)
        circle(self, 'front', 25, 25, 5)
        self.add_polyline('frame', (7, 20), (12, 12), (23, 12), (25, 20))
        self.relate('connect', 'frame', 'rear')
        self.relate('connect', 'frame', 'front')
        self.add_line('seat-post', (12, 12), (10, 4))
        self.relate('connect', 'seat-post', 'frame')
        self.add_line('seat', (6, 4), (14, 4))
        self.relate('connect', 'seat', 'seat-post')
        self.add_polyline('handle', (23, 12), (25, 2), (30, 2))
        self.relate('connect', 'handle', 'frame')

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
