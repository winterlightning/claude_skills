"""Independent 32px profile of shipping-delivery-truck-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'ee45281c-9d60-448b-b6b0-b5db76f72c3b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ee45281c-9d60-448b-b6b0-b5db76f72c3b', 'pictographic-primitives/transportation/truck_ee45281c-9d60-448b-b6b0-b5db76f72c3b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/shipping-delivery-truck-solo',)
SOLO_SOURCE_ICON_IDS = ('shipping-delivery-truck-solo',)
REFERENCE_EXPORT_SHA256 = '31be7a040ee3c4051d74facabcd9943541ce14e4dd3e6344d00cf732a3ad892f'

class DrawingVariant2(Sub32):
    icon_id = 'shipping-delivery-truck-sub32-v2'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Delivery truck with rectangular cargo body, sloped cab, vertical divider and two open circular wheels. Construction reference: truck."""
        for name, x in [('rear', 6), ('front', 26)]:
            circle(self, name, x, 24, 4)
        self.add_line('left', (2, 24), (2, 6))
        self.add_arc('tl', (2, 6), (4, 4), radius_x=2)
        self.add_line('top', (4, 4), (16, 4))
        self.add_line('divider', (16, 4), (16, 24))
        self.add_line('floor', (10, 24), (22, 24))
        self.add_polyline('cab', (16, 10), (24, 10), (30, 18), (30, 24))
        self.add_contour('cargo', 'left', 'tl', 'top', 'divider')
        for a, b in [('rear', 'cargo'), ('rear', 'floor'), ('front', 'cab'), ('front', 'floor'), ('cargo', 'floor'), ('cargo', 'cab')]:
            self.relate('connect', a, b)

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
