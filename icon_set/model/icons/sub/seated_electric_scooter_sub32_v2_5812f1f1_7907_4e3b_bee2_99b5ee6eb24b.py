"""Independent 32px profile of seated-electric-scooter.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = '5812f1f1-7907-4e3b-bee2-99b5ee6eb24b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('5812f1f1-7907-4e3b-bee2-99b5ee6eb24b', 'pictographic-primitives/transportation/scooter_5812f1f1-7907-4e3b-bee2-99b5ee6eb24b.svg'),)
PROFILE_SOURCE_KEYS = ('solo/seated-electric-scooter',)
SOLO_SOURCE_ICON_IDS = ('seated-electric-scooter',)
REFERENCE_EXPORT_SHA256 = '6d9e39f55b062cd667d346f1fd91bafc3e674d4168b6f5979154ec0d22408440'

class DrawingVariant2(Sub32):
    icon_id = 'seated-electric-scooter-sub32-v2'
    variant_of = 'seated-electric-scooter-sub32'
    variant_label = 'Source-faithful side-combination centerline repair'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'objects/transportation'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        """Seated electric scooter with two open wheels, seat and stem, low chassis and tall steering handle. Construction reference: bike."""
        for name, x in [('rear', 6), ('front', 26)]:
            circle(self, name, x, 24, 4)
        self.add_polyline('steering', (20, 4), (24, 4), (26, 20))
        self.relate('connect', 'steering', 'front')
        self.add_line('chassis', (10, 24), (17, 24))
        self.add_bezier('rise', (17, 24), ((21, 24), (22, 16), (25, 12)))
        self.add_contour('frame', 'chassis', 'rise')
        self.relate('connect', 'frame', 'rear')
        self.relate('connect', 'frame', 'steering')
        self.add_line('seat', (12, 14), (18, 14))
        self.add_line('post', (16, 14), (16, 24))
        self.relate('connect', 'seat', 'post')
        self.relate('connect', 'post', 'frame')

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
