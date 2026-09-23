# Independent repair; parent preserved.
"""Independent 32px profile of camera.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '52be666d-64a9-45bd-befb-a58dead7c51f'
SOURCE_PATH = 'pictographic-primitives/video/camera_52be666d-64a9-45bd-befb-a58dead7c51f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('52be666d-64a9-45bd-befb-a58dead7c51f', 'pictographic-primitives/video/camera_52be666d-64a9-45bd-befb-a58dead7c51f.svg'),)
PROFILE_SOURCE_KEYS = ('solo/camera',)
SOLO_SOURCE_ICON_IDS = ('camera',)
REFERENCE_EXPORT_SHA256 = 'ad6f73f47f717d597656ebf1a435fe80ec00c42ecdd36e93beec425caeaf4394'

class RepairVariant(Sub32):
    variant_label = 'Centerline and source fidelity repair'
    icon_id = 'camera-sub32-v2'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/media'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('top-left', (5, 10), (8, 10))
        self.add_bezier('housing-left', (8, 10), ((10, 10), (10, 4), (12, 4)))
        self.add_line('housing-top', (12, 4), (20, 4))
        self.add_bezier('housing-right', (20, 4), ((22, 4), (22, 10), (24, 10)))
        self.add_line('top-right', (24, 10), (27, 10))
        self.add_contour('top', 'top-left', 'housing-left', 'housing-top', 'housing-right', 'top-right')
        self.add_arc('tr', (27, 10), (30, 13), radius_x=3)
        self.add_line('right', (30, 13), (30, 25))
        self.add_arc('br', (30, 25), (27, 28), radius_x=3)
        self.add_line('bottom', (27, 28), (5, 28))
        self.add_arc('bl', (5, 28), (2, 25), radius_x=3)
        self.add_line('left', (2, 25), (2, 13))
        self.add_arc('tl', (2, 13), (5, 10), radius_x=3)
        self.relate('connect', 'top', 'tr')
        self.relate('connect', 'top', 'tl')
        self.add_contour('sides', 'tr', 'right', 'br', 'bottom', 'bl', 'left', 'tl')
        circle(self, 'lens', 16, 17, 4)

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
REPAIR_PLAN = 'Camera body with raised housing, equal corners, centered round lens.'
CONSTRUCTION_REFERENCE = 'camera'
