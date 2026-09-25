"""Independent 32px profile of rosette-ribbon.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/symbol/ribbon_4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9', 'pictographic-primitives/symbol/ribbon_4b8d63df-19f2-40b4-a07b-b9f5c17ba2a9.svg'),)
PROFILE_SOURCE_KEYS = ('solo/rosette-ribbon',)
SOLO_SOURCE_ICON_IDS = ('rosette-ribbon',)
REFERENCE_EXPORT_SHA256 = '1cbfb17661c7d9a0d7c112837ae221bf1e9ff4f741bbee4551b45bb872a54955'

class DrawingVariant2(Sub32):
    icon_id = 'rosette-ribbon-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'symbol'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Eight-lobed rosette with a center mark and notched ribbon. Construction reference: award: scalloped seal and attached ribbon."""
        pts = [(13, 5), (19, 5), (24, 7), (24, 15), (19, 17), (13, 17), (8, 15), (8, 7), (13, 5)]
        for i, (a, b, r) in enumerate(zip(pts, pts[1:], (3, 4, 4, 4, 3, 4, 4, 4))):
            self.add_arc(f'lobe-{i}', a, b, radius_x=r)
        self.add_contour('seal', *[f'lobe-{i}' for i in range(8)], closed=True)
        self.add_line('center', (16, 11), (16, 11))
        self.add_polyline('ribbon', (8, 15), (4, 30), (16, 27), (28, 30), (24, 15))
        self.relate('connect', 'ribbon', 'seal')

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
