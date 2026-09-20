"""Independent 32px profile of state32-6d29f24a-3e64-4196-858e-9eff669a98f5.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '063ab342-3eb9-4c77-b5e5-59de1a294e59'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/state/video_063ab342-3eb9-4c77-b5e5-59de1a294e59.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('063ab342-3eb9-4c77-b5e5-59de1a294e59', 'pictographic-primitives/state/video_063ab342-3eb9-4c77-b5e5-59de1a294e59.svg'), ('86847067-8fdd-411e-9dcf-21637870d1dc', 'pictographic-primitives/symbol/video_86847067-8fdd-411e-9dcf-21637870d1dc.svg'), ('6d29f24a-3e64-4196-858e-9eff669a98f5', 'pictographic-primitives/state/video_6d29f24a-3e64-4196-858e-9eff669a98f5.svg'), ('77cac2c6-9ef1-4a3f-85bf-963aeda09df3', 'pictographic-primitives/symbol/video_77cac2c6-9ef1-4a3f-85bf-963aeda09df3.svg'))
PROFILE_SOURCE_KEYS = ('solo/video', 'solo/video-86847067', 'solo/video-state', 'solo/video-symbol')
SOLO_SOURCE_ICON_IDS = ('video', 'video-86847067', 'video-state', 'video-symbol')
REFERENCE_EXPORT_SHA256 = '617cf2fd29ac4d21b9702b2e53964a47f2f624d1d990805018ef0f3895015bcf'

class DrawingVariant2(Sub32):
    icon_id = 'state32-6d29f24a-3e64-4196-858e-9eff669a98f5-v2'
    variant_of = 'state32-6d29f24a-3e64-4196-858e-9eff669a98f5'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Rounded video-camera body with attached outward flared lens on the right. Construction reference: video."""
        box(self, 'body', 2, 4, 22, 28, 4)
        self.add_polyline('lens', (22, 12), (30, 8), (30, 24), (22, 20))
        self.relate('connect', 'lens', 'body')

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
