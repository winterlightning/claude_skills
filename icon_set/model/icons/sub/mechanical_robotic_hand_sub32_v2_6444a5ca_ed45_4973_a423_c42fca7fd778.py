"""Independent 32px profile of mechanical-robotic-hand-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '6444a5ca-ed45-4973-a423-c42fca7fd778'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/hand robot_6444a5ca-ed45-4973-a423-c42fca7fd778.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('6444a5ca-ed45-4973-a423-c42fca7fd778', 'pictographic-primitives/other/hand robot_6444a5ca-ed45-4973-a423-c42fca7fd778.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mechanical-robotic-hand-solo',)
SOLO_SOURCE_ICON_IDS = ('mechanical-robotic-hand-solo',)
REFERENCE_EXPORT_SHA256 = 'b8926cc2cf3a0de9e433d7b62ad8b65f0c65d40fb47b37f680e3d8ee52251f92'

class DrawingVariant2(Sub32):
    icon_id = 'mechanical-robotic-hand-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives-generate'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Open-wrist robotic hand with raised finger and a single joint seam. Construction reference: hand: broad open palm and rounded finger tip."""
        self.add_line('upper', (2, 4), (12, 8))
        self.add_bezier('knuckle', (12, 8), ((18, 8), (20, 8), (20, 12)))
        self.add_line('notch', (20, 12), (20, 16))
        self.add_line('finger-up', (20, 16), (26, 10))
        self.add_bezier('tip', (26, 10), ((28, 8), (30, 10), (30, 12)))
        self.add_line('finger-side', (30, 12), (30, 18))
        self.add_line('finger-bottom', (30, 18), (22, 26))
        self.add_bezier('palm', (22, 26), ((20, 28), (18, 28), (16, 28)))
        self.add_line('wrist-base', (16, 28), (2, 24))
        self.add_contour('hand', 'upper', 'knuckle', 'notch', 'finger-up', 'tip', 'finger-side', 'finger-bottom', 'palm', 'wrist-base')
        self.add_line('joint', (12, 8), (12, 18))
        self.relate('connect', 'joint', 'hand')

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
