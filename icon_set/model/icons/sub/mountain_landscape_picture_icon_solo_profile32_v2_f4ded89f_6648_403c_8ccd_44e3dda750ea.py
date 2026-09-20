"""Independent 32px profile of mountain-landscape-picture-icon-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f4ded89f-6648-403c-8ccd-44e3dda750ea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/images/image_f4ded89f-6648-403c-8ccd-44e3dda750ea.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('f4ded89f-6648-403c-8ccd-44e3dda750ea', 'pictographic-primitives/images/image_f4ded89f-6648-403c-8ccd-44e3dda750ea.svg'),)
PROFILE_SOURCE_KEYS = ('solo/mountain-landscape-picture-icon-solo',)
SOLO_SOURCE_ICON_IDS = ('mountain-landscape-picture-icon-solo',)
REFERENCE_EXPORT_SHA256 = '5d1fa048e0e9db621d5bf186e1836195fc7ee7b0b915dee0cfb207d80d16c017'

class DrawingVariant2(Sub32):
    icon_id = 'mountain-landscape-picture-icon-solo-profile32-v2'
    variant_of = 'mountain-landscape-picture-icon-solo-profile32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded picture frame, round sun and two distinct mountain peaks. Construction reference: none."""
        box(self, 'frame', 2, 2, 30, 30, 3)
        circle(self, 'sun', 12, 12, 3)
        self.add_polyline('mountains', (3, 29), (10, 21), (15, 25), (23, 17), (30, 25))
        self.relate('connect', 'frame', 'mountains')

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
